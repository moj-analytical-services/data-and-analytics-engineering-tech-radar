import json
import pandas as pd
from datetime import datetime

quadrant = {
    0: "Techniques",
    1: "Tools",
    2: "Platforms",
    3: "Languages and Frameworks",
}
rings = {0: "Adopt", 1: "Trials", 2: "Assess", 3: "Hold"}
moves = {
    -1: "moved out",
    0: "not moved",
    1: "moved in",
    2: "new",
}


with open("blips.json", "r") as f1, open(
    "blips_.json", "r"
) as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

# Add new entries for testing
data1["entries"].append(
    {
        "label": "Old Entry",
        "quadrant": 1,
        "ring": 0,
        "moved": 1,
        "link": "https://github.com/moj-analytical-services/data-and-analytics-engineering-tech-radar/discussions/18",
        "active": False,
    }
)


def get_change_status(
    ring_old, moved_old, ring_new, moved_new
):
    if ring_old == ring_new and moved_old == moved_new:
        return "No changes"
    elif ring_old != ring_new and moved_old == moved_new:
        return "Ring Changed"
    elif ring_old == ring_new and moved_old != moved_new:
        return "Moved Changed"
    else:
        return "Both Changed"


def compare_tech_radar(radar_data_old, radar_data_new):
    changes = {}

    # Create a dictionary mapping labels to their data in the old radar
    old_radar_labels = {
        entry["label"]: entry
        for entry in radar_data_old["entries"]
    }

    for entry in radar_data_new["entries"]:
        label = entry["label"]
        quadrant = entry["quadrant"]

        if label in old_radar_labels:
            old_entry = old_radar_labels[label]
            changes[label] = {
                "quadrant": quadrant,
                "ring_old": old_entry["ring"],
                "ring_new": entry["ring"],
                "moved_old": old_entry["moved"],
                "moved_new": entry["moved"],
                "change": get_change_status(
                    old_entry["ring"],
                    old_entry["moved"],
                    entry["ring"],
                    entry["moved"],
                ),
            }
        else:
            # New label
            changes[label] = {
                "quadrant": quadrant,
                "ring_old": None,
                "ring_new": entry["ring"],
                "moved_old": None,
                "moved_new": entry["moved"],
                "change": "new",
            }

    for entry in [
        item
        for item in old_radar_labels.keys()
        if item not in changes.keys()
    ]:
        lost_entry = old_radar_labels[entry]
        changes[lost_entry["label"]] = {
            "quadrant": lost_entry["quadrant"],
            "ring_old": lost_entry["ring"],
            "ring_new": None,
            "moved_old": lost_entry["moved"],
            "moved_new": None,
            "change": "removed",
        }
    return changes


def get_text_value(mapping, value):
    """Helper function to get text value from mapping, or return original if not found"""
    return mapping.get(value, value)


def replace_with_text(item):
    """Replace quadrant and ring numbers with text, handling potential errors"""
    try:
        item["quadrant"] = get_text_value(
            quadrant, item["quadrant"]
        )
        item["ring_old"] = get_text_value(
            rings, item["ring_old"]
        )
        item["ring_new"] = get_text_value(
            rings, item["ring_new"]
        )
        item["moved_old"] = get_text_value(
            moves, item["moved_old"]
        )
        item["moved_new"] = get_text_value(
            moves, item["moved_new"]
        )
    except KeyError as e:
        print(
            f"KeyError: {e} not found in item. Skipping this replacement."
        )
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    return item


def process_tech_radar_data(summary):

    try:
        df = pd.DataFrame.from_dict(summary, orient="index")
        df.reset_index(inplace=True)
        df.columns = [
            "entry",
            "quadrant",
            "ring_old",
            "ring_new",
            "moved_old",
            "moved_new",
            "Status",
        ]
        df = df[df["Status"] != "No changes"]
        columns_order = [
            "quadrant",
            "entry",
            "Status",
            "ring_old",
            "ring_new",
            "moved_old",
            "moved_new",
        ]
        df = df[columns_order]

        df.sort_values("quadrant", inplace=True)
        df = df.reset_index(drop=True)
        return df

    except KeyError as e:
        print(
            f"KeyError: {e}. Please ensure all required columns are present in the input data."
        )
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# -----------------------------------
changes = compare_tech_radar(data1, data2)

# Apply the function to each item in the dictionary
summary = {}
for key, value in changes.items():
    try:
        summary[key] = replace_with_text(value.copy())
    except Exception as e:
        print(f"Error processing item '{key}': {e}")
        summary[key] = value


# print(process_tech_radar_data(summary))

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"manage_discussions/tech_radar_changes_{timestamp}.csv"

process_tech_radar_data(summary).to_csv(filename, index=False)