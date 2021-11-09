from . import Databricks

class SQLEndpoints(Databricks.Databricks):
	def __init__(self, url, token=None):
		super().__init__(token)
		self._url = url
		self._api_type = 'sql'

	def createEndpoint(self, name, cluster_size, min_num_clusters=1, max_num_clusters=1, auto_stop_mins=10, spot_instance_policy=None,
			         enable_photon=True, enable_serverless_compute=False, tags=None):
		endpoint = 'endpoints'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			"name": name,
			"cluster_size": cluster_size,
			"min_num_clusters": min_num_clusters,
			"max_num_clusters": max_num_clusters,
			"spot_instance_policy":spot_instance_policy,
			"enable_photon": enable_photon,
			"enable_serverless_compute": enable_serverless_compute,
			"tags": tags
			   }
		return self._post(url, payload)

	def listEndpoints(self):
		endpoint = 'endpoints'
		url = self._set_url(self._url, self._api_type, endpoint)
		
		return self._get(url)

	def deleteEndpoint(self, endpoint_id):
		endpoint = 'endpoints/'+endpoint_id
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._delete(url, payload)

	def getEndpoint(self, endpoint_id):
		endpoint = 'endpoints/'+endpoint_id
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)
	
	def updateEndpoint(self, endpoint_id, name=None, cluster_size=None, min_num_clusters=None, max_num_clusters=None, auto_stop_mins=None, tags=None,
			  spot_instance_policy=None, enable_photon=None, enable_serverless_compute=None):
		endpoint = 'endpoints/'+endpoint_id+'/edit'
		url = self._set_url(self._url, self._api_type, endpoint)
		
		payload = {}
		if endpoint_id != None : payload["id"] = endpoint_id
		if name != None : payload["name"] = name
		if cluster_size != None : payload["cluster_size"] = cluster_size
		if min_num_clusters != None : payload["min_num_clusters"] = min_num_clusters
		if max_num_clusters != None : payload["max_num_clusters"] = max_num_clusters
		if auto_stop_mins != None : payload["auto_stop_mins"] = auto_stop_mins
		if tags != None : payload["tags"] = tags
		if spot_instance_policy != None : payload["spot_instance_policy"] = spot_instance_policy
		if enable_photon != None : payload["enable_photon"] = enable_photon
		if enable_serverless_compute != None : payload["enable_serverless_compute"] = enable_serverless_compute

		return self._post(url, payload)


	def startEndpoint(self, endpoint_id):
		endpoint = 'endpoints'+endpoint_id+'/start'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._post(url)
	
	def stopEndpoint(self, endpoint_id):
		endpoint = 'endpoints'+endpoint_id+'/stop'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._post(url)
	
	def listGlobalEndpoints(self):
		endpoint = 'config/endpoints'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def updateGlobalEndpoints(self, security_policy, data_access_config, instance_profile_arn):
		endpoint = 'config/endpoints'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			"security_policy": security_policy,
			"data_access_config": data_access_config,
			"instance_profile_arn": instance_profile_arn
		}

		return self._put(url, payload)

	
