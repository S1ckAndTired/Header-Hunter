#!/usr/bin/env python3

import requests
import urllib3
urllib3.disable_warnings()



from helpers.header_stuff import *
from helpers.court import judger



def requester(targett,  header, api, current_headers, proxy, wordlist):
    if header is not None:
        for items in header:
            param_name, param_value = items.split(": ")
            custom_headers[param_name] = param_value

    url = targett
    if wordlist is not None:
        if proxy:
            proxy = {"https": proxy}
        base_target = (f"[•] BASE TARGET - [{targett}]")
        r = requests.head(url, proxies=proxy, headers=custom_headers, verify=False, allow_redirects=True)
        if r.url != targett:
            f = open("output-headers.txt", "a")
            f.write("                              " + "\n")
            f.write(f"[•] BASE TARGET - [{targett}]" + "\n")
            f.write(f"[»] REDIRECTION - [{r.url}]" + "\n")
            f.close()
        else:
            f = open("output-headers.txt", "a")
            f.write("                              " + "\n")
            f.write(f"[•] BASE TARGET - [{targett}]" + "\n")
            f.write(f"[-] NO REDIRECT - [{r.url}]" + "\n")
            f.close()
        headers = r.headers
        judger(headers, api, current_headers, targett, url, wordlist)
    if wordlist is None:
        if proxy:
            proxy = {"https": proxy}
        print("")
        print(f"[•] BASE TARGET - [{targett}]")
        r = requests.head(url, proxies=proxy, headers=custom_headers,  verify=False, allow_redirects=True)
        if r.url != targett:
            print(f"[»] REDIRECTION - [{r.url}]")
        else:
            print(f"[-] NO REDIRECT - [{r.url}]")
        headers = r.headers
        judger(headers, api, current_headers, targett, url, wordlist)
