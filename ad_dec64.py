import base64
import zlib
import json

#.AAE
aD = b"Adjustment_Data_Here"
aD_decoded = base64.b64decode(aD)

aD_decompress = zlib.decompress(aD_decoded, -zlib.MAX_WBITS)
aD_json = json.loads(aD_decompress)

print(json.dumps(aD_json, indent=2))
