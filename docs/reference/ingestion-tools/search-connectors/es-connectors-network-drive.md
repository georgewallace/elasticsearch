---
navigation_title: "Network drive"
---

# Elastic network drive connector reference [es-connectors-network-drive]


%  Attributes used in this file:

The *Elastic network drive connector* is a [connector](es-connectors.md) for network drive data sources. This connector is written in Python using the [Elastic connector framework](https://github.com/elastic/connectors/tree/main).

View the [**source code** for this connector](https://github.com/elastic/connectors/tree/main/connectors/sources/network_drive.py) (branch *main*, compatible with Elastic *9.0*).

::::{admonition} Choose your connector reference
Are you using a managed connector on Elastic Cloud or a self-managed connector? Expand the documentation based on your deployment method.

::::


%  //////// //// //// //// //// //// //// ////////

%  ////////   NATIVE CONNECTOR REFERENCE   ///////

%  //////// //// //// //// //// //// //// ////////


## **Elastic managed connector reference** [es-connectors-network-drive-native-connector-reference] 

:::::{dropdown} View **Elastic managed connector** reference

### Availability and prerequisites [es-connectors-network-drive-prerequisites] 

This connector is available as a **managed connector** on Elastic Cloud, as of **8.9.1**.

To use this connector natively in Elastic Cloud, satisfy all [managed connector requirements](es-native-connectors.md#es-native-connectors-prerequisites).


### Usage [es-connectors-network-drive-usage] 

To use this connector natively in Elastic Cloud, see [*Elastic managed connectors*](es-native-connectors.md).


### Configuration [es-connectors-network-drive-configuration] 

The following configuration fields are required to set up the connector:

Username
:   The username of the account for the network drive. The user must have at least ***read*** permissions for the folder path provided.

Password
:   The password of the account to be used for crawling the network drive.

IP address
:   The server IP address where the network drive is hosted. Default value is `127.0.0.1`.

Port
:   The server port where the network drive service is available. Default value is `445`.

Path
:   * The network drive path the connector will crawl to fetch files. This is the name of the folder shared via SMB. The connector uses the Python [`smbprotocol`](https://github.com/jborean93/smbprotocol) library which supports both **SMB v2** and **v3**.
* Accepts only one path— parent folders can be specified to widen the scope.
* The drive path should use **forward slashes** as path separators. Example:

    * `admin/bin`



Enable document level security
:   Toggle to enable document level security (DLS). When enabled:

    * Full syncs will fetch access control lists for each document and store them in the `_allow_access_control` field.
    * Access control syncs will fetch users' access control lists and store them in a separate index. Default value is `false`.

        ::::{tip} 
        Refer to [Document level security](es-connectors-network-drive.md#es-connectors-network-drive-dls) for more information, including prerequisites and limitations.

        ::::


Identity mappings
:   Path to a CSV file containing user and group SIDs (For Linux Network Drive).

    File should be formatted as follows:

    * Fields separated by semicolons (`;`)
    * Three fields per line: `Username;User-SID;Group-SIDs`
    * Group-SIDs are comma-separated and optional.

        **Example** with one username, user-sid and no group:

        ```text
        user1;S-1;
        ```

        **Example** with one username, user-sid and two groups:

        ```text
        user1;S-1;S-11,S-22
        ```



### Documents and syncs [es-connectors-network-drive-documents-syncs] 

The connector syncs folders as separate documents in Elasticsearch. The following fields will be added for the document type `folder`:

* `create_time`
* `title`
* `path`
* `modified`
* `time`
* `id`

::::{note} 
* Content from files bigger than 10 MB won’t be extracted. (Self-managed connectors can use the [self-managed local extraction service](es-connectors-content-extraction.md#es-connectors-content-extraction-local) to handle larger binary files.)
* Permissions are not synced by default. You must first enable [DLS](es-connectors-network-drive.md#es-connectors-network-drive-client-dls). Otherwise, **all documents** indexed to an Elastic deployment will be visible to **all users with access** to that Elastic Deployment.

::::



#### Sync types [es-connectors-network-drive-sync-types] 

[Full syncs](es-connectors-sync-types.md#es-connectors-sync-types-full) are supported by default for all connectors.

This connector also supports [incremental syncs](es-connectors-sync-types.md#es-connectors-sync-types-incremental).


### Document level security [es-connectors-network-drive-dls] 

Document Level Security (DLS) enables you to restrict access to documents based on a user’s permissions. DLS facilitates the syncing of folder and file permissions, including both user and group level permissions.

::::{note} 
***Note:*** Refer to [DLS in Search Applications](es-dls-e2e-guide.md) to learn how to search data with DLS enabled, when building a search application.

::::



#### Availability [es-connectors-network-drive-dls-availability] 

* The present version of Network Drive connector offers DLS support for Windows network drives only.
* To fetch users and groups in a Windows network drive, account credentials added in the connector configuration should have access to the Powershell of the Windows Server where the network drive is hosted.


### Sync rules [es-connectors-network-drive-sync-rules] 

[Basic sync rules](es-sync-rules.md#es-sync-rules-basic) are identical for all connectors and are available by default.


#### Advanced sync rules [es-connectors-network-drive-sync-rules-advanced] 

::::{note} 
A [full sync](es-connectors-sync-types.md#es-connectors-sync-types-full) is required for advanced sync rules to take effect.

::::


Advanced sync rules are defined through a source-specific DSL JSON snippet. Advanced sync rules for this connector use **glob patterns**.

1. Each rule must contains a glob pattern. This pattern is then matched against all the available folder paths inside the configured drive path.
2. The pattern must begin with the `drive_path` field configured in the connector.
3. If the pattern matches any available folder paths, the contents directly within those folders will be fetched.

The following sections provide examples of advanced sync rules for this connector.

$$$es-connectors-network-drive-indexing-files-and-folders-recursively-within-folders$$$
**Indexing files and folders recursively within folders**

```js
[
  {
    "pattern": "Folder-shared/a/mock/**"
  },
  {
    "pattern": "Folder-shared/b/alpha/**"
  }
]
```

%  NOTCONSOLE

$$$es-connectors-network-drive-indexing-files-and-folders-directly-inside-folder$$$
**Indexing files and folders directly inside folder**

```js
[
  {
    "pattern": "Folder-shared/a/b/test"
  }
]
```

%  NOTCONSOLE

$$$es-connectors-network-drive-indexing-files-and-folders-directly-inside-a-set-of-folders$$$
**Indexing files and folders directly inside a set of folders**

```js
[
  {
    "pattern": "Folder-shared/org/*/all-tests/test[135]"
  }
]
```

%  NOTCONSOLE

$$$es-connectors-network-drive-excluding-files-and-folders-that-match-a-pattern$$$
**Excluding files and folders that match a pattern**

```js
[
  {
    "pattern": "Folder-shared/**/all-tests/test[!7]"
  }
]
```

%  NOTCONSOLE


### Content extraction [es-connectors-network-drive-content-extraction] 

See [Content extraction](es-connectors-content-extraction.md).


### Known issues [es-connectors-network-drive-known-issues] 

There are no known issues for this connector.

See [Known issues](es-connectors-known-issues.md) for any issues affecting all connectors.


### Troubleshooting [es-connectors-network-drive-troubleshooting] 

See [Troubleshooting](es-connectors-troubleshooting.md).


### Security [es-connectors-network-drive-security] 

See [Security](es-connectors-security.md).

%  Closing the collapsible section

:::::


%  //////// //// //// //// //// //// //// ////////

%  //////// CONNECTOR CLIENT REFERENCE     ///////

%  //////// //// //// //// //// //// //// ////////


## **Self-managed connector** [es-connectors-network-drive-connector-client-reference] 

:::::{dropdown} View **self-managed connector** reference

### Availability and prerequisites [es-connectors-network-drive-client-prerequisites] 

This connector is available as a self-managed **self-managed connector**. This self-managed connector is compatible with Elastic versions **8.6.0+**.

To use this connector, satisfy all [self-managed connector requirements](es-build-connector.md).


### Usage [es-connectors-network-drive-client-usage] 

To use this connector as a **self-managed connector**, see [*Self-managed connectors*](es-build-connector.md)For additional usage operations, see [*Connectors UI in {{kib}}*](es-connectors-usage.md).


### Configuration [es-connectors-network-drive-client-configuration] 

::::{tip} 
When using the [self-managed connector](es-build-connector.md) workflow, initially these fields will use the default configuration set in the [connector source code](https://github.com/elastic/connectors/tree/main/connectors/sources/network_drive.py). These are set in the `get_default_configuration` function definition.

These configurable fields will be rendered with their respective **labels** in the Kibana UI. Once connected, you’ll be able to update these values in Kibana.

::::


The following configuration fields are required to set up the connector:

`username`
:   The username of the account for the network drive. The user must have at least ***read*** permissions for the folder path provided.

`password`
:   The password of the account to be used for crawling the network drive.

`server_ip`
:   The server IP address where the network drive is hosted. Default value is `127.0.0.1`.

`server_port`
:   The server port where the network drive service is available. Default value is `445`.

`drive_path`
:   * The network drive path the connector will crawl to fetch files. This is the name of the folder shared via SMB. The connector uses the Python [`smbprotocol`](https://github.com/jborean93/smbprotocol) library which supports both **SMB v2** and **v3**.
* Accepts only one path— parent folders can be specified to widen the scope.
* The drive path should use **forward slashes** as path separators. Example:

    * `admin/bin`



`use_document_level_security`
:   Toggle to enable document level security (DLS). When enabled:

    * Full syncs will fetch access control lists for each document and store them in the `_allow_access_control` field.
    * Access control syncs will fetch users' access control lists and store them in a separate index.

        ::::{tip} 
        Refer to [Document level security](es-connectors-network-drive.md#es-connectors-network-drive-client-dls) for more information, including prerequisites and limitations.

        ::::


`drive_type`
:   The type of network drive to be crawled. The following options are available:

    * `Windows`
    * `Linux`


`identity_mappings`
:   Path to a CSV file containing user and group SIDs (For Linux Network Drive).

    File should be formatted as follows:

    * Fields separated by semicolons (`;`)
    * Three fields per line: `Username;User-SID;Group-SIDs`
    * Group-SIDs are comma-separated and optional.

        **Example** with one username, user-sid and no group:

        ```text
        user1;S-1;
        ```

        **Example** with one username, user-sid and two groups:

        ```text
        user1;S-1;S-11,S-22
        ```



### Deployment using Docker [es-connectors-network-drive-client-docker] 

You can deploy the Network drive connector as a self-managed connector using Docker. Follow these instructions.

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
    service_type: network_drive
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



### Documents and syncs [es-connectors-network-drive-client-documents-syncs] 

The connector syncs folders as separate documents in Elasticsearch. The following fields will be added for the document type `folder`:

* `create_time`
* `title`
* `path`
* `modified`
* `time`
* `id`

::::{note} 
* Content from files bigger than 10 MB won’t be extracted
* Permissions are not synced by default. You must first enable [DLS](es-connectors-network-drive.md#es-connectors-network-drive-client-dls). Otherwise, **all documents** indexed to an Elastic deployment will be visible to **all users with access** to that Elastic Deployment.

::::



#### Sync types [es-connectors-network-drive-client-sync-types] 

[Full syncs](es-connectors-sync-types.md#es-connectors-sync-types-full) are supported by default for all connectors.

This connector also supports [incremental syncs](es-connectors-sync-types.md#es-connectors-sync-types-incremental).


### Document level security [es-connectors-network-drive-client-dls] 

Document Level Security (DLS) enables you to restrict access to documents based on a user’s permissions. DLS facilitates the syncing of folder and file permissions, including both user and group level permissions.

::::{note} 
***Note:*** Refer to [DLS in Search Applications](es-dls-e2e-guide.md) to learn how to search data with DLS enabled, when building a search application.

::::



#### Availability [es-connectors-network-drive-client-dls-availability] 

* The Network Drive self-managed connector offers DLS support for both Windows and Linux network drives.
* To fetch users and groups in a Windows network drive, account credentials added in the connector configuration should have access to the Powershell of the Windows Server where the network drive is hosted.


### Sync rules [es-connectors-network-drive-client-sync-rules] 

[Basic sync rules](es-sync-rules.md#es-sync-rules-basic) are identical for all connectors and are available by default.


#### Advanced sync rules [es-connectors-network-drive-client-sync-rules-advanced] 

::::{note} 
A [full sync](es-connectors-sync-types.md#es-connectors-sync-types-full) is required for advanced sync rules to take effect.

::::


Advanced sync rules are defined through a source-specific DSL JSON snippet. Advanced sync rules for this connector use **glob patterns**.

1. Each rule must contains a glob pattern. This pattern is then matched against all the available folder paths inside the configured drive path.
2. The pattern must begin with the `drive_path` field configured in the connector.
3. If the pattern matches any available folder paths, the contents directly within those folders will be fetched.

The following sections provide examples of advanced sync rules for this connector.

$$$es-connectors-network-drive-client-indexing-files-and-folders-recursively-within-folders$$$
**Indexing files and folders recursively within folders**

```js
[
  {
    "pattern": "Folder-shared/a/mock/**"
  },
  {
    "pattern": "Folder-shared/b/alpha/**"
  }
]
```

%  NOTCONSOLE

$$$es-connectors-network-drive-client-indexing-files-and-folders-directly-inside-folder$$$
**Indexing files and folders directly inside folder**

```js
[
  {
    "pattern": "Folder-shared/a/b/test"
  }
]
```

%  NOTCONSOLE

$$$es-connectors-network-drive-client-indexing-files-and-folders-directly-inside-a-set-of-folders$$$
**Indexing files and folders directly inside a set of folders**

```js
[
  {
    "pattern": "Folder-shared/org/*/all-tests/test[135]"
  }
]
```

%  NOTCONSOLE

$$$es-connectors-network-drive-client-excluding-files-and-folders-that-match-a-pattern$$$
**Excluding files and folders that match a pattern**

```js
[
  {
    "pattern": "Folder-shared/**/all-tests/test[!7]"
  }
]
```

%  NOTCONSOLE


### Content extraction [es-connectors-network-drive-client-content-extraction] 

See [Content extraction](es-connectors-content-extraction.md).


### End-to-end tests [es-connectors-network-drive-client-tests] 

The connector framework enables operators to run functional tests against a real data source. Refer to [Connector testing](es-build-connector.md#es-build-connector-testing) for more details.

To execute a functional test for the Network Drive self-managed connector, run the following command:

```shell
$ make ftest NAME=network_drive
```

By default, this will use a medium-sized dataset. For faster tests add the `DATA_SIZE=small` flag:

```shell
make ftest NAME=network_drive DATA_SIZE=small
```


### Known issues [es-connectors-network-drive-client-known-issues] 

There are no known issues for this connector.

See [Known issues](es-connectors-known-issues.md) for any issues affecting all connectors.


### Troubleshooting [es-connectors-network-drive-client-troubleshooting] 

See [Troubleshooting](es-connectors-troubleshooting.md).


### Security [es-connectors-network-drive-client-security] 

See [Security](es-connectors-security.md).

%  Closing the collapsible section

:::::


