#!/usr/bin/env python3


from helpers.header_stuff import *
from colorama import Fore
from helpers.out import *



def judger(headers, Application_Programming_Interface, current_headers, target, url, wordlist):
    if wordlist is not None:
        f = open("output-headers.txt", "a")
        f.write("[Info Disclosure]" + "\n")
        f.close
        for information in disclosure:
            for header in headers:
                if information in header:
                    info = (f"[*] - {header}:",headers[f"{header}"])
                    informatio_disclosure = (''.join(info))
                    f = open("output-headers.txt", "a")
                    f.write(informatio_disclosure + "\n")
                    f.close()
                else:
                    pass  
        if Application_Programming_Interface is not None:
            for must_have in mind_headers_Application_Programming_Interface:
                if must_have not in headers:
                    missing.append(must_have)
                else:
                    pass
            for header in headers:
                    casual_headers.append(header)
            out(headers, current_headers, wordlist)
        else:
            for must_have in mind_headers_html:
                if must_have not in headers:
                    missing.append(must_have)
                else:
                    pass
            for header in headers:
                    casual_headers.append(header)
            out(headers, current_headers, wordlist)
    elif wordlist is None:
        print("")
        print("[Info Disclosure]")
        for information in disclosure:
            for header in headers:
                if information in header:
                    print(f"[*] - {header}:",headers[f"{header}"])    
        if Application_Programming_Interface is True:
            for must_have in mind_headers_api:
                if must_have not in headers:
                    missing.append(must_have)
                else:
                    pass
            for header in headers:
                    casual_headers.append(header)
            out(headers, current_headers, wordlist)
        elif Application_Programming_Interface is False:
            for must_have in mind_headers_html:
                if must_have not in headers:
                    missing.append(must_have)
                else:
                    pass
            for header in headers:
                    casual_headers.append(header)
            out(headers, current_headers, wordlist)
