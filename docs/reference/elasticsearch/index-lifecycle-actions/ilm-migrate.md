# Migrate [ilm-migrate]

Phases allowed: warm, cold.

Moves the index to the [data tier](data-tiers.md) that corresponds to the current phase by updating the [`index.routing.allocation.include._tier_preference`](data-tier-shard-filtering.md#tier-preference-allocation-filter) index setting. {{ilm-init}} automatically injects the migrate action in the warm and cold phases. To prevent automatic migration, you can explicitly include the migrate action and set the enabled option to `false`.

If the `cold` phase defines a [searchable snapshot action](ilm-searchable-snapshot.md) the `migrate` action will not be injected automatically in the `cold` phase because the managed index will be mounted directly on the target tier using the same [_tier_preference](data-tier-shard-filtering.md#tier-preference-allocation-filter) infrastructure the `migrate` actions configures.

In the warm phase, the `migrate` action sets [`index.routing.allocation.include._tier_preference`](data-tier-shard-filtering.md#tier-preference-allocation-filter) to `data_warm,data_hot`. This moves the index to nodes in the [warm tier](data-tiers.md#warm-tier). If there are no nodes in the warm tier,  it falls back to the [hot tier](data-tiers.md#hot-tier).

In the cold phase, the `migrate` action sets [`index.routing.allocation.include._tier_preference`](data-tier-shard-filtering.md#tier-preference-allocation-filter) to `data_cold,data_warm,data_hot`. This moves the index to nodes in the [cold tier](data-tiers.md#cold-tier). If there are no nodes in the cold tier, it falls back to the [warm](data-tiers.md#warm-tier) tier, or the [hot](data-tiers.md#hot-tier) tier if there are no warm nodes available.

The migrate action is not allowed in the frozen phase. The frozen phase directly mounts the searchable snapshot using a [`index.routing.allocation.include._tier_preference`](data-tier-shard-filtering.md#tier-preference-allocation-filter) of `data_frozen`. This moves the index to nodes in the [frozen tier](data-tiers.md#frozen-tier).

The migrate action is not allowed in the hot phase. The initial index allocation is performed [automatically](data-tiers.md#data-tier-allocation), and can be configured manually or via [index templates](index-templates.md).

## Options [ilm-migrate-options]

`enabled`
:   (Optional, Boolean) Controls whether {{ilm-init}} automatically migrates the index during this phase. Defaults to `true`.


## Example [ilm-enabled-migrate-ex]

In the following policy, the [allocate](ilm-allocate.md) action is specified to reduce the number of replicas before {{ilm-init}} migrates the index to warm nodes.

::::{note} 
Explicitly specifying the migrate action is not required--{{ilm-init}} automatically performs the migrate action unless you disable migration.
::::


```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "migrate" : {
          },
          "allocate": {
            "number_of_replicas": 1
          }
        }
      }
    }
  }
}
```


## Disable automatic migration [ilm-disable-migrate-ex]

The migrate action in the following policy is disabled and the allocate action assigns the index to nodes that have a `rack_id` of *one* or *two*.

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "migrate" : {
           "enabled": false
          },
          "allocate": {
            "include" : {
              "rack_id": "one,two"
            }
          }
        }
      }
    }
  }
}
```


