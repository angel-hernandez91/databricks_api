from . import Databricks

class NameTypeNotSupportedException: pass

class ReturnTypeNotSupportedException: pass

class Permissions(Databricks.Databricks):
	def __init__(self, url, token=None):
		super().__init__(token)
		self._api_type = 'permissions'
		self._url = url
		
		
		
	# Token Permissions
	
	#Get token permission levels
	def getTokenPermissionLevels (self): 
		endpoint = 'authorization/tokens/permissionLevels'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)
		
	#Get all token permissions for the workspace	
	def getTokenPermissions (self): 
		endpoint = 'authorization/tokens'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)
		
	#Update token permissions for a specific entity
	def updateTokenPermissions (self, name, name_type, permission_level): 
		endpoint = 'authorization/tokens'
		url = self._set_url(self._url, self._api_type, endpoint)

		if name_type.lower() == 'user':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": permission_level
								}
							]
						}
		elif name_type.lower() == 'group':
			payload = {
						"access_control_list": 
							[
								{
									"group_name": name,
									"permission_level": permission_level
								}
							]
						}
		else:
			raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))

		return self._patch(url, payload)
		
	# Replace all token permissions for workspace, revoking tokens for users that no longer have permissions	
	def replaceTokenPermissions  (self, name, name_type, permission_level): 
		endpoint = 'authorization/tokens'
		url = self._set_url(self._url, self._api_type, endpoint)

		if name_type.lower() == 'user':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": permission_level
								}
							]
						}
		elif name_type.lower() == 'group':
			payload = {
						"access_control_list": 
							[
								{
									"group_name": name,
									"permission_level": permission_level
								}
							]
						}
		else:
			raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))

		return self._put(url, payload)
		
		
		
	# Passwords Permissions
	
	#Get Passwords permission levels
	def getPasswordsPermissionLevels (self): 
		endpoint = 'authorization/passwords/permissionLevels'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)
		
	#Get all Passwords permissions for the workspace	
	def getPasswordsPermissions (self): 
		endpoint = 'authorization/passwords'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)
		
	#Update Passwords permissions for a specific entity
	def updatePasswordsPermissions (self, name, name_type): 
		endpoint = 'authorization/passwords'
		url = self._set_url(self._url, self._api_type, endpoint)

		if name_type.lower() == 'user':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": {
										"permission_level": "CAN_USE",
										"description": "Permission to use this object. Applies to tokens and passwords."
										}
								}
							]
						}
		elif name_type.lower() == 'group':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": {
										"permission_level": "CAN_USE",
										"description": "Permission to use this object. Applies to tokens and passwords."
										}
								}
							]
						}
		else:
			raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))

		return self._patch(url, payload)
		
	# Replace all Passwords permissions for workspace, revoking Passwords for users that no longer have permissions	
	def replacePasswordsPermissions  (self, name, name_type): 
		endpoint = 'authorization/passwords'
		url = self._set_url(self._url, self._api_type, endpoint)

		if name_type.lower() == 'user':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": {
										"permission_level": "CAN_USE",
										"description": "Permission to use this object. Applies to tokens and passwords."
										}
								}
							]
						}
		elif name_type.lower() == 'group':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": {
										"permission_level": "CAN_USE",
										"description": "Permission to use this object. Applies to tokens and passwords."
										}
								}
							]
						}
		else:
			raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))

		return self._put(url, payload)
		
		
		
	# Cluster Permissions
	
	#Get cluster permission levels
	def getClusterPermissionLevels (self, cluster_id): 
		endpoint = '/permissions/clusters/'cluster_id'/permissionLevels'
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)
	
	#Get cluster permissions
	def getClusterPermissions 
		endpoint = '/permissions/clusters/'cluster_id
		url = self._set_url(self._url, self._api_type, endpoint)

		return self._get(url)
	
	#Update cluster permissions for a specific entity	
	def updateClusterPermissions (self, cluster_id, name, name_type, permission_level): 
		endpoint = '/permissions/clusters/'cluster_id
		url = self._set_url(self._url, self._api_type, endpoint)
		
		if name_type.lower() == 'user':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": permission_level
								}
							]
						}
		elif name_type.lower() == 'group':
			payload = {
						"access_control_list": 
							[
								{
									"group_name": name,
									"permission_level": permission_level
								}
							]
						}
		else:
			raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))

		return self._patch(url, payload)
	
	#Replace cluster permissions	
	def replaceClusterPermissions (self, cluster_id, name, name_type, permission_level):
		endpoint = '/permissions/clusters/'cluster_id
		url = self._set_url(self._url, self._api_type, endpoint)
		
		if name_type.lower() == 'user':
			payload = {
						"access_control_list": 
							[
								{
									"user_name": name,
									"permission_level": permission_level
								}
							]
						}
		elif name_type.lower() == 'group':
			payload = {
						"access_control_list": 
							[
								{
									"group_name": name,
									"permission_level": permission_level
								}
							]
						}
		else:
			raise NameTypeNotSupportedException("The name type '{}' is not supported. Please use either 'user' or 'group' name_types.".format(name_type))

		return self._put(url, payload)
		
	