import json
import requests
import os

class TokenNotFoundInEnvironmentException(Exception): pass

class Databricks:
	def __init__(self, token=None):
		self._token = self._set_token(token)
		self._headers = {'content_type': 'application/json', 'authorization': self._token}
		self._api_suffix = '/api/2.0/'

	def _set_token(self, token):
		if token is None:
			try:
				out = 'Bearer {}'.format(os.environ['DATABRICKS_TOKEN'])
			except KeyError:
				raise TokenNotFoundInEnvironmentException("The token could not be found using os.environ. Add the token to the environment, or pass one in explicitly.")
		else:
			out = 'Bearer {}'.format(token)
		return out
			

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
				r = requests.post(url, headers=self._headers)
			else:
				r = requests.post(url, headers=headers, files=files)
		else:
			if files is not None:
				r = requests.post(url, data=payload, headers=headers, files=files)
			else:
				r = requests.post(url, data=json.dumps(payload), headers=self._headers)
		
		try:
			return r.json()
		except json.JSONDecodeError:
			print(r.content)

	def _get(self, url, payload=None, content=False):
		if payload is None:
			r = requests.get(url, headers=self._headers)
		else:
			r = requests.get(url, data=json.dumps(payload), headers=self._headers)
		
		if content is True:
			return r.content
		else:
			try:
			 return r.json()
			except json.JSONDecodeError:
				print(r.content)
