###
# Checks if the user has the required permissions
#
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# issubset(): True if every required permission is among the user's permissions
has_permissions = required_permissions.issubset(user_permissions)   # subset
print(has_permissions)  # Will return False because "execute" is missing.