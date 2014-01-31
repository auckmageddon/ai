# Settings for AI.  Inspired by Heorku 12-factor; you should change .env rather than this file.
from os import getenv, path
from django.core.exceptions import ImproperlyConfigured
import dj_database_url

# Determine where the settings.py is located -- we use this for the relative paths later
__PROJECT_ROOT__ = path.abspath(path.dirname(__file__))

DEBUG = bool(getenv('DEVELOPMENT', 'false')) # Default to production mode
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.parse(getenv('DATABASE_URL'))
}

TIME_ZONE = 'Pacific/Auckland'
LANGUAGE_CODE = 'en-nz'
SITE_ID = 1
USE_I18N = False
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = path.join(__PROJECT_ROOT__, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = path.join(__PROJECT_ROOT__, 'static-collected')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path.join(__PROJECT_ROOT__, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'ai.storage.CachedPipelineRequireStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = getenv('SECRET_KEY')
if SECRET_KEY is None:
    raise ImproperlyConfigured('The SECRET_KEY environment variable must be set.')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ai.urls'
WSGI_APPLICATION = 'ai.wsgi.application'

TEMPLATE_DIRS = (
    path.join(__PROJECT_ROOT__, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Toolbelt
    'jstemplate',
    # 'manifesto',
    'pipeline',
    'require',
    'south',

    # Our in-project apps
    'apps.client',
    'apps.intranet'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.TemplateHTMLRenderer',
        'djangorestframework_camel_case.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.CamelCaseJSONParser', 

    ),
    'DATETIME_FORMAT': 'iso-8601',
    
}

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'styles/main.scss',
        ),
        'output_filename': 'styles/main.css',
    }
}

PIPELINE_CSS_COMPRESSOR = None
#PIPELINE_JS_COMPRESSOR = None
#PIPELINE_ENABLED = False

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)

REQUIRE_BASE_URL = "scripts/"
REQUIRE_BUILD_PROFILE = 'app.build.js'

# The name of the require.js script used by your project, relative to REQUIRE_BASE_URL.
REQUIRE_JS = "../bower_components/requirejs/require.js"

# A dictionary of standalone modules to build with almond.js.
# See the section on Standalone Modules, below.
REQUIRE_STANDALONE_MODULES = {
    'main': {
        'out': 'main.dist.js',
        'build_profile': 'main.build.js'
    }
}

# A tuple of files to exclude from the compilation result of r.js.
REQUIRE_EXCLUDE = ("build.txt",)

# The execution environment in which to run r.js: auto, node or rhino.
# auto will autodetect the environment and make use of node if available and rhino if not.
# It can also be a path to a custom class that subclasses require.environments.Environment and defines some "args" function that returns a list with the command arguments to execute.
REQUIRE_ENVIRONMENT = "node"
