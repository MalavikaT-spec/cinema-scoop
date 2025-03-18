from flask import *
from database import *
import uuid

feature=Blueprint('feature_members',__name__)

@feature.route('/feature_members')
def fea():
    return render_template("feature_members.html")

@feature.route('/view_notification')
def view():
    data={}
    qry1 = "select * from notification"
    res=select(qry1)
    if res:
        data['view']=res 
    return render_template("view_notification.html",data=data)

@feature.route('/view_entertain')
def view_ent():
    data={}
    qry1 = "select * from entertainmententities"
    res=select(qry1)
    if res:
        data['view']=res 
    return render_template("view_entertain.html",data=data)

@feature.route('/audition',methods=['GET','POST'])
def audition():
    if 'submit' in request.form:
       title=request.form['title']
       description=request.form['description']
       audition_date=request.form['audition_date']
       location=request.form['location']
       time_to_reach=request.form['time_to_reach']
       requirements=request.form['requirements']
       deadline=request.form['deadline']
       contact_number=request.form['contact_number']
       qry2="insert into audition values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(session['fm'],title,description,audition_date,location,time_to_reach,requirements,deadline,contact_number)
       insert(qry2)
       return "<script>alert('inserted');window.location='/feature_members'</script>"
    return render_template("audition.html")

@feature.route('/complaints',methods=['post','get'])
def add_comp():
    if 'submit' in request.form:
       description=request.form['description']
       qry2="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['fm'],description)
       insert(qry2)
       return "<script>alert('inserted');window.location='/complaints'</script>"
    
    data={}
    qry1 = "select * from complaint where sender_id=%s"%(session['fm'])
    res=select(qry1)
    if res:
        data['view']=res 

    return render_template("complaints.html",data=data)


@feature.route('/vacancy',methods=['post','get'])
def add_vac():
    if 'submit' in request.form:
        title=request.form['title']
        description=request.form['description']
        category=request.form['category']
        required_skills=request.form['required_skills']
        location=request.form['location']
        employment_type=request.form['employment_type']
        experience_req=request.form['experience_req']
        deadline=request.form['deadline']
        contact_mail=request.form['contact_mail']
        contact_num=request.form['contact_num']
        slots=request.form['slots']
        qry2="insert into vacancy values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(session['fm'],title,description,category,required_skills,location,employment_type,experience_req,deadline,contact_mail,contact_num,slots)
        insert(qry2)
        return "<script>alert('inserted');window.location='/feature_members'</script>"
    
    data={}
    qry1 = "select * from vacancy"
    res=select(qry1)
    if res:
        data['view']=res 

    return render_template("vacancy.html",data=data)

@feature.route('/view_application',methods=['post','get'])
def view_application():
    data={}
    qry1 = "select * from applications"
    res=select(qry1)
    if res:
        data['view']=res 
    return render_template("view_application.html",data=data)

@feature.route('/manage_feature_members',methods=['post','get'])
def manage():  
    data={}
    if 'action' in request.args:
        act=request.args['action']
        id=request.args['id']  
    else:
        act=None
        

    if act=='update':
        s="select * from feature_member where fm_id='%s'"%(id)
        data['up']=select(s)

    if 'upd' in request.form:
        fname= request.form['fname']
        phone=request.form['phone']
        prefession=request.form['prefession']  
        fle=request.files['Image'] 

        path = 'static/feature_files/'+str(uuid.uuid4())+fle.filename
        fle.save(path)

        biography_description=request.form['biography_description']  
        email=request.form['email']
        qry4 = "update feature_member set fname='%s', phone='%s', prefession='%s', file='%s',  biography_description='%s',email='%s'  where fm_id ='%s'"%(fname,phone,prefession,path,biography_description,email,id)
        update(qry4) 
        return "<script>alert('updated');window.location='/manage_feature_members'</script>"
        
    qry3 = "select * from feature_member"
    res=select(qry3)
    if res:
        data['view']=res
    return render_template("manage_feature_members.html",data=data)  
        
    