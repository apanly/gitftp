#!/usr/bin/python
#coding=utf-8
import subprocess,os
from const import CONST_ROOTPATH

class Git:
    def __init__(self,path):
        self.path=path

    def gitstatus(self):
        path=self.path
        cmd="cd %s;git add .;git status"%path
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        files={'modify':[],'add':[],'delete':[]}
        for line in p.stdout.readlines():
            if "modified:" in line:
                line=line.replace("#\tmodified:","")
                line=line.replace("\n","")
                line=line.strip()
                line="%s%s"%(CONST_ROOTPATH,line)
                files['modify'].append(line)
            if "new file:" in line:
                line=line.replace("#\tnew file:","")
                line=line.replace("\n","")
                line=line.strip()
                line="%s%s"%(CONST_ROOTPATH,line)
                files['add'].append(line)
            if "deleted:" in line:
                line=line.replace("#\tdeleted:","")
                line=line.replace("\n","")
                line=line.strip()
                line="%s%s"%(CONST_ROOTPATH,line)
                files['delete'].append(line)
        #retval = p.wait()
        return files

    def gitsubmit(self):
        path=self.path
        cmd="cd %s;git add .;git commit -am 'auto commit by gitftp';git fetch;git rebase origin/master;git push origin master:master"%path
        os.system(cmd)
