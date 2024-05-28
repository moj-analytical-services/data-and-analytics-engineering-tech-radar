from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()
GH_TOKEN = os.environ['GH_TOKEN']
transport = AIOHTTPTransport(url='https://api.github.com/graphql',
                             headers={'Authorization':f'token {GH_TOKEN}'}
                             )
client = Client(transport=transport, fetch_schema_from_transport=True)

get_repo_id = gql(
"""
query {
  repository (owner:"moj-analytical-services", name:"data-and-analytics-engineering-tech-radar")  {
        id
  }
}
"""
)

response = client.execute(get_repo_id)
repo_id = response["repository"]['id']
# print(repo_id)

get_categories = gql(
"""
query {
repository(owner:"moj-analytical-services", name:"data-and-analytics-engineering-tech-radar") {
    discussionCategories (last:20) {
    edges {
        node {
        id
        name
        }
    }
    }
}
}
"""
)

response = client.execute(get_categories)
categories = {category['node']['name']:category['node']['id'] for category in response['repository']['discussionCategories']['edges']}
# print(categories)

get_labels = gql(
"""
query {
repository(owner:"moj-analytical-services", name:"data-and-analytics-engineering-tech-radar") {
    labels (last:20) {
    edges {
        node {
        id
        name
        }
    }
    }
}
}
"""
)
response = client.execute(get_labels)
labels = {}
for category in response['repository']['labels']['edges']:
    name = category['node']['name']
    labels[name]=category['node']['id']
# print(labels)

create_discussion = gql(
"""
mutation ($name:String!,$repo_id:ID!,$category_id:ID!){
    createDiscussion(input:{
        title: $name, 
        repositoryId: $repo_id,
        categoryId: $category_id,
        body:"generated"
    })
    {
        discussion {
            id
        }
    }
    }
"""
)


add_label = gql(
"""
mutation ($label_id:ID!,$labelable_id:ID!){
    addLabelsToLabelable(input:{
        labelIds:[$label_id],
        labelableId:$labelable_id
    })
    {
        labelable{
            labels {
                totalCount
            }
        }
    }
}
"""
)

add_comment = gql(
"""
mutation ($discussion_id:ID!,$body:String!){
    addDiscussionComment(input:{
        discussionId:$discussion_id,
        body:$body
    })
    {
        comment{
            createdAt
        }
    }
}
"""
)

with open('blips.json') as f:
    entries = json.load(f)

with open('radar_config.json') as f:
    radar = json.load(f)

for entry in entries["entries"]:
    print(entry["name"])
    category_id = categories[radar['quadrants'][entry['quadrant']]['name']]
    label_name = radar['rings'][entry['ring']]['name']
    emoji = radar['rings'][entry['ring']]['emoji']
    label_id = labels[f"{label_name} {emoji}"]
    response = client.execute(create_discussion, 
                              variable_values={"name":entry["name"],
                                               "repo_id":repo_id,
                                               "category_id":category_id})
    discussion_id = response['createDiscussion']["discussion"]['id']
    client.execute(add_label, variable_values={"label_id":label_id,"labelable_id":discussion_id})
    comment = f"## {entries['date']}: {label_name}"
    client.execute(add_comment,variable_values={"discussion_id":discussion_id,"body":comment})
    # https://docs.github.com/en/graphql/overview/rate-limits-and-node-limits-for-the-graphql-api#exceeding-the-rate-limit
    time.sleep(1)
