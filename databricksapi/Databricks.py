import json
import requests

class Databricks:
	def __init__(self):
		self._token = 'Bearer {}'.format(os.environ['DATABRICKS_TOKEN'])
		self._headers ={'content_type': 'application/json', 'authorization': self._token}
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

	def _post(self, url, payload=None):
		if payload is None:
			return requests.post(url, headers=self._headers).json()
		else:
			return requests.post(url, data=json.dumps(payload), headers=self._headers).json()

	def _get(self, url, payload=None):
		if payload is None:
			return requests.post(url, headers=self._headers).json()
		else:
			return requests.get(url, data=json.dumps(payload), headers=self._headers).json()

	# def _cluster_id_payload(self, cluster_name, url):
	# 	cluster_map = GetClusterList(url).getClusterList()
		
	# 	payload = {
	# 		"cluster_id": cluster_map[cluster_name.lower()]
	# 	}
	# 	return payload

	# def _start_job_monitor(self, url, cluster_name, json_obj):
	
	# 	if json_obj != {}:
	# 		cluster_monitor = ClusterMonitor(url).clusterMonitor(cluster_name)
	# 		#running job
	# 		run_id = json_obj['run_id']
	# 		monitor = JobMonitor(url)
	# 		start_monitor = monitor.jobMonitor(run_id)
	# 		return start_monitor
	# 	else:
	# 		return "Job Failed to Start"