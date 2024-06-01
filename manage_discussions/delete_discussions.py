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

get_discussions = gql(
    """
query {
repository(owner:"moj-analytical-services", name:"data-and-analytics-engineering-tech-radar") {
    discussions(last:100) {
    edges {
        node {
            id
        }
    }
    }
}
}
"""
)

response = client.execute(get_discussions)
discussions = response["repository"]['discussions']

delete_discussion = gql(
"""
mutation ($discussion_id:ID!){
    deleteDiscussion(input:{
        id: $discussion_id,
    })
    {
        discussion {
            id
        }
    }
    }
"""
)

for discussion in response['repository']['discussions']['edges']:
    discussion_id = discussion['node']['id']
    response = client.execute(delete_discussion, 
                              variable_values={"discussion_id":discussion_id})

