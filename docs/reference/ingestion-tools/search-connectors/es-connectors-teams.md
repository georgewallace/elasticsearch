---
navigation_title: "Teams"
---

# Elastic Microsoft Teams connector reference [es-connectors-teams]


%  Attributes used in this file

The Microsoft Teams connector is written in Python using the [Elastic connector framework](https://github.com/elastic/connectors/tree/main).

View the [source code for this connector](https://github.com/elastic/connectors/tree/main/connectors/sources/microsoft_teams.py) (branch *main*, compatible with Elastic *9.0*).

%  //////// //// //// //// //// //// //// ////////

%  //////// NATIVE CONNECTOR REFERENCE (MANAGED SERVICE) ///////

%  //////// //// //// //// //// //// //// ////////


## **Elastic managed connector reference** [es-connectors-teams-native-connector-reference] 

::::::{dropdown} View **Elastic managed connector** reference

### Availability and prerequisites [es-connectors-microsoft-teams-native-availability-and-prerequisites] 

This managed connector was introduced in Elastic **8.14.0** as a managed service on Elastic Cloud.

To use this connector natively in Elastic Cloud, satisfy all [managed connector requirements](es-native-connectors.md).

::::{note} 
This connector is in ***technical preview*** and is subject to change. The design and code is less mature than official GA features and is being provided as-is with no warranties. Technical preview features are not subject to the support SLA of official GA features.

::::



### Create a Microsoft Teams connector [es-connectors-teams-create-connector-native] 


## Use the UI [es-connectors-microsoft_teams-create-use-the-ui] 

To create a new Microsoft Teams connector:

1. In the Kibana UI, navigate to the **Search → Content → Connectors** page from the main menu, or use the [global search field](https://www.elastic.co/guide/en/kibana/current/kibana-concepts-analysts.html#_finding_your_apps_and_objects).
2. Follow the instructions to create a new native  **Microsoft Teams** connector.

For additional operations, see [*Connectors UI in {{kib}}*](es-connectors-usage.md).


## Use the API [es-connectors-microsoft_teams-create-use-the-api] 

You can use the {{es}} [Create connector API](https://www.elastic.co/guide/en/elasticsearch/reference/current/connector-apis.html) to create a new native Microsoft Teams connector.

For example:

```console
PUT _connector/my-microsoft_teams-connector
{
  "index_name": "my-elasticsearch-index",
  "name": "Content synced from Microsoft Teams",
  "service_type": "microsoft_teams",
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


### Usage [es-connectors-microsoft-teams-native-usage] 

To use this connector in the UI, select the **Teams** tile when creating a new connector under **Search → Connectors**.

If you’re already familiar with how connectors work, you can also use the [Connector APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/connector-apis.html).

For additional operations, see [*Connectors UI in {{kib}}*](es-connectors-usage.md).


### Connecting to Microsoft Teams [es-connectors-microsoft-teams-native-connecting-to-microsoft-teams] 

To connect to Microsoft Teams you need to [create an Azure Active Directory application and service principal](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) that can access resources. Follow these steps:

1. Go to the [Azure portal](https://portal.azure.com) and sign in with your Azure account.
2. Navigate to the **Azure Active Directory** service.
3. Select **App registrations** from the left-hand menu.
4. Click on the **New registration** button to register a new application.
5. Provide a **name** for your app, and *optionally* select the supported account types (e.g., single tenant, multi-tenant).
6. Click on the **Register** button to create the app registration.
7. After the registration is complete, you will be redirected to the app’s overview page. Take note of the **Application (client) ID** value, as you’ll need it later.
8. Scroll down to the **API permissions** section and click on the "Add a permission" button.
9. In the "Request API permissions pane, select "Microsoft Graph" as the API.
10. Select the following **permissions**:

    * `TeamMember.Read.All` (Delegated)
    * `Team.ReadBasic.All` (Delegated)
    * `TeamsTab.Read.All` (Delegated)
    * `Group.Read.All` (Delegated)
    * `ChannelMessage.Read.All` (Delegated)
    * `Chat.Read` (Delegated) & `Chat.Read.All` (Application)
    * `Chat.ReadBasic` (Delegated) & `Chat.ReadBasic.All` (Application)
    * `Files.Read.All` (Delegated and Application)
    * `Calendars.Read` (Delegated and Application)

11. Click on the **Add permissions** button to add the selected permissions to your app.
12. Click on the **Grant admin consent** button to grant the required permissions to the app. This step requires administrative privileges. **If you are not an admin, you need to request the admin to grant consent via their Azure Portal**.
13. Under the "Certificates & Secrets" tab, go to **Client Secrets**. Generate a new client secret and keep a note of the string under the `Value` column.

After completion, use the following configuration parameters to configure the connector.


### Configuration [es-connectors-microsoft-teams-native-configuration] 

The following configuration fields are required:

`client_id` (required)
:   Unique identifier for your Azure Application, found on the app’s overview page. Example:

    * `ab123453-12a2-100a-1123-93fd09d67394`


`secret_value` (required)
:   String value that the application uses to prove its identity when requesting a token, available under the `Certificates & Secrets` tab of your Azure application menu. Example:

    * `eyav1~12aBadIg6SL-STDfg102eBfCGkbKBq_Ddyu`


`tenant_id` (required)
:   Unique identifier for your Azure Active Directory instance, found on the app’s overview page. Example:

    * `123a1b23-12a3-45b6-7c8d-fc931cfb448d`


`username` (required)
:   Username for your Azure Application. Example:

    * `dummy@3hmr2@onmicrosoft.com`


`password` (required)
:   Password for your Azure Application. Example:

    * `changeme`



#### Content Extraction [es-connectors-microsoft-teams-native-content-extraction] 

Refer to [Content extraction](es-connectors-content-extraction.md).


### Documents and syncs [es-connectors-microsoft-teams-native-documents-and-syncs] 

The connector syncs the following objects and entities:

* **USER_CHATS_MESSAGE**
* **USER_CHAT_TABS**
* **USER_CHAT_ATTACHMENT**
* **USER_CHAT_MEETING_RECORDING**
* **USER_MEETING**
* **TEAMS**
* **TEAM_CHANNEL**
* **CHANNEL_TAB**
* **CHANNEL_MESSAGE**
* **CHANNEL_MEETING**
* **CHANNEL_ATTACHMENT**
* **CALENDAR_EVENTS**

::::{note} 
* Files bigger than 10 MB won’t be extracted.
* Permissions are not synced. **All documents** indexed to an Elastic deployment will be visible to **all users with access** to that Elastic Deployment.

::::



#### Sync types [es-connectors-microsoft-teams-native-sync-types] 

[Full syncs](es-connectors-sync-types.md#es-connectors-sync-types-full) are supported by default for all connectors.

This connector also supports [incremental syncs](es-connectors-sync-types.md#es-connectors-sync-types-incremental).


### Sync rules [es-connectors-microsoft-teams-native-sync-rules] 

[Basic sync rules](es-sync-rules.md#es-sync-rules-basic) are identical for all connectors and are available by default.


### Advanced Sync Rules [es-connectors-microsoft-teams-native-advanced-sync-rules] 

Advanced sync rules are not available for this connector in the present version.


### Known issues [es-connectors-microsoft-teams-native-known-issues] 

* Messages in one-on-one chats for *Chat with Self* users are not fetched via Graph APIs. Therefore, these messages won’t be indexed into Elasticsearch.

Refer to [Known issues](es-connectors-known-issues.md) for a list of known issues for all connectors.


### Troubleshooting [es-connectors-microsoft-teams-native-troubleshooting] 

See [Troubleshooting](es-connectors-troubleshooting.md).


### Security [es-connectors-microsoft-teams-native-security] 

See [Security](es-connectors-security.md).

%  Closing the collapsible section

::::::


%  //////// //// //// //// //// //// //// ////////

%  //////// CONNECTOR CLIENT REFERENCE (SELF-MANAGED) ///////

%  //////// //// //// //// //// //// //// ////////


## **Self-managed connector reference** [es-connectors-teams-connector-client-reference] 

::::::{dropdown} View **self-managed connector** reference

### Availability and prerequisites [es-connectors-microsoft-teams-availability-and-prerequisites] 

This connector is available as a self-managed **self-managed connector**. To use this connector, satisfy all [self-managed connector prerequisites](es-build-connector.md).

::::{note} 
This connector is in **technical preview** and is subject to change. The design and code is less mature than official GA features and is being provided as-is with no warranties. Technical preview features are not subject to the support SLA of official GA features.

::::



### Create a Microsoft Teams connector [es-connectors-teams-client-create-connector-client] 


## Use the UI [es-connectors-microsoft_teams-client-create-use-the-ui] 

To create a new Microsoft Teams connector:

1. In the Kibana UI, navigate to the **Search → Content → Connectors** page from the main menu, or use the [global search field](https://www.elastic.co/guide/en/kibana/current/kibana-concepts-analysts.html#_finding_your_apps_and_objects).
2. Follow the instructions to create a new  **Microsoft Teams** self-managed connector.


## Use the API [es-connectors-microsoft_teams-client-create-use-the-api] 

You can use the {{es}} [Create connector API](https://www.elastic.co/guide/en/elasticsearch/reference/current/connector-apis.html) to create a new self-managed Microsoft Teams self-managed connector.

For example:

```console
PUT _connector/my-microsoft_teams-connector
{
  "index_name": "my-elasticsearch-index",
  "name": "Content synced from Microsoft Teams",
  "service_type": "microsoft_teams"
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


### Usage [es-connectors-microsoft-teams-usage] 

To use this connector as a **self-managed connector**, use the **Microsoft Teams** tile from the connectors list **Customized connector** workflow.

For additional operations, see [*Connectors UI in {{kib}}*](es-connectors-usage.md).


### Connecting to Microsoft Teams [es-connectors-microsoft-teams-connecting-to-microsoft-teams] 

To connect to Microsoft Teams you need to [create an Azure Active Directory application and service principal](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) that can access resources. Follow these steps:

1. Go to the [Azure portal](https://portal.azure.com) and sign in with your Azure account.
2. Navigate to the **Azure Active Directory** service.
3. Select **App registrations** from the left-hand menu.
4. Click on the **New registration** button to register a new application.
5. Provide a **name** for your app, and *optionally* select the supported account types (e.g., single tenant, multi-tenant).
6. Click on the **Register** button to create the app registration.
7. After the registration is complete, you will be redirected to the app’s overview page. Take note of the **Application (client) ID** value, as you’ll need it later.
8. Scroll down to the **API permissions** section and click on the "Add a permission" button.
9. In the "Request API permissions pane, select "Microsoft Graph" as the API.
10. Select the following **permissions**:

    * `TeamMember.Read.All` (Delegated)
    * `Team.ReadBasic.All` (Delegated)
    * `TeamsTab.Read.All` (Delegated)
    * `Group.Read.All` (Delegated)
    * `ChannelMessage.Read.All` (Delegated)
    * `Chat.Read` (Delegated) & `Chat.Read.All` (Application)
    * `Chat.ReadBasic` (Delegated) & `Chat.ReadBasic.All` (Application)
    * `Files.Read.All` (Delegated and Application)
    * `Calendars.Read` (Delegated and Application)

11. Click on the **Add permissions** button to add the selected permissions to your app.
12. Click on the **Grant admin consent** button to grant the required permissions to the app. This step requires administrative privileges. **If you are not an admin, you need to request the admin to grant consent via their Azure Portal**.
13. Under the "Certificates & Secrets" tab, go to **Client Secrets**. Generate a new client secret and keep a note of the string under the `Value` column.

After completion, use the following configuration parameters to configure the connector.


### Configuration [es-connectors-microsoft-teams-configuration] 

The following configuration fields are required:

`client_id` (required)
:   Unique identifier for your Azure Application, found on the app’s overview page. Example:

    * `ab123453-12a2-100a-1123-93fd09d67394`


`secret_value` (required)
:   String value that the application uses to prove its identity when requesting a token, available under the `Certificates & Secrets` tab of your Azure application menu. Example:

    * `eyav1~12aBadIg6SL-STDfg102eBfCGkbKBq_Ddyu`


`tenant_id` (required)
:   Unique identifier for your Azure Active Directory instance, found on the app’s overview page. Example:

    * `123a1b23-12a3-45b6-7c8d-fc931cfb448d`


`username` (required)
:   Username for your Azure Application. Example:

    * `dummy@3hmr2@onmicrosoft.com`


`password` (required)
:   Password for your Azure Application. Example:

    * `changeme`



#### Deployment using Docker [es-connectors-microsoft-teams-client-docker] 

You can deploy the Microsoft Teams connector as a self-managed connector using Docker. Follow these instructions.

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
    service_type: microsoft_teams
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



#### Content Extraction [es-connectors-microsoft-teams-content-extraction] 

Refer to [Content extraction](es-connectors-content-extraction.md).


### Documents and syncs [es-connectors-microsoft-teams-documents-and-syncs] 

The connector syncs the following objects and entities:

* **USER_CHATS_MESSAGE**
* **USER_CHAT_TABS**
* **USER_CHAT_ATTACHMENT**
* **USER_CHAT_MEETING_RECORDING**
* **USER_MEETING**
* **TEAMS**
* **TEAM_CHANNEL**
* **CHANNEL_TAB**
* **CHANNEL_MESSAGE**
* **CHANNEL_MEETING**
* **CHANNEL_ATTACHMENT**
* **CALENDAR_EVENTS**

::::{note} 
* Files bigger than 10 MB won’t be extracted.
* Permissions are not synced. **All documents** indexed to an Elastic deployment will be visible to **all users with access** to that Elastic Deployment.

::::



#### Sync types [es-connectors-microsoft-teams-sync-types] 

[Full syncs](es-connectors-sync-types.md#es-connectors-sync-types-full) are supported by default for all connectors.

This connector also supports [incremental syncs](es-connectors-sync-types.md#es-connectors-sync-types-incremental).


### Sync rules [es-connectors-microsoft-teams-sync-rules] 

[Basic sync rules](es-sync-rules.md#es-sync-rules-basic) are identical for all connectors and are available by default.


### Advanced Sync Rules [es-connectors-microsoft-teams-advanced-sync-rules] 

Advanced sync rules are not available for this connector in the present version.


### End-to-end Testing [es-connectors-microsoft-teams-end-to-end-testing] 

The connector framework enables operators to run functional tests against a real data source. Refer to [Connector testing](es-build-connector.md#es-build-connector-testing) for more details.

To perform E2E testing for the Teams connector, run the following command:

```shell
$ make ftest NAME=microsoft_teams
```

For faster tests, add the `DATA_SIZE=small` flag:

```shell
make ftest NAME=microsoft_teams DATA_SIZE=small
```


### Known issues [es-connectors-microsoft-teams-known-issues] 

* Messages in one-on-one chats for *Chat with Self* users are not fetched via Graph APIs. Therefore, these messages won’t be indexed into Elasticsearch.

Refer to [Known issues](es-connectors-known-issues.md) for a list of known issues for all connectors.


### Troubleshooting [es-connectors-microsoft-teams-troubleshooting] 

See [Troubleshooting](es-connectors-troubleshooting.md).


### Security [es-connectors-microsoft-teams-security] 

See [Security](es-connectors-security.md).

%  Closing the collapsible section

::::::


