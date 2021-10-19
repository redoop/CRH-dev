from resource_management import *
import sys
import os

class Master(Script):
  def install(self, env):
    import params
    env.set_params(params)
    self.install_packages(env)
    Execute('yum install -y httpd')
    print('service httpd installed')
    self.configure(env)

  def stop(self, env):
    import params
    env.set_params(params)
    Execute('systemctl stop httpd')
    print 'service httpd stoped'

  def start(self, env):
    import params
    env.set_params(params)
    Execute('systemctl start httpd')
    print 'service httpd started'

  def status(self, env):
    import params
    env.set_params(params)
    Execute('systemctl status httpd')
    print 'service httpd status'

  def configure(self, env):
    import params
    env.set_params(params)
    http_content=InlineTemplate(params.httpd_conf)
    #File(format("/etc/httpd/conf/httpd.conf"), content=http_content, owner=params.http_user, group=params.http_group)

if __name__ == "__main__":
   Master().execute()
