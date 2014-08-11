# -*- coding: utf-8 -*-from flask import Blueprint, render_template,requestfrom flask_login import login_requiredfrom application import app,dbfrom models.log import Logfrom sqlalchemy import descfrom pypages import Paginatorimport oslog = Blueprint('log', __name__)@log.route("/",methods=['GET', 'POST'])@log.route("/page/<int:pnum>",methods=['GET', 'POST'])def index(pnum=1):    page=pnum    pageSize=10;    page=int(page)    loglist=Log.query.order_by(desc(Log.id)).paginate(page,pageSize,False)    pagecount=Log.query.count()    pages=Paginator(pagecount, per_page=pageSize, current=page, range_num=10)    return render_template("log/index.html",list=loglist,paginate=pages)def addlog(content,flag=1):    loginuser=os.getlogin()    logtarget=Log(loginuser,flag,content)    db.session.add(logtarget)    db.session.commit()