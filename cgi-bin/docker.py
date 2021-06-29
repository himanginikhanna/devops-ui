#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()

f= cgi.FieldStorage()
cmd= f.getvalue("x")
g= sp.getoutput("sudo docker ps")
length = len(g.split('\n'))
if "docker" in cmd:
    if "run" in cmd:
        if length<=25:
            op= sp.getoutput("sudo "+ cmd)
            print(op)
            sp.getoutput("sudo echo 3 > /sys/proc/vm/drop_caches")
        else:
            print("""Already 25  containers are running(including K8s) you have to stop some in order to launch more....
            Please stop the containers using docker stop command
            PLEASE DO NOT STOP Kubernetes containers""")
    else:
        op= sp.getoutput("sudo "+ cmd)
        print(op)
        sp.getoutput("sudo echo 3 > /sys/proc/vm/drop_caches")
else:
    print("enter docker command only")
