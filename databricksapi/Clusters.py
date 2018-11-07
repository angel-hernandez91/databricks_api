from . import Databricks

class WorkerTypeNotSupportedException(Exception):
	def __init__(self, worker_type):
		Exception.__init__(self, "The worker type '{}' is not supported. Use either 'workers' or 'autoscale'.".format(worker_type))

class Clusters(Databricks.Databricks):
	def __init__(self, url):
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


	def editCluster(self, worker, worker_type, cluster_id, cluster_name, spark_version, cluster_log_conf,
					node_type_id, driver_node_type_id=None, spark_conf=None, aws_attributes=None, 
					ssh_public_keys=None, custom_tags=None, init_scripts=None, spark_env_vars=None,
					autotermination_minutes=None, enable_elastic_disk=None):
		endpoint = 'edit'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id,
			'cluster_name': cluster_name,
			'spark_version': spark_version,
			'cluster_log_conf': cluster_log_conf,
			'node_type_id': node_type_id
		}

		if worker_type.lower() == 'workers':
			payload['num_workers'] = worker
		elif worker_type.lower() == 'autoscale':
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
		endpoint = 'get'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'cluster_id': cluster_id
		}

		return self._get(url, payload)


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

	def listNoteTypes(self):
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

	def getClusterEvents(self, cluster_id, order, start_time=None, end_time=None, event_types=None, offset=None, limit=None):
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




