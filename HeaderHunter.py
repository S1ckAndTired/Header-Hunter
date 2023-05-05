#!/usr/bin/env python3



import argparse
from progress.bar import Bar
from helpers.requester import requester
from helpers.http_builder import http_builder
from helpers.header_stuff import on_the_fly


parser = argparse.ArgumentParser()

parser.add_argument("-ch","--cheaders", action="store_true", help="Fetch current headers")
parser.add_argument("-o", "--origin", metavar="", help="Origin required for API")
parser.add_argument("-x", "--proxy", metavar="", help="Proxy - http://IP:PORT")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--target", metavar="")
group.add_argument("-w", "--wordlist", metavar="", help="Provide list of targets")
parser.add_argument(" ", nargs="*")
args = parser.parse_args()
target = args.target
origin = args.origin
wordlist = args.wordlist
current_headers = args.cheaders
proxy = args.proxy



def start():
    print("Powered By: BERGHEM - Smart Security Information")
    if wordlist:
        f = open(wordlist, "r")
        for t in f:
            targett = t.strip()
            on_the_fly[targett] = on_the_fly.get(targett, 0) + 1
        
        f = open(wordlist, "r")
        bar = Bar (f" [+] Targets analysed",max=sum(on_the_fly.values()), fill="█")
        for t in f:
            print("\r    Fetching headers", end=""),bar.next()
            targett = t.strip()
            if current_headers == True:
                http_builder(targett, current_headers, origin, proxy, wordlist)
            elif current_headers == False:
                http_builder(targett, current_headers, origin, proxy, wordlist)
        bar.finish()
    elif target:
        targett = target
        if current_headers == True:
            http_builder(targett, current_headers, origin, proxy, wordlist)
        elif current_headers == False:
            http_builder(targett, current_headers, origin, proxy, wordlist)

start()
