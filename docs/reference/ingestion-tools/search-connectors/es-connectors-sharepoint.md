---
navigation_title: "SharePoint Server"
---

# Elastic SharePoint Server connector reference [es-connectors-sharepoint]


%  Attributes used in this file

The *Elastic SharePoint Server connector* is a [connector](es-connectors.md) for [Microsoft SharePoint Server](https://www.microsoft.com/en-ww/microsoft-365/sharepoint/).

This connector is written in Python using the open code [Elastic connector framework](https://github.com/elastic/connectors/tree/main). View the [source code for this connector](https://github.com/elastic/connectors/tree/main/connectors/sources/sharepoint_server.py).

::::{tip} 
Looking for the SharePoint **Online** connector? See the [SharePoint Online reference](es-connectors-sharepoint-online.md).

::::


%  //////// //// //// //// //// //// //// ////////

%  //////// NATIVE CONNECTOR REFERENCE (MANAGED SERVICE) ///////

%  //////// //// //// //// //// //// //// ////////


## **Elastic managed connector reference** [es-connectors-sharepoint-native-connector-reference] 

::::::{dropdown} View **Elastic managed connector** reference

### Availability and prerequisites [es-connectors-sharepoint-availability-prerequisites] 

This connector is available as a managed service since Elastic **8.15.0**. To use this connector, satisfy all [managed connector requirements](es-native-connectors.md).

::::{note} 
This connector is in **beta** and is subject to change. Beta features are subject to change and are not covered by the support SLA of generally available (GA) features. Elastic plans to promote this feature to GA in a future release.

::::



### Create a SharePoint Server connector [es-connectors-sharepoint-create-connector-client] 


## Use the UI [es-connectors-sharepoint_server-create-use-the-ui] 

To create a new SharePoint Server connector:

1. In the Kibana UI, navigate to the **Search → Content → Connectors** page from the main menu, or use the [global search field](https://www.elastic.co/guide/en/kibana/current/kibana-concepts-analysts.html#_finding_your_apps_and_objects).
2. Follow the instructions to create a new native  **SharePoint Server** connector.

For additional operations, see [*Connectors UI in {{kib}}*](es-connectors-usage.md).


## Use the API [es-connectors-sharepoint_server-create-use-the-api] 

You can use the {{es}} [Create connector API](https://www.elastic.co/guide/en/elasticsearch/reference/current/connector-apis.html) to create a new native SharePoint Server connector.

For example:

```console
PUT _connector/my-sharepoint_server-connector
{
  "index_name": "my-elasticsearch-index",
  "name": "Content synced from SharePoint Server",
  "service_type": "sharepoint_server",
  "is_native": true
}
```

%  TEST[skip:can’t test in isolation]

:::::{dropdown} You’ll also need to **create an API key** for the connector to use.
::::{note} 
The user needs the cluster privileges `manage_api_key`, `manage_connector` and `write_connector_secrets` to generate API keys programmatically.

::::


To create an API key for the connector:

1. Run the following command, replacing values where indicated. Note the `id` and `encoded` return values from the response:

    ```console
    POST /_security/api_key
    {
      "name": "my-connector-api-key",
      "role_descriptors": {
        "my-connector-connector-role": {
          "cluster": [
            "monitor",
            "manage_connector"
          ],
          "indices": [
            {
              "names": [
                "my-index_name",
                ".search-acl-filter-my-index_name",
                ".elastic-connectors*"
              ],
              "privileges": [
                "all"
              ],
              "allow_restricted_indices": false
            }
          ]
        }
      }
    }
    ```

2. Use the `encoded` value to store a connector secret, and note the `id` return value from this response:

    ```console
    POST _connector/_secret
    {
      "value": "encoded_api_key"
    }
    ```


%  TEST[skip:need to retrieve ids from the response]

+ . Use the API key `id` and the connector secret `id` to update the connector:

+

```console
PUT /_connector/my_connector_id>/_api_key_id
{
  "api_key_id": "API key_id",
  "api_key_secret_id": "secret_id"
}
```

%  TEST[skip:need to retrieve ids from the response]

:::::


Refer to the [{{es}} API documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/connector-apis.html) for details of all available Connector APIs.


### Usage [es-connectors-sharepoint-usage] 

See [*Elastic managed connectors*](es-native-connectors.md).

For additional operations, see [*Connectors UI in {{kib}}*](es-connectors-usage.md).


### Compatibility [es-connectors-sharepoint-compatability] 

The following SharePoint Server versions are compatible:

* SharePoint 2013
* SharePoint 2016
* SharePoint 2019


### Configuration [es-connectors-sharepoint-configuration] 

The following configuration fields are required to set up the connector:

`authentication`
:   Authentication mode, either **Basic** or **NTLM**.

`username`
:   The username of the account for the SharePoint Server instance.

`password`
:   The password of the account.

`host_url`
:   The server host url where the SharePoint Server instance is hosted. Examples:

    * `https://192.158.1.38:8080`
    * `https://<tenant_name>.sharepoint.com`


`site_collections`
:   Comma-separated list of site collections to fetch from SharePoint Server. Examples:

    * `collection1`
    * `collection1, collection2`


`ssl_enabled`
:   Whether SSL verification will be enabled. Default value is `False`.

`ssl_ca`
:   Content of SSL certificate needed for SharePoint Server. Keep this field empty, if `ssl_enabled` is set to `False`.

    Example certificate:

    ```txt
    -----BEGIN CERTIFICATE-----
    MIID+jCCAuKgAwIBAgIGAJJMzlxLMA0GCSqGSIb3DQEBCwUAMHoxCzAJBgNVBAYT
    ...
    7RhLQyWn2u00L7/9Omw=
    -----END CERTIFICATE-----
    ```


`retry_count`
:   The number of retry attempts after a failed request to the SharePoint Server instance. Default value is `3`.

`use_document_level_security`
:   Toggle to enable [Document level security (DLS)](es-dls.md). When enabled, full syncs will fetch access control lists for each document and store them in the `_allow_access_control` field. Access control syncs fetch users' access control lists and store them in a separate index.

    Once enabled, the following granular permissions toggles will be available:

    * **Fetch unique list permissions**: Enable this option to fetch unique **list** permissions. If this setting is disabled a list will inherit permissions from its parent site.
    * **Fetch unique list item permissions**: Enable this option to fetch unique **list item** permissions. If this setting is disabled a list item will inherit permissions from its parent site.

        ::::{note} 
        If left empty the default value `true` will be used for these granular permissions toggles. Note that these settings may increase sync times.

        ::::



### Documents and syncs [es-connectors-sharepoint-documents-syncs] 

The connector syncs the following SharePoint object types:

* Sites and Subsites
* Lists
* List Items and its attachment content
* Document Libraries and its attachment content(include Web Pages)

::::{note} 
* Content from files bigger than 10 MB won’t be extracted by default. Use the [self-managed local extraction service](es-connectors-content-extraction.md#es-connectors-content-extraction-local) to handle larger binary files.
* Permissions are not synced by default. Enable [document-level security (DLS)](es-dls.md) to sync permissions.

::::



#### Sync types [es-connectors-sharepoint-sync-types] 

[Full syncs](es-connectors-sync-types.md#es-connectors-sync-types-full) are supported by default for all connectors.

This connector also supports [incremental syncs](es-connectors-sync-types.md#es-connectors-sync-types-incremental).


### Document level security [es-connectors-sharepoint-document-level-security] 

Document level security (DLS) enables you to restrict access to documents based on a user’s permissions. Refer to [configuration](es-connectors-sharepoint.md#es-connectors-sharepoint-configuration) on this page for how to enable DLS for this connector.

::::{note} 
Refer to [DLS in Search Applications](es-dls-e2e-guide.md) to learn how to ingest data from a connector with DLS enabled, when building a search application. The example uses SharePoint *Online* as the data source, but the same steps apply to every connector.

::::



### Sync rules [es-connectors-sharepoint-sync-rules] 

[Basic sync rules](es-sync-rules.md#es-sync-rules-basic) are identical for all connectors and are available by default.

Advanced sync rules are not available for this connector in the present version. Currently filtering is controlled via ingest pipelines.


### Content Extraction [es-connectors-sharepoint-content-extraction] 

See [Content extraction](es-connectors-content-extraction.md).


### Known issues [es-connectors-sharepoint-known-issues] 

There are currently no known issues for this connector. Refer to [Known issues](es-connectors-known-issues.md) for a list of known issues for all connectors.


### Troubleshooting [es-connectors-sharepoint-troubleshooting] 

See [Troubleshooting](es-connectors-troubleshooting.md).


### Security [es-connectors-sharepoint-security] 

See [Security](es-connectors-security.md).


### Framework and source [es-connectors-sharepoint-source] 

This connector is written in Python using the [Elastic connector framework](https://github.com/elastic/connectors/tree/main).

View the [source code for this connector](https://github.com/elastic/connectors/tree/main/connectors/sources/sharepoint_server.py) (branch *main*, compatible with Elastic *9.0*).

%  Closing the collapsible section

::::::


%  //////// //// //// //// //// //// //// ////////

%  //////// CONNECTOR CLIENT REFERENCE (SELF-MANAGED) ///////

%  //////// //// //// //// //// //// //// ////////


## **Self-managed connector reference** [es-connectors-sharepoint-connector-client-reference] 

::::::{dropdown} View **self-managed connector** reference

### Availability and prerequisites [es-connectors-sharepoint-client-availability-prerequisites] 

This connector is available as a self-managed **self-managed connector**. This self-managed connector is compatible with Elastic versions **8.9.0+**. To use this connector, satisfy all [self-managed connector requirements](es-build-connector.md).

::::{note} 
This connector is in **beta** and is subject to change. Beta features are subject to change and are not covered by the support SLA of generally available (GA) features. Elastic plans to promote this feature to GA in a future release.

::::



### Create a SharePoint Server connector [es-connectors-sharepoint-client-create-connector-client] 


## Use the UI [es-connectors-sharepoint_server-client-create-use-the-ui] 

To create a new SharePoint Server connector:

1. In the Kibana UI, navigate to the **Search → Content → Connectors** page from the main menu, or use the [global search field](https://www.elastic.co/guide/en/kibana/current/kibana-concepts-analysts.html#_finding_your_apps_and_objects).
2. Follow the instructions to create a new  **SharePoint Server** self-managed connector.


## Use the API [es-connectors-sharepoint_server-client-create-use-the-api] 

You can use the {{es}} [Create connector API](https://www.elastic.co/guide/en/elasticsearch/reference/current/connector-apis.html) to create a new self-managed SharePoint Server self-managed connector.

For example:

```console
PUT _connector/my-sharepoint_server-connector
{
  "index_name": "my-elasticsearch-index",
  "name": "Content synced from SharePoint Server",
  "service_type": "sharepoint_server"
}
```

%  TEST[skip:can’t test in isolation]

:::::{dropdown} You’ll also need to **create an API key** for the connector to use.
::::{note} 
The user needs the cluster privileges `manage_api_key`, `manage_connector` and `write_connector_secrets` to generate API keys programmatically.

::::


To create an API key for the connector:

1. Run the following command, replacing values where indicated. Note the `encoded` return values from the response:

    ```console
    POST /_security/api_key
    {
      "name": "connector_name-connector-api-key",
      "role_descriptors": {
        "connector_name-connector-role": {
          "cluster": [
            "monitor",
            "manage_connector"
          ],
          "indices": [
            {
              "names": [
                "index_name",
                ".search-acl-filter-index_name",
                ".elastic-connectors*"
              ],
              "privileges": [
                "all"
              ],
              "allow_restricted_indices": false
            }
          ]
        }
      }
    }
    ```

2. Update your `config.yml` file with the API key `encoded` value.

:::::


Refer to the [{{es}} API documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/connector-apis.html) for details of all available Connector APIs.


### Usage [es-connectors-sharepoint-client-usage] 

To use this connector as a **self-managed connector**, see [*Self-managed connectors*](es-build-connector.md).

For additional operations, see [*Connectors UI in {{kib}}*](es-connectors-usage.md).


### Compatibility [es-connectors-sharepoint-client-compatability] 

The following SharePoint Server versions are compatible with the Elastic connector framework:

* SharePoint 2013
* SharePoint 2016
* SharePoint 2019


### Configuration [es-connectors-sharepoint-client-configuration] 

::::{tip} 
When using the [self-managed connector](es-build-connector.md) workflow, initially these fields will use the default configuration set in the [connector source code](https://github.com/elastic/connectors/tree/main/connectors/sources/sharepoint_server.py). These are set in the `get_default_configuration` function definition.

These configurable fields will be rendered with their respective **labels** in the Kibana UI. Once connected, you’ll be able to update these values in Kibana.

::::


The following configuration fields are required to set up the connector:

`authentication`
:   Authentication mode, either **Basic** or **NTLM**.

`username`
:   The username of the account for the SharePoint Server instance.

`password`
:   The password of the account.

`host_url`
:   The server host url where the SharePoint Server instance is hosted. Examples:

    * `https://192.158.1.38:8080`
    * `https://<tenant_name>.sharepoint.com`


`site_collections`
:   Comma-separated list of site collections to fetch from SharePoint Server. Examples:

    * `collection1`
    * `collection1, collection2`


`ssl_enabled`
:   Whether SSL verification will be enabled. Default value is `False`.

`ssl_ca`
:   Content of SSL certificate needed for the SharePoint Server instance. Keep this field empty, if `ssl_enabled` is set to `False`.

    Example certificate:

    ```txt
    -----BEGIN CERTIFICATE-----
    MIID+jCCAuKgAwIBAgIGAJJMzlxLMA0GCSqGSIb3DQEBCwUAMHoxCzAJBgNVBAYT
    ...
    7RhLQyWn2u00L7/9Omw=
    -----END CERTIFICATE-----
    ```


`retry_count`
:   The number of retry attempts after failed request to the SharePoint Server instance. Default value is `3`.

`use_document_level_security`
:   Toggle to enable [Document level security (DLS)](es-dls.md). When enabled, full syncs will fetch access control lists for each document and store them in the `_allow_access_control` field. Access control syncs fetch users' access control lists and store them in a separate index.

    Once enabled, the following granular permissions toggles will be available:

    * **Fetch unique list permissions**: Enable this option to fetch unique **list** permissions. If this setting is disabled a list will inherit permissions from its parent site.
    * **Fetch unique list item permissions**: Enable this option to fetch unique **list item** permissions. If this setting is disabled a list item will inherit permissions from its parent site.

        ::::{note} 
        If left empty the default value `true` will be used for these granular permissions toggles. Note that these settings may increase sync times.

        ::::



### Deployment using Docker [es-connectors-sharepoint-client-docker] 

You can deploy the SharePoint Server connector as a self-managed connector using Docker. Follow these instructions.

::::{dropdown} **Step 1: Download sample configuration file**
Download the sample configuration file. You can either download it manually or run the following command:

```sh
curl https://raw.githubusercontent.com/elastic/connectors/main/config.yml.example --output ~/connectors-config/config.yml
```

%  NOTCONSOLE

Remember to update the `--output` argument value if your directory name is different, or you want to use a different config file name.

::::


::::{dropdown} **Step 2: Update the configuration file for your self-managed connector**
Update the configuration file with the following settings to match your environment:

* `elasticsearch.host`
* `elasticsearch.api_key`
* `connectors`

If you’re running the connector service against a Dockerized version of Elasticsearch and Kibana, your config file will look like this:

```yaml
# When connecting to your cloud deployment you should edit the host value
elasticsearch.host: http://host.docker.internal:9200
elasticsearch.api_key: <ELASTICSEARCH_API_KEY>

connectors:
  -
    connector_id: <CONNECTOR_ID_FROM_KIBANA>
    service_type: sharepoint_server
    api_key: <CONNECTOR_API_KEY_FROM_KIBANA> # Optional. If not provided, the connector will use the elasticsearch.api_key instead
```

Using the `elasticsearch.api_key` is the recommended authentication method. However, you can also use `elasticsearch.username` and `elasticsearch.password` to authenticate with your Elasticsearch instance.

Note: You can change other default configurations by simply uncommenting specific settings in the configuration file and modifying their values.

::::


::::{dropdown} **Step 3: Run the Docker image**
Run the Docker image with the Connector Service using the following command:

```sh
docker run \
-v ~/connectors-config:/config \
--network "elastic" \
--tty \
--rm \
docker.elastic.co/integrations/elastic-connectors:9.0.0-beta1.0 \
/app/bin/elastic-ingest \
-c /config/config.yml
```

::::


Refer to [`DOCKER.md`](https://github.com/elastic/connectors/tree/main/docs/DOCKER.md) in the `elastic/connectors` repo for more details.

Find all available Docker images in the [official registry](https://www.docker.elastic.co/r/integrations/elastic-connectors).

::::{tip} 
We also have a quickstart self-managed option using Docker Compose, so you can spin up all required services at once: Elasticsearch, Kibana, and the connectors service. Refer to this [README](https://github.com/elastic/connectors/tree/main/scripts/stack#readme) in the `elastic/connectors` repo for more information.

::::



### Documents and syncs [es-connectors-sharepoint-client-documents-syncs] 

The connector syncs the following SharePoint object types:

* Sites and Subsites
* Lists
* List Items and its attachment content
* Document Libraries and its attachment content(include Web Pages)

::::{note} 
* Content from files bigger than 10 MB won’t be extracted by default. Use the [self-managed local extraction service](es-connectors-content-extraction.md#es-connectors-content-extraction-local) to handle larger binary files.
* Permissions are not synced. ***All documents*** indexed to an Elastic deployment will be visible to ***all users with access*** to that Elasticsearch Index.

::::



#### Sync types [es-connectors-sharepoint-client-sync-types] 

[Full syncs](es-connectors-sync-types.md#es-connectors-sync-types-full) are supported by default for all connectors.

This connector also supports [incremental syncs](es-connectors-sync-types.md#es-connectors-sync-types-incremental), but this feature is currently disabled by default. Refer to the linked documentation for enabling incremental syncs.


### Document level security [es-connectors-sharepoint-client-document-level-security] 

Document level security (DLS) enables you to restrict access to documents based on a user’s permissions. Refer to [configuration](es-connectors-sharepoint.md#es-connectors-sharepoint-client-configuration) on this page for how to enable DLS for this connector.

::::{note} 
Refer to [DLS in Search Applications](es-dls-e2e-guide.md) to learn how to ingest data from a connector with DLS enabled, when building a search application. The example uses SharePoint Online as the data source, but the same steps apply to every connector.

::::



### Sync rules [es-connectors-sharepoint-client-sync-rules] 

[Basic sync rules](es-sync-rules.md#es-sync-rules-basic) are identical for all connectors and are available by default.

Advanced sync rules are not available for this connector in the present version. Currently filtering is controlled via ingest pipelines.


### Content Extraction [es-connectors-sharepoint-client-content-extraction] 

See [Content extraction](es-connectors-content-extraction.md).


### Self-managed connector operations [es-connectors-sharepoint-client-connector-client-operations] 


### End-to-end testing [es-connectors-sharepoint-client-testing] 

The connector framework enables operators to run functional tests against a real data source. Refer to [Connector testing](es-build-connector.md#es-build-connector-testing) for more details.

To perform E2E testing for the sharepoint connector, run the following command:

```shell
$ make ftest NAME=sharepoint_server
```

For faster tests, add the `DATA_SIZE=small` flag:

```shell
make ftest NAME=sharepoint_server DATA_SIZE=small
```


### Known issues [es-connectors-sharepoint-client-known-issues] 

There are currently no known issues for this connector. Refer to [Known issues](es-connectors-known-issues.md) for a list of known issues for all connectors.


### Troubleshooting [es-connectors-sharepoint-client-troubleshooting] 

See [Troubleshooting](es-connectors-troubleshooting.md).


### Security [es-connectors-sharepoint-client-security] 

See [Security](es-connectors-security.md).


### Framework and source [es-connectors-sharepoint-client-source] 

This connector is written in Python using the [Elastic connector framework](https://github.com/elastic/connectors/tree/main).

View the [source code for this connector](https://github.com/elastic/connectors/tree/main/connectors/sources/sharepoint_server.py) (branch *main*, compatible with Elastic *9.0*).

%  Closing the collapsible section

::::::


