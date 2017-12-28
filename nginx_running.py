#!/usr/bin/env python
# coding:utf-8
import commands

Nginx = commands.getoutput("ps -C nginx --no-heading|wc -l")
#print Nginx
Nginx_restart = commands.getoutput("/usr/local/nginx/sbin/nginx")

class NGINX:
   def __init__(self):
      if Nginx == "0":
         Nginx_restart
         print ("\033[31;1mnginx\033[0m is restart")
      else:
         print ("\033[31;1mnginx\033[0m is running")

if __name__ == "__main__":
     nginx = NGINX()
