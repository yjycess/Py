#!/usr/bin/python
#coding:utf-8

import pexpect
import datetime
from threading import Thread

host=[]
for i in range(1,255):
   ip_list = '10.1.1.%s' %i
   host.append(ip_list)

report_ok=[]
report_error=[]
class PING(Thread):
  def __init__(self,ip):
    Thread.__init__(self)
    self.ip=ip
  def run(self):
    Curtime = datetime.datetime.now()  
    ping=pexpect.spawn("ping -c1 %s" % (self.ip))
    check=ping.expect([pexpect.TIMEOUT,"1 packets transmitted, 1 received, 0% packet loss"],2)
    if check == 0:
      print("%s out" %self.ip)
    elif check == 1:
      print ("%s OK" %self.ip)
    else:
      print("$s host is not" %self.ip)

T_thread=[]
for i in host:
  t=PING(i)
  T_thread.append(t)
for n in range(len(T_thread)):
  T_thread[n].start()

