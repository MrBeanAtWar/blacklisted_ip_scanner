import subprocess
import re
import unirest
import impconfig

MyOut = subprocess.Popen(['netstat', '-n' ],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
stdout, stderr = MyOut.communicate()

ip_list = re.findall('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', stdout)
# print(stdout)

length = len(ip_list)

for i in range(length):
    ip = ip_list[i]
    if ip == "127.0.0.1":
        continue
    url = impconfig.url_builder + ip
    response = unirest.get(url,
                           headers={
                               "X-RapidAPI-Host": impconfig.HOST,
                               "X-RapidAPI-Key": impconfig.API_K,
                               "Accept": "application/json"
                           }
                           )
    status = response.body.get("status").encode()
    blacklisted = response.body.get("content")
    black_list_value = blacklisted.get("blacklisted")
    print("IP: %s \t Status: %s \t Blacklisted: %d" %(ip,status,black_list_value))
    
    

