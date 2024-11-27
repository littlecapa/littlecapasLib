#
# Single Implenation according to: https://medium.com/django-unleashed/exploring-the-singleton-design-pattern-in-django-df796b181a13
#
class SingletonMeta(type):
    """
    A Singleton metaclass that ensures a class has only one instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]