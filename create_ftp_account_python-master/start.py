import os
import subprocess
from subprocess import call
import shlex

username = raw_input("inserisci username:")
password = raw_input("inserisci password:")

print username
print password

call(shlex.split('./createftp.sh' + ' ' +  username + ' ' + password))


#subprocess.Popen(["ls", "-l"])  # doesn't capture output
#call("./createftp.sh romeo giulietto")
## sudo adduser frankie && sudo usermod -d /home/frankie frankie

