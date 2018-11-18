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











