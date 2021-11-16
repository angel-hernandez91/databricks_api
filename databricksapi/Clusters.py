from . import Databricks

class WorkerTypeNotSupportedException(Exception):
	def __init__(self, worker_type):
		Exception.__init__(self, "The worker type '{}' is not supported. Use either 'workers' or 'autoscale'.".format(worker_type))

class Clusters(Databricks.Databricks):
	def __init__(self, url, token=None):
		super().__init__(token)
		self._url = url
		self._api_type = 'clusters'

	def createCluster(self, worker, worker_type, cluster_name, spark_version, cluster_log_conf, 
				      node_type_id, driver_node_type_id=None, spark_conf=None, aws_attributes=None, 
					  ssh_public_keys=None, custom_tags=None, init_scripts=None,
					  spark_env_vars=None, autotermination_minutes=None, enable_elastic_disk=None):

		endpoint = 'create'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_name': cluster_name,
			'spark_version': spark_version,
			'node_type_id': node_type_id,
			'cluster_log_conf': cluster_log_conf,
			
		}

		if worker_type == 'workers':
			payload['num_workers'] = worker
		elif worker_type == 'autoscale':
			payload['autoscale'] = worker
		else:
			raise WorkerTypeNotSupportedException(worker_type)

		if driver_node_type_id is not None:
			payload['driver_node_type_id'] = driver_node_type_id

		if spark_conf is not None:
			payload['spark_conf'] = spark_conf

		if aws_attributes is not None:
			payload['aws_attributes'] = aws_attributes

		if ssh_public_keys is not None:
			payload['ssh_public_keys'] = ssh_public_keys

		if custom_tags is not None:
			payload['custom_tags'] = custom_tags

		if init_scripts is not None:
			payload['init_scripts'] = init_scripts

		if spark_env_vars is not None:
			payload['spark_env_vars'] = spark_env_vars

		if autotermination_minutes is not None:
			payload['autotermination_minutes'] = autotermination_minutes

		if enable_elastic_disk is not None:
			payload['enable_elastic_disk'] = enable_elastic_disk

		return self._post(url, payload)

	def editCluster(self, cluster_settings):
		endpoint = 'edit'
		url = self._set_url(self._url, self._api_type, endpoint)
		
		new_cluster_settings = {}
		
		if cluster_settings.get("cluster_id") and cluster_settings.get("spark_version") and cluster_settings.get("node_type_id"):
			new_cluster_settings["cluster_id"] = cluster_settings.get("cluster_id")
			new_cluster_settings["spark_version"] = cluster_settings.get("spark_version")
			new_cluster_settings["node_type_id"] = cluster_settings.get("node_type_id")
			if cluster_settings.get("cluster_name"): new_cluster_settings["cluster_name"] = cluster_settings.get("cluster_name")
			if cluster_settings.get("aws_attributes"): new_cluster_settings["aws_attributes"] = cluster_settings.get("aws_attributes")
			if cluster_settings.get("driver_node_type_id"): new_cluster_settings["driver_node_type_id"] = cluster_settings.get("driver_node_type_id")
			if cluster_settings.get("custom_tags"): new_cluster_settings["custom_tags"] = cluster_settings.get("custom_tags")
			if cluster_settings.get("cluster_log_conf"): new_cluster_settings["cluster_log_conf"] = cluster_settings.get("cluster_log_conf")
			if cluster_settings.get("spark_env_vars"): new_cluster_settings["spark_env_vars"] = cluster_settings.get("spark_env_vars")
			if cluster_settings.get("autotermination_minutes"): new_cluster_settings["autotermination_minutes"] = cluster_settings.get("autotermination_minutes")
			if cluster_settings.get("enable_elastic_disk"): new_cluster_settings["enable_elastic_disk"] = cluster_settings.get("enable_elastic_disk")
			if cluster_settings.get("init_scripts"): new_cluster_settings["init_scripts"] = cluster_settings.get("init_scripts")
			if cluster_settings.get("enable_local_disk_encryption"): new_cluster_settings["enable_local_disk_encryption"] = cluster_settings.get("enable_local_disk_encryption")
			if cluster_settings.get("autoscale"): new_cluster_settings["autoscale"] = cluster_settings.get("autoscale")
			if cluster_settings.get("spark_conf"): new_cluster_settings["spark_conf"] = cluster_settings.get("spark_conf")
			if cluster_settings.get("ssh_public_keys"): new_cluster_settings["ssh_public_keys"] = cluster_settings.get("ssh_public_keys")
			if cluster_settings.get("docker_image"): new_cluster_settings["docker_image"] = cluster_settings.get("docker_image")
			if cluster_settings.get("instance_pool_id"): new_cluster_settings["instance_pool_id"] = cluster_settings.get("instance_pool_id")
			if cluster_settings.get("apply_policy_default_values"): new_cluster_settings["apply_policy_default_values"] = cluster_settings.get("apply_policy_default_values")
			
			return self._post(url, new_cluster_settings)
		else: 
			return ("Not all mandatory parameters (cluster_id, spark_version, node_type_id) are specified in new cluster settings.")
		
	
	def startCluster(self, cluster_id):
		endpoint = 'start'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._post(url, payload)

	def restartCluster(self, cluster_id):
		endpoint = 'restart'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._post(url, payload)

	def resizeCluster(self, cluster_id, worker, worker_type):
		endpoint = 'resize'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id,
		}

		if worker_type == 'workers':
			payload['cluster_id'] = worker
		elif worker_type == 'autoscale':
			payload['autoscale'] = worker
		else:
			raise WorkerTypeNotSupportedException(worker_type)

		return self._post(url, payload)

	def terminateCluster(self, cluster_id):
		endpoint = 'delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._post(url, payload)

	def deleteCluster(self, cluster_id):
		endpoint = 'permanent-delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._post(url, payload)

	def getCluster(self, cluster_id):
		endpoint = 'get?cluster_id='+cluster_id
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def pinCluster(self, cluster_id):
		endpoint = 'pin'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._post(url, payload)

	def unpinCluster(self, cluster_id):
		endpoint = 'unpin'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._post(url, payload)

	def listClusters(self):
		endpoint = 'list'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def listNodeTypes(self):
		endpoint = 'list-node-types'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def listZones(self):
		endpoint = 'list-zones'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def getSparkVersions(self):
		endpoint = 'spark-versions'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)

	def getClusterEvents(self, cluster_id, order='DESC', start_time=None, end_time=None, event_types=None, offset=None, limit=None):
		endpoint = 'events'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id,
			'order': order
		}

		if start_time is not None:
			payload['start_time'] = start_time

		if end_time is not None:
			payload['end_time'] = end_time

		if event_types is not None:
			payload['event_types'] = event_types

		if offset is not None:
			payload['offset'] = offset

		if limit is not None:
			payload['limit'] = limit

		return self._post(url, payload)


