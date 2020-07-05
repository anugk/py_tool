import re
import urllib;


t_check_1="03/30/2019","Mountain House, CA Market Trends - Movoto"

term = urllib.quote("'{}'".format(term))

to_check='03/30/2019,"Mountain House, CA Market Trends - Movoto"'
str = '"03/30/2019,""Mountain House, CA Market Trends - Movoto"",50,55,17,""$618,853"",""$628,950"",""$649,000"",0%,1%,0%,21,52,7,253,253,253"'
if re.search(to_check, str):
    print('Found')
else:
    print('Found')


