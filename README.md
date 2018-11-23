# Databricks API Documentation
*This package is a Python Implementation of the [Databricks API](https://docs.databricks.com/api/latest/index.html) for structured and programmatic use. This Python implementation requires that your Databricks API Token be saved as an environment variable in your system:* `export DATABRICKS_TOKEN=MY_DATABRICKS_TOKEN`

## Installation
You can either use `pip install databricksapi` to install it globally, or you can clone the repository. Please note that only compatability with Python 3.7+ is guaranteed.

## APIs Included  
* Token
* Secrets
* Clusters
* SCIM (Experimental)
* Jobs
* DBFS
* Groups
* Instance Profiles
* Libraries
* Workspace

## Token API
The Token API allows any user to create, list, and revoke tokens that can be used to authenticate and access Databricks REST APIs. Initial authentication to this API is the same as for all of the Databricks API endpoints.

### Methods
1. createToken(*lifetime_seconds*, *comment*)
2. listTokens()
3. revokeToken(*token_id*)

#### createToken(*lifetime_seconds*, *comment*)
Create and return a token.
```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

db_api.createToken(600, 'Test token')
```

#### listTokens()
List all Token IDs in your Databricks Environment.
```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

db_api.listTokens()
```

#### revokeToken(*token_id*)
Revoke an active Databricks token.
```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

#token_id can be obtained from using the listTokens() method
db_api.revokeToken('5715498424f15ee0213be729257b53fc35a47d5953e3bdfd8ed22a0b93b339f4')
```

## Secrets API
The Secrets API allows you to manage secrets, secret scopes, and access permissions.

### Methods
1. createSecretScope(*scope*, *initial_manage_principal*)
2. deleteSecretScope(*scope*)
3. listSecretScopes()
4. putSeceret(*value*, *value_type*, *scope*, *key*)
5. deleteSecret(*scope*, *key*)
6. listSecrets(*scope*)
7. putSecretACL(*scope*, *principal*, *permission*)
8. deleteSecretACL(*scope*, *principal*)
9. getSecretACL(*scope, *principal*)
10. listSecretACL(*scope*, *principal*)

#### createSecretScope(*scope*, *initial_manage_princial*)
Creates a new secret scope.

The scope name must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters. The maximum number of scopes in a workspace is 100.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'
initial_manage_princial = 'users'
db_api.createSecretScope(scope, initial_manage_princial)
```

#### deleteSecretScope(*scope*)

Delete a secret scope.
```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'
db_api.deleteSecretScope(scope)
```

#### listSecretScopes()
List all secret scopes in the workspace

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

db_api.listSecretScopes()
```

#### putSecret(*value*, *value_type*, *scope*, *key*)  
Inserts a secret under the provided scope with the given name. If a secret already exists with the same name, this command overwrites the existing secret’s value. The server encrypts the secret using the secret scope’s encryption settings before storing it. You must have WRITE or MANAGE permission on the secret scope.

The `value_type` parameter can either be set to `string` or `bytes` depending on the type fo value the user passes in.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

#set parameters
value = 'BeepBoop'
value_type = 'string'
scope = 'SomeSecretScope'
key = 'uniqueScopekey'

db_api.putSecret(value, value_type, scope, key)
```

#### deleteSecret(*scope*, *key*)
Deletes the secret stored in this secret scope. You must have WRITE or MANAGE permission on the secret scope.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'
key = 'uniqueScopekey'

db_api.deleteSecret(scope, key)
```

#### listSecrets(*scope*)
Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data cannot be retrieved using this API. Users need READ permission to make this call.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'

db_api.listSecrets(scope)
```

#### putSecretACL(*scope*, *principal*, *permission*)
Creates or overwrites the ACL associated with the given principal (user or group) on the specified scope point. In general, a user or group will use the most powerful permission available to them

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'
prinicpal = 'users'
permission = 'READ'

db_api.putSecretACL(scope, principal, permission)
```

#### deleteSecretACL(*scope*, *principal*)  
Deletes the given ACL on the given scope.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'
prinicpal = 'users'

db_api.deleteSecretACL(scope, principal)
```

#### getSecretACL(*scope, *principal*)
Describes the details about the given ACL, such as the group and permission.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'
prinicpal = 'users'

db_api.getSecretACL(scope, principal)
```

#### listSecretACL(*scope*, *principal*)
Lists the ACLs set on the given scope.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

scope = 'SomeSecretScope'
prinicpal = 'users'

db_api.listSecretACL(scope, principal)
```

## Clusters API
The Clusters API allows you to create, start, edit, list, terminate, and delete clusters via the API. The maximum allowed size of a request to the Clusters API is 10MB.

### Methods
1. createCluster(*worker*, *worker_type*, *cluster_name*, *spark_version*, *cluster_log_conf*, *node_type_id*, *driver_node_type_id=None*, *spark_conf=None*, *aws_attributes=None*, *ssh_public_keys=None*, *custom_tags=None*, *init_scripts=None*, *spark_env_vars=None*, *autotermination_minutes=None*, *enable_elastic_disk=None*)
2. editCluster(*worker*, *worker_type*, *cluster_name*, *spark_version*, *cluster_log_conf*, *node_type_id*, *driver_node_type_id=None*, *spark_conf=None*, *aws_attributes=None*, *ssh_public_keys=None*, *custom_tags=None*, *init_scripts=None*, *spark_env_vars=None*, *autotermination_minutes=None*, *enable_elastic_disk=None*)
3. startCluster(*cluster_id*)
4. restartCluster(*cluster_id*)
5. resizeCluster(*cluster_id*, *worker*, *worker_type*)
6. terminateCluster(*cluster_id*)
7. deleteCluster(*cluster_id*)
8. getCluster(*cluster_id*)
9. pinCluster(*cluster_id*)
10. unpinCluster(*cluster_id*)
11. listClusters()
12. listNodeTypes()
13. listZones()
14. getSparkVersions()
15. getClusterEvents(*cluster_id*, *order='DESC'*, *start_time=None*, *end_time=None*, *event_types=None*, *offset=None*, *limit=None*)

#### createCluster(*worker*, *worker_type*, *cluster_name*, *spark_version*, *cluster_log_conf*, *node_type_id*, *driver_node_type_id=None*, *spark_conf=None*, *aws_attributes=None*, *ssh_public_keys=None*, *custom_tags=None*, *init_scripts=None*, *spark_env_vars=None*, *autotermination_minutes=None*, *enable_elastic_disk=None*)

Creates a new Spark cluster. This method acquires new instances from the cloud provider if necessary. This method is asynchronous; the returned cluster_id can be used to poll the cluster state. When this method returns, the cluster is in a PENDING state. The cluster is usable once it enters a RUNNING state.

The `worker_type` can be either `workers` or `autoscale`. If a `autoscale` is set, then the `min_workers` and `max_workers` must be specified. 

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

worker = 25
worker_type = 'workers'
cluster_name = 'TestCluster'
spark_version = '4.0.x-scala2.11'
cluster_log_conf = '/dbfs/log/path'
node_type_id = 'i3.xlarge'

db_api.createCluster(worker=worker, worker_type=worker_type, cluster_name=cluster_name, spark_version=spark_version, cluster_log_conf=cluster_log_conf, node_type_id=node_type_id)
```

#### editCluster(*worker*, *worker_type*, *cluster_name*, *spark_version*, *cluster_log_conf*, *node_type_id*, *driver_node_type_id=None*, *spark_conf=None*, *aws_attributes=None*, *ssh_public_keys=None*, *custom_tags=None*, *init_scripts=None*, *spark_env_vars=None*, *autotermination_minutes=None*, *enable_elastic_disk=None*)

Edit an existings clusters configuration.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

worker = 35
worker_type = 'workers'
cluster_name = 'TestCluster'
spark_version = '4.0.x-scala2.11'
cluster_log_conf = '/dbfs/new/log/path'
node_type_id = 'i5.xlarge'

db_api.editCluster(worker=worker, worker_type=worker_type, cluster_name=cluster_name, spark_version=spark_version, cluster_log_conf=cluster_log_conf, node_type_id=node_type_id)
```

#### startCluster(*cluster_id*) 
Starts a terminated Spark cluster given its ID.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'
db_api.startCluster(cluster_id)
```

#### restartCluster(*cluster_id*)
Restarts a Spark cluster given its id. If the cluster is not in a RUNNING state, nothing will happen.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'
db_api.restartCluster(cluster_id)
```

#### resizeCluster(*cluster_id*, *worker*, *worker_type*)
Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a RUNNING state.

The parameter `worker_type` can be one of `workers` or `autoscale`. 

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'
workers = 30

db_api.resizeCluster(cluster_id, workers, worker_type='workers')
```

#### terminateCluster(*cluster_id*)
Terminates a Spark cluster given its id. The cluster is removed asynchronously. Once the termination has completed, the cluster will be in a TERMINATED state. If the cluster is already in a TERMINATING or TERMINATED state, nothing will happen.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'

db_api.terminateCluster(cluster_id)
```

#### deleteCluster(*cluster_id*)
Permanently deletes a Spark cluster. If the cluster is running, it is terminated and its resources are asynchronously removed. If the cluster is terminated, then it is immediately removed.

You cannot perform any action on a permanently deleted cluster and a permanently deleted cluster is no longer returned in the cluster list.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'

db_api.deleteCluster(cluster_id)
```

#### getCluster(*cluster_id*)
Returns information about all pinned clusters, currently active clusters, up to 70 of the most recently terminated interactive clusters in the past 30 days, and up to 30 of the most recently terminated job clusters in the past 30 days.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'

db_api.getCluster(cluster_id)
```


#### pinCluster(*cluster_id*)
Pinning a cluster ensures that the cluster is always returned by the List API. Pinning a cluster that is already pinned has no effect.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'

db_api.pinCluster(cluster_id)
```

#### unpinCluster(*cluster_id*)
Unpinning a cluster will allow the cluster to eventually be removed from the list returned by the List API. Unpinning a cluster that is not pinned has no effect.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'

db_api.unpinCluster(cluster_id)
```

#### listClusters()
Retrieves the information for a cluster given its identifier. Clusters can be described while they are running, or up to 30 days after they are terminated.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

db_api.listClusters()
```

#### listNodeTypes()
Returns a list of supported Spark node types. These node types can be used to launch a cluster.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

db_api.listNodeTypes()
```

#### listZones()
Returns a list of availability zones where clusters can be created in (ex: us-west-2a). These zones can be used to launch a cluster.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

db_api.listZones()
```

#### getSparkVersions()
Returns the list of available Spark versions. These versions can be used to launch a cluster.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

db_api.getSparkVersions()
```

#### getClusterEvents(*cluster_id*, *order='DESC'*, *start_time=None*, *end_time=None*, *event_types=None*, *offset=None*, *limit=None*)
Retrieves a list of events about the activity of a cluster. This API is paginated. If there are more events to read, the response includes all the parameters necessary to request the next page of events.

```python
url = 'https://url.for.databricks.net'
db_api = Token(url)

cluster_id = '1202-211320-brick1'

db_api.getClusterEvents(cluster_id)
```







