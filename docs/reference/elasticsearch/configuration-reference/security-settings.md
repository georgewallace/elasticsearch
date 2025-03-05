---
navigation_title: "Security settings"
---

# Security settings in {{es}} [security-settings]


You configure `xpack.security` settings to [enable anonymous access](security-settings.md#anonymous-access-settings) and perform message authentication, [set up document and field level security](security-settings.md#field-document-security-settings), [configure realms](security-settings.md#realm-settings), [encrypt communications with SSL](security-settings.md#ssl-tls-settings),and [audit security events](auditing-settings.md).

All of these settings can be added to the `elasticsearch.yml` configuration file, with the exception of the secure settings, which you add to the {{es}} keystore. For more information about creating and updating the {{es}} keystore, see [Secure settings](secure-settings.md).


### General security settings [general-security-settings] 

`xpack.security.enabled`
:   ([Static](settings.md#static-cluster-setting)) Defaults to `true`, which enables {{es}} {security-features} on the node. This setting must be enabled to use Elasticsearch’s authentication, authorization and audit features.<br>

    If set to `false`, {{security-features}} are disabled, which is not recommended. It also affects all {{kib}} instances that connect to this {{es}} instance; you do not need to disable {{security-features}} in those `kibana.yml` files. For more information about disabling {{security-features}} in specific {{kib}} instances, see [{{kib}} security settings](https://www.elastic.co/guide/en/kibana/current/security-settings-kb.html).


`xpack.security.autoconfiguration.enabled`
:   ([Static](settings.md#static-cluster-setting)) Defaults to `true`, which enables [security auto configuration](configuring-stack-security.md).

    If set to `false`, security auto configuration is disabled, which is not recommended. When disabled, security is not configured automatically when starting {{es}} for the first time, which means that you must [manually configure security](manually-configure-security.md).


`xpack.security.enrollment.enabled`
:   ([Static](settings.md#static-cluster-setting)) Defaults to `false`. Controls enrollment (of nodes and {{kib}}) to a local node that’s been [autoconfigured for security](configuring-stack-security.md). When set to `true`, the local node can generate new enrollment tokens. Existing tokens can be used for enrollment if they are still valid.

    The security autoconfiguration process will set this to `true` unless an administrator sets it to `false` before starting {{es}}.


`xpack.security.hide_settings`
:   ([Static](settings.md#static-cluster-setting)) A comma-separated list of settings that are omitted from the results of the [cluster nodes info API](cluster-nodes-info.md). You can use wildcards to include multiple settings in the list. For example, the following value hides all the settings for the ad1 active_directory realm: `xpack.security.authc.realms.active_directory.ad1.*`. The API already omits all `ssl` settings, `bind_dn`, and `bind_password` due to the sensitive nature of the information.

`xpack.security.fips_mode.enabled`
:   ([Static](settings.md#static-cluster-setting)) Enables fips mode of operation. Set this to `true` if you run this {{es}} instance in a FIPS 140-2 enabled JVM. For more information, see [FIPS 140-2](fips-140-compliance.md). Defaults to `false`.

`xpack.security.fips_mode.required_providers`
:   ([Static](settings.md#static-cluster-setting)) Optionally enforce specific Java JCE/JSSE security providers. For example, set this to `["BCFIPS", "BCJSSE"]` (case-insensitive) to require the Bouncy Castle FIPS JCE and JSSE security providers. Only applicable when `xpack.security.fips_mode.enabled` is set to `true`.


### Password hashing settings [password-hashing-settings] 

`xpack.security.authc.password_hashing.algorithm`
:   ([Static](settings.md#static-cluster-setting)) Specifies the hashing algorithm that is used for secure user credential storage. See [Table 2, Password hashing algorithms](security-settings.md#password-hashing-algorithms). If `xpack.security.fips_mode.enabled` is true (see [FIPS 140-2](fips-140-compliance.md)), defaults to `pbkdf2_stretch`. In all other cases, defaults to `bcrypt`.


### Anonymous access settings [anonymous-access-settings] 

You can configure the following anonymous access settings in `elasticsearch.yml`. For more information, see [Enabling anonymous access](anonymous-access.md).

`xpack.security.authc.anonymous.username`
:   ([Static](settings.md#static-cluster-setting)) The username (principal) of the anonymous user. Defaults to `_es_anonymous_user`.

`xpack.security.authc.anonymous.roles`
:   ([Static](settings.md#static-cluster-setting)) The roles to associate with the anonymous user. Required.

`xpack.security.authc.anonymous.authz_exception`
:   ([Static](settings.md#static-cluster-setting)) When `true`, an HTTP 403 response is returned if the anonymous user does not have the appropriate permissions for the requested action. The user is not prompted to provide credentials to access the requested resource. When set to `false`, an HTTP 401 response is returned and the user can provide credentials with the appropriate permissions to gain access. Defaults to `true`.


### Automata Settings [security-automata-settings] 

In places where the {{security-features}} accept wildcard patterns (e.g. index patterns in roles, group matches in the role mapping API), each pattern is compiled into an Automaton. The follow settings are available to control this behaviour.

`xpack.security.automata.max_determinized_states`
:   ([Static](settings.md#static-cluster-setting)) The upper limit on how many automaton states may be created by a single pattern. This protects against too-difficult (e.g. exponentially hard) patterns. Defaults to `100,000`.

`xpack.security.automata.cache.enabled`
:   ([Static](settings.md#static-cluster-setting)) Whether to cache the compiled automata. Compiling automata can be CPU intensive and may slowdown some operations. The cache reduces the frequency with which automata need to be compiled. Defaults to `true`.

`xpack.security.automata.cache.size`
:   ([Static](settings.md#static-cluster-setting)) The maximum number of items to retain in the automata cache. Defaults to `10,000`.

`xpack.security.automata.cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) The length of time to retain in an item in the automata cache (based on most recent usage). Defaults to `48h` (48 hours).


### Document and field level security settings [field-document-security-settings] 

You can set the following document and field level security settings in `elasticsearch.yml`. For more information, see [Setting up field and document level security](field-and-document-access-control.md).

`xpack.security.dls_fls.enabled`
:   ([Static](settings.md#static-cluster-setting)) Set to `false` to prevent document and field level security from being configured. Defaults to `true`.

`xpack.security.dls.bitset.cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) The time-to-live for cached `BitSet` entries for document level security. Document level security queries may depend on Lucene BitSet objects, and these are automatically cached to improve performance. Defaults to expire entries that are unused for `2h` (2 hours).

`xpack.security.dls.bitset.cache.size`
:   ([Static](settings.md#static-cluster-setting)) The maximum memory usage of cached `BitSet` entries for document level security. Document level security queries may depend on Lucene BitSet objects, and these are automatically cached to improve performance. Can be configured as a raw number of bytes (such as `200mb` or `1g`) or a percentage of the node’s JVM heap memory (such as `5%`). When the default value is exceeded, the least recently used entries are evicted. Defaults to `10%` of the heap assigned to the node.


### Token service settings [token-service-settings] 

You can set the following token service settings in `elasticsearch.yml`.

`xpack.security.authc.token.enabled`
:   ([Static](settings.md#static-cluster-setting)) Set to `false` to disable the built-in token service. Defaults to `true` unless `xpack.security.http.ssl.enabled` is `false`. This prevents sniffing the token from a connection over plain http.

`xpack.security.authc.token.timeout`
:   ([Static](settings.md#static-cluster-setting)) The length of time that a token is valid for. By default this value is `20m` or 20 minutes. The maximum value is 1 hour.


### API key service settings [api-key-service-settings] 

You can set the following API key service settings in `elasticsearch.yml`.

`xpack.security.authc.api_key.enabled`
:   ([Static](settings.md#static-cluster-setting)) Set to `false` to disable the built-in API key service. Defaults to `true`.

`xpack.security.authc.api_key.cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) The time-to-live for cached API key entries. A API key id and a hash of its API key are cached for this period of time. Specify the time period using the standard {{es}} [time units](api-conventions.md#time-units). Defaults to `1d`.

`xpack.security.authc.api_key.cache.max_keys`
:   ([Static](settings.md#static-cluster-setting)) The maximum number of API key entries that can live in the cache at any given time. Defaults to 10,000.

`xpack.security.authc.api_key.cache.hash_algo`
:   ([Static](settings.md#static-cluster-setting), Expert) The hashing algorithm that is used for the in-memory cached API key credentials. For possible values, see [Table 1, Cache hash algorithms](security-settings.md#cache-hash-algo). Defaults to `ssha256`.

$$$api-key-service-settings-delete-retention-period$$$

`xpack.security.authc.api_key.delete.retention_period`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) Invalidated or expired API keys older than the retention period are eligible for deletion. Defaults to `7d`.

::::{note} 
Large real-time clock inconsistency across cluster nodes can cause problems with evaluating the API key retention period. That is, if the clock on the node invalidating the API key is significantly different than the one performing the deletion, the key may be retained for longer or shorter than the configured retention period.
::::


`xpack.security.authc.api_key.delete.interval`
:   ([Dynamic](settings.md#dynamic-cluster-setting), Expert) Cluster nodes schedule the automatic deletion of invalidated or expired API keys that are older than the retention period. This setting controls the minimum time interval between two such deletion jobs. Defaults to `24h`.

    ::::{note} 
    This is a low-level setting that currently controls the interval between deletion jobs triggered per-node, not across the cluster.
    ::::


`xpack.security.authc.api_key.delete.timeout`
:   ([Static](settings.md#static-cluster-setting), Expert) Sets the timeout of the internal search and delete call.

`xpack.security.authc.api_key.hashing.algorithm`
:   ([Static](settings.md#static-cluster-setting)) Specifies the hashing algorithm that is used for securing API key credentials. See [Table 3, Secure token hashing algorithms](security-settings.md#secure-token-hashing-algorithms). Defaults to `ssha256`.


### Security domain settings [security-domain-settings] 

%  tag::security-domain-settings-description-tag[]

You configure security domain settings in the `xpack.security.authc.domains` namespace in `elasticsearch.yml`.

For example:

```yaml
xpack:
  security:
    authc:
      domains:
        my_domain: <1>
          realms: [ 'default_native', 'saml1' ] <2>
```

1. Specifies the name of the security domain
2. Specifies the realms that belong to the domain


%  end::security-domain-settings-description-tag[]


### Realm settings [realm-settings] 

%  tag::realm-settings-description-tag[]

You configure realm settings in the `xpack.security.authc.realms` namespace in `elasticsearch.yml`.

For example:

```yaml
xpack.security.authc.realms:

    native.realm1: <1>
        order: 0 <2>
        ...

    ldap.realm2:
        order: 1
        ...

    active_directory.realm3:
        order: 2
        ...
    ...
```

1. Specifies the type of realm (for example, `native`, `ldap`, `active_directory`, `pki`, `file`, `kerberos`, `saml`) and the realm name. This information is required.
2. Specifies priority of a realm in the realm chain. This information is required.


The valid settings vary depending on the realm type. For more information, see [*User authentication*](setting-up-authentication.md).

%  end::realm-settings-description-tag[]


#### Settings valid for all realms [ref-realm-settings] 

%  tag::realm-order-tag[]

`order`
:   ([Static](settings.md#static-cluster-setting)) The priority of the realm within the realm chain. Realms with a lower order are consulted first. The value must be unique for each realm. This setting is required.

%  end::realm-order-tag[]

`enabled`
:   ([Static](settings.md#static-cluster-setting)) Indicates whether a realm is enabled. You can use this setting to disable a realm without removing its configuration information. Defaults to `true`.


#### Native realm settings [ref-native-settings] 

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following optional settings:

`cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) The time-to-live for cached user entries. A user and a hash of its credentials are cached for this period of time. Specify the time period using the standard {{es}} [time units](api-conventions.md#time-units). Defaults to `20m`.

`cache.max_users`
:   ([Static](settings.md#static-cluster-setting)) The maximum number of user entries that can live in the cache at any given time. Defaults to 100,000.

`cache.hash_algo`
:   ([Static](settings.md#static-cluster-setting), Expert) The hashing algorithm that is used for the in-memory cached user credentials. For possible values, see [Table 1, Cache hash algorithms](security-settings.md#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](run-as-privilege.md) and [authorization realms](realm-chains.md#authorization_realms) features). Defaults to `true`.


#### File realm settings [ref-users-settings] 

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings:

`cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) The time-to-live for cached user entries. A user and a hash of its credentials are cached for this configured period of time. Defaults to `20m`. Specify values using the standard {{es}} [time units](api-conventions.md#time-units). Defaults to `20m`.

`cache.max_users`
:   ([Static](settings.md#static-cluster-setting)) The maximum number of user entries that can live in the cache at a given time. Defaults to 100,000.

`cache.hash_algo`
:   ([Static](settings.md#static-cluster-setting), Expert) The hashing algorithm that is used for the in-memory cached user credentials. See [Table 1, Cache hash algorithms](security-settings.md#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](run-as-privilege.md) and [authorization realms](realm-chains.md#authorization_realms) features). Defaults to `true`.


#### LDAP realm settings [ref-ldap-settings] 

In addition to the [Settings valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings:

`url`
:   ([Static](settings.md#static-cluster-setting)) One or more LDAP URLs in the `ldap[s]://<server>:<port>` format. Required.

    To provide multiple URLs, use a YAML array (`["ldap://server1:636", "ldap://server2:636"]`) or comma-separated string (`"ldap://server1:636, ldap://server2:636"`).

    While both are supported, you can’t mix the `ldap` and `ldaps` protocols.


`load_balance.type`
:   ([Static](settings.md#static-cluster-setting)) The behavior to use when there are multiple LDAP URLs defined. For supported values see [load balancing and failover types](security-settings.md#load-balancing). Defaults to `failover`.

`load_balance.cache_ttl`
:   ([Static](settings.md#static-cluster-setting)) When using `dns_failover` or `dns_round_robin` as the load balancing type, this setting controls the amount of time to cache DNS lookups. Defaults to `1h`.

`bind_dn`
:   ([Static](settings.md#static-cluster-setting)) The DN of the user that is used to bind to the LDAP and perform searches. Only applicable in user search mode. If not specified, an anonymous bind is attempted. Defaults to Empty. Due to its potential security impact, `bind_dn` is not exposed via the [nodes info API](cluster-nodes-info.md).

`bind_password`
:   ([Static](settings.md#static-cluster-setting)) [6.3] Use `secure_bind_password` instead. The password for the user that is used to bind to the LDAP directory. Defaults to Empty. Due to its potential security impact, `bind_password` is not exposed via the [nodes info API](cluster-nodes-info.md).

`secure_bind_password`
:   ([Secure](secure-settings.md), [Reloadable](secure-settings.md#reloadable-secure-settings)) The password for the user that is used to bind to the LDAP directory. Defaults to Empty.

`user_dn_templates`
:   ([Static](settings.md#static-cluster-setting)) The DN template that replaces the user name with the string `{{0}}`. This setting is multivalued; you can specify multiple user contexts. Required to operate in user template mode. If `user_search.base_dn` is specified, this setting is not valid. For more information on the different modes, see [LDAP user authentication](ldap-realm.md).

`authorization_realms`
:   ([Static](settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the LDAP realm does not perform role mapping and instead loads the user from the listed realms. The referenced realms are consulted in the order that they are defined in this list. See [Delegating authorization to another realm](realm-chains.md#authorization_realms).

    ::::{note} 
    If any settings starting with `user_search` are specified, the `user_dn_templates` settings are ignored.
    ::::


`user_group_attribute`
:   ([Static](settings.md#static-cluster-setting)) Specifies the attribute to examine on the user for group membership. If any `group_search` settings are specified, this setting is ignored. Defaults to `memberOf`.

`user_full_name_attribute`
:   ([Static](settings.md#static-cluster-setting)) Specifies the attribute to examine on the user for the full name of the user. Defaults to `cn`.

`user_email_attribute`
:   ([Static](settings.md#static-cluster-setting)) Specifies the attribute to examine on the user for the email address of the user. Defaults to `mail`.

`user_search.base_dn`
:   ([Static](settings.md#static-cluster-setting)) Specifies a container DN to search for users. Required to operated in user search mode. If `user_dn_templates` is specified, this setting is not valid. For more information on the different modes, see [LDAP user authentication](ldap-realm.md).

`user_search.scope`
:   ([Static](settings.md#static-cluster-setting)) The scope of the user search. Valid values are `sub_tree`, `one_level` or `base`. `one_level` only searches objects directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is the user object, and that it is the only user considered. Defaults to `sub_tree`.

`user_search.filter`
:   ([Static](settings.md#static-cluster-setting)) Specifies the filter used to search the directory in attempts to match an entry with the username provided by the user. Defaults to `(uid={{0}})`. `{{0}}` is substituted with the username provided when searching.

`user_search.attribute`
:   ([Static](settings.md#static-cluster-setting)) [5.6] Use `user_search.filter` instead. The attribute to match with the username sent with the request. Defaults to `uid`.

`user_search.pool.enabled`
:   ([Static](settings.md#static-cluster-setting)) Enables or disables connection pooling for user search. If set to `false`, a new connection is created for every search. The default is `true` when `bind_dn` is set.

`user_search.pool.size`
:   ([Static](settings.md#static-cluster-setting)) The maximum number of connections to the LDAP server to allow in the connection pool. Defaults to `20`.

`user_search.pool.initial_size`
:   ([Static](settings.md#static-cluster-setting)) The initial number of connections to create to the LDAP server on startup. Defaults to `0`. If the LDAP server is down, values greater than `0` could cause startup failures.

`user_search.pool.health_check.enabled`
:   ([Static](settings.md#static-cluster-setting)) Enables or disables a health check on LDAP connections in the connection pool. Connections are checked in the background at the specified interval. Defaults to `true`.

`user_search.pool.health_check.dn`
:   ([Static](settings.md#static-cluster-setting)) The distinguished name that is retrieved as part of the health check. Defaults to the value of `bind_dn` if present; if not, falls back to `user_search.base_dn`.

`user_search.pool.health_check.interval`
:   ([Static](settings.md#static-cluster-setting)) The interval to perform background checks of connections in the pool. Defaults to `60s`.

`group_search.base_dn`
:   ([Static](settings.md#static-cluster-setting)) The container DN to search for groups in which the user has membership. When this element is absent, {{es}} searches for the attribute specified by `user_group_attribute` set on the user in order to determine group membership.

`group_search.scope`
:   ([Static](settings.md#static-cluster-setting)) Specifies whether the group search should be `sub_tree`, `one_level` or `base`.  `one_level` only searches objects directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is a group object, and that it is the only group considered. Defaults to  `sub_tree`.

`group_search.filter`
:   ([Static](settings.md#static-cluster-setting)) Specifies a filter to use to look up a group. When not set, the realm searches for `group`, `groupOfNames`, `groupOfUniqueNames`, or `posixGroup` with the attributes `member`, `memberOf`, or `memberUid`. Any instance of `{{0}}` in the filter is replaced by the user attribute defined in `group_search.user_attribute`.

`group_search.user_attribute`
:   ([Static](settings.md#static-cluster-setting)) Specifies the user attribute that is fetched and provided as a parameter to the filter. If not set, the user DN is passed into the filter. Defaults to Empty.

`unmapped_groups_as_roles`
:   ([Static](settings.md#static-cluster-setting)) If set to `true`, the names of any unmapped LDAP groups are used as role names and assigned to the user. A group is considered to be *unmapped* if it is not referenced in a [role-mapping file](mapping-roles.md#mapping-roles-file). API-based role mappings are not considered. Defaults to `false`.

`files.role_mapping`
:   ([Static](settings.md#static-cluster-setting)) The [location](security-files.md) for the [YAML role mapping configuration file](mapping-roles.md). Defaults to `ES_PATH_CONF/role_mapping.yml`.

`follow_referrals`
:   ([Static](settings.md#static-cluster-setting)) Specifies whether {{es}} should follow referrals returned by the LDAP server. Referrals are URLs returned by the server that are to be used to continue the LDAP operation (for example, search). Defaults to `true`.

`metadata`
:   ([Static](settings.md#static-cluster-setting)) A list of additional LDAP attributes that should be loaded from the LDAP server and stored in the authenticated user’s metadata field.

`timeout.tcp_connect`
:   ([Static](settings.md#static-cluster-setting)) The TCP connect timeout period for establishing an LDAP connection. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`timeout.tcp_read`
:   ([Static](settings.md#static-cluster-setting)) [7.7] The TCP read timeout period after establishing an LDAP connection. This is equivalent to and is deprecated in favor of `timeout.response` and they cannot be used simultaneously. An `s` at the end indicates seconds, or `ms` indicates milliseconds.

`timeout.response`
:   ([Static](settings.md#static-cluster-setting)) The time interval to wait for the response from the LDAP server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to the value of `timeout.ldap_search`.

`timeout.ldap_search`
:   ([Static](settings.md#static-cluster-setting)) The timeout period for an LDAP search. The value is specified in the request and is enforced by the receiving LDAP Server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`ssl.key`
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.

    If the LDAP server requires client authentication, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`ssl.key_passphrase`
:   ([Static](settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional. [7.17.0] Prefer `ssl.secure_key_passphrase` instead.

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


`ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

`ssl.certificate`
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.

    This certificate is presented to clients when they connect.


`ssl.certificate_authorities`
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.

    You cannot use this setting and `ssl.truststore.path` at the same time.


`ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

+ You cannot use this setting and `ssl.key` at the same time.

`ssl.keystore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.keystore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

`ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`ssl.keystore.secure_key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

+ You cannot use this setting and `ssl.certificate_authorities` at the same time.

`ssl.truststore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

`ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.

`ssl.truststore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the truststore file. It must be either `jks` or `PKCS12`. If the file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.verification_mode`
:   ([Static](settings.md#static-cluster-setting)) Indicates the type of verification when using `ldaps` to protect against man in the middle attacks and certificate forgery.

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


`ssl.supported_protocols`
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


`ssl.cipher_suites`
:   ([Static](settings.md#static-cluster-setting)) Specifies the cipher suites that should be supported when communicating with the LDAP server. Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


% TBD: Can this be updated to using the Java 11 URL instead or does it have to stay java8?

`cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) Specifies the time-to-live for cached user entries. A user and a hash of its credentials are cached for this period of time. Use the standard {{es}} [time units](api-conventions.md#time-units). Defaults to  `20m`.

`cache.max_users`
:   ([Static](settings.md#static-cluster-setting)) Specifies the maximum number of user entries that the cache can contain. Defaults to `100000`.

`cache.hash_algo`
:   ([Static](settings.md#static-cluster-setting), Expert) Specifies the hashing algorithm that is used for the in-memory cached user credentials. See [Table 1, Cache hash algorithms](security-settings.md#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](run-as-privilege.md) and [authorization realms](realm-chains.md#authorization_realms) features). Defaults to `true`.


#### Active Directory realm settings [ref-ad-settings] 

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings:

`url`
:   ([Static](settings.md#static-cluster-setting)) One or more LDAP URLs in the `ldap[s]://<server>:<port>` format. Defaults to `ldap://<domain_name>:389`. This setting is required when connecting using SSL/TLS or when using a custom port.

    To provide multiple URLs, use a YAML array (`["ldap://server1:636", "ldap://server2:636"]`) or comma-separated string (`"ldap://server1:636, ldap://server2:636"`).

    While both are supported, you can’t mix the `ldap` and `ldaps` protocols.

    If no URL is provided, {{es}} uses a default of `ldap://<domain_name>:389`. This default uses the `domain_name` setting value and assumes an unencrypted connection to port 389.


`load_balance.type`
:   ([Static](settings.md#static-cluster-setting)) The behavior to use when there are multiple LDAP URLs defined. For supported values see [load balancing and failover types](security-settings.md#load-balancing). Defaults to `failover`.

`load_balance.cache_ttl`
:   ([Static](settings.md#static-cluster-setting)) When using `dns_failover` or `dns_round_robin` as the load balancing type, this setting controls the amount of time to cache DNS lookups. Defaults to `1h`.

`domain_name`
:   ([Static](settings.md#static-cluster-setting)) The domain name of Active Directory. If the `url` and the `user_search.base_dn` settings are not specified, the cluster can derive those values from this setting. Required.

`bind_dn`
:   ([Static](settings.md#static-cluster-setting)) The DN of the user that is used to bind to Active Directory and perform searches. Defaults to Empty. Due to its potential security impact, `bind_dn` is not exposed via the [nodes info API](cluster-nodes-info.md).

`bind_password`
:   ([Static](settings.md#static-cluster-setting)) [6.3] Use `secure_bind_password` instead. The password for the user that is used to bind to Active Directory. Defaults to Empty. Due to its potential security impact, `bind_password` is not exposed via the [nodes info API](cluster-nodes-info.md).

`secure_bind_password`
:   ([Secure](secure-settings.md), [Reloadable](secure-settings.md#reloadable-secure-settings)) The password for the user that is used to bind to Active Directory. Defaults to Empty.

`unmapped_groups_as_roles`
:   ([Static](settings.md#static-cluster-setting)) If set to `true`, the names of any unmapped Active Directory groups are used as role names and assigned to the user. A group is considered *unmapped* when it is not referenced in any role-mapping files. API-based role mappings are not considered. Defaults to `false`.

`files.role_mapping`
:   ([Static](settings.md#static-cluster-setting)) The [location](security-files.md) for the YAML role mapping configuration file. Defaults to `ES_PATH_CONF/role_mapping.yml`.

`user_search.base_dn`
:   ([Static](settings.md#static-cluster-setting)) The context to search for a user. Defaults to the root of the Active Directory domain.

`user_search.scope`
:   ([Static](settings.md#static-cluster-setting)) Specifies whether the user search should be `sub_tree`, `one_level` or `base`. `one_level` only searches users directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is a user object, and that it is the only user considered. Defaults to `sub_tree`.

`user_search.filter`
:   ([Static](settings.md#static-cluster-setting)) Specifies a filter to use to lookup a user given a username. The default filter looks up `user` objects with either `sAMAccountName` or `userPrincipalName`. If specified, this must be a valid LDAP user search filter. For example `(&(objectClass=user)(sAMAccountName={{0}}))`. For more information, see [Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.upn_filter`
:   ([Static](settings.md#static-cluster-setting)) Specifies a filter to use to lookup a user given a user principal name. The default filter looks up `user` objects with a matching `userPrincipalName`. If specified, this must be a valid LDAP user search filter. For example, `(&(objectClass=user)(userPrincipalName={{1}}))`. `{{1}}` is the full user principal name provided by the user. For more information, see [Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.down_level_filter`
:   ([Static](settings.md#static-cluster-setting)) Specifies a filter to use to lookup a user given a down level logon name (DOMAIN\user). The default filter looks up `user` objects with a matching `sAMAccountName` in the domain provided. If specified, this must be a valid LDAP user search filter. For example, `(&(objectClass=user)(sAMAccountName={{0}}))`. For more information, see [Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.pool.enabled`
:   ([Static](settings.md#static-cluster-setting)) Enables or disables connection pooling for user search. When disabled a new connection is created for every search. The default is `true` when `bind_dn` is provided.

`user_search.pool.size`
:   ([Static](settings.md#static-cluster-setting)) The maximum number of connections to the Active Directory server to allow in the connection pool. Defaults to `20`.

`user_search.pool.initial_size`
:   ([Static](settings.md#static-cluster-setting)) The initial number of connections to create to the Active Directory server on startup. Defaults to `0`. If the LDAP server is down, values greater than 0 could cause startup failures.

`user_search.pool.health_check.enabled`
:   ([Static](settings.md#static-cluster-setting)) Enables or disables a health check on Active Directory connections in the connection pool. Connections are checked in the background at the specified interval. Defaults to `true`.

`user_search.pool.health_check.dn`
:   ([Static](settings.md#static-cluster-setting)) The distinguished name to be retrieved as part of the health check. Defaults to the value of `bind_dn` if that setting is present. Otherwise, it defaults to the value of the `user_search.base_dn` setting.

`user_search.pool.health_check.interval`
:   ([Static](settings.md#static-cluster-setting)) The interval to perform background checks of connections in the pool. Defaults to `60s`.

`group_search.base_dn`
:   ([Static](settings.md#static-cluster-setting)) The context to search for groups in which the user has membership. Defaults to the root of the Active Directory domain.

`group_search.scope`
:   ([Static](settings.md#static-cluster-setting)) Specifies whether the group search should be `sub_tree`, `one_level` or `base`.  `one_level` searches for groups directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is a group object, and that it is the only group considered. Defaults to `sub_tree`.

`metadata`
:   ([Static](settings.md#static-cluster-setting)) A list of additional LDAP attributes that should be loaded from the LDAP server and stored in the authenticated user’s metadata field.

`timeout.tcp_connect`
:   ([Static](settings.md#static-cluster-setting)) The TCP connect timeout period for establishing an LDAP connection. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`timeout.tcp_read`
:   ([Static](settings.md#static-cluster-setting)) [7.7] The TCP read timeout period after establishing an LDAP connection. This is equivalent to and is deprecated in favor of `timeout.response` and they cannot be used simultaneously. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to the value of `timeout.ldap_search`.

`timeout.response`
:   ([Static](settings.md#static-cluster-setting)) The time interval to wait for the response from the AD server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to the value of `timeout.ldap_search`.

`timeout.ldap_search`
:   ([Static](settings.md#static-cluster-setting)) The timeout period for an LDAP search. The value is specified in the request and is enforced by the receiving LDAP Server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`ssl.certificate`
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.

    This certificate is presented to clients when they connect.


`ssl.certificate_authorities`
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.

    You cannot use this setting and `ssl.truststore.path` at the same time.


`ssl.key`
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.

    If the Active Directory server requires client authentication, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`ssl.key_passphrase`
:   ([Static](settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional. [7.17.0] Prefer `ssl.secure_key_passphrase` instead.

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


`ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

`ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`ssl.keystore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

`ssl.secure_keystore.password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

% TBD: Why/how is this different than `ssl.keystore.secure_password`?

`ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

+ You cannot use this setting and `ssl.key` at the same time.

`ssl.keystore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.truststore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

`ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.

`ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

+ You cannot use this setting and `ssl.certificate_authorities` at the same time.

`ssl.truststore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the truststore file. It must be either `jks` or `PKCS12`. If the file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.verification_mode`
:   ([Static](settings.md#static-cluster-setting)) Indicates the type of verification when using `ldaps` to protect against man in the middle attacks and certificate forgery.

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


`ssl.supported_protocols`
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


`ssl.cipher_suites`
:   ([Static](settings.md#static-cluster-setting)) Specifies the cipher suites that should be supported when communicating with the Active Directory server. Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


% TBD: Can this be updated to using the Java 11 URL instead or does it have to stay java8?

`cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) Specifies the time-to-live for cached user entries. A user and a hash of its credentials are cached for this configured period of time. Use the standard Elasticsearch [time units](api-conventions.md#time-units)). Defaults to `20m`.

`cache.max_users`
:   ([Static](settings.md#static-cluster-setting)) Specifies the maximum number of user entries that the cache can contain. Defaults to `100000`.

`cache.hash_algo`
:   ([Static](settings.md#static-cluster-setting), Expert) Specifies the hashing algorithm that is used for the in-memory cached user credentials. See [Table 1, Cache hash algorithms](security-settings.md#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](run-as-privilege.md) and [authorization realms](realm-chains.md#authorization_realms) features). Defaults to `true`.

`follow_referrals`
:   ([Static](settings.md#static-cluster-setting)) If set to `true`, {{es}} follows referrals returned by the LDAP server. Referrals are URLs returned by the server that are to be used to continue the LDAP operation (such as `search`). Defaults to `true`.


#### PKI realm settings [ref-pki-settings] 

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings:

`username_pattern`
:   ([Static](settings.md#static-cluster-setting)) The regular expression pattern used to extract the username from the certificate DN. The username is used for auditing and logging. The username can also be used with the [role mapping API](role-mapping-resources.md) and [authorization delegation](configuring-authorization-delegation.md). The first match group is the used as the username. Defaults to `CN=(.*?)(?:,|$)`.

`certificate_authorities`
:   ([Static](settings.md#static-cluster-setting)) List of paths to the PEM certificate files that should be used to authenticate a user’s certificate as trusted. Defaults to the trusted certificates configured for SSL. This setting cannot be used with `truststore.path`.

`truststore.algorithm`
:   ([Static](settings.md#static-cluster-setting)) Algorithm for the truststore. Defaults to `SunX509`.

`truststore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

If `truststore.path` is set, this setting is required.

`truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.

`truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path of a truststore to use. Defaults to the trusted certificates configured for SSL. This setting cannot be used with `certificate_authorities`.

`files.role_mapping`
:   ([Static](settings.md#static-cluster-setting)) Specifies the [location](security-files.md) of the [YAML role mapping configuration file](mapping-roles.md). Defaults to `ES_PATH_CONF/role_mapping.yml`.

`authorization_realms`
:   ([Static](settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the PKI realm does not perform role mapping and instead loads the user from the listed realms. See [Delegating authorization to another realm](realm-chains.md#authorization_realms).

`cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) Specifies the time-to-live for cached user entries. A user and a hash of its credentials are cached for this period of time. Use the standard {{es}} [time units](api-conventions.md#time-units)). Defaults to `20m`.

`cache.max_users`
:   ([Static](settings.md#static-cluster-setting)) Specifies the maximum number of user entries that the cache can contain. Defaults to `100000`.

`delegation.enabled`
:   ([Static](settings.md#static-cluster-setting)) Generally, in order for the clients to be authenticated by the PKI realm they must connect directly to {{es}}. That is, they must not pass through proxies which terminate the TLS connection. In order to allow for a **trusted** and **smart** proxy, such as Kibana, to sit before {{es}} and terminate TLS connections, but still allow clients to be authenticated on {{es}} by this realm, you need to toggle this to `true`. Defaults to `false`. If delegation is enabled, then either `truststore.path` or `certificate_authorities` setting must be defined. For more details, see [Configuring authentication delegation for PKI realms](pki-realm.md#pki-realm-for-proxied-clients).


#### SAML realm settings [ref-saml-settings] 

%  tag::saml-description-tag[]

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings.

%  end::saml-description-tag[]

%  tag::saml-idp-entity-id-tag[]

`idp.entity_id` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Entity ID of the SAML Identity Provider. An Entity ID is a URI with a maximum length of 1024 characters. It can be a URL ([https://idp.example.com/](https://idp.example.com/)) or a URN (`urn:example.com:idp`) and can be found in the configuration or the SAML metadata of the Identity Provider.

%  end::saml-idp-entity-id-tag[]

%  tag::saml-idp-metadata-path-tag[]

`idp.metadata.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path *(recommended)* or URL to a SAML 2.0 metadata file describing the capabilities and configuration of the Identity Provider. If a path is provided, then it is resolved relative to the {{es}} config directory. If a URL is provided, then it must be either a `file` URL or a `https` URL.

    {{es}} automatically polls this metadata resource and reloads the IdP configuration when changes are detected. File based resources are polled at a frequency determined by the global {{es}} `resource.reload.interval.high` setting, which defaults to 5 seconds. HTTPS resources are polled at a frequency determined by the realm’s `idp.metadata.http.refresh` and `idp.metadata.http.minimum_refresh` settings.

    If the metadata resource is loaded from a file then the file must exist at node startup, if it does not exist then the node will fail to start. If the resource is loaded over HTTPS then (by default) the node will be tolerant of a failure to load the resource - the node will start and will continue to poll the URL for updates. The affected SAML realm will fail to authenticate users until the problem is resolved. To force the node to fail if the metadata is unavailable set `idp.metadata.http.fail_on_error` to `true`.


%  end::saml-idp-metadata-path-tag[]

%  tag::saml-idp-metadata-http-refresh-tag[]

`idp.metadata.http.fail_on_error`
:   ([Static](settings.md#static-cluster-setting)) If set to `true`, the realm will fail on startup (and prevent the node from starting) if it attempts to load metadata over HTTPS and that metadata is not available. If set to `false` (the default), the node will start but the affected SAML realm will not support user authentication until the metadata can be successfully loaded. This setting is ignored if metadata is loaded from a file.

%  end::saml-idp-metadata-http-refresh-tag[]

%  tag::saml-idp-metadata-http-refresh-tag[]

`idp.metadata.http.refresh` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the frequency with which `https` metadata is checked for changes. Defaults to `1h` (1 hour).

    Under some circumstances {{es}} may determine that the metadata needs to be checked more frequently. This may occur if previous attempts to load the metadata encountered an error, or if the metadata indicates that it is due to expire in less than the configured refresh interval. In these cases {{es}} will poll more often, but never more frequently than `idp.metadata.http.minimum_refresh`. If there is an attempt to authenticate against a realm that has not yet loaded metadata successfully, that realm may attempt to load metadata outside of the configured polling frequency.


%  end::saml-idp-metadata-http-refresh-tag[]

%  tag::saml-idp-metadata-http-minimum-refresh-tag[]

`idp.metadata.http.minimum_refresh`
:   ([Static](settings.md#static-cluster-setting)) Controls the minimum frequency with which `https` metadata is checked for changes. In regular operation {{es}} will use the value of `idp.metadata.http.refresh` as the polling interval. However, under some circumstances {{es}} may determine that it needs to poll more frequently. In these cases, the `minimum_refresh` will set the minimum frequency at which the metdata will be checked. Defaults to `5m` (5 minutes) and must not be set to a value greater than `idp.metadata.http.refresh`

%  end::saml-idp-metadata-http-minimum-refresh-tag[]

%  tag::saml-idp-use-single-logout-tag[]

`idp.use_single_logout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Indicates whether to utilise the Identity Provider’s Single Logout service (if one exists in the IdP metadata file). Defaults to `true`.

%  end::saml-idp-use-single-logout-tag[]

%  tag::saml-sp-entity-id-tag[]

`sp.entity_id` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Entity ID to use for this SAML Service Provider. This should be entered as a URI. We recommend that you use the base URL of your Kibana instance. For example, `https://kibana.example.com/`.

%  end::saml-sp-entity-id-tag[]

%  tag::saml-sp-acs-tag[]

`sp.acs` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The URL of the Assertion Consumer Service within {{kib}}. Typically this is the "api/security/saml/callback" endpoint of your Kibana server. For example, `https://kibana.example.com/api/security/saml/callback`.

%  end::saml-sp-acs-tag[]

%  tag::saml-sp-logout-tag[]

`sp.logout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The URL of the Single Logout service within {{kib}}. Typically this is the "logout" endpoint of your Kibana server. For example, `https://kibana.example.com/logout`.

%  end::saml-sp-logout-tag[]

%  tag::saml-attributes-principal-tag[]

`attributes.principal` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s principal (username).

%  end::saml-attributes-principal-tag[]

%  tag::saml-attributes-groups-tag[]

`attributes.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s groups.

%  end::saml-attributes-groups-tag[]

%  tag::saml-attributes-name-tag[]

`attributes.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s full name.

%  end::saml-attributes-name-tag[]

%  tag::saml-attributes-mail-tag[]

`attributes.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s email address.

%  end::saml-attributes-mail-tag[]

%  tag::saml-attributes-dn-tag[]

`attributes.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s X.50 *Distinguished Name*.

%  end::saml-attributes-dn-tag[]

%  tag::saml-attributes-patterns-principal-tag[]

`attribute_patterns.principal` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A Java regular expression that is matched against the SAML attribute specified by `attributes.principal` before it is applied to the user’s *principal* property. The attribute value must match the pattern and the value of the first *capturing group* is used as the principal. For example, `^([^@]+)@example\\.com$` matches email addresses from the "example.com" domain and uses the local-part as the principal.

%  end::saml-attributes-patterns-principal-tag[]

%  tag::saml-attributes-patterns-groups-tag[]

`attribute_patterns.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *group* property.

%  end::saml-attributes-patterns-groups-tag[]

%  tag::saml-attributes-patterns-name-tag[]

`attribute_patterns.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *name* property.

%  end::saml-attributes-patterns-name-tag[]

%  tag::saml-attributes-patterns-mail-tag[]

`attribute_patterns.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *mail* property.

%  end::saml-attributes-patterns-mail-tag[]

%  tag::saml-attributes-patterns-dn-tag[]

`attribute_patterns.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *dn* property.

%  end::saml-attributes-patterns-dn-tag[]

%  tag::saml-attributes-delimiters-groups-tag[]

`attribute_delimiters.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A plain string that is used as a delimiter to split a single-valued SAML attribute specified by `attributes.groups` before it is applied to the user’s *groups* property. For example, splitting the SAML attribute value `engineering,elasticsearch-admins,employees` on a delimiter value of `,` will result in `engineering`, `elasticsearch-admins`, and `employees` as the list of groups for the user. The delimiter will always be split on, regardless of escaping in the input string. This setting does not support multi-valued SAML attributes. It cannot be used together with the `attribute_patterns` setting. You can only configure this setting for the groups attribute.

%  end::saml-attributes-delimiters-groups-tag[]

%  tag::saml-nameid-format-tag[]

`nameid_format` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The NameID format that should be requested when asking the IdP to authenticate the current user. The default is to not include the `nameid_format` attribute.

%  end::saml-nameid-format-tag[]

%  tag::saml-nameid-allow-create-tag[]

`nameid.allow_create` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The value of the `AllowCreate` attribute of the `NameIdPolicy` element in an authentication request. The default value is false.

%  end::saml-nameid-allow-create-tag[]

%  tag::saml-nameid-sp-qualifier-tag[]

`nameid.sp_qualifier` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The value of the `SPNameQualifier` attribute of the `NameIdPolicy` element in an authentication request. The default is to not include the `SPNameQualifier` attribute.

%  end::saml-nameid-sp-qualifier-tag[]

%  tag::saml-force-authn-tag[]

`force_authn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies whether to set the `ForceAuthn` attribute when requesting that the IdP authenticate the current user. If set to `true`, the IdP is required to verify the user’s identity, irrespective of any existing sessions they might have. Defaults to `false`.

%  end::saml-force-authn-tag[]

%  tag::saml-populate-user-metadata-tag[]

`populate_user_metadata` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies whether to populate the {{es}} user’s metadata with the values that are provided by the SAML attributes. Defaults to `true`.

%  end::saml-populate-user-metadata-tag[]

`authorization_realms`
:   ([Static](settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the SAML realm does not perform role mapping and instead loads the user from the listed realms. See [Delegating authorization to another realm](realm-chains.md#authorization_realms).

%  tag::saml-allowed-clock-skew-tag[]

`allowed_clock_skew` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The maximum amount of skew that can be tolerated between the IdP’s clock and the {{es}} node’s clock. Defaults to `3m` (3 minutes).

%  end::saml-allowed-clock-skew-tag[]

%  tag::saml-req-authn-context-tag[]

`req_authn_context_class_ref` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A comma separated list of Authentication Context Class Reference values to be included in the Requested Authentication Context when requesting the IdP to authenticate the current user. The Authentication Context of the corresponding authentication response should contain at least one of the requested values.

    For more information, see [Requesting specific authentication methods](saml-guide-stack.md#req-authn-context).


%  end::saml-req-authn-context-tag[]


#### SAML realm signing settings [ref-saml-signing-settings] 

%  tag::saml-signing-description-tag[]

If a signing key is configured (that is, either `signing.key` or `signing.keystore.path` is set), then {{es}} signs outgoing SAML messages. Signing can be configured using the following settings:

%  end::saml-signing-description-tag[]

%  tag::saml-signing-messages-tag[]

`signing.saml_messages` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A list of SAML message types that should be signed or `*` to sign all messages. Each element in the list should be the local name of a SAML XML Element. Supported element types are `AuthnRequest`, `LogoutRequest` and `LogoutResponse`. Only valid if `signing.key` or `signing.keystore.path` is also specified. Defaults to `*`.

%  end::saml-signing-messages-tag[]

%  tag::saml-signing-key-tag[]

`signing.key` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path to the PEM encoded private key to use for SAML message signing. `signing.key` and `signing.keystore.path` cannot be used at the same time.

%  end::saml-signing-key-tag[]

`signing.secure_key_passphrase` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Secure](secure-settings.md)) Specifies the passphrase to decrypt the PEM encoded private key (`signing.key`) if it is encrypted.

%  tag::saml-signing-certificate-tag[]

`signing.certificate` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path to the PEM encoded certificate (or certificate chain) that corresponds to the `signing.key`. This certificate must also be included in the Service Provider metadata or manually configured within the IdP to allow for signature validation. This setting can only be used if `signing.key` is set.

%  end::saml-signing-certificate-tag[]

%  tag::saml-signing-keystore-path-tag[]

`signing.keystore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path to the keystore that contains a private key and certificate. It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `signing.key` at the same time.

%  end::saml-signing-keystore-path-tag[]

%  tag::saml-signing-keystore-type-tag[]

`signing.keystore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The type of the keystore in `signing.keystore.path`. Must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or "pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

%  end::saml-signing-keystore-type-tag[]

%  tag::saml-signing-keystore-alias-tag[]

`signing.keystore.alias` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the alias of the key within the keystore that should be used for SAML message signing. If the keystore contains more than one private key, this setting must be specified.

%  end::saml-signing-keystore-alias-tag[]

`signing.keystore.secure_password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Secure](secure-settings.md)) The password to the keystore in `signing.keystore.path`.

`signing.keystore.secure_key_password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Secure](secure-settings.md)) The password for the key in the keystore (`signing.keystore.path`). Defaults to the keystore password.


#### SAML realm encryption settings [ref-saml-encryption-settings] 

%  tag::saml-encryption-description-tag[]

If an encryption key is configured (that is, either `encryption.key` or `encryption.keystore.path` is set), then {{es}} publishes an encryption certificate when generating metadata and attempts to decrypt incoming SAML content. Encryption can be configured using the following settings:

%  end::saml-encryption-description-tag[]

%  tag::saml-encryption-key-tag[]

`encryption.key` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path to the PEM encoded private key to use for SAML message decryption. `encryption.key` and `encryption.keystore.path` cannot be used at the same time.

%  end::saml-encryption-key-tag[]

`encryption.secure_key_passphrase`
:   ([Secure](secure-settings.md)) Specifies the passphrase to decrypt the PEM encoded private key (`encryption.key`) if it is encrypted.

%  tag::saml-encryption-certificate-tag[]

`encryption.certificate` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path to the PEM encoded certificate (or certificate chain) that is associated with the `encryption.key`. This certificate must also be included in the Service Provider metadata or manually configured within the IdP to enable message encryption. This setting can be used only if `encryption.key` is set.

%  end::saml-encryption-certificate-tag[]

%  tag::saml-encryption-keystore-path-tag[]

`encryption.keystore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path to the keystore that contains a private key and certificate. It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `encryption.key` at the same time.

%  end::saml-encryption-keystore-path-tag[]

%  tag::saml-encryption-keystore-type-tag[]

`encryption.keystore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The type of the keystore (`encryption.keystore.path`). Must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or "pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

%  end::saml-encryption-keystore-type-tag[]

%  tag::saml-encryption-keystore-alias-tag[]

`encryption.keystore.alias` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the alias of the key within the keystore (`encryption.keystore.path`) that should be used for SAML message decryption. If not specified, all compatible key pairs from the keystore are considered as candidate keys for decryption.

%  end::saml-encryption-keystore-alias-tag[]

`encryption.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password to the keystore (`encryption.keystore.path`).

`encryption.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore (`encryption.keystore.path`). Only a single password is supported. If you are using multiple decryption keys, they cannot have individual passwords.


#### SAML realm SSL settings [ref-saml-ssl-settings] 

%  tag::saml-ssl-description-tag[]

If you are loading the IdP metadata over SSL/TLS (that is, `idp.metadata.path` is a URL using the `https` protocol), the following settings can be used to configure SSL.

::::{note} 
These settings are not used for any purpose other than loading metadata over https.
::::


%  end::saml-ssl-description-tag[]

%  tag::saml-ssl-key-tag[]

`ssl.key` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


%  end::saml-ssl-key-tag[]

%  tag::saml-ssl-key-passphrase-tag[]

`ssl.key_passphrase` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional. [7.17.0] Prefer `ssl.secure_key_passphrase` instead.

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


%  end::saml-ssl-key-passphrase-tag[]

`ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

+ You cannot use this setting and `ssl.key_passphrase` at the same time.

%  tag::saml-ssl-certificate-tag[]

`ssl.certificate` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


%  end::saml-ssl-certificate-tag[]

%  tag::saml-ssl-certificate-authorities-tag[]

`ssl.certificate_authorities` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.


%  end::saml-ssl-certificate-authorities-tag[]

%  tag::saml-ssl-keystore-path-tag[]

`ssl.keystore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

%  end::saml-ssl-keystore-path-tag[]

%  tag::saml-ssl-keystore-type[]

`ssl.keystore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

%  end::saml-ssl-keystore-type[]

%  tag::saml-ssl-keystore-password-tag[]

`ssl.keystore.password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

%  end::saml-ssl-keystore-password-tag[]

`ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

+ You cannot use this setting and `ssl.keystore.password` at the same time.

% TBD: Why is this different name than `ssl.secure_keystore.password` elsewhere in this file?

`ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

+ You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

You cannot use this setting and `ssl.keystore.key_password` at the same time.

%  tag::saml-ssl-truststore-path-tag[]

`ssl.truststore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

%  end::saml-ssl-truststore-path-tag[]

%  tag::saml-ssl-truststore-type-tag[]

`ssl.truststore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The format of the truststore file. It must be either `jks` or `PKCS12`. If the file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`. Otherwise, it defaults to `jks`.

%  end::saml-ssl-truststore-type-tag[]

%  tag::saml-ssl-truststore-password-tag[]

`ssl.truststore.password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

%  end::saml-ssl-truststore-password-tag[]

`ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.

+ This setting cannot be used with `ssl.truststore.password`.

%  tag::saml-ssl-verification-mode-tag[]

`ssl.verification_mode` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the verification of certificates.

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


%  end::saml-ssl-verification-mode-tag[]

%  tag::saml-ssl-supported-prototols-tag[]

`ssl.supported_protocols` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


%  end::saml-ssl-supported-prototols-tag[]

%  tag::saml-ssl-cipher-suites-tag[]

`ssl.cipher_suites` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


%  end::saml-ssl-cipher-suites-tag[]


#### Kerberos realm settings [ref-kerberos-settings] 

%  tag::kerberos-description-tag[]

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings:

%  end::kerberos-description-tag[]

%  tag::kerberos-keytab-path-tag[]

`keytab.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path to the Kerberos keytab file that contains the service principal used by this {{es}} node. This must be a location within the {{es}} configuration directory and the file must have read permissions. Required.

%  end::kerberos-keytab-path-tag[]

%  tag::kerberos-remove-realm-name-tag[]

`remove_realm_name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Set to `true` to remove the realm part of principal names. Principal names in Kerberos have the form `user/instance@REALM`. If this option is `true`, the realm part (`@REALM`) will not be included in the username. Defaults to `false`.

%  end::kerberos-remove-realm-name-tag[]

`krb.debug`
:   ([Static](settings.md#static-cluster-setting)) Set to `true` to enable debug logs for the Java login module that provides support for Kerberos authentication. Defaults to `false`.

%  tag::kerberos-cache-ttl-tag[]

`cache.ttl` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The time-to-live for cached user entries. A user is cached for this period of time. Specify the time period using the standard {{es}} [time units](api-conventions.md#time-units). Defaults to `20m`.

%  end::kerberos-cache-ttl-tag[]

%  tag::kerberos-cache-max-users-tag[]

`cache.max_users` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The maximum number of user entries that can live in the cache at any given time. Defaults to 100,000.

%  end::kerberos-cache-max-users-tag[]

%  tag::kerberos-authorization-realms-tag[]

`authorization_realms` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the Kerberos realm does not perform role mapping and instead loads the user from the listed realms. See [Delegating authorization to another realm](realm-chains.md#authorization_realms).

%  end::kerberos-authorization-realms-tag[]


#### OpenID Connect realm settings [ref-oidc-settings] 

%  tag::oidc-description-tag[]

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings.

%  end::oidc-description-tag[]

%  tag::oidc-op-issuer-tag[]

`op.issuer` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A verifiable Identifier for your OpenID Connect Provider. An Issuer Identifier is usually a case sensitive URL using the https scheme that contains scheme, host, and optionally, port number and path components and no query or fragment components. The value for this setting should be provided by your OpenID Connect Provider.

%  end::oidc-op-issuer-tag[]

%  tag::oidc-op-auth-endpoint-tag[]

`op.authorization_endpoint` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The URL for the Authorization Endpoint at the OpenID Connect Provider. The value for this setting should be provided by your OpenID Connect Provider.

%  end::oidc-op-auth-endpoint-tag[]

%  tag::oidc-token-endpoint-tag[]

`op.token_endpoint` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The URL for the Token Endpoint at the OpenID Connect Provider. The value for this setting should be provided by your OpenID Connect Provider.

%  end::oidc-token-endpoint-tag[]

%  tag::oidc-userinfo-endpoint-tag[]

`op.userinfo_endpoint` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The URL for the User Info Endpoint at the OpenID Connect Provider. The value for this setting should be provided by your OpenID Connect Provider.

%  end::oidc-userinfo-endpoint-tag[]

%  tag::oidc-endsession-endpoint-tag[]

`op.endsession_endpoint` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The URL for the End Session Endpoint at the OpenID Connect Provider. The value for this setting should be provided by your OpenID Connect Provider.

%  end::oidc-endsession-endpoint-tag[]

%  tag::oidc-op-jwkset-path-tag[]

`op.jwkset_path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting))

The file name or URL to a JSON Web Key Set (JWKS) with the public key material used to verify tokens and claims responses signed by the OpenID Connect Provider. A value is considered a file name if it does not begin with `https` or `http`. The file name is resolved relative to the {{es}} configuration directory.  Changes to the file are polled at a frequency determined by the global {{es}} `resource.reload.interval.high` setting, which defaults to 5 seconds.

+ If a URL is provided, then it must begin with `https://` or `http://`. {{es}} automatically caches the retrieved JWK and will attempt to refresh the JWK upon signature verification failure, as this might indicate that the OpenID Connect Provider has rotated the signing keys.

%  end::oidc-op-jwkset-path-tag[]

`authorization_realms`
:   ([Static](settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the OpenID Connect realm does not perform role mapping and instead loads the user from the listed realms. See [Delegating authorization to another realm](realm-chains.md#authorization_realms).

%  tag::rp-client-id-tag[]

`rp.client_id` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The OAuth 2.0 Client Identifier that was assigned to {{es}} during registration at the OpenID Connect Provider.

%  end::rp-client-id-tag[]

`rp.client_secret`
:   ([Secure](secure-settings.md)) The OAuth 2.0 Client Secret that was assigned to {{es}} during registration at the OpenID Connect Provider.

%  tag::rp-client-auth-method-tag[]

`rp.client_auth_method` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The client authentication method used by {{es}} to authenticate to the OpenID Connect Provider. Can be `client_secret_basic`, `client_secret_post`, or `client_secret_jwt`. Defaults to `client_secret_basic`.

%  end::rp-client-auth-method-tag[]

%  tag::rp-client-auth-jwt-signature-algorithm[]

`rp.client_auth_jwt_signature_algorithm` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The signature algorithm that {{es}} uses to sign the JWT with which it authenticates as a client to the OpenID Connect Provider when `client_secret_jwt` is selected for `rp.client_auth_method`. Can be either `HS256`, `HS384`, or `HS512`. Defaults to `HS384`.

%  end::rp-client-auth-jwt-signature-algorithm[]

%  tag::rp-redirect-uri-tag[]

`rp.redirect_uri` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Redirect URI within {{kib}}. If you want to use the authorization code flow, this is the `api/security/oidc/callback` endpoint of your {{kib}} server. If you want to use the implicit flow,  it is the `api/security/oidc/implicit` endpoint. For example, `https://kibana.example.com/api/security/oidc/callback`.

%  end::rp-redirect-uri-tag[]

%  tag::rp-response-type-tag[]

`rp.response_type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) OAuth 2.0 Response Type value that determines the authorization processing flow to be used. Can be `code` for authorization code grant flow, or one of `id_token`, `id_token token` for the implicit flow.

%  end::rp-response-type-tag[]

%  tag::rp-signature-algorithm-tag[]

`rp.signature_algorithm` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The signature algorithm that will be used by {{es}} in order to verify the signature of the id tokens it will receive from the OpenID Connect Provider. Allowed values are `HS256`, `HS384`, `HS512`, `ES256`, `ES384`, `ES512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`. Defaults to `RS256`.

%  end::rp-signature-algorithm-tag[]

%  tag::rp-requested-scopes-tag[]

`rp.requested_scopes` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The scope values that will be requested by the OpenID Connect Provider as part of the Authentication Request. Optional, defaults to `openid`

%  end::rp-requested-scopes-tag[]

%  tag::rp-post-logout-redirect-url-tag[]

`rp.post_logout_redirect_uri` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The Redirect URI (usually within {{kib}}) that the OpenID Connect Provider should redirect the browser to after a successful Single Logout.

%  end::rp-post-logout-redirect-url-tag[]

%  tag::oidc-claims-principal-tag[]

`claims.principal`
:   ([Static](settings.md#static-cluster-setting)) The name of the OpenID Connect claim that contains the user’s principal (username).

%  end::oidc-claims-principal-tag[]

%  tag::oidc-claims-groups-tag[]

`claims.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the OpenID Connect claim that contains the user’s groups.

%  end::oidc-claims-groups-tag[]

%  tag::oidc-claims-mail-tag[]

`claims.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the OpenID Connect claim that contains the user’s full name.

%  end::oidc-claims-mail-tag[]

%  tag::oidc-claims-mail-tag[]

`claims.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the OpenID Connect claim that contains the user’s email address.

%  end::oidc-claims-mail-tag[]

%  tag::oidc-claims-dn-tag[]

`claims.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the OpenID Connect claim that contains the user’s X.509 *Distinguished Name*.

%  end::oidc-claims-dn-tag[]

%  tag::oidc-claim-pattern-principal-tag[]

`claim_patterns.principal` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A Java regular expression that is matched against the OpenID Connect claim specified by `claims.principal` before it is applied to the user’s *principal* property. The attribute value must match the pattern and the value of the first *capturing group* is used as the principal. For example, `^([^@]+)@example\\.com$` matches email addresses from the "example.com" domain and uses the local-part as the principal.

%  end::oidc-claim-pattern-principal-tag[]

%  tag::oidc-claim-pattern-groups-tag[]

`claim_patterns.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `claim_patterns.principal`, but for the *group* property.

%  end::oidc-claim-pattern-groups-tag[]

%  tag::oidc-claim-pattern-name-tag[]

`claim_patterns.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `claim_patterns.principal`, but for the *name* property.

%  end::oidc-claim-pattern-name-tag[]

%  tag::oidc-claim-pattern-mail-tag[]

`claim_patterns.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `claim_patterns.principal`, but for the *mail* property.

%  end::oidc-claim-pattern-mail-tag[]

%  tag::oidc-claim-pattern-dn-tag[]

`claim_patterns.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) As per `claim_patterns.principal`, but for the *dn* property.

%  end::oidc-claim-pattern-dn-tag[]

%  tag::oidc-allowed-clock-skew-tag[]

`allowed_clock_skew` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The maximum allowed clock skew to be taken into consideration when validating id tokens with regards to their creation and expiration times. Defaults to `60s`.

%  end::oidc-allowed-clock-skew-tag[]

%  tag::oidc-populate-user-metadata-tag[]

`populate_user_metadata` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies whether to populate the {{es}} user’s metadata with the values that are provided by the OpenID Connect claims. Defaults to `true`.

%  end::oidc-populate-user-metadata-tag[]

`http.proxy.host`
:   ([Static](settings.md#static-cluster-setting)) Specifies the address of the proxy server that will be used by the internal http client for all back-channel communication to the OpenID Connect Provider endpoints. This includes requests to the Token Endpoint, the Userinfo Endpoint and requests to fetch the JSON Web Key Set from the OP if `op.jwkset_path` is set as a URL.

`http.proxy.scheme`
:   ([Static](settings.md#static-cluster-setting)) Specifies the protocol to use to connect to the proxy server that will be used by the http client for all back-channel communication to the OpenID Connect Provider endpoints. Defaults to `http`. Allowed values are `http` or `https`.

`http.proxy.port`
:   ([Static](settings.md#static-cluster-setting)) Specifies the port of the proxy server that will be used by the http client for all backchannel communication to the OpenID Connect Provider endpoints. Defaults to `80`.

%  tag::oidc-http-connect-timeout-tag[]

`http.connect_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the behavior of the http client used for back-channel communication to the OpenID Connect Provider endpoints. Specifies the timeout until a connection is established. A value of zero means the timeout is not used. Defaults to `5s`.

%  end::oidc-http-connect-timeout-tag[]

%  tag::oidc-http-read-timeout-tag[]

`http.connection_read_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the behavior of the http client used for back-channel communication to the OpenID Connect Provider endpoints. Specifies the timeout used when requesting a connection from the connection manager. Defaults to `5s`

%  end::oidc-http-read-timeout-tag[]

%  tag::oidc-http-socket-timeout[]

`http.socket_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the behavior of the http client used for back-channel communication to the OpenID Connect Provider endpoints. Specifies the socket timeout (SO_TIMEOUT) in milliseconds, which is the timeout for waiting for data or, put differently, a maximum period inactivity between two consecutive data packets). Defaults to `5s`.

%  end::oidc-http-socket-timeout[]

%  tag::oidc-http-max-connections-tag[]

`http.max_connections` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the behavior of the http client used for back-channel communication to the OpenID Connect Provider endpoints. Specifies the maximum number of connections allowed across all endpoints. Defaults to `200`.

%  end::oidc-http-max-connections-tag[]

%  tag::oidc-http-max-endpoint-connections-tag[]

`http.max_endpoint_connections` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the behavior of the http client used for back-channel communication to the OpenID Connect Provider endpoints. Specifies the maximum number of connections allowed per endpoint. Defaults to `200`.

%  end::oidc-http-max-endpoint-connections-tag[]

%  tag::oidc-http-tcp-keepalive-tag[]

`http.tcp.keep_alive` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Whether to enable TCP keepalives on HTTP connections used for back-channel communication to the OpenID Connect Provider endpoints. Defaults to `true`.

%  end::oidc-http-tcp-keepalive-tag[]

%  tag::oidc-http-connection-pool-ttl-tag[]

`http.connection_pool_ttl` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the behavior of the http client used for back-channel communication to the OpenID Connect Provider endpoints. Specifies the time-to-live of connections in the connection pool (default to 3 minutes). A connection is closed if it is idle for more than the specified timeout.

The server can also set the `Keep-Alive` HTTP response header. The effective time-to-live value is the smaller value between this setting and the `Keep-Alive` response header. Configure this setting to `-1` to let the server dictate the value. If the header is not set by the server and the setting has value of `-1`, the time-to-live is infinite and connections never expire.

%  end::oidc-http-connection-pool-ttl-tag[]


#### OpenID Connect realm SSL settings [ref-oidc-ssl-settings] 

%  tag::oidc-ssl-description-tag[]

The following settings can be used to configure SSL for all outgoing http connections to the OpenID Connect Provider endpoints.

::::{note} 
These settings are *only* used for the back-channel communication between {{es}} and the OpenID Connect Provider
::::


%  end::oidc-ssl-description-tag[]

%  tag::oidc-ssl-key-tag[]

`ssl.key` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


%  end::oidc-ssl-key-tag[]

%  tag::oidc-ssl-key-passphrase-tag[]

`ssl.key_passphrase` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional. [7.17.0] Prefer `ssl.secure_key_passphrase` instead.

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


%  end::oidc-ssl-key-passphrase-tag[]

`ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

+ You cannot use this setting and `ssl.key_passphrase` at the same time.

%  tag::oidc-ssl-certificate-tag[]

`ssl.certificate` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


%  end::oidc-ssl-certificate-tag[]

%  tag::oidc-ssl-certificate-authorities-tag[]

`ssl.certificate_authorities` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.


%  end::oidc-ssl-certificate-authorities-tag[]

%  tag::oidc-ssl-keystore-path-tag[]

`ssl.keystore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

%  end::oidc-ssl-keystore-path-tag[]

%  tag::oidc-ssl-keystore-type-tag[]

`ssl.keystore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

%  end::oidc-ssl-keystore-type-tag[]

%  tag::oidc-ssl-keystore-password-tag[]

`ssl.keystore.password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

%  end::oidc-ssl-keystore-password-tag[]

`ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

+ You cannot use this setting and `ssl.keystore.password` at the same time.

`ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

+ You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

+ You cannot use this setting and `ssl.keystore.key_password` at the same time.

%  tag::oidc-ssl-truststore-path-tag[]

`ssl.truststore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

%  end::oidc-ssl-truststore-path-tag[]

%  tag::oidc-ssl-truststore-type-tag[]

`ssl.truststore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The format of the truststore file. It must be either `jks` or `PKCS12`. If the file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`. Otherwise, it defaults to `jks`.

%  end::oidc-ssl-truststore-type-tag[]

%  tag::oidc-ssl-truststore-password-tag[]

`ssl.truststore.password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

%  end::oidc-ssl-truststore-password-tag[]

`ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.

+ You cannot use this setting and `ssl.truststore.password` at the same time.

%  tag::oidc-ssl-verification-mode-tag[]

`ssl.verification_mode` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the verification of certificates.

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


%  end::oidc-ssl-verification-mode-tag[]

%  tag::oidc-ssl-supported-protocols-tag[]

`ssl.supported_protocols` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


%  end::oidc-ssl-supported-protocols-tag[]

%  tag::oidc-ssl-cipher-suites-tag[]

`ssl.cipher_suites` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


%  end::oidc-ssl-cipher-suites-tag[]


#### JWT realm settings [ref-jwt-settings] 

%  tag::jwt-description-tag[]

In addition to the [settings that are valid for all realms](security-settings.md#ref-realm-settings), you can specify the following settings.

%  end::jwt-description-tag[]

%  tag::jwt-token-type-tag[]

`token_type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The token type, `id_token` or `access_token`, that the JWT realm uses to verify incoming JWTs. Defaults to `id_token`.

%  end::jwt-token-type-tag[]

%  tag::jwt-allowed-audiences-tag[]

`allowed_audiences` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A list of allowed JWT audiences that {{es}} should verify. {{es}} will only consume JWTs that were intended for any of these audiences, as denoted by the `aud` claim in the JWT). The audiences are compared with exact string matches and do not support wildcards or regex. Examples of `aud` claim are `https://example.com/client1` and `other_service,elasticsearch`. When `token_type` is `access_token`, the audiences can be optionally denoted by a different claim in the JWT if `aud` does not exist. See also [`fallback_claims.aud`](security-settings.md#security-settings-jwt-fallback-claims-aud).

%  end::jwt-allowed-audiences-tag[]

%  tag::jwt-allowed-clock-skew-tag[]

`allowed_clock_skew` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The maximum allowed clock skew to be taken into consideration when validating JWTs with regards to their creation, not before, and expiration times.

%  end::jwt-allowed-clock-skew-tag[]

%  tag::jwt-allowed-issuer-tag[]

`allowed_issuer` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A verifiable Identifier for your JWT Issuer. An Issuer Identifier is usually a case sensitive URL using the https scheme that contains scheme, host, and optionally, port number and path components and no query or fragment components. However, it can be any string. The value for this setting should be provided by your JWT Issuer. The issuer is compared with exact string matches and do not support wildcards or regex. Examples of `iss` claim are `https://example.com:8443/jwt` and `issuer123`.

%  end::jwt-allowed-issuer-tag[]

%  tag::jwt-allowed-subjects-tag[]

`allowed_subjects` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A list of allowed JWT subjects that {{es}} should verify. {{es}} will only consume JWTs that were issued for any of these subjects, as denoted by the `sub` claim in the JWT. The subjects are compared with exact string matches and do not support wildcards or regex. Examples of `sub` claim are `https://example.com/user1` and `user_1,user2`. When `token_type` is `access_token`, this setting is mandatory and the subject can be optionally denoted by a different claim in the JWT if `sub` does not exist. See also [`fallback_claims.sub`](security-settings.md#security-settings-jwt-fallback-claims-sub).

%  end::jwt-allowed-subjects-tag[]

%  tag::jwt-fallback-claims-sub-tag[]

$$$security-settings-jwt-fallback-claims-sub$$$

`fallback_claims.sub` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The alternative claim to look for the subject information if the `sub` claim does not exist. It is configurable only when the `token_type` is `access_token`. The fallback is applied everywhere the `sub` claim is used.

%  end::jwt-fallback-claims-sub-tag[]

%  tag::jwt-fallback-claims-aud-tag[]

$$$security-settings-jwt-fallback-claims-aud$$$

`fallback_claims.aud` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The alternative claim to look for the audiences information if the `aud` claim does not exist. It is configurable only when the `token_type` is `access_token`. The fallback is applied everywhere the `aud` claim is used.

%  end::jwt-fallback-claims-aud-tag[]

%  tag::jwt-required-claims-tag[]

`required_claims` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Additional claims and associated values that {{es}} should verify. This is a group setting that takes key/value pairs, where the key is a string and the value must be either a string or an array of strings. The values are compared with exact string matches and do not support wildcards or regex.

For example:

```yaml
xpack.security.authc.realms.jwt.jwt1:
  required_claims:
    token_use: "id"
    versions: ["1.0", "2.0"]
```

%  end::jwt-required-claims-tag[]

%  tag::jwt-allowed-signature-algorithms-tag[]

`allowed_signature_algorithms` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) A list of signature algorithms that will be used by {{es}} in order to verify the signature of the JWT it will receive from the JWT Issuer. Defaults to `RS256`. Examples are `HS512,RS512,ES512` and `ES384`. Allowed values are `HS256`, `HS384`, `HS512`, `ES256`, `ES384`, `ES512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`.

%  end::jwt-allowed-signature-algorithms-tag[]

`authorization_realms`
:   ([Static](settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the JWT realm does not perform role mapping and instead loads the user from the listed realms. See [Delegating authorization to another realm](realm-chains.md#authorization_realms).

%  tag::jwt-claims-dn-tag[]

`claims.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the JWT claim that contains the user’s Distinguished Name (DN), which uniquely identifies a user or group.

%  end::jwt-claims-dn-tag[]

%  tag::jwt-claims-pattern-dn-tag[]

`claim_patterns.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Accepts the same Java regular expression as [`claim_patterns.principal`](security-settings.md#jwt-claim-pattern-principal), but for the `dn` property.

%  end::jwt-claims-pattern-dn-tag[]

%  tag::jwt-claims-groups-tag[]

`claims.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the JWT claim that contains the user’s groups, such as `groups` and `roles`.

%  end::jwt-claims-groups-tag[]

%  tag::jwt-claim-pattern-groups-tag[]

`claim_patterns.group` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Accepts the same Java regular expression as [`claim_patterns.principal`](security-settings.md#jwt-claim-pattern-principal), but for the `group` property.

%  end::jwt-claim-pattern-groups-tag[]

%  tag::jwt-claims-mail-tag[]

`claims.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the JWT claim that contains the user’s e-mail address.

%  end::jwt-claims-mail-tag[]

%  tag::jwt-claims-pattern-mail-tag[]

`claim_patterns.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Accepts the same Java regular expression as [`claim_patterns.principal`](security-settings.md#jwt-claim-pattern-principal), but for the `mail` property.

%  end::jwt-claims-pattern-mail-tag[]

%  tag::jwt-claims-name-tag[]

`claims.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The name of the JWT claim that contains the user’s username.

%  end::jwt-claims-name-tag[]

%  tag::jwt-claims-pattern-name-tag[]

`claim_patterns.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Accepts the same Java regular expression as [`claim_patterns.principal`](security-settings.md#jwt-claim-pattern-principal), but for the `name` property.

%  end::jwt-claims-pattern-name-tag[]

%  tag::jwt-claims-principal-tag[]

`claims.principal`
:   ([Static](settings.md#static-cluster-setting)) The name of the JWT claim that contains the user’s principal (username), such as `sub`, `name`, `email`, and `dn`.

%  end::jwt-claims-principal-tag[]

%  tag::jwt-claim-pattern-principal-tag[]

`claim_patterns.principal` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) An optional Java regular expression that is matched against the JWT claim specified by `claims.principal` before it is applied to the user’s `principal` property. The value must match the pattern and the value of the first *capturing group* is used as the principal. For example, `^([^@]+)@example\\.com$` matches email addresses from the `example.com` domain and uses the local-part as the principal. Another example is `sub` which may not need a pattern setting.

%  end::jwt-claim-pattern-principal-tag[]

%  tag::jwt-client-authentication-type-tag[]

`client_authentication.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies whether to use `shared_secret` or `none` to authenticate incoming client requests. If this value is `shared_secret`, the client is authenticated using an HTTP request header that must match a pre-configured secret value. The client must provide this shared secret with every request in the `ES-Client-Authentication` header. If this value is `none`, then the request header `ES-Client-Authentication` is ignored. Defaults to `shared_secret`.

    Enabling client authentication is recommended. If JWT bearer tokens are shared with other clients or services, client authentication restricts which ones are allowed to submit those JWTs to {{es}}.


%  end::jwt-client-authentication-type-tag[]

%  tag::jwt-client-authentication-shared-secret-tag[]

`client_authentication.shared_secret` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Secure](secure-settings.md), [reloadable](secure-settings.md#reloadable-secure-settings)) Secret value string for client authentication. Required if `client_authentication.type` is `shared_secret`.

%  end::jwt-client-authentication-shared-secret-tag[]

%  tag::jwt-client-authentication-rotation-grace-period-tag[]

`client_authentication.rotation_grace_period`
:   ([Static](settings.md#static-cluster-setting)) Sets the grace period for how long after rotating the `client_authentication.shared_secret` is valid. `client_authentication.shared_secret` can be rotated by updating the keystore then calling the [reload API](cluster-nodes-reload-secure-settings.md). Defaults to `1m`.

%  end::jwt-client-authentication-rotation-grace-period-tag[]

%  tag::jwt-http-connect-timeout-tag[]

`http.connect_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Sets the timeout for the HTTP client that is used for fetching the JSON Web Key Set from a remote URL. A value of zero means the timeout is not used. Defaults to `5s`.

%  end::jwt-http-connect-timeout-tag[]

%  tag::jwt-http-read-timeout-tag[]

`http.connection_read_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the HTTP timeout used when requesting a connection from the connection manager. Defaults to `5s`.

%  end::jwt-http-read-timeout-tag[]

%  tag::jwt-http-socket-timeout[]

`http.socket_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the maximum socket timeout (SO_TIMEOUT) for the HTTP client to wait for inactivity between two consecutive data packets. Defaults to `5s`.

%  end::jwt-http-socket-timeout[]

%  tag::jwt-http-max-connections-tag[]

`http.max_connections` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the maximum number of connections allowed across all endpoints.

%  end::jwt-http-max-connections-tag[]

%  tag::jwt-http-max-endpoint-connections-tag[]

`http.max_endpoint_connections` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the maximum number of connections allowed per endpoint.

%  end::jwt-http-max-endpoint-connections-tag[]

`jwt.cache.size`
:   ([Static](settings.md#static-cluster-setting)) Specifies the maximum number of JWT cache entries. If clients use a different JWT for every request, set to `0` to disable the JWT cache. Defaults to `100000`.

`jwt.cache.ttl`
:   ([Static](settings.md#static-cluster-setting)) Specifies the time-to-live for the period of time to cache JWT entries. JWTs can only be cached if client authentication is successful (or disabled). Uses the standard {{es}} [time units](api-conventions.md#time-units). If clients use a different JWT for every request, set to `0` to disable the JWT cache. Defaults to `20m`.

%  tag::jwt-pkc-jwkset-path-tag[]

`pkc_jwkset_path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The file name or URL to a JSON Web Key Set (JWKS) with the public key material that the JWT Realm uses for verifying token signatures. A value is considered a file name if it does not begin with `https`. The file name is resolved relative to the {{es}} configuration directory. If a URL is provided, then it must begin with `https://` (`http://` is not supported). {{es}} automatically caches the JWK set and will attempt to refresh the JWK set upon signature verification failure, as this might indicate that the JWT Provider has rotated the signing keys.

%  end::jwt-pkc-jwkset-path-tag[]

%  tag::jwt-hmac-jwkset-tag[]

`hmac_jwkset` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Secure](secure-settings.md)) Contents of a JSON Web Key Set (JWKS), including the secret key that the JWT realm uses to verify token signatures. This format supports multiple keys and optional attributes, and is preferred over the `hmac_key` setting. Cannot be used in conjunction with the `hmac_key` setting. Refer to [Configure {{es}} to use a JWT realm](jwt-auth-realm.md).

%  end::jwt-hmac-jwkset-tag[]

%  tag::jwt-hmac-key-tag[]

`hmac_key` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Secure](secure-settings.md)) Contents of a single JSON Web Key (JWK), including the secret key that the JWT realm uses to verify token signatures. This format only supports a single key without attributes, and cannot be used with the `hmac_jwkset` setting. This format is compatible with OIDC. The HMAC key must be a UNICODE string, where the key bytes are the UTF-8 encoding of the UNICODE string. The `hmac_jwkset` setting is preferred. Refer to [Configure {{es}} to use a JWT realm](jwt-auth-realm.md).

%  end::jwt-hmac-key-tag[]

%  tag::jwt-populate-user-metadata-tag[]

`populate_user_metadata` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies whether to populate the {{es}} user’s metadata with the values that are provided by the JWT claims. Defaults to `true`.

%  end::jwt-populate-user-metadata-tag[]


#### JWT realm SSL settings [ref-jwt-ssl-settings] 

%  tag::jwt-ssl-description-tag[]

The following settings can be used to configure SSL for fetching the JSON Web Key Set from a remote URL.

::::{note} 
These settings are *only* used for the back-channel communication between {{es}} and the JWT Issuer.
::::


%  end::jwt-ssl-description-tag[]

%  tag::jwt-ssl-key-tag[]

`ssl.key` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


%  end::jwt-ssl-key-tag[]

%  tag::jwt-ssl-key-passphrase-tag[]

`ssl.key_passphrase` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional. [7.17.0] Prefer `ssl.secure_key_passphrase` instead.

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


%  end::jwt-ssl-key-passphrase-tag[]

`ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

+ You cannot use this setting and `ssl.key_passphrase` at the same time.

%  tag::jwt-ssl-certificate-tag[]

`ssl.certificate` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


%  end::jwt-ssl-certificate-tag[]

%  tag::jwt-ssl-certificate-authorities-tag[]

`ssl.certificate_authorities` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.


%  end::jwt-ssl-certificate-authorities-tag[]

%  tag::jwt-ssl-keystore-path-tag[]

`ssl.keystore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

%  end::jwt-ssl-keystore-path-tag[]

%  tag::jwt-ssl-keystore-type-tag[]

`ssl.keystore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

%  end::jwt-ssl-keystore-type-tag[]

%  tag::jwt-ssl-keystore-password-tag[]

`ssl.keystore.password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

%  end::jwt-ssl-keystore-password-tag[]

`ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

+ You cannot use this setting and `ssl.keystore.password` at the same time.

`ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

+ You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

+ You cannot use this setting and `ssl.keystore.key_password` at the same time.

%  tag::jwt-ssl-truststore-path-tag[]

`ssl.truststore.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

%  end::jwt-ssl-truststore-path-tag[]

%  tag::jwt-ssl-truststore-type-tag[]

`ssl.truststore.type` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The format of the truststore file. It must be either `jks` or `PKCS12`. If the file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`. Otherwise, it defaults to `jks`.

%  end::jwt-ssl-truststore-type-tag[]

%  tag::jwt-ssl-truststore-password-tag[]

`ssl.truststore.password` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

%  end::jwt-ssl-truststore-password-tag[]

`ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.

+ You cannot use this setting and `ssl.truststore.password` at the same time.

%  tag::jwt-ssl-verification-mode-tag[]

`ssl.verification_mode` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Controls the verification of certificates.

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


%  end::jwt-ssl-verification-mode-tag[]

%  tag::jwt-ssl-supported-protocols-tag[]

`ssl.supported_protocols` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


%  end::jwt-ssl-supported-protocols-tag[]

%  tag::jwt-ssl-cipher-suites-tag[]

`ssl.cipher_suites` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on {{ess}}")
:   ([Static](settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


%  end::jwt-ssl-cipher-suites-tag[]


#### Load balancing and failover [load-balancing] 

The [static](settings.md#static-cluster-setting) `load_balance.type` setting can have the following values:

* `failover`: The URLs specified are used in the order that they are specified. The first server that can be connected to will be used for all subsequent connections. If a connection to that server fails then the next server that a connection can be established to will be used for subsequent connections.
* `dns_failover`: In this mode of operation, only a single URL may be specified. This URL must contain a DNS name. The system will be queried for all IP addresses that correspond to this DNS name. Connections to the Active Directory or LDAP server will always be tried in the order in which they were retrieved. This differs from `failover` in that there is no reordering of the list and if a server has failed at the beginning of the list, it will still be tried for each subsequent connection.
* `round_robin`: Connections will continuously iterate through the list of provided URLs. If a server is unavailable, iterating through the list of URLs will continue until a successful connection is made.
* `dns_round_robin`: In this mode of operation, only a single URL may be specified. This URL must contain a DNS name. The system will be queried for all IP addresses that correspond to this DNS name. Connections will continuously iterate through the list of addresses. If a server is unavailable, iterating through the list of URLs will continue until a successful connection is made.


### General TLS settings [ssl-tls-settings] 

`xpack.security.ssl.diagnose.trust`
:   ([Static](settings.md#static-cluster-setting)) Controls whether to output diagnostic messages for SSL/TLS trust failures. If this is `true` (the default), a message will be printed to the Elasticsearch log whenever an SSL connection (incoming or outgoing) is rejected due to a failure to establish trust. This diagnostic message contains information that can be used to determine the cause of the failure and assist with resolving the problem. Set to `false` to disable these messages.


#### TLS/SSL key and trusted certificate settings [tls-ssl-key-settings] 

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. If no trusted certificates are configured, the default certificates that are trusted by the JVM will be trusted along with the certificate(s) associated with a key in the same context. The key and certificate must be in place for connections that require client authentication or when acting as a SSL enabled server.

::::{note} 
:name: pkcs12-truststore-note

Storing trusted certificates in a PKCS#12 file, although supported, is uncommon in practice. The [`elasticsearch-certutil` tool](certutil.md), as well as Java’s `keytool`, are designed to generate PKCS#12 files that can be used both as a keystore and as a truststore, but this may not be the case for container files that are created using other tools. Usually, PKCS#12 files only contain secret and private entries. To confirm that a PKCS#12 container includes trusted certificate ("anchor") entries look for `2.16.840.1.113894.746875.1.1: <Unsupported tag 6>` in the `openssl pkcs12 -info` output, or `trustedCertEntry` in the `keytool -list` output.
::::


## HTTP TLS/SSL settings [http-tls-ssl-settings]

You can configure the following TLS/SSL settings.

`xpack.security.http.ssl.enabled`
:   ([Static](settings.md#static-cluster-setting)) Used to enable or disable TLS/SSL on the HTTP networking layer, which {{es}} uses to communicate with other clients. The default is `false`.

`xpack.security.http.ssl.supported_protocols`
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


`xpack.security.http.ssl.client_authentication`
:   ([Static](settings.md#static-cluster-setting)) Controls the server’s behavior in regard to requesting a certificate from client connections. Valid values are `required`, `optional`, and `none`. `required` forces a client to present a certificate, while `optional` requests a client certificate but the client is not required to present one. Defaults to `none`.

`xpack.security.http.ssl.verification_mode`
:   ([Static](settings.md#static-cluster-setting)) The SSL settings in `xpack.security.http.ssl` control a *server context* for TLS, which defines the settings for the TLS connection. The use of `verification_mode` in a TLS *server* is discouraged. Defines how to verify the certificates presented by another party in the TLS connection:

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


`xpack.security.http.ssl.cipher_suites`
:   ([Static](settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


### HTTP TLS/SSL key and trusted certificate settings [security-http-tls-ssl-key-trusted-certificate-settings]

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. A private key and certificate must be configured.


### PEM encoded files [_pem_encoded_files_2]

When using PEM encoded files, use the following settings:

`xpack.security.http.ssl.key`
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`xpack.security.http.ssl.key_passphrase`
:   ([Static](settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional. [7.17.0] Prefer `ssl.secure_key_passphrase` instead.

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


`xpack.security.http.ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

`xpack.security.http.ssl.certificate`
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


`xpack.security.http.ssl.certificate_authorities`
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.



### Java keystore files [_java_keystore_files_2]

When using Java keystore files (JKS), which contain the private key, certificate and certificates that should be trusted, use the following settings:

`xpack.security.http.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.http.ssl.keystore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

`xpack.security.http.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.http.ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`xpack.security.http.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.http.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.http.ssl.truststore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

`xpack.security.http.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.


### PKCS#12 files [security-http-pkcs12-files]

{{es}} can be configured to use PKCS#12 container files (`.p12` or `.pfx` files) that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

`xpack.security.http.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.http.ssl.keystore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`xpack.security.http.ssl.keystore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

`xpack.security.http.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.http.ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`xpack.security.http.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.http.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.http.ssl.truststore.type`
:   ([Static](settings.md#static-cluster-setting)) Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

% TBD:Should this use the ssl-truststore-type definition and default values?

`xpack.security.http.ssl.truststore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

`xpack.security.http.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.



## Transport TLS/SSL settings [transport-tls-ssl-settings]

You can configure the following TLS/SSL settings.

`xpack.security.transport.ssl.enabled`
:   ([Static](settings.md#static-cluster-setting)) Used to enable or disable TLS/SSL on the transport networking layer, which nodes use to communicate with each other. The default is `false`.

`xpack.security.transport.ssl.supported_protocols`
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


`xpack.security.transport.ssl.client_authentication`
:   ([Static](settings.md#static-cluster-setting)) Controls the server’s behavior in regard to requesting a certificate from client connections. Valid values are `required`, `optional`, and `none`. `required` forces a client to present a certificate, while `optional` requests a client certificate but the client is not required to present one. Defaults to `required`.

`xpack.security.transport.ssl.verification_mode`
:   ([Static](settings.md#static-cluster-setting)) Defines how to verify the certificates presented by another party in the TLS connection:

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


`xpack.security.transport.ssl.cipher_suites`
:   ([Static](settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


### Transport TLS/SSL key and trusted certificate settings [security-transport-tls-ssl-key-trusted-certificate-settings]

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. A private key and certificate must be configured.


### PEM encoded files [_pem_encoded_files_3]

When using PEM encoded files, use the following settings:

`xpack.security.transport.ssl.key`
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`xpack.security.transport.ssl.key_passphrase`
:   ([Static](settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional. [7.17.0] Prefer `ssl.secure_key_passphrase` instead.

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


`xpack.security.transport.ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

`xpack.security.transport.ssl.certificate`
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


`xpack.security.transport.ssl.certificate_authorities`
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.



### Java keystore files [_java_keystore_files_3]

When using Java keystore files (JKS), which contain the private key, certificate and certificates that should be trusted, use the following settings:

`xpack.security.transport.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.transport.ssl.keystore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

`xpack.security.transport.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.transport.ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`xpack.security.transport.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.transport.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.transport.ssl.truststore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

`xpack.security.transport.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.


### PKCS#12 files [security-transport-pkcs12-files]

{{es}} can be configured to use PKCS#12 container files (`.p12` or `.pfx` files) that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

`xpack.security.transport.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.transport.ssl.keystore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`xpack.security.transport.ssl.keystore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the keystore. [7.17.0] Prefer `ssl.keystore.secure_password` instead.

% TBD: You cannot use this setting and `ssl.keystore.secure_password` at the same time.

`xpack.security.transport.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.transport.ssl.keystore.key_password`
:   ([Static](settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password. [7.17.0] Prefer `ssl.keystore.secure_key_password` instead.

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.keystore.secure_key_password` at the same time.

`xpack.security.transport.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.transport.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.transport.ssl.truststore.type`
:   ([Static](settings.md#static-cluster-setting)) Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

% TBD:Should this use the ssl-truststore-type definition and default values?

`xpack.security.transport.ssl.truststore.password`
:   ([Static](settings.md#static-cluster-setting)) The password for the truststore. [7.17.0] Prefer `ssl.truststore.secure_password` instead.

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


% TBD: You cannot use this setting and `ssl.truststore.secure_password` at the same time.

`xpack.security.transport.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.



## Remote cluster server (API key based model) TLS/SSL settings [remote-cluster-server-tls-ssl-settings]

You can configure the following TLS/SSL settings.

`xpack.security.remote_cluster_server.ssl.enabled`
:   ([Static](settings.md#static-cluster-setting)) Used to enable or disable TLS/SSL on the remote cluster server networking layer, which {{es}} uses to communicate with remote cluster clients. The default is `true`.

`xpack.security.remote_cluster_server.ssl.supported_protocols`
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


`xpack.security.remote_cluster_server.ssl.client_authentication`
:   ([Static](settings.md#static-cluster-setting)) Controls the server’s behavior in regard to requesting a certificate from client connections. Valid values are `required`, `optional`, and `none`. `required` forces a client to present a certificate, while `optional` requests a client certificate but the client is not required to present one. Defaults to `none`.

`xpack.security.remote_cluster_server.ssl.verification_mode`
:   ([Static](settings.md#static-cluster-setting)) The SSL settings in `xpack.security.remote_cluster_server.ssl` control a *server context* for TLS, which defines the settings for the TLS connection. The use of `verification_mode` in a TLS *server* is discouraged. Defines how to verify the certificates presented by another party in the TLS connection:

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


`xpack.security.remote_cluster_server.ssl.cipher_suites`
:   ([Static](settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


### Remote cluster server (API key based model) TLS/SSL key and trusted certificate settings [security-remote-cluster-server-tls-ssl-key-trusted-certificate-settings]

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. A private key and certificate must be configured.


### PEM encoded files [_pem_encoded_files_4]

When using PEM encoded files, use the following settings:

`xpack.security.remote_cluster_server.ssl.key`
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`xpack.security.remote_cluster_server.ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

`xpack.security.remote_cluster_server.ssl.certificate`
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


`xpack.security.remote_cluster_server.ssl.certificate_authorities`
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.



### Java keystore files [_java_keystore_files_4]

When using Java keystore files (JKS), which contain the private key, certificate and certificates that should be trusted, use the following settings:

`xpack.security.remote_cluster_server.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.remote_cluster_server.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.remote_cluster_server.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.remote_cluster_server.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.remote_cluster_server.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.


### PKCS#12 files [security-remote-cluster-server-pkcs12-files]

{{es}} can be configured to use PKCS#12 container files (`.p12` or `.pfx` files) that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

`xpack.security.remote_cluster_server.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.remote_cluster_server.ssl.keystore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`xpack.security.remote_cluster_server.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.remote_cluster_server.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.remote_cluster_server.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.remote_cluster_server.ssl.truststore.type`
:   ([Static](settings.md#static-cluster-setting)) Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

% TBD:Should this use the ssl-truststore-type definition and default values?

`xpack.security.remote_cluster_server.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.



## Remote cluster client (API key based model) TLS/SSL settings [remote-cluster-client-tls-ssl-settings]

You can configure the following TLS/SSL settings.

`xpack.security.remote_cluster_client.ssl.enabled`
:   ([Static](settings.md#static-cluster-setting)) Used to enable or disable TLS/SSL on the remote cluster client networking layer, which {{es}} uses to communicate with remote cluster servers. The default is `true`.

`xpack.security.remote_cluster_client.ssl.supported_protocols`
:   ([Static](settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    {{es}} relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](jdk-tls-versions.md) for more information.

    ::::{note} 
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](fips-140-compliance.md).
    ::::


`xpack.security.remote_cluster_client.ssl.verification_mode`
:   ([Static](settings.md#static-cluster-setting)) Defines how to verify the certificates presented by another party in the TLS connection:

    ::::{dropdown} Valid values
    `full`
    :   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.

    `certificate`
    :   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.

    `none`
    :   Performs no certificate validation.

        ::::{important} 
        Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
        ::::


    ::::


    Defaults to `full`.


`xpack.security.remote_cluster_client.ssl.cipher_suites`
:   ([Static](settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.md#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).


### Remote cluster client (API key based model) TLS/SSL key and trusted certificate settings [security-remote-cluster-client-tls-ssl-key-trusted-certificate-settings]

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. A private key and certificate are optional and would be used if the server requires client authentication for PKI authentication.


### PEM encoded files [_pem_encoded_files_5]

When using PEM encoded files, use the following settings:

`xpack.security.remote_cluster_client.ssl.key`
:   ([Static](settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`xpack.security.remote_cluster_client.ssl.secure_key_passphrase`
:   ([Secure](secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

% TBD: You cannot use this setting and `ssl.key_passphrase` at the same time.

`xpack.security.remote_cluster_client.ssl.certificate`
:   ([Static](settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


`xpack.security.remote_cluster_client.ssl.certificate_authorities`
:   ([Static](settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.



### Java keystore files [_java_keystore_files_5]

When using Java keystore files (JKS), which contain the private key, certificate and certificates that should be trusted, use the following settings:

`xpack.security.remote_cluster_client.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.remote_cluster_client.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.remote_cluster_client.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.remote_cluster_client.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.remote_cluster_client.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.


### PKCS#12 files [security-remote-cluster-client-pkcs12-files]

{{es}} can be configured to use PKCS#12 container files (`.p12` or `.pfx` files) that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

`xpack.security.remote_cluster_client.ssl.keystore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


% TBD: It must be either a Java keystore (jks) or a PKCS#12 file.

% TBD: You cannot use this setting and `ssl.key` at the same time.

`xpack.security.remote_cluster_client.ssl.keystore.type`
:   ([Static](settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`xpack.security.remote_cluster_client.ssl.keystore.secure_password`
:   ([Secure](secure-settings.md)) The password for the keystore.

% TBD: You cannot use this setting and `ssl.keystore.password` at the same time.

`xpack.security.remote_cluster_client.ssl.keystore.secure_key_password`
:   ([Secure](secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

% TBD: You cannot use this setting and `ssl.keystore.key_password` at the same time.

`xpack.security.remote_cluster_client.ssl.truststore.path`
:   ([Static](settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


% TBD: You cannot use this setting and `ssl.certificate_authorities` at the same time.

`xpack.security.remote_cluster_client.ssl.truststore.type`
:   ([Static](settings.md#static-cluster-setting)) Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

% TBD:Should this use the ssl-truststore-type definition and default values?

`xpack.security.remote_cluster_client.ssl.truststore.secure_password`
:   ([Secure](secure-settings.md)) Password for the truststore.

% TBD: You cannot use this setting and `ssl.truststore.password` at the same time.


#### Transport profile TLS/SSL settings [ssl-tls-profile-settings] 

The same settings that are available for the [default transport](security-settings.md#transport-tls-ssl-settings) are also available for each transport profile. By default, the settings for a transport profile will be the same as the default transport unless they are specified.

As an example, lets look at the key setting. For the default transport this is `xpack.security.transport.ssl.key`. In order to use this setting in a transport profile, use the prefix `transport.profiles.$PROFILE.xpack.security.` and append the portion of the setting after `xpack.security.transport.`. For the key setting, this would be `transport.profiles.$PROFILE.xpack.security.ssl.key`.


## IP filtering settings [ip-filtering-settings] 

You can configure the following settings for [IP filtering](ip-filtering.md).

`xpack.security.transport.filter.allow`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to allow.

`xpack.security.transport.filter.deny`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to deny.

`xpack.security.http.filter.allow`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to allow just for HTTP.

`xpack.security.http.filter.deny`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to deny just for HTTP.

`transport.profiles.$PROFILE.xpack.security.filter.allow`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to allow for this profile.

`transport.profiles.$PROFILE.xpack.security.filter.deny`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to deny for this profile.

`xpack.security.remote_cluster.filter.allow`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to allow just for the [remote cluster server configured with the API key based model](remote-clusters-api-key.md).

`xpack.security.remote_cluster.filter.deny`
:   ([Dynamic](settings.md#dynamic-cluster-setting)) List of IP addresses to deny just for the remote cluster server configured with the [API key based model](remote-clusters-api-key.md).


## User cache and password hash algorithms [hashing-settings] 

Certain realms store user credentials in memory. To limit exposure to credential theft and mitigate credential compromise, the cache only stores a hashed version of the user credentials in memory. By default, the user cache is hashed with a salted `sha-256` hash algorithm. You can use a different hashing algorithm by setting the [static](settings.md#static-cluster-setting) `cache.hash_algo` realm settings to any of the following values:

$$$cache-hash-algo$$$

|     |     |     |     |
| --- | --- | --- | --- |
| Algorithm |  |  | Description |
| `ssha256` |  |  | Uses a salted `sha-256` algorithm (default). |
| `md5` |  |  | Uses `MD5` algorithm. |
| `sha1` |  |  | Uses `SHA1` algorithm. |
| `bcrypt` |  |  | Uses `bcrypt` algorithm with salt generated in 1024 rounds. |
| `bcrypt4` |  |  | Uses `bcrypt` algorithm with salt generated in 16 rounds. |
| `bcrypt5` |  |  | Uses `bcrypt` algorithm with salt generated in 32 rounds. |
| `bcrypt6` |  |  | Uses `bcrypt` algorithm with salt generated in 64 rounds. |
| `bcrypt7` |  |  | Uses `bcrypt` algorithm with salt generated in 128 rounds. |
| `bcrypt8` |  |  | Uses `bcrypt` algorithm with salt generated in 256 rounds. |
| `bcrypt9` |  |  | Uses `bcrypt` algorithm with salt generated in 512 rounds. |
| `pbkdf2` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations. |
| `pbkdf2_1000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000 iterations. |
| `pbkdf2_10000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations. |
| `pbkdf2_50000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 50000 iterations. |
| `pbkdf2_100000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 100000 iterations. |
| `pbkdf2_500000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                              pseudorandom function using 500000 iterations. |
| `pbkdf2_1000000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000000 iterations. |
| `pbkdf2_stretch` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_1000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_10000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_50000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 50000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_100000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 100000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_500000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 500000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_1000000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000000 iterations, after hashing the                             initial input with SHA512 first. |
| `noop`,`clear_text` |  |  | Doesn’t hash the credentials and keeps it in clear text in                            memory. CAUTION: keeping clear text is considered insecure                            and can be compromised at the OS level (for example through                            memory dumps and using `ptrace`). |

Likewise, realms that store passwords hash them using cryptographically strong and password-specific salt values. You can configure the algorithm for password hashing by setting the [static](settings.md#static-cluster-setting) `xpack.security.authc.password_hashing.algorithm` setting to one of the following:

$$$password-hashing-algorithms$$$

| Algorithm |  |  | Description |
| --- | --- | --- | --- |
| `bcrypt` |  |  | Uses `bcrypt` algorithm with salt generated in 1024 rounds. (default) |
| `bcrypt4` |  |  | Uses `bcrypt` algorithm with salt generated in 16 rounds. |
| `bcrypt5` |  |  | Uses `bcrypt` algorithm with salt generated in 32 rounds. |
| `bcrypt6` |  |  | Uses `bcrypt` algorithm with salt generated in 64 rounds. |
| `bcrypt7` |  |  | Uses `bcrypt` algorithm with salt generated in 128 rounds. |
| `bcrypt8` |  |  | Uses `bcrypt` algorithm with salt generated in 256 rounds. |
| `bcrypt9` |  |  | Uses `bcrypt` algorithm with salt generated in 512 rounds. |
| `bcrypt10` |  |  | Uses `bcrypt` algorithm with salt generated in 1024 rounds. |
| `bcrypt11` |  |  | Uses `bcrypt` algorithm with salt generated in 2048 rounds. |
| `bcrypt12` |  |  | Uses `bcrypt` algorithm with salt generated in 4096 rounds. |
| `bcrypt13` |  |  | Uses `bcrypt` algorithm with salt generated in 8192 rounds. |
| `bcrypt14` |  |  | Uses `bcrypt` algorithm with salt generated in 16384 rounds. |
| `pbkdf2` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations. |
| `pbkdf2_1000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000 iterations. |
| `pbkdf2_10000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations. |
| `pbkdf2_50000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 50000 iterations. |
| `pbkdf2_100000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 100000 iterations. |
| `pbkdf2_500000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                              pseudorandom function using 500000 iterations. |
| `pbkdf2_1000000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000000 iterations. |
| `pbkdf2_stretch` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_1000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_10000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_50000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 50000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_100000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 100000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_500000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 500000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_1000000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000000 iterations, after hashing the                             initial input with SHA512 first. |

Furthermore, {{es}} supports authentication via securely-generated high entropy tokens, for instance [API keys](security-api-create-api-key.md). Analogous to passwords, only the tokens' hashes are stored. Since the tokens are guaranteed to have sufficiently high entropy to resist offline attacks, secure salted hash functions are supported in addition to the password-hashing algorithms mentioned above.

You can configure the algorithm for API key stored credential hashing by setting the [static](settings.md#static-cluster-setting) `xpack.security.authc.api_key.hashing.algorithm` setting to one of the following

$$$secure-token-hashing-algorithms$$$

| Algorithm |  |  | Description |
| --- | --- | --- | --- |
| `ssha256` |  |  | Uses a salted `sha-256` algorithm. (default) |
| `bcrypt` |  |  | Uses `bcrypt` algorithm with salt generated in 1024 rounds. |
| `bcrypt4` |  |  | Uses `bcrypt` algorithm with salt generated in 16 rounds. |
| `bcrypt5` |  |  | Uses `bcrypt` algorithm with salt generated in 32 rounds. |
| `bcrypt6` |  |  | Uses `bcrypt` algorithm with salt generated in 64 rounds. |
| `bcrypt7` |  |  | Uses `bcrypt` algorithm with salt generated in 128 rounds. |
| `bcrypt8` |  |  | Uses `bcrypt` algorithm with salt generated in 256 rounds. |
| `bcrypt9` |  |  | Uses `bcrypt` algorithm with salt generated in 512 rounds. |
| `bcrypt10` |  |  | Uses `bcrypt` algorithm with salt generated in 1024 rounds. |
| `bcrypt11` |  |  | Uses `bcrypt` algorithm with salt generated in 2048 rounds. |
| `bcrypt12` |  |  | Uses `bcrypt` algorithm with salt generated in 4096 rounds. |
| `bcrypt13` |  |  | Uses `bcrypt` algorithm with salt generated in 8192 rounds. |
| `bcrypt14` |  |  | Uses `bcrypt` algorithm with salt generated in 16384 rounds. |
| `pbkdf2` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations. |
| `pbkdf2_1000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000 iterations. |
| `pbkdf2_10000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations. |
| `pbkdf2_50000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 50000 iterations. |
| `pbkdf2_100000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 100000 iterations. |
| `pbkdf2_500000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                              pseudorandom function using 500000 iterations. |
| `pbkdf2_1000000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000000 iterations. |
| `pbkdf2_stretch` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_1000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_10000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 10000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_50000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 50000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_100000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 100000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_500000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 500000 iterations, after hashing the                             initial input with SHA512 first. |
| `pbkdf2_stretch_1000000` |  |  | Uses `PBKDF2` key derivation function with `HMAC-SHA512` as a                             pseudorandom function using 1000000 iterations, after hashing the                             initial input with SHA512 first. |



