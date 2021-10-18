import os
import subprocess

jenkins_workspace_dir = "/var/lib/jenkins/workspace/CRH-Dev/"
output_dir = jenkins_workspace_dir+'output/'

def env_check():
        if not os.path.isdir(jenkins_workspace_dir):
                print("jenkins workspace error!")
                return -1
        #if subprocess.call(["yum", "install", "-y", "tar"], shell=False) is not 0:
        #        print("tar installed failed!")
        #        return -1
        if not os.path.exists(output_dir): os.makedirs(output_dir)
        return 0

def get_workspace():
        if env_check() == -1: return -1
        res = []
        for p in os.listdir(jenkins_workspace_dir):
                if p == ".git" or p == "JENKINS" or p == "output": continue
                # if p == "stacks": stacks.append(s) for s in os.listdir(jenkins_workspace_dir+"stacks/")
                if p == "STACK": continue
                if os.path.isdir(jenkins_workspace_dir+p): res.append(p)
        for i in res:
                if not os.path.exists(output_dir+i): os.makedirs(output_dir+i)
        return res

os.chdir(jenkins_workspace_dir)
res = get_workspace()

for i in res:
        service_dir = output_dir+i+'/'
        subprocess.call(["cp", jenkins_workspace_dir+"JENKINS/install.sh", jenkins_workspace_dir+"JENKINS/Readme.md", service_dir])
        subprocess.call(['tar', '-zcvf', service_dir+i+'.tar.gz' ,i], shell=False)
subprocess.call(['tar', '-zcvf', output_dir+'stack'+'.tar.gz' , 'STACK'], shell=False)

