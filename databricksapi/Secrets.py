from . import Databricks

class ValueTypeNotSupportedException(Exception):
	def __init__(self, value_type):
		Exception.__init__(self, "The value type '{}' is not supported. Use either 'string' or 'bytes'.".format(value_type))

class Secrets:
	def __init__(self, url):
		self._url = url
		self._api_type = 'secrets'

	def createSecretScope(self, scope, initial_manage_principal):
		endpoint = 'scopes/create'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope,
			'initial_manage_principal': initial_manage_principal
		}

		return self._post(url, payload)

	def deleteSecretScope(self, scope):
		endpoint = 'scopes/delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope
		}

		return self._post(url, payload)

	def listSecretScopes(self):
		endpoint = 'scopes/list'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def putSeceret(self, value, value_type, scope, key):
		endpoint = 'put'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope,
			'key': key
		}

		if value_type == 'string':
			payload['string_value'] = value
		elif value_type == 'bytes':
			payload['bytes_value'] = value
		else:
			raise ValueTypeNotSupportedException(value_type)

		return self._post(url, payload)

	def deleteSecret(self, scope, key):
		endpoint = 'delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope,
			'key': key
		}

		return self._post(url, payload)


	def listSecrets(self, scope):
		endpoint = 'list'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope
		}

		return self._get(url, payload)


	def putSecretACL(self, scope, principal, permission):
		endpoint = 'acls/put'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope,
			'principal': principal,
			'permission': permission	
		}

		return self._post(self._url, self._api_type, endpoint)

	def deleteSecretACL(self, scope, principal):
		endpoint = 'acls/delete'
		url = self._post_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope,
			'principal': principal
		}

		return self._post(url, payload)


	def getSecretACL(self, scope, principal):
		endpoint = 'acls/get'
		url = self._post_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope,
			'principal': principal
		}

		return self._get(url, payload)

	def listSecretACL(self, scope):
		endpoint = 'acls/list'
		url = self._post_url(self._url, self._api_type, endpoint)

		payload = {
			'scope': scope
		}

		return self._get(url, payload)

	