#!/usr/bin/env python3 

from helpers.header_stuff import *

def out(headers, current_headers, wordlist):
    if wordlist is not None:
        f = open("output-headers.txt", "a")
        f.write("[Missing Security Headers]" + "\n")
        f.close()
        for i_miss_you in missing:
            missing_headers = (f"[x] - {i_miss_you}")
            f = open("output-headers.txt", "a")
            f.write(missing_headers + "\n")
            f.close()
        missing.clear()
        if current_headers == True:
            f = open("output-headers.txt", "a")
            f.write("[Current Headers]" + "\n")
            f.close()
            for casual in casual_headers:
                in_use_headers = (f"[✓] - {casual}")
                f = open("output-headers.txt", "a")
                f.write(in_use_headers + "\n")
                f.close()
            casual_headers.clear()
        else:
            pass
    elif wordlist is None:
        print("")
        print("[Missing Security Headers]")
        for i_miss_you in missing:
            print(f"[x] - {i_miss_you}")
        missing.clear()
        if current_headers == True:
            print("")
            print("[Current Headers]")
            for casual in casual_headers:
                print(f"[✓] - {casual}")
            casual_headers.clear()
