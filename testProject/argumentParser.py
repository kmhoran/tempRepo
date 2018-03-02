import os
import argparse
import configparser
from lib import config_manager
from lib.modules.twitter_bug import Twitter



def arg_parse():
    parser = argparse.ArgumentParser(description="test parser")
    parser.add_argument("commit_message", type=str, help="the message from the last commit")
    return parser.parse_args()
    



def run(args=None):
    config_file = config_manager.get_confilg_file()

    config = configparser.ConfigParser()
    config.read(config_file)
    profile = config._sections
    if not args:
        print ("\nNo args given")
    else: 
        twitter = Twitter(profile)
        print("\n")
        twitter.Tweet(args.commit_message)


if __name__ == "__main__":

    args = arg_parse()
    run(args)