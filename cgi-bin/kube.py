#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()

f= cgi.FieldStorage()
cmd= f.getvalue("x")
g= sp.getoutput("sudo kubectl get pods")
length = len(g.split('\n'))
	
if "kubectl" in cmd:
		if "deployment" in cmd:
			if "--replicas" in cmd:
				l=int(cmd[-1])
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

