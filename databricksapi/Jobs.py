import Databricks

class Jobs(Databricks.Databricks):
	def __init__(self, url):
		super().__init__(self, url)
		self._url = url
		self._api_type = 'jobs'

	def createJob(cluster, cluster_type, task, task_type, name, 
				  libraries=None, email_notications=None, timeout_seconds=None,
				  max_retries=None, min_retry_intervals=None, retry_on_timeout=None,
				  schedule=None, max_concurrent_runs=None):
		endpoint = 'create'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'name': name
		}
		if cluster_type.lower() == 'existing':
			payload['existing_cluster_id'] = cluster
		elif cluster_type.lower() == 'new':
			payload['new_cluster'] = cluster
		else:
			raise ClusterTypeNotSupportedExpcetion("The cluster type '{}' is not supported. Use either 'existing' or 'new'.".format(cluster_type))

		if task_type.lower() == 'notebook':
			payload['notebook_task'] = task
		elif task_type.lower() == 'jar':
			payload['spark_jar_task'] = task
		elif task_type.lower() == 'python':
			payload['spark_python_task'] = task
		elif task_type.lower() == 'submit':
			payload['spark_submit_task'] = task
		else:
			raise TaskTypeNotSupportedException(
				"The task type '{}' is not supported. Use either 'notebook', 'jar', 'python', or 'submit'.".format(cluster_type)
				)
		