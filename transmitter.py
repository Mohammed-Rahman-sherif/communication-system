import json
import requests

command = {"command": "move_forward", "distance": 10}
json_command = json.dumps(command)

response = requests.post("http://192.168.197.58:8000/execute_command", data=json_command)

if response.status_code == 200:
    print("Command executed successfully")
else:
    print("Command execution failed")
