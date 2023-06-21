#!/usr/bin/env python3



import argparse
from progress.bar import Bar
from helpers.requester import requester
from helpers.http_builder import http_builder
from helpers.header_stuff import on_the_fly

blah = {}
parser = argparse.ArgumentParser()

parser.add_argument("-ch","--cheaders", action="store_true", help="Fetch current headers")
parser.add_argument("-H", "--header", metavar="", action="append", help="This is self explaining")
parser.add_argument("-x", "--proxy", metavar="", help="Proxy - http://IP:PORT")
parser.add_argument("-api", "--api", action="store_true", help="Set it for api")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--target", metavar="")
group.add_argument("-w", "--wordlist", metavar="", help="Provide list of targets")
parser.add_argument(" ", nargs="*")
args = parser.parse_args()
target = args.target
header = args.header
wordlist = args.wordlist
current_headers = args.cheaders
proxy = args.proxy
api = args.api

def start():
    print("\nPowered By: BERGHEM - Smart Information Security")
    if wordlist:
        f = open(wordlist, "r")
        for t in f:
            targett = t.strip()
            on_the_fly[targett] = on_the_fly.get(targett,  header, 0) + 1
        
        f = open(wordlist, "r")
        bar = Bar (f" [+] Targets analysed",max=sum(on_the_fly.values()), fill="█")
        for t in f:
            print("\r    Fetching headers", end=""),bar.next()
            targett = t.strip()
            if current_headers == True:
                http_builder(targett, header, api, current_headers, proxy, wordlist)
            elif current_headers == False:
                http_builder(targett, header, api, current_headers, proxy, wordlist)
        bar.finish()
    elif target:
        targett = target
        if current_headers == True:
            http_builder(targett,  header, api, current_headers, proxy, wordlist)
        elif current_headers == False:
            http_builder(targett,  header, api, current_headers, proxy, wordlist)

start()
