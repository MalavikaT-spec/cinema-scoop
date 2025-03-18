from flask import *
from database import *
import uuid
pub=Blueprint('public',__name__)

@pub.route('/')
def home():
    return render_template("home.html")
@pub.route('/login',methods=['post','get'])
def login():

    if 'login' in request.form:
        u=request.form['uname']
        p=request.form['psw']

        qry1="select * from login where Username='%s' and Password='%s'"%(u,p)
        res1=select(qry1)
        if res1:
            session['log']=res1[0]['Login_id']
            if res1[0]['usertype']=='admin':
                return redirect(url_for('admin.adm'))
            

            if res1[0]['usertype']=='normal_members':
                a="select * from normal_members where login_id='%s'"%(session['log'])
                b=select(a)
                if b:
                    session['nm']=b[0]['nm_id']
                    return redirect(url_for('normal_members.nor'))
            if res1[0]['usertype']=='feature_members':
                a="select * from feature_member where login_id='%s'"%(session['log'])
                b=select(a)
                if b:
                    session['fm']=b[0]['fm_id']
                    return redirect(url_for('feature_members.fea'))    
        print(res1,"+++++++++++++++++")
    return render_template("login.html")
@pub.route('/norm_regist',methods=['post','get'])
def norm_regist():
    if 'submit' in request.form:
        fname=request.form['fname']
        ph=request.form['phone']
        em=request.form['email']
        image=request.files['image']
        path = 'static/norm_imgs'+str(uuid.uuid4())+image.filename
        image.save(path)

        prf=request.form['professional_intrest']
        skill=request.form['skills']
        username=request.form['username']
        psw=request.form['psw']
        #print(fn,ph,em,path,prf,skill,username,psw)
        
        qry1="insert into login values(null,'%s','%s','normal_members')"%(username,psw)
        res=insert(qry1)


        qry2="insert into normal_members values(null,'%s','%s','%s','%s','%s','%s','%s')"%(fname,ph,em,path,prf,skill,res)
        insert(qry2)
        return "<script>alert('inserted');window.location='/login'</script>"
    return render_template("norm_regist.html")

@pub.route('/feat_regist',methods=['post','get'])
def feat_regist():
    if 'submit' in request.form:
        fname=request.form['fname']
        ph=request.form['phone']
        prf=request.form['prefession']
        fle=request.files['image'] 

        path = 'static/feature_files/'+str(uuid.uuid4())+fle.filename
        fle.save(path)
        bio=request.form['biography_description']
        portfolio=request.form['portfolio_link']
        email=request.form['email']
        username=request.form['username']
        psw=request.form['psw']
        #print(fname,ph,prf,path,bio,portfolio,email,username,psw)

        qry1="insert into login values(null,'%s','%s','feature_members')"%(username,psw)
        res=insert(qry1)




        qry2="insert into feature_member values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(fname,ph,prf,path,bio,portfolio,email,res)
        insert(qry2)
        return "<script>alert('inserted');window.location='/login'</script>"
    return render_template("feat_regist.html")
@pub.route('/payment',methods=['post','get'])
def payment():
    if 'submit'in request.form:
        card=request.form['cardNumber']
        exp=request.form['expiryDate']
        cvv=request.form['cvv']
        name=request.form['cardHolderName']
        add=request.form['billingAddress']

        return "<script>alert('payment sucessfull..');window.location='/feat_regist'</script>"
    
    if 'upi_btn' in request.form:
        return "<script>alert('payment sucessfull..');window.location='/feat_regist'</script>"
    return render_template("payment.html")





@pub.route('/forgotpassword',methods=['post','get'])
def forgotpassword():
    if 'submit' in request.form:
        email=request.form['email']

        qry="select * from normal_members where email='%s'"%(email)
        res=select(qry)

        if res:
            login_id=res[0]['login_id']
            return redirect(url_for('public.normal_members_new_pass',login_id=login_id))
        else:
            return "<script>alert('Invalid email...');window.location='/login'</script>"


    return render_template("forgotpassword.html")
@pub.route('/normal_members_new_pass',methods=['get','post'])
def normal_members_new_pass():
    login_id = request.args.get('login_id')
    if 'submit' in request.form:
        newpsw=request.form['new-password']
        confirmpsw=request.form['confirm_password']

        if newpsw==confirmpsw:

            z="update login set password='%s' where login_id='%s'"%(newpsw,login_id)
            update(z)
            return """<script>alert("Password Updated");window.location="/login"</script>"""

        else:
            return """<script>alert("New and Confirm password didnt match");window.location="/login"</script>"""


    return render_template("normal_memebrs_new_pass.html")