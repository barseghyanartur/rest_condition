__all__ = ('Boolean',)

class Boolean(int):
    def __new__(cls, x, message):
        obj = int.__new__(cls, x)
        obj.message = message
        return obj
