# Mixin AdminAccessMixin с метод force_access(obj),
# който използва name mangling, за да върне __value без парола

class AdminAccessMixin:
    def force_access(self, obj):
        return obj._SecureData__value