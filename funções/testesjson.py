import json
import urllib2


response = urllib.urlo

json_data = '{"person": {"name": "John", "age": 30}}'
data = json.loads(json_data)
# Accessing nested data

print(data['person'].keys())


