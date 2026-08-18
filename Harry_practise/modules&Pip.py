# 2 types 1.Builtin module, 2. External Module
import math
print(math.ceil(4))
print(math.floor(4))
print(math.pow(2,3))

import json
print(json.dumps({"a":1,"b":2,"c":3},sort_keys=True))
print(json.JSONEncoder().encode({"a":1,"b":2,"c":3}))

import os
#print(os.getcwd())
#rint(os.listdir())
import requests
r= requests.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=815461296140&hvpos=&hvnetw=g&hvrand=629141053414558824&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007740&hvtargid=kwd-64107830&hydadcr=14452_2462829&mcid=e9c68a2d0f333bcaacd29ec00843c329&hvocijid=629141053414558824--&hvexpln=nav&gad_source=1")
#print(r.status_code)
print(r.text)
print(r.json())


#2 External Library
import importMyModule
print(importMyModule.Squarert(5))
print(importMyModule.add(5,10))
