from flask import *
from DBConnection import *

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/login_post',methods=['post'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="select * from login WHERE username='"+username+"' and password='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        if res['type']=='admin':
            return redirect('/ad_home')
        else :
            return '''<script>alert("Password Doesn't Match");window.location='/'</script>'''
    else:
        return '''<script>alert("Password Doesn't Match");window.location='/'</script>'''


@app.route('/Login')
def Login():
    return render_template('Login.html')

@app.route('/ad_home')
def ad_home():
    return render_template('index.html')

@app.route('/Admin_home')
def Admin_home():
    return render_template('index.html')


@app.route('/hod_manage')
def hod_manage():
    db=Db()
    qry="select teachers.name,hod.*,dept.dept_name from hod join teachers on teachers.Teach_lid=hod.teach_lid join dept on dept.dept_id=hod.dept_id"
    res=db.select(qry)
    return render_template('hod_manage.html',data=res)


@app.route('/teacher_manage')
def teacher_manage():
    db=Db()
    qry="select dept.dept_name,teachers.* from teachers join dept on dept.dept_id=teachers.dept_id"
    res=db.select(qry)
    return render_template('view_teacher.html', data=res)
@app.route('/add_teacher')
def add_teacher():
    db = Db()
    qry = "select * from dept"
    res = db.select(qry)
    return render_template('Add_Teacher.html',data=res)

@app.route('/add_teacher_post',methods=['post'])
def add_teacher_post():
    db=Db()
    nme=request.form['textfield']
    dep=request.form['textfield2']
    dob=request.form['textfield3']
    qlf=request.form['textfield4']
    hm=request.form['textfield5']
    plc=request.form['textfield6']
    pst=request.form['textfield7']
    pin=request.form['textfield8']
    cty=request.form['textfield9']
    dst=request.form['textfield10']
    ste=request.form['textfield11']
    phn=request.form['textfield12']
    mail=request.form['textfield13']
    from datetime import datetime
    pht=request.files['fileField']
    date=datetime.now().strftime("%Y%m%d-%H%M%S")
    pht.save("C:\\Users\\Shabeeb\\Desktop\\SPAS\\static\\teacher_image\\"+date+".jpg")
    path="/static/teacher_image/"+date+".jpg"
    qry="insert into login (username,`password`,`type`)values ('"+mail+"','"+phn+"','teacher')"
    res=db.insert(qry)
    qry1="insert into teachers(Teach_lid,`name`,dept_id,dob,qualification,h_name,place,city,state,pin,ph_no,photo,email,post,District)values('"+str(res)+"','"+nme+"','"+dep+"','"+dob+"','"+qlf+"','"+hm+"','"+plc+"','"+cty+"','"+ste+"','"+pin+"','"+phn+"','"+path+"','"+mail+"','"+pst+"','"+dst+"')"
    print(qry1)
    res1=db.insert(qry1)
    return '''<script>alert("Added Teacher");window.location="/teacher_manage"</script>'''

@app.route('/delete_teacher/<id>')
def delete_teacher(id):
    db=Db()
    qry="delete from teachers where Teach_lid='"+id+"'"
    res = db.delete(qry)
    return '''<script>alert("Deleted");window.location="/teacher_manage"</script>'''

@app.route('/edit_teacher/<id>')
def edit_teacher(id):
    db=Db()
    qry="update from teachers where Teach_lid="
    res=db.update(qry)
    return '''<script>alert("Updated");window.location="/teacher_manage"</script>'''



@app.route('/manage_student')
def manage_student():
    db=Db()
    qry="select * from students WHERE `status`='pending'"
    res=db.select(qry)
    return render_template('student.html',data=res)
    # from datetime import datetime
    # pht=request.files['fileField']
    # date=datetime.now().strftime("%Y%m%d-%H%M%S")
    # pht.save("C:\\Users\\Shabeeb\\Desktop\\SPAS\\static\\student_imaqe\\"+date+".jpg")
    # path="/static/student_image/"+date+".jpg"
    # qry="insert into login (username,`password`,`type`)values ('"+mail+"','"+phn+"','student')"
    # res=db.insert(qry)

@app.route('/student_approve/<id>/<lid>')
def student_approve(id,lid):
    db=Db()
    qry="UPDATE `students` SET `status`='approved' WHERE `Std_id`='"+id+"'"
    res=db.update(qry)
    qry1="UPDATE `login` SET `type`='student' WHERE`Log_id`='"+lid+"'"
    res=db.update(qry1)
    return '''<script>alert("Approved");window.location="/manage_student"</script>'''


@app.route('/student_reject/<id>')
def student_reject(id):
    db=Db()
    qry="UPDATE `students` SET `status`='reject' WHERE `Std_id`='"+id+"'"
    res=db.update(qry)
    return '''<script>alert("Rejected");window.location="/manage_student"</script>'''


@app.route('/view_approved_students')
def view_approved_students():
    db=Db()
    qry="select * from students WHERE `status`='Approved'"
    res=db.select(qry)
    return render_template("view approved students.html",data=res)

@app.route('/student_block/<id>')
def student_block(id):
    db = Db()
    qry = "UPDATE `students` SET `status`='block' WHERE `Std_id`='" + id + "'"
    res = db.update(qry)
    return redirect("/view_approved_students")

@app.route('/add_department')
def add_department():
    return render_template('Department.html')

@app.route('/add_department_post',methods=['post'])
def add_department_post():
    db=Db()
    dep=request.form['textfield2']
    qry = "insert into dept(dept_name)values('"+dep+"')"
    res = db.insert(qry)
    return '''<script>alert("Added Department");window.location="/view_dept"</script>'''


@app.route('/delete_department/<id>')
def delete_department(id):
        db = Db()
        qry = "delete from dept where dept_name='" + id + "'"
        res = db.delete(qry)
        return '''<script>alert("Deleted");window.location="/view_dept"</script>'''


@app.route('/view_dept')
def view_dept():
    db=Db()
    qry="select * from dept"
    res=db.select(qry)
    return render_template('View_Dept.html',data=res)

@app.route('/add_course')
def add_course():
    db=Db()
    qry="select * from dept"
    res=db.select(qry)
    return render_template('course.html',data=res)

@app.route('/add_course_post', methods=['POST'])
def add_course_post():
    dep=request.form['dept']
    crs=request.form['textfield2']
    sem=request.form['textfield3']
    qry="insert into course (course_name,sem_duration,dept_id)values('"+crs+"','"+sem+"','"+dep+"')"
    db=Db()
    res=db.insert(qry)
    return '''<script>alert("Added Course");window.location="/viewcourse"</script>'''

@app.route('/delete_course/<id>')
def delete_course(id):
    db = Db()
    qry = "delete from course where course_name='" + id + "'"
    res = db.delete(qry)
    return '''<script>alert("Deleted");window.location="/viewcourse"</script>'''



@app.route('/viewcourse')
def viewcourse():
    db=Db()
    qry="select dept.dept_name,course. * from course join dept on dept.dept_id=course.dept_id"
    res=db.select(qry)
    return render_template('View_course.html',data=res)



@app.route('/add_subject')
def add_subject():
    db=Db()
    qry="select * from course"
    res=db.select(qry)
    return render_template("subject.html",data=res)



@app.route('/add_subject_post',methods=['post'])
def add_subject_post():
    db = Db()
    sub=request.form['textfield2']
    cnm=request.form['crs']
    sem=request.form['textfield4']
    qry1="insert into sub(sub_name,course_id,sem) values ('"+sub+"','"+cnm+"','"+sem+"')"
    res=db.insert(qry1)
    return '''<script>alert("Added Subject");window.location="/view_subject"</script>'''

@app.route('/delete_subject/<id>')
def delete_subject(id):
    db = Db()
    qry = "delete from sub where sub_name='" + id + "'"
    res = db.delete(qry)
    return '''<script>alert("Deleted");window.location="/view_subject"</script>'''



@app.route('/view_subject')
def view_subject():
    db=Db()
    qry="select course.course_name,sub.* from sub join course on course.course_id=sub.course_id"
    res=db.select(qry)
    return render_template('View_Subject.html',data=res)


@app.route('/add_tt')
def add_tt():
    db=Db()
    qry="SELECT * from dept"
    res=db.select(qry)

    qry1 = "SELECT * from course"
    res1 = db.select(qry1)
    qry2 = "SELECT * from sub"
    res2 = db.select(qry2)

    return render_template('Add_TimeTable.html',data=res,data1=res1,data2=res2)

@app.route('/add_tt_post',methods=['post'])
def add_tt_post():
    db=Db()
    day=request.form['Day']
    sub=request.form['subject']
    per=request.form['periods']
    qry1="INSERT INTO time_table (`periods`,`sub_id`,`days`) VALUES ('"+per+"','"+sub+"','"+day+"')"
    res=db.insert(qry1)
    return "OK"
@app.route('/view_timetable')
def view_timetable():
    db=Db()
    qry="select * from dept"
    res = db.select(qry)
    qry1 = "select * from course"
    res1= db.select(qry1)
    return render_template('View_timetable.html', data11=res,data1=res1,data=[], len=0)

@app.route('/view_timetable_post',methods=['post'])
def view_timetable_post():
    db = Db()
    crs= request.form['course']
    sem= request.form['sem']


    day=["Monday","Tuesday","Wednesday","Thursday","Friday"]

    tmt=[]
    per=["1","2","3","4","5"]

    for i in day:
        m=[]
        for j in per:

            qry="SELECT * FROM `sub` INNER JOIN `time_table` ON `sub`.`sub_id`=`time_table`.`sub_id` WHERE `sub`.`course_id`='"+crs+"' AND `sub`.`sem`='"+sem+"' AND `time_table`.`periods`='"+j+"' AND `time_table`.`days`='"+i+"'"
            res=db.selectOne(qry)

            if res is not None:
                m.append(res['sub_name'])
            else:
                m.append("free")
        tmt.append(m)
    return render_template("View_timetable.html",data=tmt, len=1)


@app.route('/std_attendence')
def std_attendence():
    db=Db()
    qry="select students.name,std_attendence.* from std_attendence join students on students.std_id=std_attendence.std_id"
    res=db.select(qry)
    return render_template('Std_attendence.html',data=res)


@app.route('/staff_attendence')
def staff_attendence():
    db=Db()
    qry="select teachers.name,staff_att.* from staff_att join teachers on teachers.teach_id=staff_att.teach_id"
    res=db.select(qry)
    return render_template('Staff_attendence.html',data=res)

@app.route('/View_Internals')
def View_Internals():
    db=Db()
    qry="select students.name,sub.sub_name,internal_mark.* from internal_mark join students on students.std_id=internal_mark.std_id join sub on sub.sub_id=internal_mark.sub_id"
    res=db.select(qry)
    return render_template('Internal_mark.html',data=res)

@app.route('/feedback')
def feedback():
    db=Db()
    qry="select students.name,sub.sub_name,feedback.* From feedback join students on students.std_id=feedback.std_id join sub on sub.sub_id=feedback.std_id"
    res=db.select(qry)
    return render_template('Feedback.html',data=res)

@app.route('/add_notification')
def add_notification():
    return render_template('Notification1.html')

@app.route('/add_notification_post',methods=['post'])
def add_notification_post():
    noti=request.form['textarea']
    db=Db()
    qry="insert into notification (notif_date,notification) values (CURDATE(),'"+noti+"')"
    res=db.insert(qry)
    return '''<script>alert("1 NOTIFICATION IS SENDED");window.location="/view_notification"</script>'''

@app.route('/delete_notification/<id>')
def delete_notification(id):
    db = Db()
    qry = "delete from notification where notification='" + id + "'"
    res = db.delete(qry)
    return '''<script>alert("Deleted");window.location="/view_notification"</script>'''


@app.route('/view_notification')
def view_notification():
    db = Db()
    qry = "select * from notification"
    res = db.select(qry)
    return render_template('View_Notification.html', data=res)

############################################################################

@app.route('/and_login_post',methods=['post'])
def and_login_Post():
    username=request.form['username']
    password=request.form['password']
    db = Db()
    qry = "select * from login WHERE username='" + username + "' and password='" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        if res['type'] == 'hod':
            return jsonify(status='ok',type='hod',lid=res["Log_id"])
        elif res['type']=='teacher':
            return jsonify(status='ok',type='teacher',lid=res["Log_id"])
        elif res['type'] == 'student':
            return jsonify(status='ok',
                           type='student',lid=res["Log_id"])
        elif res['type'] == 'parent':
            return jsonify(status='ok',type='parent',lid=res["Log_id"])
    else:
        return jsonify(status='No')

@app.route('/hod_add_tt')
def hod_add_tt():
        db = Db()
        qry1 = "SELECT * from course"
        res1 = db.select(qry1)
        qry2 = "SELECT * from sub"
        res2 = db.select(qry2)
        return jsonify(status='ok',data1=res1,data2=res2)

@app.route('/hod_Add_TT_Post',methods=['post'])
def hod_Add_TT_Post():
    # periods=request.form['periods']
    sub_id=request.form['sub_id']
    days=request.form['days']
    hour=request.form['hour']
    db = Db()
    qry = "INSERT INTO time_table (`sub_id`,`days`,`time_t_hrs`) VALUES ('" + sub_id + "','" + days + "','"+hour+"')"
    res = db.insert(qry)
    return jsonify(status='ok',data=res)

@app.route('/hod_view_timetable')
def hod_view_timetable():
    db=Db()
    qry="select * from dept"
    res = db.select(qry)
    qry1 = "select * from course"
    res1= db.select(qry1)
    return jsonify(status='ok', data11=res,data1=res1,data=[], len=0)

@app.route('/hod_view_timetable_post',methods=['post'])
def hod_view_timetable_post():
    db = Db()
    crs= request.form['course']
    sem= request.form['sem']


    day=["Monday","Tuesday","Wednesday","Thursday","Friday"]

    tmt=[]
    per=["1","2","3","4","5"]

    for i in day:
        m=[]
        for j in per:

            qry="SELECT * FROM `sub` INNER JOIN `time_table` ON `sub`.`sub_id`=`time_table`.`sub_id` WHERE `sub`.`course_id`='"+crs+"' AND `sub`.`sem`='"+sem+"' AND `time_table`.`periods`='"+j+"' AND `time_table`.`days`='"+i+"'"
            res=db.selectOne(qry)

            if res is not None:
                m.append(res['sub_name'])
            else:
                m.append("free")
        tmt.append(m)
    print(tmt)
    return jsonify(status='ok',data=tmt, len=1)

@app.route('/hod_edit_tt', methods=['POST'])
def edit_tt():
    days=request.form['day']
    hour=request.form['hour']
    sub_id=request.form['sub_id']
    time_t_id=request.form['time_t_id']
    db=Db()
    qry="UPDATE time_table SET sub_id='"+sub_id+"',days='"+days+"',`hour`='"+hour+"' WHERE time_t_id='"+time_t_id+"'"
    res=db.update(qry)
    return jsonify(status='ok',data=res)

@app.route('/hod_allocateSub_tcr_get', methods=['POST'])
def hod_allocateSub_tcr_get():
    teach_id = request.form['teach_id']
    sub_id = request.form['sub_id']
    db=Db()
    qry1="select * from teachers"
    res1=db.select(qry1)
    qry2="select * from sub"
    res2=db.select(qry2)
    return jsonify(status='ok',data1=res1,data2=res2)


@app.route('/hod_allocateSub_tcr_post', methods=['POST'])
def hod_allocateSub_tcr_post():
    teach_id=request.form['teach_id']
    sub_id=request.form['sub_id']
    db = Db()
    qry = "INSERT INTO sub_allocation (`teach_id`,`sub_id`) VALUES ('" + teach_id + "','" + sub_id + "')"
    res = db.insert(qry)
    print(res)
    return jsonify(status='ok',data=res)

@app.route('/hod_view_TeachAtt_post', methods=['POST'])
def hod_view_TeachAtt_post():
    dates=request.form['dates']
    teach_id=request.form['teach_id']
    dept_id=request.form['dept_id']
    db = Db()
    qry = "select teachers.name,staff_att.* from staff_att join teachers on teachers.teach_id=staff_att.teach_id  WHERE dept_id='"+dept_id+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)


@app.route('/hod_view_stdAtt_post', methods=['POST'])
def hod_view_stdAtt_post():
    date = request.form['date']
    std_id = request.form['std_id']
    dept_id = request.form['dept_id']
    db=Db()
    qry="SELECT students.name,std_attendence.* FROM std_attendence JOIN students ON students.std_id=std_attendence.std_id JOIN course ON course.course_id=students.course_id WHERE dept_id='"+dept_id+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)


@app.route('/ho_view_allocated_subject_new', methods=['POST'])
def ho_view_allocated_subject_new():
    Teach_lid=request.form['Teach_lid']
    db=Db()
    print(Teach_lid)
    qry = "SELECT `sub`.*,`teachers`.`name`,`hod`.`teach_lid` FROM `sub_allocation` JOIN `sub` ON `sub`.`sub_id` = `sub_allocation`.`sub_id` JOIN `teachers` ON `teachers`.`Teach_lid` =`sub_allocation`.`teach_id` JOIN `course` ON `course`.`course_id`=`sub`.`course_id` JOIN `hod` ON `hod`.`dept_id`=`course`.`dept_id` WHERE `hod`.`teach_lid`='"+Teach_lid+"'"
    res = db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)

@app.route('/hod_View_Internal_post', methods=['POST'])
def hod_View_Internal_post():
    std_id = request.form['std_id']
    sub_id = request.form['sub_id']
    dept_id = request.form['dept_id']
    db = Db()
    qry="SELECT students.name,sub.sub_name,internal_mark.* FROM internal_mark JOIN students ON students.std_id=internal_mark.std_id JOIN sub ON sub.sub_id=internal_mark.sub_id JOIN course ON course.course_id=students.course_id WHERE dept_id='"+dept_id+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)


@app.route('/hot_view_internal_post_new', methods=['POST'])
def hot_view_internal_post_new():
    Teach_lid=request.form["Teach_lid"]
    db = Db()
    qry = "SELECT * FROM `internal_mark` JOIN `students` ON `students`.`std_lid` = `internal_mark`.`std_id` JOIN`course` ON `students`.`course_id` = `course`.`course_id` JOIN `sub` ON `internal_mark`.`sub_id` =`sub`.`sub_id` JOIN`hod` ON `hod`.`dept_id`=`course`.`dept_id`  WHERE `hod`.`teach_lid`='"+Teach_lid+"'"
    res = db.select(qry)
    return jsonify(status="ok",data = res)


@app.route('/hod_View_feedback_post', methods=['POST'])
def hod_View_feedback_post():
    # sub_id = request.form['sub_id']
    dept_id = request.form['dept_id']
    db = Db()
    qry = "SELECT students.name,sub.sub_name,feedback.* FROM feedback JOIN students ON students.std_id=feedback.std_id JOIN sub ON sub.sub_id=feedback.std_id JOIN course ON course.course_id=students.course_id WHERE dept_id='"+dept_id+"'"
    res = db.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/hod_View_feedback_post_new', methods=['POST'])
def hod_View_feedback_post_new():
    sub_id = request.form['sub_id']
    # dept_id = request.form['dept_id']
    db = Db()
    qry = "SELECT `feedback`.*,`sub`.`sub_name`,`sub`.`sub_id`,`students`.`std_lid`,`students`.`Reg_no`,`students`.`name` FROM `feedback` JOIN `sub` ON `sub`.`sub_id` = `feedback`.`sub_id` JOIN `students` ON `students`.`std_lid` = `feedback`.`std_id` WHERE `feedback`.`sub_id`='"+sub_id+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/hod_view_course_post', methods=['POST'])
def hod_view_course_post():
    teach_lid=request.form['teach_lid']
    db=Db()
    qry="SELECT `course`.*,`hod`.`teach_lid`,`hod`.`dept_id` FROM course JOIN hod ON `course`.`dept_id`=`hod`.`dept_id`WHERE `teach_lid`='"+teach_lid+"'"
    res=db.select(qry)
    print(res)
    return jsonify(status='ok',data=res)


@app.route('/hod_View_Teacher_post', methods=['POST'])
def hod_View_Teacher_post():
    Teach_lid=request.form['Teach_lid']
    # dept_id = request.form['dept_id']
    db = Db()
    qry = "SELECT dept.dept_name,teachers.*  FROM `teachers` JOIN `dept` ON `dept`.`dept_id` = `teachers`.`dept_id` JOIN `hod` ON `hod`.`dept_id` =`teachers`.`dept_id` WHERE `hod`.`teach_lid`='"+Teach_lid+"'  AND `hod`.`teach_lid` != `teachers`.`Teach_lid`"
    res = db.select(qry)
    qry1 = "SELECT `sub`.* FROM `sub` JOIN `course` ON `course`.`course_id`=`sub`.`course_id`  JOIN `hod` ON `hod`.`dept_id`=`course`.`dept_id` WHERE `hod`.`teach_lid`='" + Teach_lid + "'"
    res1 = db.select(qry1)
    print(res1)
    return jsonify(status='ok',data=res, val=res1)

@app.route('/hod_viewSub_post', methods=['POST'])
def hod_viewSub_post():
    Teach_lid = request.form['Teach_lid']
    dept_id = request.form['dept_id']
    db = Db()
    qry="SELECT course.course_name,sub.* FROM sub JOIN course ON course.course_id=sub.course_id WHERE course.dept_id='"+dept_id+"'"
    res=db.select(qry)
    print(res)
    return jsonify(status='ok',data=res)


@app.route('/hod_viewSub_post_new', methods=['POST'])
def hod_viewSub_post_new():
    Teach_lid = request.form['Teach_lid']
    # dept_id = request.form['dept_id']
    db = Db()
    qry="SELECT `sub`.* FROM `sub` JOIN `course` ON `course`.`course_id`=`sub`.`course_id`  JOIN `hod` ON `hod`.`dept_id`=`course`.`dept_id` WHERE `hod`.`teach_lid`='"+Teach_lid+"'"
    res=db.select(qry)
    print(res)
    return jsonify(status='ok',data=res)

@app.route('/hod_view_subjects_new', methods=['POST'])
def hod_view_subjects_new():
    Teach_lid = request.form['Teach_lid']
    # dept_id = request.form['dept_id']
    db = Db()
    qry="SELECT course.course_name,sub.* FROM sub JOIN course ON course.course_id=sub.course_id  JOIN `hod` ON `course`.`dept_id`=`hod`.`dept_id`WHERE `hod`.`teach_lid`='"+Teach_lid+"'"
    res=db.select(qry)
    print(res)
    return jsonify(status='ok',data=res)

@app.route('/hod_view_teachProfile_post', methods=['POST'])
def hod_view_teachProfile_post():
    Teach_lid = request.form['Teach_lid']
    dept_id = request.form['dept_id']
    db = Db()
    qry ="select * from teachers WHERE Teach_lid='"+Teach_lid+"'"
    res=db.selectOne(qry)
    return jsonify(status='ok',data=res)

@app.route('/hod_sndNotification_post', methods=['POST'])
def hod_sndNotification_post():
    teach_lid = request.form['lid']
    # dept_id = request.form['dept_id']
    notif=request.form['notification']
    db = Db()
    qry="INSERT INTO `hod_notification`(`date`,`notification`,teach_lid) VALUES (CURDATE(),'"+notif+"','"+teach_lid+"')"
    print(qry)
    res=db.insert(qry)
    print(res)
    return jsonify(status='ok', data=res)

@app.route('/hod_view_student_new', methods=['POST'])
def hod_view_student_new():
    db =Db()
    Teach_lid=request.form['Teach_lid']
    qry="SELECT `students`.*,`hod`.`teach_lid` ,`course`.`course_name` FROM `students`  JOIN `course` ON `course`.`course_id`=`students`.`course_id` JOIN`hod` ON `hod`.`dept_id`=`course`.`dept_id` WHERE `hod`.`teach_lid`='"+Teach_lid+"'"
    res= db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/hod_view_std_attendacnce_new', methods=['POST'])
def hod_view_std_attendacnce_new():
    Teach_lid = request.form['Teach_lid']
    # std_lid = request.form['std_lid']
    db = Db()
    qry = "SELECT `students`.name , `hod`.`teach_lid`,`students`.`Reg_no`,`students`.`std_lid`,SUM(CASE WHEN `std_attendence`.status = 'present' THEN 1 ELSE 0 END) / COUNT(*) * 100 AS attendance_percentage " \
          "FROM `std_attendence`JOIN `students`  ON `students`.`std_lid` = `std_attendence`.`std_id` JOIN `course` ON `course`.`course_id`=`students`.`course_id`" \
          " JOIN`hod` ON `hod`.`dept_id`=`course`.`dept_id`" \
          " WHERE " \
          " `hod`.`teach_lid`='"+Teach_lid+"'    GROUP BY `students`.`std_lid`;"
    res = db.select(qry)
    print(res)
    return jsonify(status='ok', data=res)


@app.route('/hod_view_staff_attendacnce_new', methods=['POST'])
def hod_view_staff_attendacnce_new():
    Teach_lid = request.form['Teach_lid']
    # std_lid = request.form['std_lid']
    db = Db()
    qry = "SELECT * FROM `staff_att` JOIN `teachers` ON `teachers`.`Teach_lid` = `staff_att`.`teach_id` JOIN `hod` ON `hod`.`dept_id`=`teachers`.`dept_id`  WHERE `hod`.`teach_lid` ='"+Teach_lid+"' AND `hod`.`teach_lid` != `teachers`.`Teach_lid`"
    res = db.select(qry)
    print(res)
    return jsonify(status='ok', data=res)

##############################################################################

@app.route('/teacher_view_students_new', methods=['POST'])
def teacher_view_students_new():
    Teach_lid = request.form['Teach_lid']
    # sub_id = request.form['sub_id']
    db = Db()
    qry = "SELECT `students`.*,`sub_allocation`.`teach_id` FROM `sub_allocation` JOIN `sub` ON `sub`.`sub_id` = `sub_allocation`.`sub_id` JOIN `students` ON `students`.`course_id` = `sub`.`course_id` AND `sub`.`sem` = `students`.`sem` WHERE `sub_allocation`.`teach_id` = '"+Teach_lid+"' GROUP BY `students`.`std_lid` "
    res = db.select(qry)
    return  jsonify(status="ok", data = res)

@app.route('/teach_uploadInternel_post', methods=['POST'])
def teach_uploadInternel_post():
    std_id=request.form['std_id']
    sub_id=request.form['sub_id']
    tmark=request.form['tmark']
    smark=request.form['smark']
    asmrk=request.form['asmrk']
    atmrk=request.form['atmrk']
    grade=request.form['grade']
    total = int(smark)+int(tmark)+int(asmrk)+int(atmrk)
    print(total)
    db = Db()
    qry1 = "SELECT * FROM `internal_mark` WHERE `std_id`='"+std_id+"' AND `sub_id`='"+sub_id+"'"
    res1 = db .selectOne(qry1)
    if res1 is not None:
        qry2 = "UPDATE `internal_mark` SET `test_mrk`='" + tmark + "',`semi_mrk`='" + smark + "',`assignt_mrk`='" + asmrk + "',`att_mrk`='" + atmrk + "',`total`='" +str(total)+ "',`grade`='" + grade + "' WHERE `std_id`='" + std_id + "' AND `sub_id`='" + sub_id + "'"
        db.update(qry2)
        return jsonify(status="done")
    else:
        qry = "INSERT INTO `internal_mark` (`std_id`,`sub_id`,`test_mrk`,`semi_mrk`,`assignt_mrk`,`att_mrk`,`total`,`grade`) VALUES ('"+std_id+"','"+sub_id+"','"+tmark+"','"+smark+"','"+asmrk+"','"+atmrk+"','"+str(total)+"','"+grade+"')"
        db.insert(qry)
        return jsonify(status="ok")




@app.route('/teach_uploadStudyMaterial_post', methods=['POST'])
def teach_uploadStudyMaterial_post():
    sub_id = request.form['sub_id']
    pdf = request.form['pdf']
    db = Db()
    import time, datetime
    from encodings.base64_codec import base64_decode
    import base64
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(pdf)

    fh = open("D:/Riss/Projects/spas full/SPAS/static/study_material/" + timestr + ".pdf", "wb")
    fh.write(a)
    fh.close()
    path = '/static/study_material/' + timestr + ".pdf"
    qry = "INSERT INTO `files` (`sub_id`,`file_name`,`date_of_upld`) VALUES('"+sub_id+"','"+path+"',CURDATE())"
    res=db.insert(qry)
    return jsonify(status="ok")




@app.route('/teach_viewProfile_post', methods=['POST'])
def teach_viewProfile_post():
    Teach_lid = request.form['Teach_lid']
    db = Db()
    qry = "select * from teachers WHERE Teach_lid='" + Teach_lid + "'"
    res = db.selectOne(qry)
    return jsonify(status='ok',data=res)

@app.route('/teach_attMark_post', methods=['POST'])
def teach_attMark_post():
    teach_id = request.form['teach_id']
    db = Db()
    qry="INSERT INTO `staff_att` (`dates`,`teach_id`,`check_in_time`,`check_out_time`) VALUES (CURDATE(),'"+teach_id+"',CURTIME(),'pending') "
    res=db.insert(qry)
    print(res)
    return jsonify(status='ok',data=res)

@app.route('/teach_check_out_post', methods=['POST'])
def teach_check_out_post():
    teach_id=request.form['teach_id']
    db=Db()
    qry1 = "UPDATE `staff_att` SET `check_out_time`=CURTIME() WHERE `teach_id`='" + teach_id + "' AND `dates`=CURDATE()"
    res=db.update(qry1)
    print(res)
    return jsonify(status='ok', data=res)

@app.route('/teach_stdAtt_post', methods=['POST'])
def teach_stdAtt_post():
    std_id=request.form.getlist('std_id')
    hour=request.form['hour']
    status=request.form['status']
    db=Db()

    for i in std_id:
        qry="INSERT INTO `std_attendence` (`std_id`,`date`,`hours`,`status`) VALUES ('"+i+"',CURDATE(),'"+hour+"','present')"
        res=db.insert(qry)
        qry2="SELECT * FROM students WHERE `std_lid`!='"+i+"'"
        res2=db.selectOne(qry2)
        qry3 = "INSERT INTO `std_attendence` (`std_id`,`date`,`hours`,`status`) VALUES ('" + res2['std_lid'] + "',CURDATE(),'" + hour + "','absent')"
        res3 = db.insert(qry3)

        return jsonify(status='ok',data=res)

@app.route('/teach_view_students_post', methods=['POST'])
def teach_view_students_post():
    db=Db()
    teach_id=request.form['teach_id']
    qry="SELECT `sub_allocation`.`sub_id`,`sub_allocation`.`teach_id`,`sub`.`course_id`,`sub`.`sub_name`,`students`.`sem`,`students`.`name` FROM `sub_allocation` JOIN `sub` ON `sub`.`sub_id`=`sub_allocation`.`sub_id` JOIN `students`ON `students`.`sem`=`sub`.`sem`WHERE teach_id='"+teach_id+"'"
    res=db.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/teach_View_allSub_post', methods=['POST'])
def teach_View_allSub_post():
    teach_id = request.form['teach_id']
    db=Db()
    qry="SELECT sub.*,sub_allocation.* FROM `sub_allocation` JOIN sub ON sub.sub_id=sub_allocation.sub_id WHERE sub_allocation.teach_id='"+teach_id+"'"
    res=db.select(qry)
    return jsonify(status='ok',data=res)
@app.route('/teach_view_All_tt_post', methods=['POST'])
def teach_view_All_tt_post():
    sub_id = request.form['sub_id']
    teach_id=request.form['teach_id']
    db = Db()
    qry = "SELECT * FROM `time_table`JOIN`sub`ON time_table.sub_id=sub.sub_id JOIN `sub_allocation`ON time_table.sub_id=`sub_allocation`.sub_id WHERE teach_id='"+teach_id+"' "
    res = db.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/teach_View_StdDetails_post', methods=['POST'])
def teach_View_StdDetails_post():
    std_lid = request.form['std_lid']
    teach_id = request.form['teach_id']
    db = Db()
    qry = "SELECT students.* FROM `students`JOIN sub ON students.course_id=sub.course_id JOIN `sub_allocation`ON `sub`.`sub_id`=`sub_allocation`.`sub_id`WHERE teach_id='"+teach_id+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)
@app.route('/teach_view_std_att_post', methods=['POST'])
def teach_view_std_att_post():
    std_lid = request.form['std_lid']
    teach_id = request.form['teach_id']
    dept_id = request.form['dept_id']
    db = Db()
    qry="SELECT students.name,std_attendence.* FROM std_attendence JOIN students ON students.std_id=std_attendence.std_id JOIN course ON course.course_id=students.course_id WHERE dept_id='"+dept_id+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)
@app.route('/teach_View_Feedback_post', methods=['POST'])
def teach_View_Feedback_post():
    # sub_id = request.form['sub_id']
    Teach_lid = request.form['Teach_lid']
    db = Db()
    qry = "SELECT `feedback`.*, `students`.`name`,`sub_allocation`.`teach_id` FROM `feedback` JOIN `students` ON `students`.`std_lid` =`feedback`.`std_id` JOIN`sub_allocation` ON `sub_allocation`.`sub_id` =`feedback`.`sub_id` WHERE `sub_allocation`.`teach_id` ='"+Teach_lid+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)



@app.route('/teacher_view_std_attendc_new', methods=['POST'])
def teacher_view_std_attendc_new():
    db = Db()
    Teach_lid= request.form['Teach_lid']
    qry = " SELECT  `students`.name ,`students`.`Reg_no`,`students`.`std_lid`, SUM(CASE WHEN `std_attendence`.status = 'present' THEN 1 ELSE 0 END) / COUNT(*) * 100 AS attendance_percentage FROM `std_attendence`JOIN `students`  ON `students`.`std_lid` = `std_attendence`.`std_id` JOIN `sub` ON `sub`.`course_id`=`students`.`course_id` AND `students`.`sem`=`sub`.`sem` JOIN `sub_allocation` ON `sub_allocation`.`sub_id`= `sub`.`sub_id`  WHERE `sub_allocation`.`teach_id`='"+Teach_lid+"'  GROUP BY `students`.`std_lid`; "
    res = db.select(qry)
    return  jsonify(status="ok",data=res)

#####################################################################


@app.route('/std_reg_post', methods=['POST'])
def std_reg_post():
    name=request.form['name']
    bld_grp=request.form['bld_grp']
    H_name=request.form['H_name']
    place=request.form['place']
    city=request.form['city']
    state=request.form['state']
    pin=request.form['pin']
    Admn_no=request.form['Admn_no']
    Reg_no=request.form['Reg_no']
    Parent_name=request.form['Parent_name']
    parent_ph=request.form['parent_ph']
    parent_job=request.form['parent_job']
    parent_mail=request.form['parent_mail']
    Std_ph=request.form['Std_ph']
    dob=request.form['dob']
    course_id=request.form['course']
    sem=request.form['sem']
    prev_schl=request.form['prev_schl']
    cast= request.form['cast']
    religion = request.form['religion']
    prev_mark = request.form['prev_mark']
    # status= request.form['status']

    std_mail=request.form['Std_mail']
    photo = request.form['photo']
    db=Db()

    import time, datetime
    from encodings.base64_codec import base64_decode
    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(photo)
    fh = open("C:/Users/computer/Desktop/SPAS/static/student/" + timestr + ".jpg", "wb")

    fh.write(a)
    fh.close()


    # import base64
    # from datetime import datetime
    # import time
    # b=time.strftime("%Y%m%d-%H%M%S")
    # sp="C:\\Users\\Shabeeb\\Desktop\\SPAS\\static\\student\\"
    #
    # a=base64.b64decode(photo)
    # # fh=open(sp+b,'wb')
    # fh=open("C:\\Users\\Shabeeb\\Desktop\\SPAS\\static\\student\\"+b+".jpg","wb")
    # fh.write(a)
    # fh.close()

    path='/static/student/'+timestr+".jpg"

    qry="INSERT INTO login (`username`,`password`,`type`) VALUES ('"+std_mail+"','"+Std_ph+"','pending')"
    res = db.insert(qry)
    qry1="INSERT INTO login (`username`,`password`,`type`) VALUES ('"+parent_mail+"','"+parent_ph+"','parent')"
    res1 = db.insert(qry1)
    print(res1)
    qry2="INSERT INTO students (std_lid,`parent_lid`,`name`,`bld_grp`,`H_name`,`place`,`city`,`state`,`pin`,`Admn_no`,`Reg_no`,`Parent_name`,`parent_ph`,`parent_job`,`parent-mail`,`Std_ph`,`dob`,`course_id`,`sem`,`prev_schl`,`cast`,`religion`,`prev-mark`,photo,Std_mail,status) VALUES ('"+str(res)+"','"+str(res1)+"','"+name+"','"+bld_grp+"','"+H_name+"','"+place+"','"+city+"','"+state+"','"+pin+"','"+Admn_no+"','"+Reg_no+"','"+Parent_name+"','"+parent_ph+"','"+parent_job+"','"+parent_mail+"','"+Std_ph+"','"+dob+"','"+course_id+"','"+sem+"','"+prev_schl+"','"+cast+"','"+religion+"','"+prev_mark+"','"+path+"','"+std_mail+"','pending')"
    print(qry2)
    res=db.insert(qry2)
    print(res)
    return jsonify(status='ok')

@app.route('/std_edit_profile_post', methods=['POST'])
def std_edit_profile_post():
    name = request.form['name']
    bld_grp = request.form['bld_grp']
    H_name = request.form['H_name']
    place = request.form['place']
    city = request.form['city']
    state = request.form['state']
    pin = request.form['pin']
    Admn_no = request.form['Admn_no']
    Reg_no = request.form['Reg_no']
    Parent_name = request.form['Parent_name']
    parent_ph = request.form['parent_ph']
    parent_job = request.form['parent_job']
    parent_mail = request.form['parent_mail']
    Std_ph = request.form['Std_ph']
    dob = request.form['dob']
    course_id = request.form['course']
    sem = request.form['sem']
    prev_schl = request.form['prev_schl']
    cast = request.form['cast']
    religion = request.form['religion']
    prev_mark = request.form['prev_mark']
    std_mail = request.form['std_mail']
    status = request.form['status']
    std_lid=request.form['std_lid']
    photo = request.form['photo']


    db = Db()
    if len(photo)>1:

        import base64
        from datetime import datetime
        b = datetime.now().strftime("%Y%n%d-%H%M%S-%f") + ".jpg"
        sp = "C:\\Users\\Shabeeb\\Desktop\\SPAS\\static\\student\\"

        a = base64.b64decode(photo)
        with open(sp + b, 'wb') as fh:
            fh.write(a)

        path = '/static/student/' + b
        qry="UPDATE students `name`='"+name+"',`bld_grp`='"+bld_grp+"',`H_name`='"+H_name+"',`place`='"+place+"',`city`='"+city+"',`state`='"+state+"',`pin`='"+pin+"'," \
             "`Admn_no`='"+Admn_no+"',`Reg_no`='"+Reg_no+"',`Parent_name`='"+Parent_name+"',`parent_ph`='"+parent_ph+"',`parent_job`='"+parent_job+"',`parent_mail`='"+parent_mail+"'," \
             "`Std_ph`='"+Std_ph+"',`dob`='"+dob+"',`course_id`='"+course_id+"',`sem`='"+sem+"',`prev_schl`='"+prev_schl+"',`cast`='"+cast+"'," \
            "`religion`='"+religion+"',`prev_mark`='"+prev_mark+"',`status`='"+status+"',`photo`='"+path+"',`std_mail`='"+std_mail+"' WHERE `std_lid`='"+std_lid+"'"
        res=db.update(qry)
        return jsonify(status="ok")
    else:
        qry = "UPDATE students `name`='" + name + "',`bld_grp`='" + bld_grp + "',`H_name`='" + H_name + "',`place`='" + place + "',`city`='" + city + "',`state`='" + state + "',`pin`='" + pin + "'," \
                                                                                                                                                                                                  "`Admn_no`='" + Admn_no + "',`Reg_no`='" + Reg_no + "',`Parent_name`='" + Parent_name + "',`parent_ph`='" + parent_ph + "',`parent_job`='" + parent_job + "',`parent-mail`='" + parent_mail + "'," \
                                                                                                                                                                                                                                                                                                                                                                                                "`Std_ph`='" + Std_ph + "',`dob`='" + dob + "',`course_id`='" + course_id + "',`sem`='" + sem + "',`prev_schl`='" + prev_schl + "',`cast`='" + cast + "'," \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      "`religion`='" + religion + "',`prev-mark`='" + prev_mark + "',`status`='" + status + "',`std_mail`='" + std_mail + "' WHERE `std_lid`='" + std_lid + "'"
        res = db.update(qry)
        return jsonify(status="ok")


@app.route('/std_view_studyMet_post', methods=['POST'])
def std_view_studyMet_post():
    # sub_id = request.form['sub_id']
    std_lid = request.form['std_lid']
    db = Db()
    qry = "SELECT files.* FROM files JOIN sub ON files.sub_id=sub.sub_id JOIN `students`ON `students`.`sem`=`sub`.`sem` WHERE std_lid='"+std_lid+"'"
    res = db.select(qry)
    print(res)
    print(qry)
    return jsonify(status='ok', data=res)

@app.route('/std_viewPrfl_post', methods=['POST'])
def std_viewPrfl_post():
    std_lid = request.form['std_lid']
    db = Db()
    qry = "select * from students WHERE std_lid='" + std_lid + "'"
    res = db.selectOne(qry)
    if res is not None:
        return jsonify(status='ok', name=res["name"],bld_grp=res["bld_grp"],H_name=res["H_name"],place=res["place"],city=res["city"],state=res["state"],pin=res["pin"],Admn_no=res["Admn_no"],Reg_no=res["Reg_no"],Parent_name=res["Parent_name"],parent_ph=res["parent_ph"],parent_job=res["parent_job"],parent_mail=res["parent_mail"],Std_ph=res["Std_ph"],dob=res["dob"],course=res["course_id"],sem=res["sem"],prev_schl=res["prev_schl"],prev_mark=res["prev_mark"],std_mail=res["Std_mail"],photo=res["photo"],cast=res["cast"],religion=res["religion"]);
    else:
        return jsonify(status="no")

@app.route('/std_viewTeach_post', methods=['POST'])
def std_viewTeach_post():
    # Teach_lid = request.form['Teach_lid']
    std_lid=request.form['std_lid']
    print(std_lid)
    db = Db()
    qry = "SELECT * FROM `sub_allocation` JOIN `teachers` ON `teachers`.`Teach_lid` =`sub_allocation`.`teach_id`  JOIN `sub` ON `sub`.`sub_id`=`sub_allocation`.`sub_id` JOIN `students` ON `students`.`sem` =`sub`.`sem` WHERE `students`.`std_lid` ='"+std_lid+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/std_viewSub_post', methods=['POST'])
def std_viewSub_post():
    std_lid = request.form['std_lid']
    db = Db()
    qry = "SELECT sub.*,`course`.`course_name` FROM sub JOIN `course` ON `sub`.`course_id`=`course`.`course_id`JOIN `students`ON `sub`.`sem`=`students`.`sem` WHERE `std_lid`='"+std_lid+"'"
    res = db.select(qry)
    print(std_lid)
    print(res)
    return jsonify(status='ok', data=res)

@app.route('/std_viewAtt_post', methods=['POST'])
def std_viewAtt_post():
    std_lid = request.form['std_lid']
    db = Db()
    qry = "SELECT students.name,std_attendence.* FROM std_attendence JOIN students ON students.std_id=std_attendence.std_id WHERE std_lid='"+std_lid+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/std_sndFeed_post', methods=['POST'])
def std_sndFeed_post():
    feedback=request.form['feedback']
    sub_id=request.form['subject']
    rating=request.form['rating']
    std_id = request.form['std_id']
    db = Db()
    qry ="INSERT INTO `feedback` (`std_id`,`sub_id`,`feedback`,`dates`,`rating`) VALUES ('"+std_id+"','"+sub_id+"','"+feedback+"',CURDATE(),'"+rating+"')"
    print(qry)
    res = db.insert(qry)
    print(res)
    return jsonify(status='ok')

@app.route('/std_viewInternl_post', methods=['POST'])
def std_viewInternl_post():
    std_id = request.form['std_id']
    print(std_id)
    db = Db()
    qry = "SELECT `internal_mark`.*,`sub`.`sub_name` FROM `internal_mark` JOIN sub ON `internal_mark`.sub_id=sub.sub_id  WHERE std_id='"+std_id+"' "
    res = db.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/std_view_notification_post', methods=['POST'])
def view_notification_post():
    db = Db()
    qry = "select * from notification"
    res = db.select(qry)
    return jsonify(status='ok', data=res)


@app.route('/std_view_std_attendacnce_new', methods=['POST'])
def std_view_std_attendacnce_new():
    Teach_lid = request.form['Teach_lid']
    # std_lid = request.form['std_lid']
    db = Db()
    qry = "SELECT `students`.name , `hod`.`teach_lid`,`students`.`Reg_no`,`students`.`std_lid`,SUM(CASE WHEN `std_attendence`.status = 'present' THEN 1 ELSE 0 END) / COUNT(*) * 100 AS attendance_percentage " \
          "FROM `std_attendence`JOIN `students`  ON `students`.`std_lid` = `std_attendence`.`std_id` JOIN `course` ON `course`.`course_id`=`students`.`course_id`" \
          " JOIN`hod` ON `hod`.`dept_id`=`course`.`dept_id`" \
          " WHERE " \
          " `students`.`std_lid`='"+Teach_lid+"'    GROUP BY `students`.`std_lid`;"
    res = db.select(qry)
    print(res)
    return jsonify(status='ok', data=res)



##################################################################


@app.route('/std_viewPrfl_post2', methods=['POST'])
def std_viewPrfl_post2():
    std_lid = request.form['std_lid']
    db = Db()
    qry = "select * from students WHERE `parent_lid`='" + std_lid + "'"
    res = db.selectOne(qry)
    if res is not None:
        return jsonify(status='ok', name=res["name"],bld_grp=res["bld_grp"],H_name=res["H_name"],place=res["place"],city=res["city"],state=res["state"],pin=res["pin"],Admn_no=res["Admn_no"],Reg_no=res["Reg_no"],Parent_name=res["Parent_name"],parent_ph=res["parent_ph"],parent_job=res["parent_job"],parent_mail=res["parent_mail"],Std_ph=res["Std_ph"],dob=res["dob"],course=res["course_id"],sem=res["sem"],prev_schl=res["prev_schl"],prev_mark=res["prev_mark"],std_mail=res["Std_mail"],photo=res["photo"],cast=res["cast"],religion=res["religion"]);
    else:
        return jsonify(status="no")

@app.route('/par_childPfl_post', methods=['POST'])
def par_childPfl_post():
    parent_lid=request.form['parent_lid']
    # print(parent_lid,"hii")
    db = Db()
    qry = "SELECT * FROM `students`WHERE `parent_lid`='"+parent_lid+"'"
    res = db.selectOne(qry)
    print(res,"hloooooooooo")
    return jsonify(status='ok', data=res)

@app.route('/par_viewStdAtt_post', methods=['POST'])
def par_viewStdAtt_post():
    p_lid = request.form['p_lid']
    # std_lid = request.form['std_lid']
    db = Db()
    qry = "SELECT `students`.name , `hod`.`teach_lid`,`students`.`Reg_no`,`students`.`std_lid`,SUM(CASE WHEN `std_attendence`.status = 'present' THEN 1 ELSE 0 END) / COUNT(*) * 100 AS attendance_percentage " \
          "FROM `std_attendence`JOIN `students`  ON `students`.`std_lid` = `std_attendence`.`std_id` JOIN `course` ON `course`.`course_id`=`students`.`course_id`" \
          " JOIN`hod` ON `hod`.`dept_id`=`course`.`dept_id`" \
          " WHERE " \
          " `students`.`parent_lid`='" + p_lid + "'    GROUP BY `students`.`std_lid`;"
    res = db.select(qry)
    print(res)
    return jsonify(status='ok', data=res)

@app.route('/par_viewInternl_post', methods=['POST'])
def par_viewInternl_post():
    parent_lid = request.form['parent_lid']
    db = Db()
    qry = "SELECT  `internal_mark`.*,`sub`.`sub_name`  FROM `internal_mark` JOIN `sub` ON `sub`.`sub_id` =`internal_mark`.`sub_id` JOIN `students` ON `students`.`std_lid`=`internal_mark`.`std_id` WHERE `students`.`parent_lid` ='"+str(parent_lid)+"'"
    res = db.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/par_view_notification_post', methods=['POST'])
def par_view_notification_post():
    db = Db()
    qry = "select * from notification"
    res = db.select(qry)
    return jsonify(status='ok', data=res)





if __name__ == '__main__':
    app.run(debug=True,port=4000,host="0.0.0.0")