from . import Databricks

class Libraries(Databricks.Databricks):
	def __init__(self, url, token=None):
		super().__init__(token)
		self._url = url
		self._api_type = 'libraries'

	def allClusterStatuses(self, status):
		endpoint = 'all-cluster-statuses'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def clusterStatus(self, cluster_id):
		endpoint = 'cluster-status'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._get(url, payload)

	def installLibrary(self, cluster_id, libraries):
		endpoint = 'install'

		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id,
			'libraries': libraries
		}

		return self._post(url, payload)

	def uninstallLibrary(self, cluster_id, libraries):
		endpoint = 'uninstall'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id,
			'libraries': libraries
		}

		return self._post(url, payload)
