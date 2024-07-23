# Tech Radar Discussion Management

`get_discussions.py` extracts technology radar entries from [the tech radar GitHub Discussions](https://github.com/moj-analytical-services/data-and-analytics-engineering-tech-radar/discussions) and outputs them in a structured `JSON` format used by the visualization framework. It can also compare the extracted data with a previous snapshot to identify changes. The `create_discussions.py` script generates new discussions in the GitHub repository based on the entries defined in `blips.json`, assigns appropriate labels, and posts initial comments to each discussion. Lastly, the `delete_discussion.py` script deletes discussions from the GitHub repository, ensuring that any unnecessary or outdated discussions are removed.



## Setup for using discussion management

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


### Usage

- Setup: Ensure `radar_config.json` and `blips.json` (if comparing) are properly configured.

- Fetch and Update Discussions: Run `get_discussions.py` to fetch and update local data.

- Create Discussions: Use `create_discussions.py` to add new discussions to the GitHub repository based on `blips.json`.

- Delete Discussions: Run `delete_discussion.py` to remove discussions from the GitHub repository.

#### Run the Script
```bash
python manage_discussions/get_discussions.py
```
### Output

The script will generate two JSON files:

- `blips.json`: Contains the extracted radar entries with the current date, which also updates the visualization.

- `entries_skipped.json`: (If any) Lists discussions that didn't match the criteria for radar entries.
</ol>