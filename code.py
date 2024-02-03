import platform

SYSTEM = platform.system()
NAME = platform.uname()
NODE = platform.node()
Release = platform.release()
VERSION = platform.version()
MaCHINE = platform.machine()
PRocessor = platform.processor()

print(SYSTEM)
print(NAME)
print(NODE)
print(Release)
print(VERSION)
print(MaCHINE)
print(PRocessor)

import httpagentparser

if SYSTEM == "Darwin":
    s = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/532.9 (KHTML, like Gecko) \
        Chrome/5.0.307.11 Safari/532.9"
else:

    s = "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) \
        Chrome/5.0.307.11 Safari/532.9"

print(httpagentparser.simple_detect(s))