# CRLFuzzer
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.x-blue.svg"></a>
<a href="https://opensource.org/license/MIT"><img src="https://img.shields.io/badge/license-MIT-green.svg"></a>

CRLFuzzer is a tool for scanning CRLF vulnerabilities using threadpool, so that the scanning process can run quickly and accurately. This tool is equipped with a built-in payload to check vulnerabilities on targeted websites, so you don't need to provide an additional payload.

# Disclaimer

This tool is intended **only for ethical purposes** such as bug bounty programs and vulnerability reporting on authorized platforms.  
Misuse of this tool is strictly prohibited and is the sole responsibility of the user.  
Use it only on systems you own or have explicit permission to test.

# Screenshots

<img src="https://raw.githubusercontent.com/randixploit/crlfuzzer/refs/heads/main/images/Screenshot_20250127-183928.jpg">

# Help

```
usage: crlfuzzer [-h] [-u <URL> | -l <FILE>]

options:
  -h, --help            show this help message and exit
  -u <URL>, --url <URL>
                        target
  -l <FILE>, --list <FILE>
                        file
```

# Installation

```
$ git clone https://github.com/randixploit/crlfuzzer
$ cd crlfuzzer
$ pip3 install -r requirements.txt
$ python3 setup.py install
```

# Usage

Single Scanning:
```
$ crlfuzzer -u http://example.com
```

Mass Scanning:
```
$ crlfuzzer -l file.txt
```

<i>I hope my project can be useful for everyone, thank you for using the tools I made</i>
