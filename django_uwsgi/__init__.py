__version__ = '0.1.0'


try:
    import uwsgi
except ImportError:
    uwsgi = False


try:
    import cPickle as pickle
except ImportError:
    import pickle


default_app_config = 'django_uwsgi.apps.uWSGIKitConfig'
