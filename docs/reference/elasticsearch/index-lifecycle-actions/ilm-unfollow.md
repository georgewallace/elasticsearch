# Unfollow [ilm-unfollow]

Phases allowed: hot, warm, cold, frozen.

Converts a [{{ccr-init}}](https://www.elastic.co/guide/en/elasticsearch/reference/current/ccr-apis.html) follower index into a regular index. This enables the shrink, rollover, and searchable snapshot actions to be performed safely on follower indices. You can also use unfollow directly when moving follower indices through the lifecycle. Has no effect on indices that are not followers, phase execution just moves to the next action.

::::{note} 
This action is triggered automatically by the [rollover](ilm-rollover.md), [shrink](ilm-shrink.md), and [searchable snapshot](ilm-searchable-snapshot.md) actions when they are applied to follower indices.
::::


This action waits until is it safe to convert a follower index into a regular index. The following conditions must be met:

* The leader index must have `index.lifecycle.indexing_complete` set to `true`. This happens automatically if the leader index is rolled over using the [rollover](ilm-rollover.md) action, and can be set manually using the [index settings](indices-update-settings.md) API.
* All operations performed on the leader index have been replicated to the follower index. This ensures that no operations are lost when the index is converted.

Once these conditions are met, unfollow performs the following operations:

* Pauses indexing following for the follower index.
* Closes the follower index.
* Unfollows the leader index.
* Opens the follower index (which is at this point is a regular index).

## Options [ilm-unfollow-options]

None.


## Example [ilm-unfollow-ex]

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "unfollow" : {}
        }
      }
    }
  }
}
```


