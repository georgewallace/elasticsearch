# Delete [ilm-delete]

Phases allowed: delete.

Permanently removes the index.

## Options [ilm-delete-options]

`delete_searchable_snapshot`
:   (Optional, Boolean) Deletes the searchable snapshot created in a previous phase. Defaults to `true`. This option is applicable when the [searchable snapshot](ilm-searchable-snapshot.md) action is used in any previous phase.

    If you set this option to `false`, use the [Delete snapshots API](delete-snapshot-api.md) to remove {{search-snaps}} from your snapshot repository when they are no longer needed.

    If you manually delete an index before the {{ilm-cap}} delete phase runs, then {{ilm-init}} will not delete the underlying {{search-snap}}. Use the [Delete snapshots API](delete-snapshot-api.md) to remove the {{search-snap}} from your snapshot repository when it is no longer needed.

    See [Reliability of {{search-snaps}}](searchable-snapshots.md#searchable-snapshots-reliability) for further information about deleting {{search-snaps}}.


::::{warning} 
If a policy with a searchable snapshot action is applied on an existing searchable snapshot index, the snapshot backing this index will NOT be deleted because it was not created by this policy. If you want to clean this snapshot, please delete it manually after the index is deleted using the [delete snapshot API](delete-snapshot-api.md), you can find the repository and snapshot name using the [get index API](indices-get-index.md).
::::



## Example [ilm-delete-action-ex]

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "delete": {
        "actions": {
          "delete" : { }
        }
      }
    }
  }
}
```


