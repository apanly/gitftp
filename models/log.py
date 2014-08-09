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
    uid     = Column(Integer,nullable=False,index=True)
    flag    = Column(SMALLINT,nullable=False,index=True)
    content = Column(Text,nullable=False)
    created = Column(TIMESTAMP, nullable=False,server_default='0000-00-00 00:00:00')
    updated = Column(TIMESTAMP, nullable=False,server_default='0000-00-00 00:00:00')

    def __init__(self,uid,flag,content):
        self.uid=uid
        self.flag=flag
        self.content=content
        self.created=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated=self.created