import re;

#find all digits in the string

str1 = "get my 4205 address 9090 and zip 94538."

#print (re.findall('\d+',str1))

result = re.findall('\d+',str1);

#print(result[0])
#print(result[1])

for result_num in result:
    print (result_num)