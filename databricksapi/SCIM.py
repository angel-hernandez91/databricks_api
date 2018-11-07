from . import Databricks

class SCIM:
	def __init__(self, url):
		self._url = url
		self._api_type = 'preview/scim/v2'
		self._write_headers = {'content-type': 'application/scim+json', 'authorization': self._token}
		self._accept = {'content-type': 'application/scim+json'}

	def _scim_post(self, url, payload=None):
		if payload is None:
			return requests.post(url, headers=self._write_headers, accept=self._accept)
		else:
			return requests.post(url, payload=json.dumps(payload), headers=self._write_headers, accept=self._accept)

	def _scim_get(self, url, payload=None):
		if payload is None:
			return requests.get(url, headers=self._write_headers, accept=self._accept)
		else:
			return requests.get(url, payload=json.dumps(payload), headers=self._write_headers, accept=self._accept)

	def _scim_patch(self, url, payload):
		if payload is None:
			return requests.patch(url, headers=self._write_headers, accept=self._accept)
		else:
			return requests.patch(url, payload=json.dumps(payload), headers=self._write_headers, accept=self._accept)

	def _scim_put(self, url, payload):
		if payload is None:
			return requests.put(url, headers=self._write_headers, accept=self._accept)
		else:
			return requests.put(url, payload=json.dumps(payload), headers=self._write_headers, accept=self._accept)

	def _scim_delete(self, url, payload):
		if payload is None:
			return requests.delete(url, headers=self._write_headers, accept=self._accept)
		else:
			return requests.delete(url, payload=json.dumps(payload), headers=self._write_headers, accept=self._accept)


	def getUsers(self, filter_string=None):
		endpoint = 'Users'
		url = self._set_url(self._url, self._api_type, endpoint)

		if filter_string is not None:
			url = '{}?{}'.format(url, filter_string)

		return self._scim_get(url)

	def getUsersById(self, user_id, filter_string=None):
		endpoint = 'Users/{}'.format(user_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		if filter_string is not None:
			url = '{}?{}'.format(url, filter_string)

		return self._scim_get(url)

	def createUser(self, schemas, userName, groups, entitlements):
		endpoint = 'Users'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'schemas': schemas,
			'userName': userName,
			'groups': groups,
			'entitlements': entitlements
		}

		return self._scim_post(url, payload)

	def updateUserById(self, user_id, schemas, operations):
		endpoint = 'Users/{}'.format(user_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'schemas': schemas,
			'Operations': operations
		}

		return self._scim_patch(url, payload)

	def updateUserById(self, user_id, schemas, userName, entitlements, roles, groups):
		endpoint = 'Users/{}'.format(user_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'schemas': schemas,
			'userName': userName,
			'entitlements': entitlements,
			'roles': roles,
			'groups': groups
		}

		return self._scim_put(url, payload)

	def deleteUserById(self, user_id):
		endpoint = 'Users/{}'.format(user_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._scim_delete(url)

	def getGroups(self, filter_string=None):
		endpoint = 'Groups'
		url = self._set_url(self._url, self._api_type, endpoint)

		if filter_string is not None:
			url = '{}?{}'.format(url, filter_string)

		return self._scim_get(url)		


	def getGroupById(self, group_id):
		endpoint = 'Groups/{}'.format(group_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._scim_get(url)

	def createGroup(self, schemas, displayName, members):
		endpoint = 'Groups/{}'.format(group_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'schemas': schemas,
			'displayName': displayName,
			'members': members
		}

		return self._scim_post(url, payload)

	def updateGroup(self, group_id, schemas, operations):
		endpoint = 'Groups/{}'.format(group_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'schemas': schemas,
			'Operations': operations
		}		

		return self._scim_patch(url, payload)


	def deleteGroup(self, group_id):
		endpoint = 'Groups/{}'.format(group_id)
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._scim_delete(url, payload)

