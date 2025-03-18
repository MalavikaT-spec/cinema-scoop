from flask import *
from database import *
import uuid

normal=Blueprint('normal_members',__name__)

@normal.route('/normal_members')
def nor():
    return render_template("normal_members.html")

@normal.route('/view_notifi')
def view():
    data={}
    qry1 = "select * from notification"
    res=select(qry1)
    if res:
        data['view']=res 
    return render_template("view_notifi.html",data=data)

@normal.route('/view_entertainment')
def view_ent():
    data={}
    qry1 = "select * from entertainmententities"
    res=select(qry1)
    if res:
        data['view']=res 
    return render_template("view_entertainment.html",data=data)


@normal.route('/complaint',methods=['post','get'])
def add_comp():
    if 'submit' in request.form:
       description=request.form['description']
       qry2="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['nm'],description)
       insert(qry2)
       return "<script>alert('inserted');window.location='/complaint'</script>"
    
    data={}
    qry1 = "select * from complaint where sender_id=%s"%(session['nm'])
    res=select(qry1)
    if res:
        data['view']=res 

    return render_template("complaint.html",data=data)

@normal.route('/portfolio',methods=['post','get'])
def portfolio():
    if 'submit' in request.form:
        title=request.form['title']
        image_video=request.files['image_video'] 

        path = 'static/portfolio/'+str(uuid.uuid4())+image_video.filename
        image_video.save(path)
        achievements =request.form['achievements']
        qry2="insert into portfolio values(null,'%s','%s','%s','%s',curdate())"%(session['nm'],title,path,achievements)
        insert(qry2)
        return "<script>alert('inserted');window.location='/portfolio'</script>"
    
    data={}
    qry3 = "select * from portfolio"
    res=select(qry3)
    if res:
        data['view']=res

    
    # data={}
    if 'action' in request.args:
        act=request.args['action']
        id=request.args['id']
    
    else:
        act=None
    if act=='update':
        s="select * from portfolio where portfolio_id='%s'"%(id)
        data['up']=select(s)

    if 'upd' in request.form:
        title= request.form['title']
        image_video=request.files['image_video'] 

        path = 'static/feature_files/'+str(uuid.uuid4())+image_video.filename
        image_video.save(path)
        achivement=request.form['achievements']    
        qry4 = "update portfolio set title='%s', image_video='%s', achivements='%s' where portfolio_id='%s'"%(title,path,achivement,id)
        update(qry4) 
        return "<script>alert('updated');window.location='/portfolio'</script>"
    return render_template("portfolio.html",data=data)


@normal.route('/view_audition',methods=['post','get'])
def audition():
    data={}
    qry3 = "select * from audition"
    res=select(qry3)
    if res:
        data['view']=res
    return render_template("view_audition.html",data=data) 

@normal.route('/view_feature_members',methods=['post','get'])
def view_feature_members():
   data={}
   qry3 = "select * from feature_member"
   res=select(qry3)
   if res:
        data['view']=res
   return render_template("view_feature_member.html",data=data) 
@normal.route('/add_review',methods=['post','get'])
def review():
    fmid=request.args['id']
    if 'submit' in request.form:
       review=request.form['review']
       rating=request.form['rating']
       qry2="insert into review values(null,'%s','%s','%s','%s',curdate())"%(fmid,session['nm'],review,rating)
       insert(qry2)
       return "<script>alert('inserted');window.location='/view_feature_members'</script>"
    return render_template("add_review.html")


@normal.route('/view_vacancy',methods=['post','get'])
def vac():
    data={}
    qry3 = "select * from vacancy"
    res=select(qry3)
    if res:
        data['view']=res
    return render_template("view_vacancy.html",data=data)


@normal.route('/application',methods=['post','get'])
def application():
    
    vcid=request.args['id']
    if 'submit' in request.form:
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        resume=request.files['resume']

        path = 'static/appli_imgs'+str(uuid.uuid4())+resume.filename
        resume.save(path)

        portfolio_link=request.form['portfolio_link']
        qry2="insert into applications values(null,'%s','%s','%s','%s','%s','%s','%s',curdate(),'pending')"%(vcid,session['nm'],name,email,phone,path,portfolio_link)
        insert(qry2)
        return "<script>alert('inserted');window.location='/view_vacancy'</script>"
    return render_template("application.html")