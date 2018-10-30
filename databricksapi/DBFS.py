import Databricks

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

		return self._post(url, payload).json()

	def closeStream(self, handle):
		endpoint = 'close'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			"handle": handle
		}
		return self._post(url, payload).json()

	def createFile(self, path, overwrite):
		endpoint = 'create'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'overwrite': overwrite

		}
		return self._post(url, payload).json()

	def deleteFile(self, path, recursive):
		endpoint = 'delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path,
			'recurisve': recursive
		}

		return self._post(url, payload).json()

	def getStatus(self, path):
		endpoint = 'get-status'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'path': path
		}
		return self._post(url, payload).json()




if __name__ == '__main__':
	dbfs = DBFS()