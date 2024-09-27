import json
import sys

json.dump({"hello": "world from trusted cgi"}, sys.stdout)
