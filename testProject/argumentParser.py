import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description="test parser")
    parser.add_argument("-t", "--twitter", action='store_true')
    return parser.parse_args()

def run(args=None):
    if not args:
        print ("No args given")
    else: 
        if args.twitter:
            print("Let's tweet!")
        else:
            print("no tweeting today")

# 
# comment r
if __name__ == "__main__":
    print("Entering argument parser!")
    args = arg_parse()
    run(args)s