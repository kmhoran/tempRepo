import sys
import os
import configparser
from lib import projectpaths
from lib.modules import twitter_bug as twitter


CONFIG_NAME = 'my_config.ini'


def build_config_file():
    
    basepath = projectpaths.APP_CONFIG_PATH
    print('\n##Building Configuration ##\n')
    parser = configparser.ConfigParser()
    parser['Default'] = {'ProjectName': 'Untitled'}

    twitter_title = twitter._get_config_title()
    parser[twitter_title] = twitter._set_config()
    
    config_path = os.path.join(basepath, CONFIG_NAME)

    with open(config_path, 'w') as configfile:
        parser.write(configfile)
    


def get_confilg_file():
    basepath = projectpaths.APP_CONFIG_PATH
    if not os.path.exists(basepath): 
        os.mkdir(basepath)
    if CONFIG_NAME not in os.listdir(basepath):
        build_config_file()
        if CONFIG_NAME not in os.listdir(basepath):
            raise OSError("Unable to create config file.")
            sys.exit(1)
    return os.path.join(basepath, CONFIG_NAME) 