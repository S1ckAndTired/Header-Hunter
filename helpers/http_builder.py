#!/usr/bin/env python3

from helpers.requester import requester

def http_builder(targett, current_headers, origin, proxy, wordlist):
    if origin:
        if targett:
            try:
                if not targett.startswith("https://") or not origin.startswith("https://"):
                    try:
                        targett = (f"https://{targett.split('//')[1]}")
                        if origin is not None:
                            if origin.startswith("http://"): #or not 
                                origin = (f"https://{origin.split('//')[1]}")
                            elif origin.startswith("https://"):
                                pass
                            else:
                                origin = (f"https://{origin}")
                        requester(targett, origin, current_headers, proxy, wordlist)
                    except:
                        targett = (f"https://{targett}")
                        if origin is not None:
                            if origin.startswith("http://"): #or not 
                                origin = (f"https://{origin.split('//')[1]}")
                            elif origin.startswith("https://"):
                                pass
                            else:
                                origin = (f"https://{origin}") 
                        requester(targett, origin, current_headers, proxy, wordlist)
                else:
                    requester(targett, origin, current_headers, proxy, wordlist)
            except AttributeError:
                pass
    else:
        if targett:
            try:
                if not targett.startswith("https://"):
                    try:
                        targett = (f"https://{targett.split('//')[1]}")
                        requester(targett, origin, current_headers, proxy, wordlist)
                    except: 
                        targett = (f"https://{targett}")
                        requester(targett, origin, current_headers, proxy, wordlist)
                else:
                    requester(targett, origin, current_headers, proxy, wordlist)
            except AttributeError:
                pass