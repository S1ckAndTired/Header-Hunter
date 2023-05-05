#!/usr/bin/env python3

import requests
import urllib3
urllib3.disable_warnings()



from helpers.header_stuff import *
from helpers.court import judger



def requester(targett, origin, current_headers, proxy, wordlist):
    url = targett
    if wordlist is not None:
        if proxy:
            proxy = {"https": proxy}
        if origin != None:
            headers = {"Origin": origin}
            r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=True)
            if r.url != targett:
                f = open("output-headers.txt", "a")
                f.write("                              " + "\n")
                f.write(f"[•] BASE TARGET - [{targett}]" + "\n")
                f.write(f"[»] REDIRECTION - [{r.url}]" + "\n")
                f.close()
            else:
                pass
            headers = r.headers
            judger(headers, current_headers, targett, url, wordlist)
            
        elif origin == None:
            base_target = (f"[•] BASE TARGET - [{targett}]")
            r = requests.get(url, proxies=proxy, verify=False, allow_redirects=True)
            if r.url != targett:
                f = open("output-headers.txt", "a")
                f.write("                              " + "\n")
                f.write(f"[•] BASE TARGET - [{targett}]" + "\n")
                f.write(f"[»] REDIRECTION - [{r.url}]" + "\n")
                f.close()
            else:
                pass
            headers = r.headers
            judger(headers, current_headers, targett, url, wordlist)
    if wordlist is None:
        if proxy:
            proxy = {"https": proxy}
        if origin != None:
            print("")
            print(f"[•] BASE TARGET - [{targett}]")
            headers = {"Origin": origin}
            r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=True)
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                pass
            headers = r.headers
            judger(headers, current_headers, targett, url, wordlist)
            
        elif origin == None:
            print("")
            print(f"[•] BASE TARGET - [{targett}]")
            r = requests.get(url, proxies=proxy, verify=False, allow_redirects=True)
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                pass
            headers = r.headers
            judger(headers, current_headers, targett, url, wordlist)
            
