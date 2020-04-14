import requests
import sys
import re
import subprocess


print("Python version")
print (sys.version)


#Below Apple Script to create a POPUP
applescript = """
display dialog "Your Item is Available" ¬
with title "POPUP FROM PYTHON" ¬
with icon caution ¬
buttons {"OK"}
"""

##muliline comment Command+/
#https://realpython.com/python-requests/
#https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
#https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/
#https://stackoverflow.com/questions/20065094/simple-pop-up-balloon-message-on-mac-using-python

#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
headers = {'User-Agent': user_agent}
#OOS
#url='https://www.costco.com/lg-32%22-class-full-hd-ips-monitor.product.100454122.html'

#In Stock
url='https://www.costco.com/.product.100512138.html'


r = requests.get(url,headers=headers)
print(r.status_code)
#print(r.text)
#print(r.content)

my_text='value="Add to Cart"'

if re.search('value="Add to Cart"',r.text):
    print("IN Stock")
    subprocess.call("osascript -e '{}'".format(applescript), shell=True)
else:
    print("Out Of Stock")



print ("complete")