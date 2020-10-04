import sys
import string
import re

# estrarre coordinate (Latitudine/longitudine) da URL google maps

url = "https://maps.google.it/maps?q=Museo+Guggenheim,+Quinta+Strada,+New+York,+Stati+Uniti&hl=it&ll=40.783921,-73.959017&spn=0.038864,0.078964&sll=41.442726,12.392578&sspn=9.847002,20.214844&oq=guggenheim+museum&t=h&hq=Museo+Guggenheim,&hnear=5th+Ave,+New+York,+Stati+Uniti&z=14&iwloc=A"
coordinate = re.findall(r'it&ll=(.*?)&spn',url)[0]
latitudine = re.findall(r'(.*?),',coordinate)[0]
longitudine = re.findall(r',(.*?)',coordinate)[0]
print coordinate
print latitudine
print longitudine




