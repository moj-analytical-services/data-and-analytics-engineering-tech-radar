from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from dotenv import load_dotenv
import os
import json
import datetime

load_dotenv()
GH_TOKEN = os.environ['GH_TOKEN']
transport = AIOHTTPTransport(url='https://api.github.com/graphql',
                             headers={'Authorization':f'token {GH_TOKEN}'}
                             )
client = Client(transport=transport, fetch_schema_from_transport=True)
COMPARE=True

query = gql(
    """
query($after: String) {
repository(owner:"moj-analytical-services", name:"data-and-analytics-engineering-tech-radar") {
    discussions(first: 100, after: $after) {
    pageInfo {
        endCursor
        hasNextPage
        }
    edges {
        node {
        title
        url
        closed
        category {
            name
        }
        labels(first:1) {
            edges {
            node {
                name
            }
            }
        }
        }
    }
    }
}
}
"""
)

blips_old = {}
if COMPARE:
    with open('blips.json') as f:
        config = json.load(f)
    for entry in config['entries']:
        blips_old[entry['label']] = entry['ring']

with open('radar_config.json') as f:
    radar = json.load(f)
ring_index = {}
for i,ring in enumerate(radar['rings']):
    ring_index[f"{i+1}: {ring['name']} {ring['emoji']}"] = i
# print(ring_index)
quadrant_index = {}
for i,quadrant in enumerate(radar['quadrants']):
    quadrant_index[quadrant['name']] = i
# print(quadrant_index)

after = None
entries_new = []
entries_skipped = []
has_next_page = True

while has_next_page:
    print(after)
    response = client.execute(query, variable_values={"after":after})
    discussions = response['repository']['discussions']['edges']

    for discussion in discussions:
        details = discussion['node']
        print(details['title'])
        category = details['category']['name']
        if (len(details['labels']['edges'])==1 
            and category in quadrant_index
            and not details['closed']):
            quadrant = quadrant_index[category]
            assessment = details['labels']['edges'][0]['node']['name']
            if assessment in ring_index:
                ring = ring_index[assessment]
                ring_change = None
                ring_old = blips_old.get(details['title'])
                if ring_old is not None:
                    ring_change = ring_old - ring
                entries_new.append({"label":details['title'],
                                    "quadrant":quadrant,
                                    "ring":ring,
                                    "moved":ring_change,
                                    "link": details['url']
                                    })
                
            else:
                entries_skipped.append(details)
        else:
            entries_skipped.append(details)

    has_next_page = response['repository']['discussions']['pageInfo']['hasNextPage']
    after = response['repository']['discussions']['pageInfo']['endCursor']

entries_new = sorted(entries_new, key=lambda k: k['label'].lower())
blips_new = {"date":str(datetime.date.today()),"entries":entries_new}

with open(f'blips.json', 'w') as f:
    json.dump(blips_new, f, indent=2)
if len(entries_skipped)>0:  
    with open('entries_skipped.json', 'w') as f:
        json.dump(entries_skipped, f, indent=2)