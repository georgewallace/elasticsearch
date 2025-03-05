# Document level security [document-level-security]

Document level security restricts the documents that users have read access to. In particular, it restricts which documents can be accessed from document-based read APIs.

To enable document level security, you use a query to specify the documents that each role can access. The document `query` is associated with a particular data stream, index, or wildcard (`*`) pattern and operates in conjunction with the privileges specified for the data streams and indices.

The specified document `query`:

* Expects the same format as if it was defined in the search request
* Supports [templating a role query](field-and-document-access-control.md#templating-role-query) that can access the details of the currently authenticated user
* Accepts queries written as either string values or nested JSON
* Supports the majority of the {{es}} [Query Domain Specific Language (DSL)](query-dsl.md), with [some limitations](security-limitations.md#field-document-limitations) for field and document level security

::::{important} 
Omitting the `query` parameter entirely disables document level security for the respective indices permission entry.
::::


The following role definition grants read access only to documents that belong to the `click` category within all the `events-*` data streams and indices:

```console
POST /_security/role/click_role
{
  "indices": [
    {
      "names": [ "events-*" ],
      "privileges": [ "read" ],
      "query": "{\"match\": {\"category\": \"click\"}}"
    }
  ]
}
```

You can write this same query using nested JSON syntax:

```console
POST _security/role/click_role
{
  "indices": [
    {
      "names": [ "events-*" ],
      "privileges": [ "read" ],
      "query": {
        "match": {
          "category": "click"
        }
      }
    }
  ]
}
```

The following role grants read access only to the documents whose `department_id` equals `12`:

```console
POST /_security/role/dept_role
{
  "indices" : [
    {
      "names" : [ "*" ],
      "privileges" : [ "read" ],
      "query" : {
        "term" : { "department_id" : 12 }
      }
    }
  ]
}
```

