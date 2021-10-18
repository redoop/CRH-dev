import sys
import os
from resource_management import *

class FuseClient(Script):
	def install(self, env):
		import params
		env.set_params(params)
		self.install_packages(env)
		self.configure(env)
		Execute('yum install fuse -y')
		print "install fuse for client"
		self.configure(env)

	def fuse_mount(self, env):
		import params
		env.set_params(params)
		pass

	def configure(self, env):
		import params
		env.set_params(params)
		pass
		#fuse_content=InlineTemplate(params.fuse_config)
		#File(format("/etc/fuse.conf"), content=fuse_content, owner=params.fuse_user, group=params.fuse_group)

if __name__ == "__main__":
	FuseClient().execute()

