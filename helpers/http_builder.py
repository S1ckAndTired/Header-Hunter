#!/usr/bin/env python3

from helpers.requester import requester

def http_builder(targett,  header, Application_Programming_Interface, current_headers, proxy, wordlist):
    if targett:
        try:
            if not targett.startswith("https://"):
                try:
                    targett = (f"https://{targett.split('//')[1]}")
                    requester(targett,  header, Application_Programming_Interface, current_headers, proxy, wordlist)
                except:
                    targett = (f"https://{targett}")
                    requester(targett,  header, Application_Programming_Interface, current_headers, proxy, wordlist)
            else:
                requester(targett,  header, Application_Programming_Interface, current_headers, proxy, wordlist)
        except AttributeError:
            pass
    else:
        pass
