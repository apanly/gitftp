# -*- coding: utf-8 -*-

from ftp import GITFTP
from git import Git
from const import CONST_HOSTADDR,CONST_PASSWORD,CONST_USERNAME,CONST_PORT,CONST_ROOTPATH

if __name__ == '__main__':
    git=Git(CONST_ROOTPATH)
    files=git.gitstatus()
    gitftp=GITFTP(CONST_HOSTADDR,CONST_USERNAME,CONST_PASSWORD,CONST_PORT)
    gitftp.login()
    #add files
    addfiles=files['add']
    if addfiles:
        gitftp.upload_files(addfiles)
    modifyfiles=files['modify']
    if modifyfiles:
        gitftp.upload_files(modifyfiles)
    deletefiles=files['delete']
    if deletefiles:
        gitftp.delete_files(deletefiles)
    gitftp.close()
    git.gitsubmit()