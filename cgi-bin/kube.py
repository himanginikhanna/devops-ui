#!/usr/bin/python3
import cgi,re
import subprocess as sp

print("content-type: text/html")
print()

f= cgi.FieldStorage()
cmd= f.getvalue("x")
g= sp.getoutput("sudo kubectl get pods")
length = int(len(g.split('\n')))
#cmd = "kubectl create deployment --image=centos --replicas=10"
def find_number(text, c):
    return re.findall(r'%s(\d+)' % c, text)	
if ("kubectl" in cmd):
    if "deployment" in cmd and  (length <= 4):
        if ("--replicas" in cmd):
            k=find_number(cmd, 'replicas=')
            l=int(k[0])
            #print(l)
	    #l=int(cmd[-1])
            if l<=5:
                op= sp.getoutput("sudo "+ cmd)
                print(op)
                sp.getoutput("sudo echo 3 > /sys/proc/vm/drop_caches")
            else:
                print(" Sorry you cant launch replicas more than 5 ")
        else:
            op= sp.getoutput("sudo "+ cmd)
            print(op)
            sp.getoutput("sudo echo 3 > /sys/proc/vm/drop_caches")
    else:
        if "delete" in cmd:
            op= sp.getoutput("sudo "+ cmd)
            print(op)
            sp.getoutput("sudo echo 3 > /sys/proc/vm/drop_caches")
        elif "get" in cmd:
            op= sp.getoutput("sudo "+ cmd)
            print(op)
            sp.getoutput("sudo echo 3 > /sys/proc/vm/drop_caches")
        else:
            if length<=5:
                op= sp.getoutput("sudo "+ cmd)
                print(op)
                sp.getoutput("sudo echo 3 > /sys/proc/vm/drop_caches")
            else:
                print("""You have to delete pods first in order to launch more or do something more!!
	    Note: Pods must be less than equal to 5 to do further things""")
else:
    print("enter kubernetes command only")




#Do not launch deployment with more than 5 replicas otherwise backend might not give you desired output
#After testing our site do delete all the setup by clicking on delete all button

