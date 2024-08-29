from typing import Optional, Sequence

import dlt
from dlt.sources import DltResource

from helpers import get_discussions


@dlt.source
def github_discussions(
    owner: str,
    name: str,
    access_token: str = dlt.secrets.value,
    items_per_page: int = 100,
    max_items: Optional[int] = None,
) -> Sequence[DltResource]:
    return (
        dlt.resource(
            get_discussions(
                owner=owner,
                name=name,
                access_token=access_token,
                items_per_page=items_per_page,
                max_items=max_items,
            )
        ),
    )


pipeline = dlt.pipeline(
    "github_discussions",
    destination="duckdb",
    dataset_name="filesystem_discussions",
    full_refresh=True,
)

data = github_discussions(
    owner="moj-analytical-services", name="data-and-analytics-engineering-tech-radar"
)

# run pipeline and print load output
print(pipeline.run(data=data, loader_file_format="jsonl"))
