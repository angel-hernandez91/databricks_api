from . import Databricks

class ClusterTypeNotSupportedExpcetion(Exception):
	def __init__(self, cluster_type):
		Exception.__init__(self, "The cluster type '{}' is not supported. Use either 'existing' or 'new'.".format(cluster_type))

class TaskTypeNotSupportedException(Exception):
	def __init__(self, task_type):
			Exception.__init__(self,	"The task type '{}' is not supported. Use either 'notebook', 'jar', 'python', or 'submit'.".format(task_type))

class RunTypeNotSupportedException(Exception):
	def __init__(self, run_type):
		Exception.__init__(self, "The run type '{}' is not supported. Use either 'active' or 'completed'.".format(run_type))

class Jobs(Databricks.Databricks):
	def __init__(self, url):
		super().__init__(self, url)
		self._url = url
		self._api_type = 'jobs'

	def createJob(cluster, cluster_type, task, task_type, name, 
				  libraries=None, email_notications=None, timeout_seconds=None,
				  max_retries=None, min_retry_interval_millis=None, retry_on_timeout=None,
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
			raise ClusterTypeNotSupportedExpcetion(cluster_type)

		if task_type.lower() == 'notebook':
			payload['notebook_task'] = task
		elif task_type.lower() == 'jar':
			payload['spark_jar_task'] = task
		elif task_type.lower() == 'python':
			payload['spark_python_task'] = task
		elif task_type.lower() == 'submit':
			payload['spark_submit_task'] = task
		else:
			raise TaskTypeNotSupportedException(task_type)

		if libraries is not None:
			payload['libraries'] = libraries
		if email_notications is not None:
			payload['email_notications'] = email_notications
		if timeout_seconds is not None:
			payload['timeout_seconds'] = timeout_seconds
		if max_retries is not None:
			payload['max_retries'] = max_retries
		if min_retry_interval_millis is not None:
			payload['min_retry_interval_millis'] = min_retry_interval_millis
		if retry_on_timeout is not None:
			payload['retry_on_timeout'] = retry_on_timeout
		if schedule is not None:
			payload['schedule'] = schedule
		if max_concurrent_runs is not None:
			payload['max_concurrent_runs'] = max_concurrent_runs

		return self._post(url, payload)

	def listJobs(self):
		endpoint = 'list'
		url = self._set_url(self._url, self._api_type, endpoint)
		payload = None
		return self._post(url, payload)

	def deleteJob(self, job_id):
		endpoint = 'delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'job_id': job_id
		}

		return self._post(url, payload)

	def batchDelete(self, job_ids):
		for job in job_ids:
			self.deleteJob(job)

	def deleteAllJobs(self):
		pass

	def mapJobNames(self):
		pass

	def getJob(self, job_id):
		endpoint = 'get'
		url = self._set_url(self._url, self._api_type, endpoint)
		payload = {
			'job_id': job_id
		}

		return self._post(url, payload)

	def resetJob(self, job_id, new_settings):
		endpoint = 'reset'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'job_id': job_id,
			'new_settings': new_settings
		}

		return self._post(url, payload)

	def runJob(self, job_id, job_type, params):
		endpoint = 'run-now'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'job_id': job_id,
		}

		if job_type == 'notebook':
			payload['notebook_params'] = params
		elif job_type == 'jar':
			payload['jar_params'] = params
		elif job_type == 'python':
			payload['python_params'] = params
		elif job_type == 'submit':
			payload['spark_submit_params'] = params
		else:
			raise TaskTypeNotSupportedException(job_type)	

		return self._post(url, payload)

	def runsSubmit(self, run_name, cluster, task, cluster_type, task_type, libraries=None, timeout_seconds=None):
		endpoint = 'runs/submit'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'run_name': run_name,
		}

		if cluster_type == 'existing':
			payload['existing_cluster_id'] = cluster
		elif cluster_type == 'new':
			payload['new_cluster'] = cluster
		else:
			raise ClusterTypeNotSupportedExpcetion(cluster_type)

		#set the tasks
		if task_type.lower() == 'notebook':
			payload['notebook_task'] = task
		elif task_type.lower() == 'jar':
			payload['spark_jar_task'] = task
		elif task_type.lower() == 'python':
			payload['spark_python_task'] = task
		elif task_type.lower() == 'submit':
			payload['spark_submit_task'] = task
		else:
			raise TaskTypeNotSupportedException(task_type)

		if libraries is not None:
			payload['libraries'] = libraries

		if timeout_seconds is not None:
			payload['timeout_seconds'] = timeout_seconds

		return self._post(url, payload)

	def runsList(self, run, run_type, job_id, offset, limit):
		endpoint = 'runs/list'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'job_id': job_id,
			'offset': offset,
			'limit': limit
		}

		if run_type.lower() == 'active':
			payload['active_only'] = run
		elif run_type.lower() == 'completed':
			payload['completed_only'] = run
		else:
			raise RunTypeNotSupportedException(run_type)

		return self._post(url, payload)

	def runsGet(self, run_id):
		endpiont = 'runs/submit'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'run_id': run_id
		}

		return self._post(url, payload)

	def runsExport(self, run_id, views_to_export):
		endpoint = 'runs/export'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'run_id': run_id,
			'views_to_export': views_to_export
		}

		return self._post(url, payload)

	def runsCancel(self, run_id):
		endpoint = 'runs/cancel'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'run_id': run_id
		}

		return self._post(url, payload)

	def runsGetOutPut(self, run_id):
		endpoint = 'runs/get-output'
		url = self._set_url(self._url, self._api_type, endpoint)

		payload = {
			'run_id': run_id
		}

		return self._post(url, payload)

	def runsDelete(self, run_id):
		endpoint = 'runs/delete'
		url = self._set_url(self._url, self._api_type, endpoint)

		payloads = {
			'run_id': run_id
		}

		return self._post(url, payload)
