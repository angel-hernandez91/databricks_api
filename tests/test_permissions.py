import json
from databricksapi import Permissions, Jobs

# url = 'https://me.cloud.databricks.com'
# token = 'dapi88888888888888888888888888888888'

#pe = Permissions.Permissions(url, token)
jo = Jobs.Jobs(url, token)
#joblist = Jobs.Jobs(url, token).listJobs()['jobs']

joblist = [133,297,298,314,315,316,379,485,563,612,658,2352,2603,2625,2671,2731,2749,2834,2858,2897,2987,3183,3264,3356,3600,3655,3663,3697,3758,3792,3859,3953,4009,4010,4032,4103,4131,4485,4535,4596,4848,4886,4955,5040,5082]
#111,107,108,110,111,
for job in joblist:
    cur_job = jo.getJob(job)
    if cur_job.get("settings").get("new_cluster","empty") != "empty":
        if cur_job.get("settings").get("new_cluster").get("cluster_log_conf","empty") == "empty":
            logging_struct = {"dbfs": {"destination": "dbfs:/cluster-logs/" + str(job)}}
            new_cluster = cur_job.get("settings").get("new_cluster")
            new_cluster["cluster_log_conf"] = logging_struct
            job_settings = {"job_id": job, "new_settings": {"new_cluster": new_cluster}}
            jo.updateJob(job_settings)
            print(jo.getJob(job))
        else:
            print("Job "+str(job)+" already have log settings: ")
            print(cur_job.get("settings").get("new_cluster").get("cluster_log_conf","empty"))
    else:
        print("Job "+str(job)+" has fixed cluster")



#print(jo.getJob(196))

#joblist = [2603,2625,2671,2749,2834,2858,2897,2987,3183,3264,3356]

# for job in joblist:
#     #job_id = job.get('job_id');
#
#     print('replacing permissions..')
#     print(pe.replacePermissions(new_permissions_map, "Job", job))
#     print('actual permissions:')
#     print(pe.getPermissions("Job", job).get('access_control_list'))

