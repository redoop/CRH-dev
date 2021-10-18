from resource_management.libraries.functions.default import default
from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions.version import format_stack_version
import sys, os, glob, socket, commands
# server configurations

# user
config = Script.get_config()
fuse_user = "root"
fuse_group = "root"
#a,listen_address = commands.getstatusoutput("hostname -i | awk '{print $NF}'")

# log . pid
#fuse_logs_dir = '/var/log/fuse'
#fuse_logs = '/var/log/fuse/fuse.log'
#fuse_pid_dir = '/var/run/fuse'
#fuse_pid = '/var/run/fuse/fuse.pid'

# conf

fuse_config = config['configurations']['fuse-env']['content']


