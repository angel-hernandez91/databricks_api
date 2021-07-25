from databricksapi import Permissions

url = 'https://my.cloud.databricks.com'
token = 'dapi88888888888888888888888888'

pe = Permissions2.Permissions(url, token)

res = pe.getPermissions('Passwords')
print(res)

res = pe.updatePermissions('my@gmail.com','user','CAN_USE','Passwords')
print('added: ',res)

res = pe.revokePermissions('my@gmail.com','user','CAN_USE','Passwords')
print('revoked: ',res)

res = pe.getPermissions('Passwords')
print(res)

res = pe.getPermissions('Job',85)
print(res)
