from . import Databricks

class Token(Databricks.Databricks):
	def __init__(self, url):
		self._url = url
		self._api_type = 'token'


	def createToken(self, lifetime_seconds, comment):
		endpoint = 'create'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'lifetime_seconds': lifetime_seconds,
			'comment': comment
		}

		return self._post(url, payload)

	def listTokens(self):
		endpoint = 'list'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def revokeToken(self, token_id):
		endpoint = 'delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'token_id': token_id
		}

		return self._post(url, payload)
