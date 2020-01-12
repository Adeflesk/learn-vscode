import os
response = os.popen('ping -n l 10.0.0.1')

for line in response.readlines():
    print(line)
