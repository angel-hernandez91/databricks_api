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
5. deleteSecretI*scope*, *key*)
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











