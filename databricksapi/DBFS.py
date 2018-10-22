import Databricks

class DBFS(Databricks.Databricks):
	def __init__(self, url):
		super().__init__(self)
		self._api_endpoint = 'dbfs/add-block'
		self._url = self._set_url(url, self._api_endpoint)

	def addBlock(self, data, handle):
		payload = { 
			"data": data,
			"handle": handle
		}

		r = requests.post(self._url, data=json.dumps(payload), headers=self._headers)
		return r

if __name__ == '__main__':
	dbfs = DBFS()