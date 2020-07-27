import os

try:
    if os.environ['ENV'] == 'local':
        from .local import *
    elif os.environ['ENV'] == 'development':
        from .development import *
    elif os.environ['ENV'] == 'production':
        from .production import *
except KeyError:
    from .local import *
