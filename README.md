# CRLFuzzer

A fast tool for scanning CRLF vulnerabilities

<img src="https://raw.githubusercontent.com/randixploit/crlfuzzer/refs/heads/main/images/Screenshot_20250127-183928.jpg">

# About CRLFuzzer

CRLFuzzer is a tool for scanning CRLF vulnerabilities using threadpool, so that the scanning process can run quickly and accurately. This tool is equipped with a built-in payload to check vulnerabilities on targeted websites, so you don't need to provide an additional payload.

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
