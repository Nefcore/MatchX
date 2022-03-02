# -*- coding: utf-8 -*-

# Command line arguments 
import argparse
from urllib.parse import parse_qs
from http.cookies import SimpleCookie
from MatchX.utils.user_agents import headers

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Target URL.')
parser.add_argument('-l', '--list', help='List of URLs.')

matching_grp = parser.add_argument_group('Matching arguments')
matching_grp.add_argument('-mw', '--match-words', help='Provide a list of words or strings that you want to find in the response (Example: <script>...</script>, token=*, key=*).')
matching_grp.add_argument('-mr', '--match-regex', help='Provide a list of regex patterns that you want to find in the response (Example: root:.*:0:0).')

request_grp = parser.add_argument_group('Request arguments')
request_grp.add_argument('-m','--method', help='Request method (GET/POST), example: --method POST. Default is GET.', default="GET")
request_grp.add_argument('-d','--data', help='POST data (Example: --data "squery=google&data=hacked").')
request_grp.add_argument('--user-agent', help='Specify User agent (Example: Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0).', default=headers)
request_grp.add_argument('--timeout', help='Connection timeout, default is 30.', default=30)
request_grp.add_argument('--cookies', help='Specify cookies if required (Example: --cookies "PASS=TEST; hack=hack").')
request_grp.add_argument('--verify', help='Verify SSL cert. Default is false.', default=False, action='store_true')

other_grp = parser.add_argument_group('Other arguments')
other_grp.add_argument('-t', '--threads', help='Number of concurrent threads, default is 50.',default=50, type=int)
other_grp.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
output_grp = parser.add_argument_group('Output arguments')
output_grp.add_argument('-o', '--output', help='Write json output, default is output.json.', default='output.json')

args = parser.parse_args()

url = args.url
urls = args.list
match_words = args.match_words
match_regex = args.match_regex
user_agent = args.user_agent
timeout = args.timeout
verify = args.verify
threads = args.threads
output = args.output
cookies = args.cookies
verbose = args.verbose
method = args.method
data = args.data

if data:
    result = parse_qs(data, strict_parsing=True)
    for key in result:
        if len(result[key]) == 1:
            result[key] = result[key][0]
            data = result

if cookies:
    raw_data = cookies
    cookie = SimpleCookie()
    cookie.load(raw_data)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
else:
    pass