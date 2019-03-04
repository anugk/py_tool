import re
file = open('/Users/Shared/temp/ip_file.txt', 'r')
for eachline in file.readlines():
    # ip_regex = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', eachline)
    ip_regex = re.findall('(?:\d{1,3}\.){3}\d{1,3}/\d{1,2}',eachline)

    print (ip_regex)