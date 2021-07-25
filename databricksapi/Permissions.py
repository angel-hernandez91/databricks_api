from . import Databricks

class NameTypeNotSupportedException: pass

class ReturnTypeNotSupportedException: pass

papi = {
    'Tokens': {'endpoint': 'authorization/tokens', 'id_needed': 0},
    'Passwords': {'endpoint': 'authorization/passwords', 'id_needed': 0},
    'Cluster': {'endpoint': 'clusters', 'id_needed': 1},
    'Pool': {'endpoint': 'instance-pools', 'id_needed': 1},
    'Job': {'endpoint': 'jobs', 'id_needed': 1},
    'Notebook': {'endpoint': 'notebooks', 'id_needed': 1},
    'Directory': {'endpoint': 'directories', 'id_needed': 1},
    'RegisteredModel': {'endpoint': 'registered_models', 'id_needed': 1},
}


class Permissions(Databricks.Databricks):
    def __init__(self, url, token=None):
        super().__init__(token)
        self._api_type = 'permissions'
        self._url = url

    # Get permission levels
    def getPermissionLevels(self, permission_object, permission_object_id = 0):
        permission_object_settings = papi.get(permission_object, 'none')
        if permission_object_settings == 'none':
            raise NameTypeNotSupportedException("Permission object '{}' is not supported. Please use one of (Tokens,Passwords,Cluster,Pool,Job,Notebook,Directory,RegisteredModel) object types.".format(permission_object))
        else:
            if permission_object_settings['id_needed'] == 0:
                url = self._set_url(self._url, self._api_type, permission_object_settings['endpoint']+"/permissionLevels")
            else:
                url = self._set_url(self._url, self._api_type, permission_object_settings['endpoint']+'/'+str(permission_object_id)+"/permissionLevels")

            return self._get(url)

    # Get all permissions for the workspace
    def getPermissions(self, permission_object, permission_object_id = 0):
        permission_object_settings = papi.get(permission_object, 'none')
        if permission_object_settings == 'none':
            raise NameTypeNotSupportedException("Permission object '{}' is not supported. Please use one of (Tokens,Passwords,Cluster,Pool,Job,Notebook,Directory,RegisteredModel) object types.".format(permission_object))
        else:
            if permission_object_settings['id_needed'] == 0:
                url = self._set_url(self._url, self._api_type, permission_object_settings['endpoint'])
            else:
                url = self._set_url(self._url, self._api_type, permission_object_settings['endpoint']+'/'+str(permission_object_id))

            return self._get(url)

    # Update permissions for a specific entity
    def updatePermissions(self, name, name_type, permission_level, permission_object, permission_object_id = 0):
        permission_object_settings = papi.get(permission_object, 'none')
        if permission_object_settings == 'none':
            raise NameTypeNotSupportedException("Permission object '{}' is not supported. Please use one of (Tokens,Passwords,Cluster,Pool,Job,Notebook,Directory,RegisteredModel) object types.".format(permission_object))
        else:
            if permission_object_settings['id_needed'] == 0:
                url = self._set_url(self._url, self._api_type, permission_object_settings['endpoint'])
            else:
                url = self._set_url(self._url, self._api_type, permission_object_settings['endpoint']+'/'+str(permission_object_id))

            if name_type.lower() == 'user':
                payload = {"access_control_list": [{"user_name": name, "permission_level": permission_level}]}
            elif name_type.lower() == 'group':
                payload = {"access_control_list": [{"group_name": name, "permission_level": permission_level}]}
            else:
                raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))

            return self._patch(url, payload)

    # Revoke specified permission for specified identity for specified object
    def revokePermissions(self, name, name_type, permission_level, permission_object, permission_object_id = 0):

        if (name_type.lower() == 'user' or name_type.lower() == 'group'):

            permission_object_settings = papi.get(permission_object, 'none')
            if permission_object_settings != 'none':

                if permission_object_settings['id_needed'] == 0:
                    url = self._set_url(self._url, self._api_type, permission_object_settings['endpoint'])
                else:
                    url = self._set_url(self._url, self._api_type,permission_object_settings['endpoint']+'/'+str(permission_object_id))

                acl = self.getPermissions(permission_object,permission_object_id)
                new_acl = []
                for identity in acl.get('access_control_list','none'):
                    if identity.get('group_name','none') != 'none':
                        for permission in identity.get('all_permissions'):
                            if not( name_type == 'group' and identity.get('group_name','none') == name and permission_level == permission.get('permission_level','none') ):
                                new_acl.append( {'group_name': identity.get('group_name','none'), 'permission_level': permission.get('permission_level','none')} )
                    elif identity.get('user_name', 'none') != 'none':
                        for permission in identity.get('all_permissions'):
                            if not (name_type == 'user' and identity.get('user_name','none') == name and permission_level == permission.get('permission_level', 'none')):
                                new_acl.append({'user_name': identity.get('user_name', 'none'),'permission_level': permission.get('permission_level', 'none')})

                payload = { "access_control_list": new_acl }

                return self._put(url, payload)
            else:
                raise NameTypeNotSupportedException("Permission object '{}' is not supported. Please use one of (Tokens,Passwords,Cluster,Pool,Job,Notebook,Directory,RegisteredModel) object types.".format(permission_object))
        else:
            raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))
