from . import Databricks

class InstanceProfile(Databricks.Databricks):
	def __init__(self, url):
		super().__init__(self)
		self._url = url
		self._api_type = 'instance-profiles'

	def addProfile(self, profile_arn, skip_validation=None):
		endpoint = 'add'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'instance_profile_arn': profile_arn
		}

		if skip_validation is not None:
			payload['skip_validation'] = skip_validation

		return self._post(url, payload)

	def listProfiles(self):
		endpoint = 'list'
		url = self._set_url(self._url, self._api_type, endpoint)
		
		return self._post(url)

	def removeProfile(self):
		endpoint = 'remove'
		url = self._set_url(self._url, self._api_type, endpoint)
		
		return self._post(url)


