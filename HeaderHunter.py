#!/usr/bin/env python3



import argparse
from progress.bar import Bar
from helpers.requester import requester
from helpers.http_builder import http_builder
from helpers.header_stuff import on_the_fly
from colorama import Fore

blah = {}
parser = argparse.ArgumentParser()

parser.add_argument("-H", "--header", metavar="", action="append", help="This is self explaining")
parser.add_argument("-o", "--output", action="store_true", help="Output results to file")
parser.add_argument("-x", "--proxy", metavar="", help="Proxy - http://IP:PORT")
parser.add_argument("-api", "--api", action="store_true", help="Set it for api")
parser.add_argument("-r", "--raw", action="store_true", help="Display raw response")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--target", metavar="")
group.add_argument("-w", "--wordlist", metavar="", help="Provide list of targets")
parser.add_argument(" ", nargs="*")
args = parser.parse_args()
raw = args.raw
output = args.output
target = args.target
header = args.header
wordlist = args.wordlist
proxy = args.proxy
api = args.api


def start():
    ORANGE = '\33[33m'
    NC = '\033[0m'
    print(Fore.BLUE +"Powered By: " + Fore.RESET + ORANGE + "BERGHEM - Smart Information Security" + NC)
    if wordlist:
        if output:
            f = open("output-headers.txt", "a")
            f.write(ORANGE+f"Created by: SickAndTired"+NC + "\n")
            f = open(wordlist, "r")
            for t in f:
                targett = t.strip()
                on_the_fly[targett] = on_the_fly.get(targett, 0) + 1
            
            f = open(wordlist, "r")
            bar = Bar (f"[+] Targets analysed",max=sum(on_the_fly.values()), fill="█")
            for t in f:
                print("\r    Fetching headers", end=""),bar.next()
                targett = t.strip()
                http_builder(targett, header, api, proxy, wordlist, raw, output)
            bar.finish()
        else:
            f = open(wordlist, "r")
            for t in f:   
                targett = t.strip()
                http_builder(targett, header, api, proxy, wordlist, raw, output)
            
    elif target:
        targett = target
        http_builder(targett,  header, api, proxy, wordlist, raw, output)

start()
