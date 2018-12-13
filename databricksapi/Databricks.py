import json
import requests
import os

class Databricks:
	def __init__(self):
		self._token = 'Bearer {}'.format(os.environ['DATABRICKS_TOKEN'])
		self._headers = {'content_type': 'application/json', 'authorization': self._token}
		self._api_suffix = '/api/2.0/'

	def _url_sanitize(self, url):
		if url[-1] == '/':
			return url[0:-1]
		else:
			return url

	def _set_url(self, url, api_type, endpoint):
		return '{}{}{}/{}'.format(self._url_sanitize(url), self._api_suffix, api_type, endpoint)

	def _merge_dict(self, *args):
		merged = args[0].copy()
		for d in args[1::]:
			merged.update(d)
		return merged

	def _json_flattener(self, start_dict):
		out = {}

		def flatten(temp_dict, name=''):
			if isinstance(temp_dict, dict):
				for key in temp_dict:
					flatten(temp_dict[key], key)
			else:
				out[name] = temp_dict

		flatten(start_dict)
		return out

	def _post(self, url, payload=None, files=None):
		headers = {'content_type': 'multipart/form-data', 'authorization': self._token}
		if payload is None:
			if files is None:
				return requests.post(url, headers=self._headers).json()
			else:
				
				return requests.post(url, headers=headers, files=files).json()
		else:
			if files is not None:

				return requests.post(url, data=payload, headers=headers, files=files).json()
			else:
				return requests.post(url, data=json.dumps(payload), headers=self._headers).json()



	def _get(self, url, payload=None):
		if payload is None:
			return requests.get(url, headers=self._headers).json()
		else:
			return requests.get(url, data=json.dumps(payload), headers=self._headers).json()
