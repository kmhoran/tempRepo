import configparser
from lib import projectpaths
def _get_config_title():
    return 'Twitter'

def _set_config():
    config = {}
    enable_twitter_input = input("Post commit messages to Twitter? [Y/n]\n")
    enable_twitter = False if enable_twitter_input.lower() == 'n' else True
    config['TwitterEnabled'] = str(enable_twitter)

    if enable_twitter:
        print(
        """
        ###########################################################
        Posting to Twitter must be done through your Twitter App.
            Please take a moment to gather your access credentials.
            If you do not yet have these, leave the following 
            credential inputs blank. You will be prompted for them 
            again at your next commit.
        ############################################################
        """)
        
        config['ConsumerKey'] = input("Consumer Key:\n")
        config['ConsumerSecret'] = input("Consumer Secret:\n")
        config['AccessTokenKey'] = input("Access Token Key:\n")
        config['AccessTokenSecret']= input("Access Token Secret:\n")
    return config



class Twitter:
    
    @property
    def config_title(self):
        return _get_config_title()

    # @classmethod
    # def get_profile(cls, config_title):
    #     print(projectpaths.APP_CONFIG_PATH)
    #     config = configparser.ConfigParser()
    #     config.read(projectpaths.APP_CONFIG_PATH)
    #     return config._sections

    def __init__(self, profile):
        self.profile = profile[self.config_title]
        print("new twitter class: {0}".format(self.profile))
    

    def Tweet(self, message):
        print("tweeting: " + message)