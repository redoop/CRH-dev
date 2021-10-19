from resource_management.libraries.functions.default import default
from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions.version import format_stack_version
import sys, os, glob, socket, commands
# server configurations

# user
config = Script.get_config()
http_user = "root"
http_group = "root"
#a,listen_address = commands.getstatusoutput("hostname -i | awk '{print $NF}'")

# log . pid
httpd_logs_dir = '/var/log/httpd'
httpd_logs = '/var/log/httpd/httpd.log'
httpd_pid_dir = '/var/run/httpd'
httpd_pid = '/var/run/httpd/httpd.pid'

# conf
httpd_config = config['configurations']['httpd']['conf']
