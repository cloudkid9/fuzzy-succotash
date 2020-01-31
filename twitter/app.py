import twitter
import argparse 

parser = argparse.ArgumentParser(description="The ting for the twitter")
parser.add_argument('--name', help='foo help')

args = parser.parse_args()

name = args.name
if not name:
    name = "anonimoose"


print("You are here forever %s." % args.name)
# api = twitter.Api(consumer_key='consumer_key',
#     consumer_secret='consumer_secret',
#     access_token_key='access_token',
#     access_token_secret='access_token_secret')

# print(api.VerifyCredentials())

# results = api.GetSearch(
#     raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")

# print(results)