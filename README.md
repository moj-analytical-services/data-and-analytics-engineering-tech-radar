# Data and Analytics Engineering Tech Radar

The MoJ [Data and Analytics Engineering community](https://ministryofjustice.github.io/data-and-analytics-engineering/), 
maintains a [public Tech Radar](http://zalando.github.io/tech-radar/) to help
align technology choices within our teams. This Tech Radar is based on [pioneering work
by ThoughtWorks](https://www.thoughtworks.com/radar) and uses a modified version of Zalando's 
[`radar.js`](https://github.com/zalando/tech-radar/blob/master/docs/radar.js) with [d3.js v4](https://d3js.org) for visualisation.

Tech radar blips are configured in `blips.json`, while tech radar rings and quadrants are set up in `radar_config.json`. Additional context for the blips is provided by GitHub discussions, which are queried using the GitHub GraphQL API to populate `blips.json`


# Tech Radar Discussion Management

This script extracts technology radar entries from [the tech radar GitHub Discussions](https://github.com/moj-analytical-services/data-and-analytics-engineering-tech-radar/discussions) and outputs them in a structured `JSON` format used by the visualization framework. It can also compare the extracted data with a previous snapshot to identify changes.



## Setup

### Clone the Repository:

```bash
git clone git@github.com:moj-analytical-services/data-and-analytics-engineering-tech-radar.git
```
```bash
cd data-and-analytics-engineering-tech-radar
```
### Create `.env` File: 

Create a file named `.env` in the script's directory and add your GitHub personal access token in the following format:
```bash
GH_TOKEN=<your_github_token>
```
Replace `<your_github_token>` with your actual GitHub personal access token (PAT) that has the necessary permissions for GraphQL API access.

**For GitHub Personal Access Token:**
<ol>
<li> Go to your [GitHub account settings](https://github.com/settings/profile). </li> 
<li> Navigate to Developer settings -> Personal access tokens. </li>
<li> Click Generate new token and select the repo scope. </li>
<li> Copy the generated token into the .env file. </li> 

</ol>

### Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate
```
### Install the python packages required


```pythpn
pip install -r requirements.txt
```

## Configure `radar_config.json`: 
Create a file named `radar_config.json` to define your radar's structure:

```json
{
  "quadrants": [
    {"name": "Quadrant 1 Name",
      "_location": "Top"},
    {"name": "Quadrant 2 Name",
    "_location": "Bottom"},
    ...
  ],
  "rings": [
    {"name": "Ring 1 Name", "emoji": "✅"},
    {"name": "Ring 2 Name", "emoji": "🧪"},
    ...
  ]
}
```

**Example:**
```json
{
  "quadrants": [
    {"name": "Techniques"},
    {"name": "Platforms"},
    {"name": "Languages & Frameworks"},
    {"name": "Data Tools"}
  ],
  "rings": [
    {"name": "Adopt", "emoji": "✅"},
    {"name": "Trial", "emoji": "🧪"},
    {"name": "Assess", "emoji": "🔎"},
    {"name": "Hold", "emoji": "🛑"}
  ]
}
```

#### (Optional) Prepare `blips.json` for Comparison:

    If you want to compare with previous data, create a `blips.json` file with the following structure:

```json
{
  "date": "YYYY-MM-DD",
  "entries": [
    {
      "label": "Entry 1 Label",
      "quadrant": 0, 
      "ring": 2 
    },
    ...
  ]
}
```

### Usage

#### Run the Script
```bash
python manage_discussions/get_discussions.py
```
### Output

The script will generate two JSON files:

- `blips.json`: Contains the extracted radar entries with the current date, which also updates the visualization.

- `entries_skipped.json`: (If any) Lists discussions that didn't match the criteria for radar entries.
</ol>

### Viewing the Output Locally in VS Code
#### Install Live Server Extension
<ol>
  <li>Open Visual Studio Code: Launch VS Code on your computer.</li>
  <li>Access Extensions: Click on the Extensions icon in the Activity Bar on the side of the window.</li>
<li>Search for Live Server: In the Extensions view, type "Live Server" in the search bar.</li>
<li>Install Live Server: Click on the Install button for the Live Server extension.</li>
</ol>

#### Start Live Server

<ol>
  <li> Open Your Project: Open the folder containing your project files, including index.html</li>
  <li>Start Live Server: Right-click on your index.html file and select "Open with Live Server" from the context menu.</li>
</ol>
