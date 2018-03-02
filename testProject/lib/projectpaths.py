import os

SOURCE_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir
))

APP_PATH= os.path.normpath(os.getcwd())

SOURCE_LIB_PATH = os.path.join(SOURCE_PATH, 'lib')
SOURCE_MODULE_PATH = os.path.join(SOURCE_PATH, 'modules')
APP_LIB_PATH = os.path.join(APP_PATH, 'lib')
APP_MODULE_PATH = os.path.join(APP_PATH, 'modules')
APP_CONFIG_PATH = os.path.join(APP_LIB_PATH, '.config')
