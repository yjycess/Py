#!/usr/bin/env python
# coding:utf-8

import pexpect

host = []
for i in range(80,100):
   ip_list = '10.1.1.%s' %i
   host.append(ip_list)
#print (" IP如下：%s" %host)

class Ping():
   def __init__(self):
      for i in host:
         #print (i)
         p = pexpect.spawn("ping -c1 %s" %i)
         #print (p)
         #check=p.expect([pexpect.TIMEOUT,"1 packets transmitted, 1 received, 0% packet loss"],2)
         check=p.expect_exact([pexpect.TIMEOUT,"1 packets transmitted, 1 received, 0% packet loss"],2)
         if check == 0 :
             print ("%s ping不通" %i)
         else:
             #print ("%s ping的通" %i)
             continue

ping=Ping()
