from . import Databricks

class DBFS(Databricks.Databricks):
	def __init__(self, url):
		super().__init__(self)
		self._api_type = 'dbfs'
		self._url = url

	def addBlock(self, data, handle):
		endpoint = 'add-block'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = { 
			"data": data,
			"handle": handle
		}

		return self._post(url, payload)

	def closeStream(self, handle):
		endpoint = 'close'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			"handle": handle
		}
		return self._post(url, payload)

	def createFile(self, path, overwrite):
		endpoint = 'create'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'overwrite': overwrite

		}
		return self._post(url, payload)

	def deleteFile(self, path, recursive):
		endpoint = 'delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'recurisve': recursive
		}

		return self._post(url, payload)

	def getStatus(self, path):
		endpoint = 'get-status'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path
		}
		return self._post(url, payload)

	def listFiles(self, path):
		endpoint = 'list'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path
		}

		return self._post(url, payload)

	def makeDirs(self, path):
		endpoint = 'mkdirs'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path
		}

		return self._post(url, payload)

	def moveFiles(self, source_path, target_path):
		endpoint = 'move'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'source_path': source_path,
			'target_path': target_path
		}

		return self._post(url, payload)

	def putFiles(self, path, overwrite, contents=None):
		endpoint = 'put'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'contents': contents,
			'overwrite': overwrite
		}

		if contents is None:
			payload.pop('contents')

		return self._post(url, payload)

	def readFiles(self, path, offset, length):
		endpoint = 'read'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'offset': offset,
			'length': length
		}

		return self._post(url, payload)





if __name__ == '__main__':
	dbfs = DBFS()