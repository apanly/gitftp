#!/usr/bin/python
#coding=utf-8
from ftplib import FTP
import os
from functions import debug_print,deal_error,printsep
from const import CONST_BUFFER_SIZE,CONST_ROOTPATH
class GITFTP:
    def __init__(self, hostaddr, username, password, port=21):
        self.hostaddr = hostaddr
        self.username = username
        self.password = password
        self.port     = port
        self.ftp      = FTP()
        self.file_list = []

    def login(self):
        ftp = self.ftp
        try:
            ftp.connect(self.hostaddr, self.port)
            ftp.login(self.username,self.password)
            debug_print(ftp.getwelcome())
        except Exception:
            deal_error("连接或登录失败")

    def upload_file(self,filepath):
        if not os.path.isfile(filepath):
            return
        f = open(filepath, "rb")
        file_name = os.path.split(filepath)[-1]
        const_path=os.path.dirname(CONST_ROOTPATH)
        ftppath=os.path.dirname(filepath)
        ftppath=ftppath.replace(const_path,"")
        try:
            self.ftp.cwd(ftppath)
            self.ftp.storbinary('STOR %s'%file_name, f, CONST_BUFFER_SIZE)
        except Exception:
            return False
        return True

    def upload_files(self,files):
        if files:
            for file in files:
                self.upload_file(file)
        pass

    def delete_files(self,files):
        pass

    def close(self):
        self.ftp.quit()
        self.ftp.close()