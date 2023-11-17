#!/usr/bin/env python3

from helpers.requester import requester
import asyncio

def http_builder(targett,  header, api, proxy, wordlist, raw, output):
    if targett:
        try:
            if not targett.startswith("https://"):
                try:
                    targett = (f"https://{targett.split('//')[1]}")
                    asyncio.run(requester(targett,  header, api, proxy, wordlist, raw, output))
                except:
                    targett = (f"https://{targett}")
                    asyncio.run(requester(targett,  header, api, proxy, wordlist, raw, output))
            else:
                asyncio.run(requester(targett,  header, api, proxy, wordlist, raw, output))
        except AttributeError:
            pass
    else:
        pass
