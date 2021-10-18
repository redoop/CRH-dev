import os
import subprocess
import glob

service = glob.glob("*.tar.gz")[0]
ambari_path = "/var/lib/ambari-server/resources/stacks/CRH/"
latest_version = "8.3.1.1"
if os.path.isdir(ambari_path):
	res = []
	for p in os.listdir(ambari_path):
		if os.path.isdir(ambari_path+p): res.append(p)
	latest_version = max(res)
	if subprocess.call(["tar", "-zxvf", "./"+service, "-C", ambari_path+latest_version+"/services/"]) is 0:
		print(service + " service installed successfully!")
		print("please run 'systemctl restart ambari-server' then install the service to cluster through ambari-web page:8080")
	else:
		print(service + " service installed failed")
else:
	print("ambari servier is not installed")



