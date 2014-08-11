# -*- coding: utf-8 -*-
# author:郭威
# email: apanly@163.com
# QQ:364054110

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text, TIMESTAMP
from sqlalchemy.dialects.mysql import SMALLINT
from application import db
import datetime

class Log(db.Model):
    __tablename__ = "log"

    id      = Column(Integer, primary_key=True)
    loginuser = Column(String(20),nullable=False,index=True)
    flag    = Column(SMALLINT,nullable=False,index=True) #1 profile 2 projects
    content = Column(Text,nullable=False)
    created = Column(TIMESTAMP, nullable=False,server_default='0000-00-00 00:00:00')
    updated = Column(TIMESTAMP, nullable=False,server_default='0000-00-00 00:00:00')

    def __init__(self,loginuser,flag,content):
        self.loginuser=loginuser
        self.flag=flag
        self.content=content
        self.created=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated=self.created