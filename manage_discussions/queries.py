DISCUSSIONS_QUERY = """
query($owner: String!, $name: String!, $items_per_page: Int, $page_after: String) {
  repository(owner: $owner, name: $name){
    discussions(first: $items_per_page, after: $page_after) {
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
          labels(first: 1) {
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
