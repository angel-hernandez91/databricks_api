from databricksapi import Permissions #, Jobs

url = 'https://me.cloud.databricks.com'
token = 'dapi88888888888888888888888888888888'

pe = Permissions.Permissions(url, token)
#joblist = Jobs.Jobs(url, token).listJobs()['jobs']
new_permissions_map = {"access_control_list":
    [
    {"group_name": "admins", "permission_level": "CAN_MANAGE_RUN"}
    ]
}

joblist = [2603,2625,2671,2749,2834,2858,2897,2987,3183,3264,3356]

for job in joblist:
    #job_id = job.get('job_id');

    print('replacing permissions..')
    print(pe.replacePermissions(new_permissions_map, "Job", job))
    print('actual permissions:')
    print(pe.getPermissions("Job", job).get('access_control_list'))

