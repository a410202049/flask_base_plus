#!/usr/bin/python
# -*- encoding: utf-8 -*-
from StringIO import StringIO
from operator import and_

import xlrd
import xlwt
import os

from sqlalchemy import or_, func, case
import copy
from app import db
from app import CommonResponse, ResultType
from app.controller.admin import admin
from flask import request, current_app as app, url_for, render_template, Response
from flask_login import login_required

from app.helpers.common_helper import create_uuid, fragment
from app.models.Enroll import Student, Organization, BedInfo, RoomRule, EnrollFees, OrderFees, Order, TDTCFees
import collections

@admin.route('/student-list', methods=['GET', 'POST'])
@login_required
def student_list():
    title = u'学生管理'
    page = request.args.get('page', 1, type=int)
    student_no = request.args.get('student_no', '')
    exam_no = request.args.get('exam_no', '')
    id_card_no = request.args.get('id_card_no', '')

    rows = db.session.query(Student, Organization).join(
        Organization, Organization.serial_no == Student.org_no
    ).order_by(Student.id.desc())
    if student_no != '':
        rows = rows.filter(Student.student_no == student_no)
    if exam_no != '':
        rows = rows.filter(Student.exam_no == exam_no)
    if id_card_no != '':
        rows = rows.filter(Student.id_card_no == id_card_no)

    paginate = rows.paginate(
        page, per_page=app.config['PAGE_SIZE'], error_out=True)
    students = paginate.items

    academys = db.session.query(
        Organization.academy
    ).group_by(Organization.academy).all()

    data = {
        "student_no": student_no,
        "exam_no": exam_no,
        "students": students,
        "id_card_no": id_card_no,
        "pagination": paginate,
        "fragment": fragment(),
        "academys":academys
    }
    return render_template('admin/enroll/student_list.html', data=data, title=title)


@admin.route('/student-import', methods=['GET', 'POST'])
@login_required
def student_import():
    try:
        file = request.files['file']
        extensions = ['xlsx', 'xls']
        if file:
            ext = file.filename.rsplit('.', 1)[1]
            file_read = file.read()
            if ext not in extensions:
                return CommonResponse(ResultType.Failed, message=u"文件格式不正确").to_json()
            table_data = xlrd.open_workbook(file_contents=file_read)
            # 获取第一个工作簿
            table = table_data.sheets()[0]

            ncols = table.ncols  # 列数
            rows_data = table.get_rows()  # 第一个工作簿数据
            student_no_list = []
            exam_no_list = []
            id_card_no_list = []
            title_list = []
            organization_list = []
            mobile_list = []

            def is_organization_exist(organization):
                for org in organization_list:
                    if org.academy == organization.academy and org.grade == organization.grade and \
                                    org.major == organization.major and org.class_name == organization.class_name:
                        return org.serial_no
                return False

            for i, row in enumerate(rows_data):
                data = []
                for j in range(0, ncols):
                    row_data = row[j]
                    # 0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error
                    ctype = row_data.ctype
                    value = row_data.value
                    if ctype == 2:
                        value = str(int(value))  # 将浮点转换成整数再转换成字符串
                    if i > 0:
                        if ctype == 0:
                            title_name = title_list[j]
                            return CommonResponse(ResultType.Failed,
                                                  message=u"第{0}行的{1}不能为空".format(i + 1, title_name)).to_json()
                        if j == 1:
                            # 性别
                            value = 1 if value == u'男' else 0
                        if j == 2:
                            # 学号
                            if value not in student_no_list:
                                student_no_list.append(value)
                            else:
                                return CommonResponse(ResultType.Failed,
                                                      message=u"第{0}行的学号数据重复".format(i + 1)).to_json()
                        if j == 3:
                            # 考生号
                            if value not in exam_no_list:
                                exam_no_list.append(value)
                            else:
                                return CommonResponse(ResultType.Failed,
                                                      message=u"第{0}行的考生号数据重复".format(i + 1)).to_json()
                        if j == 4:
                            # 身份证
                            if value not in id_card_no_list:
                                id_card_no_list.append(value)
                            else:
                                return CommonResponse(ResultType.Failed,
                                                      message=u"第{0}行的身份证号数据重复".format(i + 1)).to_json()

                        if j == 9:
                            # 手机号码
                            if value not in mobile_list:
                                mobile_list.append(value)
                            else:
                                return CommonResponse(ResultType.Failed,
                                                      message=u"第{0}行的手机号数据重复".format(i + 1)).to_json()

                    data.append(value)
                if i == 0:
                    title_list = data
                elif i > 0:
                    student = db.session.query(
                        Student
                    ).filter(Student.student_no == data[2]).first()

                    organization = db.session.query(Organization).filter(
                        Organization.academy == data[5],
                        Organization.grade == data[8],
                        Organization.major == data[6],
                        Organization.class_name == data[7]
                    ).first()

                    # 判断学校信息是否存在
                    if not organization:
                        organization = Organization()
                        organization.academy = data[5]
                        organization.grade = data[8]
                        organization.major = data[6]
                        organization.class_name = data[7]
                        serial_no = is_organization_exist(organization)
                        if not serial_no:
                            serial_no = create_uuid()
                            organization.serial_no = serial_no
                            organization_list.append(organization)
                            db.session.add(organization)
                    else:
                        serial_no = organization.serial_no

                    if student:
                        student.name = data[0]
                        student.sex = data[1]
                        student.student_no = data[2]
                        student.exam_no = data[3]
                        student.id_card_no = data[4]
                        student.mobile = data[9]
                        student.org_no = serial_no
                        db.session.merge(student)
                    else:
                        student = Student()
                        student.name = data[0]
                        student.sex = data[1]
                        student.student_no = data[2]
                        student.exam_no = data[3]
                        student.id_card_no = data[4]
                        student.mobile = data[9]
                        student.org_no = serial_no
                        db.session.add(student)

            db.session.commit()
        return CommonResponse(ResultType.Success, message=u"导入成功").to_json()
    except Exception, e:
        db.session.rollback()
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"导入学生信息异常").to_json()


@admin.route('/bed-info-list', methods=['GET', 'POST'])
@login_required
def bed_info_list():
    title = u'寝室床位'
    page = request.args.get('page', 1, type=int)
    build_name = request.args.get('build_name', '')
    floor_no = request.args.get('floor_no', '')
    dorm_no = request.args.get('dorm_no', '')

    rows = db.session.query(BedInfo).order_by(BedInfo.build_name.asc(),BedInfo.floor_no.asc(),BedInfo.dorm_no.asc(),BedInfo.bed_no.asc())

    if build_name != '':
        rows = rows.filter(BedInfo.build_name == build_name)
    if floor_no != '':
        rows = rows.filter(BedInfo.floor_no == floor_no)
    if dorm_no != '':
        rows = rows.filter(BedInfo.dorm_no == dorm_no)

    paginate = rows.paginate(
        page, per_page=app.config['PAGE_SIZE'], error_out=True)
    beds = paginate.items
    data = {
        "build_name": build_name,
        "floor_no": floor_no,
        "beds": beds,
        "dorm_no": dorm_no,
        "pagination": paginate,
        "fragment": fragment(),
    }
    return render_template('admin/enroll/bed_info_list.html', data=data, title=title)


@admin.route('/student-export', methods=['GET', 'POST'])
@login_required
def student_export():
    try:
        buffer = StringIO()
        wb = xlwt.Workbook()
        ws = wb.add_sheet(u"学生列表")
        row = 0


        rows = db.session.query(Student, Organization).join(
            Organization, Organization.serial_no == Student.org_no
        ).order_by(Student.id.desc())

        data_list = []
        title_data = [u'学生姓名',u'考生号',u'学号',u'身份证号',u'手机号',u'性别',u'院系',u'专业',u'班级',u'年级',u'身高',u'胸围',u'腰围',u'鞋码']
        data_list.append(title_data)
        for student,org in rows:
            sex = u'男' if student.sex == 1 else u'女'
            temp_list = [student.name,student.exam_no,student.student_no,student.id_card_no,student.mobile,sex,org.academy,org.major,org.class_name,org.grade,student.height,student.bust,student.waist,student.shoe_size]
            data_list.append(temp_list)

        for data in data_list:
            for i in xrange(0, len(data)):
                name = data[i]
                ws.write(row, i, name)
            row += 1
        wb.save(buffer)

        return Response(buffer.getvalue(),
                       mimetype="application/vnd.ms-excel",
                       headers={"Content-Disposition": "attachment;filename=学生列表.xls"})

    except Exception, e:
        return CommonResponse(ResultType.Failed, message=u"导出学生异常").to_json()

@admin.route('/bed-info-import', methods=['GET', 'POST'])
@login_required
def bed_info_import():
    try:
        file = request.files['file']
        extensions = ['xlsx', 'xls']
        # 楼栋列表
        builds = []
        list_data = []
        if file:
            ext = file.filename.rsplit('.', 1)[1]
            file_read = file.read()
            if ext not in extensions:
                return CommonResponse(ResultType.Failed, message=u"文件格式不正确").to_json()
            table_data = xlrd.open_workbook(file_contents=file_read)
            # 获取第一个工作簿
            table = table_data.sheets()[1]
            ncols = table.ncols  # 列数
            rows_data = table.get_rows()  # 第一个工作簿数据

            for i, row in enumerate(rows_data):
                data = []
                for j in range(0, ncols):
                    row_data = row[j]
                    ctype = row_data.ctype
                    value = row_data.value
                    if ctype == 1:
                        value = value.strip()
                    if ctype == 2:
                        value = str(int(value))  # 将浮点转换成整数再转换成字符串

                    if ctype == 0 or value == '':
                        # 当为空的时候跳过
                        continue
                    data.append(value)
                if data:
                    list_data.append(data)

            init_build_dict = {
                "floor_no_list": [],
                "build_name": "",
            }

            for i, data_row in enumerate(list_data):
                if data_row[0] == u'宿舍楼栋名':
                    build_name = data_row[1]
                    init_build_dict['build_name'] = build_name
                if data_row[0] == u'房号':
                    tmp_dict = {
                        "dorm_no_list": []
                    }
                    bed_data = list_data[i + 1]
                    for j, dorm_data in enumerate(data_row):
                        if j == 0:
                            continue
                        tmp_dict['floor_no'] = data_row[j][1:2]
                        tmp_dict['dorm_no_list'].append({
                            "dorm_no": data_row[j],
                            "bed_no": bed_data[j]
                        })
                    init_build_dict['floor_no_list'].append(tmp_dict)
                if data_row[0] == u'合计':
                    builds.append(init_build_dict)
                    init_build_dict = {
                        "floor_no_list": [],
                        "build_name": "",
                    }

            # 每一次导入清空床位信息
            db.session.execute("truncate table t_bed_info;")
            db.session.commit()

            # print builds
            # 生成数据到数据库
            BedInfoAnalysis().create_bed_info(builds)
            return CommonResponse(ResultType.Success, message=u"导入成功").to_json()

    except Exception, e:
        db.session.rollback()
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"导入床位信息异常").to_json()



@admin.route('/get-student-info', methods=['GET', 'POST'])
@login_required
def get_student_info():
    try:
        student_id = request.form.get('student_id')

        student_info = db.session.query(
            Student.id,
            Student.name,
            Student.mobile,
            Student.org_no,
            Student.exam_no,
            Student.id_card_no,
            Student.student_no,
            Student.sex,
            Organization.major,
            Organization.academy,
            Organization.class_name,
            Organization.grade
        ).join(
            Organization,Student.org_no == Organization.serial_no
        ).filter(
            Student.id == student_id
        ).first()

        data = {
            "id":student_info.id,
            "name": student_info.name,
            "mobile": student_info.mobile,
            "org_no": student_info.org_no,
            "exam_no": student_info.exam_no,
            "id_card_no": student_info.id_card_no,
            "student_no": student_info.student_no,
            "sex": student_info.sex,
            "major": student_info.major,
            "academy": student_info.academy,
            "class_name": student_info.class_name,
            "grade": student_info.grade
        }

        return CommonResponse(ResultType.Success, message=u"获取成功",data=data).to_json()
    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"获取学生信息异常").to_json()

@admin.route('/get-organization-info', methods=['GET', 'POST'])
@login_required
def get_organization_info():
    try:
        form_type = request.form.get('type')
        rows = []
        if form_type == 'academy':
            academy = request.form.get('academy')
            rows = db.session.query(
                Organization.major
            ).filter(
                Organization.academy == academy
            ).group_by(
                Organization.major
            ).all()
        elif form_type == 'major':
            academy = request.form.get('academy')
            major = request.form.get('major')
            rows = db.session.query(
                Organization.class_name
            ).filter(
                Organization.major == major,
                Organization.academy == academy
            ).group_by(
                Organization.class_name
            ).all()

        elif form_type == 'class_name':
            academy = request.form.get('academy')
            major = request.form.get('major')
            class_name = request.form.get('class_name')
            rows = db.session.query(
                Organization.grade
            ).filter(
                Organization.major == major,
                Organization.academy == academy,
                Organization.class_name == class_name
            ).group_by(
                Organization.grade
            ).all()

        data = []
        for row in rows:
            data.append(row[0])
        return CommonResponse(ResultType.Success, message=u"获取成功",data=data).to_json()
    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"获取学生信息异常").to_json()


@admin.route('/save-student-info', methods=['GET', 'POST'])
@login_required
def save_student_info():
    try:
        form_data = request.form

        student = db.session.query(
            Student
        ).filter(
            or_(
                Student.id_card_no == form_data.get('id_card_no'),
                Student.exam_no == form_data.get('exam_no'),
                Student.student_no == form_data.get('student_no'),
                Student.mobile == form_data.get('mobile')
            ),
            Student.id != form_data.get('id')
        ).all()
        if student:
            return CommonResponse(ResultType.Failed, message=u"数据已存在请检查身份证号，考生号，学号，手机号").to_json()

        org_data = db.session.query(
            Organization
        ).filter(
            Organization.grade == form_data.get('grade'),
            Organization.major == form_data.get('major'),
            Organization.class_name == form_data.get('class_name'),
            Organization.academy == form_data.get('academy')
        ).first()

        if not org_data:
            return CommonResponse(ResultType.Failed, message=u"请选择学生所属班级").to_json()
        student_info = db.session.query(
            Student
        ).filter(
            Student.id == form_data.get('id')
        ).first()
        student_info.name = form_data.get('student_name')
        student_info.exam_no = form_data.get('exam_no')
        student_info.student_no = form_data.get('student_no')
        student_info.mobile = form_data.get('mobile')
        student_info.id_card_no = form_data.get('id_card_no')
        student_info.org_no = org_data.serial_no
        db.session.merge(student_info)
        db.session.commit()
        return CommonResponse(ResultType.Success, message=u"保存成功").to_json()

    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"保存学生信息异常").to_json()


@admin.route('/dorm-rule', methods=['GET', 'POST'])
@login_required
def dorm_rule():
    try:
        title = u'寝室分配'
        page = request.args.get('page', 1, type=int)
        academy = request.args.get('academy', '')
        major = request.args.get('major', '')
        grade = request.args.get('grade', '')
        class_name = request.args.get('class_name', '')

        rows = db.session.query(
            Organization
        ).order_by(
            Organization.class_name.desc()
        )

        if academy != '':
            rows = rows.filter(Organization.academy == academy)
        if major != '':
            rows = rows.filter(Organization.major == major)
        if grade != '':
            rows = rows.filter(Organization.grade == grade)
        if class_name != '':
            rows = rows.filter(Organization.class_name == class_name)

        paginate = rows.paginate(
            page, per_page=app.config['PAGE_SIZE'], error_out=True)

        orgs = paginate.items

        data_orgs = []
        for org in orgs:
            man_room_rule = db.session.query(
                RoomRule
            ).filter(
                RoomRule.org_no == org.serial_no,
                RoomRule.sex == 1
            ).first()

            woman_room_rule = db.session.query(
                RoomRule
            ).filter(
                RoomRule.org_no == org.serial_no,
                RoomRule.sex == 0
            ).first()

            _ = {
                "id": org.id,
                "serial_no":org.serial_no,
                "grade": org.grade,
                "academy": org.academy,
                "major": org.major,
                "class_name": org.class_name,
                "man_room_rule":man_room_rule,
                "woman_room_rule":woman_room_rule
            }
            data_orgs.append(_)
        data = {
            "academy": academy,
            "major": major,
            "grade": grade,
            "class_name": class_name,
            "pagination": paginate,
            "fragment": fragment(),
            "orgs": data_orgs
        }
        return render_template('admin/enroll/dorm_rule.html',title=title,data=data)
    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"寝室规则异常").to_json()

@admin.route('/distribution-dorm', methods=['GET', 'POST'])
@login_required
def distribution_dorm():
    try:
        title = u'寝室分配'
        org_no = request.args.get('org_no', '')
        sex = int(request.args.get('sex', ''))

        rows = db.session.query(
            BedInfo,
            RoomRule
        ).outerjoin(
            RoomRule,BedInfo.serial_no == RoomRule.bed_no
        ).order_by(
            BedInfo.build_name
        ).order_by(
            BedInfo.dorm_no
        ).all()

        room = collections.OrderedDict()
        # status = 0 #未选择 1选择 2禁用
        for bed,rule in rows:
            if bed.build_name not in room.keys():
                room[bed.build_name] = collections.OrderedDict(sex=None)
            if bed.dorm_no not in room[bed.build_name].keys():
                room[bed.build_name][bed.dorm_no] = {
                    "status": 0,
                    "serial_no": bed.serial_no,
                    "dorm_no": bed.dorm_no,
                    "bed_num": 1,
                    "org_no":rule.org_no if rule else None,
                    "sex": rule.sex if rule else None,
                }
            else:
                room[bed.build_name][bed.dorm_no].update({'bed_num': room[bed.build_name][bed.dorm_no]['bed_num'] + 1})
                if rule and room[bed.build_name][bed.dorm_no]['sex'] is None:
                    room[bed.build_name][bed.dorm_no].update({'sex': rule.sex})
            if (room[bed.build_name]['sex'] is None) and rule:
                room[bed.build_name]['sex'] = rule.sex


        for key,value in room.items():
            for dorm in value.values():
                if isinstance(dorm,dict):
                    if sex != value['sex'] and (value['sex'] is not None):
                        dorm['status'] = 2
                    if (dorm['org_no'] is not None) and (dorm['org_no'] == org_no) and sex == value['sex']:
                        dorm['status'] = 1
                    elif (dorm['org_no'] is not None) and (dorm['org_no'] != org_no):
                        dorm['status'] = 2


        return render_template('admin/enroll/distribution_dorm.html', title=title, data=room, sex=sex, org_no =org_no)
    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"分配寝室异常").to_json()


@admin.route('/distribution-dorm-method', methods=['GET', 'POST'])
@login_required
def distribution_dorm_method():
    try:


        dorm_no = request.form.get('dorm_no')
        org_no = request.form.get('org_no')
        distribution = int(request.form.get('distribution'))
        sex = int(request.form.get('sex'))

        beds = db.session.query(
            BedInfo
        ).filter(
            BedInfo.dorm_no == dorm_no
        ).all()

        if not beds:
            return CommonResponse(ResultType.Failed, message=u"该寝室不存在，请刷新重试").to_json()

        room_rule = db.session.query(
            RoomRule
        ).filter(
            RoomRule.dorm_no == dorm_no
        ).first()

        if room_rule and (room_rule.sex != sex):
            return CommonResponse(ResultType.Failed, message=u"男女不能混住").to_json()

        if room_rule and (room_rule.org_no != org_no):
            return CommonResponse(ResultType.Failed, message=u"该寝室已被其它专业分配").to_json()

        if distribution:
            if room_rule:
                return CommonResponse(ResultType.Failed, message=u"该寝室已被当前专业分配").to_json()
            for bed in beds:
                room_rule = RoomRule()
                room_rule.dorm_no = dorm_no
                room_rule.bed_no = bed.serial_no
                room_rule.sex = sex
                room_rule.org_no = org_no
                db.session.add(room_rule)
        else:
            db.session.query(
                RoomRule
            ).filter(
                RoomRule.dorm_no == dorm_no
            ).delete()
        db.session.commit()
        return CommonResponse(ResultType.Success, message=u"操作成功").to_json()

    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"分配寝室异常").to_json()


@admin.route('/payment-statistics', methods=['GET', 'POST'])
@login_required
def payment_statistics():
    try:
        # 缴费项目统计
        title = u'缴费项统计'
        student_num = db.session.query(func.count(Student.id)).scalar()


        enroll_total_amount_case = case([((EnrollFees.amount * student_num) == None, 0)], else_=(EnrollFees.amount * student_num))
        enroll_total_amt_case = case([(func.sum(Order.pay_amt) == None, 0)],else_=func.sum(Order.pay_amt))
        enroll_fees = db.session.query(
            EnrollFees.fee_no,
            EnrollFees.name.label('fee_name'),
            enroll_total_amount_case.label('total_amount'),
            enroll_total_amt_case.label('total_amt')
        ).outerjoin(
            OrderFees, OrderFees.fee_no == EnrollFees.fee_no
        ).outerjoin(
            Order, and_(Order.order_no == OrderFees.order_no, Order.status == 'paied')
        ).group_by(
            EnrollFees.fee_no
        ).all()

        tdtc_total_amount_case = case([((TDTCFees.amt + TDTCFees.paid_amt) * student_num == None, 0)], else_=(TDTCFees.amt + TDTCFees.paid_amt) * student_num)
        tdtc_total_amt_case = case([(func.sum(TDTCFees.paid_amt) == None, 0)], else_=func.sum(TDTCFees.paid_amt))

        tdtc_fees = db.session.query(
            TDTCFees.fee_no,
            TDTCFees.fee_name,
            tdtc_total_amount_case.label('total_amount'),
            tdtc_total_amt_case.label('total_amt')
        ).group_by(
            TDTCFees.fee_name
        ).all()


        fee_data = []

        total_amt = 0
        for enroll_fee in enroll_fees:
            _ = {
                "fee_no":enroll_fee.fee_no,
                "fee_name":enroll_fee.fee_name,
                "total_amount":enroll_fee.total_amount,
                "total_amt":enroll_fee.total_amt
            }
            fee_data.append(_)
            total_amt+= enroll_fee.total_amt

        for tdtc_fee in tdtc_fees:
            _ = {
                "fee_no":tdtc_fee.fee_no,
                "fee_name":tdtc_fee.fee_name,
                "total_amount":'',
                "total_amt":tdtc_fee.total_amt
            }
            fee_data.append(_)
            total_amt += tdtc_fee.total_amt

        return render_template('admin/enroll/payment_statistics.html', fee_data=fee_data, title=title,total_amt=total_amt)
    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"缴费项目统计异常").to_json()


@admin.route('/academy-statistics', methods=['GET', 'POST'])
@login_required
def academy_statistics():
    try:

        academy = request.args.get('academy', '')
        major = request.args.get('major', '')
        grade = request.args.get('grade', '')
        class_name = request.args.get('class_name', '')
        page = request.args.get('page', 1, type=int)

        query_data = db.session.query(
            Organization.academy,
            Organization.major,
            Organization.grade,
            Organization.class_name,
            func.count(Student.id).label('student_num'),
            Organization.serial_no
        ).group_by(
            Organization.serial_no
        ).outerjoin(
            Student,Student.org_no == Organization.serial_no
        )

        if academy:
            query_data = query_data.filter(
                Organization.academy == academy
            )

        if major:
            query_data = query_data.filter(
                Organization.major == major
            )

        if grade:
            query_data = query_data.filter(
                Organization.grade == grade
            )

        if class_name:
            query_data = query_data.filter(
                Organization.class_name == class_name
            )

        paginate = query_data.paginate(page, per_page=app.config['PAGE_SIZE'], error_out=True)
        rows = paginate.items
        data_list = []
        for row in rows:
            enroll_total_amt_case = case([(func.sum(Order.pay_amt) == None, 0)], else_=func.sum(Order.pay_amt))
            tdtc_total_amt_case = case([(func.sum(TDTCFees.paid_amt) == None, 0)], else_=func.sum(TDTCFees.paid_amt))

            enroll_data = db.session.query(
                func.count(Student.id).label('student_num'),
                enroll_total_amt_case.label('total_amt')
            ).outerjoin(
                Order,and_(Order.student_no == Student.student_no,Order.status == 'paied')
            ).filter(
                Student.org_no == row.serial_no
            ).first()

            tdtc_data = db.session.query(
                func.count(Student.id).label('student_num'),
                tdtc_total_amt_case.label('total_amt')
            ).outerjoin(
                TDTCFees,TDTCFees.student_no == Student.student_no
            ).filter(
                Student.org_no == row.serial_no
            ).first()
            total_amt = enroll_data.total_amt + tdtc_data.total_amt
            _ = {
                "academy": row.academy,
                "major": row.major,
                "grade": row.grade,
                "class_name": row.class_name,
                "total_amt": total_amt,

            }
            data_list.append(_)

        data = {
            "academy": academy,
            "major": major,
            "grade": grade,
            "class_name": class_name,
            "pagination": paginate
        }

        return render_template('admin/enroll/academy_statistics.html',data=data,data_list=data_list)
    except Exception, e:
        app.logger.info(e)
        return CommonResponse(ResultType.Failed, message=u"院系缴费项目统计异常").to_json()


class BedInfoAnalysis(object):
    @staticmethod
    def create_bed_info(bulids):
        for build in bulids:
            build_name = build['build_name'].replace('S ', '')
            for floor_no_data in build['floor_no_list']:
                floor_no = floor_no_data['floor_no']
                for dorm_no_data in floor_no_data['dorm_no_list']:
                    dorm_no = dorm_no_data['dorm_no']
                    for bed_id in range(1, int(dorm_no_data['bed_no']) + 1):
                        bed_info = BedInfo()
                        bed_info.build_name = build_name
                        bed_info.floor_no = floor_no
                        bed_info.dorm_no = dorm_no
                        bed_info.bed_no = bed_id
                        bed_info.serial_no = create_uuid()
                        db.session.add(bed_info)
        db.session.commit()
