from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/admin')
def adm():
    return render_template("admin.html")

@admin.route('/view_complaints', methods=['POST','GET'])
def view_complaints():
    data={}
    qry="select * from complaint"
    res=select(qry)
    if res:
        data['view']=res

    if 'submit' in request.form:
        reply= request.form['reply']
        id=request.form['id']  
        qry2=  "update complaint set reply='%s' where complaint_id ='%s'"%(reply,id) 
        update(qry2)

        return "<script>alert('success');window.location='/view_complaints'</script>"

    return render_template("view_complaints.html",data=data)
@admin.route('/notification', methods=['POST','GET'])
def notification():
    if 'submit' in request.form:
        title= request.form['title']
        description=request.form['description']
        date_time=request.form['date_time']  
        
        qry1="insert into notification values(null,'%s','%s','%s')"%(title,description,date_time)
        insert(qry1)

        return "<script>alert('inserted');window.location='/admin'</script>"
    return render_template("notification.html")
@admin.route('/review', methods=['POST','GET'])
def review():
    data={}
    qry1 = "select * from review"
    res=select(qry1)
    if res:
        data['view']=res 
    return render_template("review.html",data=data)


@admin.route('/entertainment', methods=['POST','GET'])
def entertainment():
    if 'submit' in request.form:
        entity_type= request.form['entity_type']
        name=request.form['name']
        location=request.form['location']  
        phone=request.form['phone'] 
        email=request.form['email']
        website_link=request.form['website_link']  
        description=request.form['description']
        established_date=request.form['established_date']
        
        qry1="insert into entertainmententities values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(entity_type,name,location,phone,email,website_link,description,established_date)
        insert(qry1)
        return "<script>alert('inserted');window.location='/admin'</script>"
    data={}
    qry3 = "select * from entertainmententities"
    res=select(qry3)
    if res:
        data['view']=res

    return render_template("entertainment.html",data=data)

@admin.route('/view_rating', methods=['POST','GET'])
def view_rating():
    data={}
    qry3 = "select * from review"
    res=select(qry3)
    if res:
        data['view']=res

    return render_template("view_rating.html",data=data)