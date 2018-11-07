from . import Databricks

class Workspace(Databricks.Databricks):
	def __init__(self, url):
		self._url = url
		self._api_type = 'workspace'

	def deleteWorkspace(self, path, recursive):
		endpoint = 'delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'recursive': recursive
		}

		return self._post(url, payload)

	def exportWorkspace(self, path, export_format, direct_download):
		endpoint = 'export'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'format': export_format,
			'direct_download': direct_download
		}

		return self._post(url, payload)


	def getWorkspaceStatus(self, path):
		endpoint = 'get-status'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path
		}

		return self._get(url, payload)

	def importWorkspace(self, path, export_format, language, content, overwrite):
		endpoint = 'import'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'format': export_format,
			'language': language,
			'content': content,
			'overwrite': overwrite
		}

		return self._post(url, payload)

	def listWorkspace(self, path):
		endpoint = 'list'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path
		}

		return self._get(url, payload)


	def mkdirsWorkspace(self, path):
		endpoint = 'mkdirs'
		url = self._set_url(self._set_url, self._api_type, endpoint)

		payload = {
			'path': path
		}

		return self._post(url, payload)