from secure_data import SecureData
from tools import AdminAccessMixin

class AdminData(SecureData, AdminAccessMixin):
    pass

data = AdminData("SECRET", "abc123")
print(data.access("wrong"))        # None
print(data.force_access(data))     # SECRET