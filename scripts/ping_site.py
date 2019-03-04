import os

def check_ping(host_name,count,waitinsec):
    response= os.system("ping "+host_name)
    # print(f" response is {response}")



check_ping('www.google.com',5,2)