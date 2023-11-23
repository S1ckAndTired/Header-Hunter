#!/usr/bin/env python3

from helpers.header_stuff import *
from colorama import Fore
from helpers.court import judger
import requests, httpx, asyncio, sys, os
from urllib3 import disable_warnings
disable_warnings()


async def requester(targett, header, api, proxy, wordlist, raw, output):
    url = targett
    if header is not None:
        for items in header:
            param_name, param_value = items.split(": ")
            custom_headers[param_name] = param_value
    if proxy:
        proxy1, proxy2 = {"https://": proxy}, {"https": proxy}
    else:
        proxy1, proxy2 = None, None
    
    client = httpx.AsyncClient(http2=True, verify=False, proxies=proxy)
    if wordlist is None:
        print("")
        print(f"[•] BASE TARGET - [{targett}]")
        try:
            r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
            headers = r.headers
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                print(f"[-] NO REDIRECT - [{r.url}]")
            headers = r.headers
            if raw is True:
                print("")
                print(f"[▼] RAW CONTENT - [{r.url}]")
                print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
                for header, value in zip(headers, headers.values()):
                    print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
                print("")
            judger(headers, api, wordlist, output)
        except httpx.RemoteProtocolError:
            try:
                r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    print(f"[»] REDIRECTION - [{r.url}]")
                else:
                    print(f"[-] NO REDIRECT - [{r.url}]")
                headers = r.headers
                
                if raw is True:
                    print(f"[▼] RAW CONTENT - [{r.url}]")
                    print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
                    for header, value in zip(headers, headers.values()):
                        print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                    print("")
                judger(headers, api, wordlist, output)
            except requests.exceptions.ConnectionError as errc:
                print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
                print(Fore.RED+f"[-] ERROR [{errc}]"+NC)
                print(Fore.GREEN+"[*] Consider proxing it!"+NC)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
        except httpx.ConnectError:
            r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
            headers = r.headers
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                print(f"[-] NO REDIRECT - [{r.url}]")
            if raw is True:
                print("")
                print(f"[▼] RAW CONTENT - [{r.url}]")
                print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+NC)
                for header, value in zip(headers, headers.values()):
                    print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                print("")
            judger(headers, api, wordlist, output)
        except requests.exceptions.ConnectionError as e:
            print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
            print(Fore.RED+f"[-] ERROR {e}"+NC)
            print(Fore.GREEN+"[*] Consider proxing it!"+NC)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
        except httpx.ConnectTimeout as e:
            print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
            print(Fore.RED+f"[-] ERROR {e}"+NC)
            print(Fore.GREEN+"[*] Consider proxing it!"+NC)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
    if wordlist is not None:
        if proxy:
            proxy1, proxy2 = {"https://": proxy}, {"https": proxy}
        else:
            proxy1, proxy2 = None, None
        
        if output:
            client = httpx.AsyncClient(http2=True, verify=False, proxies=proxy)
            try:
                r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    if raw is True:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.YELLOW+"[»]"+NC+f" REDIRECTION - [{Fore.YELLOW+str(r.url)+NC}]" + "\n")
                        f.write("                              " + "\n")
                        f.write(f"[+] RAW CONTENT - [{r.url}]" + "\n")
                        f.write(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+NC + "\n")
                        for header, value in zip(headers, headers.values()):
                            f.write(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                    else:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.YELLOW+"[»]"+NC+f" REDIRECTION - [{Fore.YELLOW+str(r.url)+NC}]" + "\n")
                        f.close()
                else:
                    if raw is True:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.WHITE+"[-]"+NC+f" NO REDIRECT - [{Fore.WHITE+str(r.url)+NC}]" + "\n")
                        f.write("                              " + "\n")
                        f.write(f"[+] RAW CONTENT - [{r.url}]" + "\n")
                        f.write(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+NC + "\n")
                        for header, value in zip(headers, headers.values()):
                            f.write(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                    else:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.WHITE+"[-]"+NC+f" NO REDIRECT - [{Fore.WHITE+str(r.url)+NC}]" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                judger(headers, api, wordlist, output)
            except httpx.RemoteProtocolError:
                r = requests.get(url, proxies=proxy, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    if raw is True:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.YELLOW+"[»]"+NC+f" REDIRECTION - [{Fore.YELLOW+str(r.url)+NC}]" + "\n")
                        f.write("                              " + "\n")
                        f.write(f"[+] RAW CONTENT - [{r.url}]" + "\n")
                        f.write(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}"+NC + "\n")
                        for header, value in zip(headers, headers.values()):
                            f.write(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                    else:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.YELLOW+"[»]"+NC+f" REDIRECTION - [{Fore.YELLOW+str(r.url)+NC}]" + "\n")
                        f.close()
                else:
                    if raw is True:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(f"[-] NO REDIRECT - [{targett}]" + "\n")
                        f.write("                              " + "\n")
                        f.write(f"[▼] RAW CONTENT - [{targett}]" + "\n")
                        f.write(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}"+NC + "\n")
                        for header, value in zip(headers, headers.values()):
                            f.write(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                    else:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(f"[-] NO REDIRECT - [{targett}]" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                judger(headers, api, wordlist, output)
            except httpx.ConnectError:
                r = requests.get(url, proxies=proxy, headers=custom_headers,  verify=False, allow_redirects=True)
                headers = r.headers
                if r.url != targett:
                    if raw is True:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.YELLOW+"[»]"+NC+f" REDIRECTION - [{Fore.YELLOW+str(r.url)+NC}]" + "\n")
                        f.write("                              " + "\n")
                        f.write(f"[+] RAW CONTENT - [{r.url}]" + "\n")
                        f.write(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}"+NC + "\n")
                        for header, value in zip(headers, headers.values()):
                            f.write(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                    else:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(Fore.YELLOW+"[»]"+NC+f" REDIRECTION - [{Fore.YELLOW+str(r.url)+NC}]" + "\n")
                        f.close()
                else:
                    if raw is True:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(Fore.RED+"[•]"+NC+f" BASE TARGET - [{Fore.RED+targett+NC}]" + "\n")
                        f.write(f"[-] NO REDIRECT - [{targett}]" + "\n")
                        f.write("                              " + "\n")
                        f.write(f"[▼] RAW CONTENT - [{targett}]" + "\n")
                        f.write(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}"+NC + "\n")
                        for header, value in zip(headers, headers.values()):
                            f.write(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                    else:
                        f = open("output-headers.txt", "a")
                        f.write("                              " + "\n")
                        f.write(f"[•] BASE TARGET AQUI-2- [{targett}]" + "\n")
                        f.write(f"[-] NO REDIRECT - [{targett}]" + "\n")
                        f.write("                              " + "\n")
                        f.close()
                judger(headers, api, wordlist, output)
        else:
            print("AQUI AQUI AQUI AQUI")        
            try:
                if proxy:
                    proxy1, proxy2 = {"https://": proxy}, {"https": proxy}
                else:
                    proxy1, proxy2 = None, None
                client = httpx.AsyncClient(http2=True, verify=False, proxies=proxy1)
                print("")
                print(f"[•] BASE TARGET - [{targett}]")
                try:
                    r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
                    headers = r.headers
                    if r.url != targett:
                        print(f"[»] REDIRECTION - [{r.url}]")
                    else:
                        print(f"[-] NO REDIRECT - [{r.url}]")
                    if raw is True:
                        print("")
                        print(f"[▼] RAW CONTENT - [{r.url}]")
                        print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+NC)
                        for header, value in zip(headers, headers.values()):
                            print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                        print("")
                    judger(headers, api, wordlist, output)
                except httpx.RemoteProtocolError:
                    try:
                        r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                        headers = r.headers
                        if r.url != targett:
                            print(f"[»] REDIRECTION - [{r.url}]")
                        else:
                            print(f"[-] NO REDIRECT - [{r.url}]")
                        headers = r.headers
                        
                        if raw is True:
                            print(f"[▼] RAW CONTENT - [{r.url}]")
                            print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
                            for header, value in zip(headers, headers.values()):
                                print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                            print("")
                        judger(headers, api, wordlist, output)
                    except requests.exceptions.ConnectionError as errc:
                        print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
                        print(Fore.RED+f"[-] ERROR [{errc}]"+NC)
                        print(Fore.GREEN+"[*] Consider proxing it!"+NC)
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ConnectError:
                    r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
                    headers = r.headers
                    if r.url != targett:
                        print(f"[»] REDIRECTION - [{r.url}]")
                    else:
                        print(f"[-] NO REDIRECT - [{r.url}]")
                    if raw is True:
                        print("")
                        print(f"[▼] RAW CONTENT - [{r.url}]")
                        print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+NC)
                        for header, value in zip(headers, headers.values()):
                            print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                        print("")
                    judger(headers, api, wordlist, output)
                except requests.exceptions.ConnectionError as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
                    print(Fore.RED+f"[-] ERROR {e}"+NC)
                    print(Fore.GREEN+"[*] Consider proxing it!"+NC)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ConnectTimeout as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
                    print(Fore.RED+f"[-] ERROR {e}"+NC)
                    print(Fore.GREEN+"[*] Consider proxing it!"+NC)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            except UnboundLocalError:
                r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    print(f"[»] REDIRECTION - [{r.url}]")
                else:
                    print(f"[-] NO REDIRECT - [{r.url}]")
                if raw is True:
                    print("")
                    print(f"[▼] RAW CONTENT - [{r.url}]")
                    print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+NC)
                    for header, value in zip(headers, headers.values()):
                        print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                    print("")
                judger(headers, api, wordlist, output)
            except httpx.RemoteProtocolError:
                try:
                    r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                    headers = r.headers
                    if r.url != targett:
                        print(f"[»] REDIRECTION - [{r.url}]")
                    else:
                        print(f"[-] NO REDIRECT - [{r.url}]")
                    
                    if raw is True:
                        print(f"[▼] RAW CONTENT - [{r.url}]")
                        print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
                        for header, value in zip(headers, headers.values()):
                            print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                        print("")
                    judger(headers, api, wordlist, output)
                except requests.exceptions.ConnectionError as errc:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
                    print(Fore.RED+f"[-] ERROR {e}"+NC)
                    print(Fore.GREEN+"[*] Consider proxing it!"+NC)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            except httpx.ConnectError:
                r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    print(f"[»] REDIRECTION - [{r.url}]")
                else:
                    print(f"[-] NO REDIRECT - [{r.url}]")
                if raw is True:
                    print("")
                    print(f"[▼] RAW CONTENT - [{r.url}]")
                    print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+NC)
                    for header, value in zip(headers, headers.values()):
                        print(f"{Fore.WHITE+header+NC}: {Fore.GREEN+value+NC}")
                    print("")
                judger(headers, api, wordlist, output)
            except requests.exceptions.ConnectionError:
                print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
                print(Fore.RED+f"[-] ERROR {e}"+NC)
                print(Fore.GREEN+"[*] Consider proxing it!"+NC)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            except httpx.ConnectTimeout:
                print(Fore.RED+f"[-] Host [{targett}] errored out"+NC)
                print(Fore.RED+f"[-] ERROR {e}"+NC)
                print(Fore.GREEN+"[*] Consider proxing it!"+NC)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
