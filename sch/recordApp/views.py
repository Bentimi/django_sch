from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponse
from recordApp.forms import courseAddForm, courseEditForm, reg_cbt, course_details, question_form, test_form
from .models import User
from recordApp.models import course_register, course_model, cbt, questions, course_form, grading
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from adminApp.models import fees_table
from paymentApp.models import invoice_table, tuition_invoice_table, lateReg_invoice_table
from datetime import datetime, timedelta
from django.utils import timezone
import time



# Create your views here.

@login_required
def courseSetup(request):
    if request.method == 'POST':
        form = courseAddForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form_save = form.save(commit=False)
                instructor = form.cleaned_data['instructor']
                title = form.cleaned_data['course']
                code = form.cleaned_data['course_code']
                user = User.objects.all().filter(username=instructor)

                if user:
                    for profile in user:
                        user_id = profile.id
                        course_model.objects.create(user_id=user_id, course=code).DoesNotExist
                        cbt.objects.create(course_title=title, course_code=code).DoesNotExist
                        form_save.save()

                    Course_Model = course_model.objects.all().filter(course=code)

                    if Course_Model:
                        for model_course in Course_Model:
                            course_register.objects.all().filter(course_code=code, course=title).update(course_model_id=model_course.course_id)
                    
                    reg_id = course_register.objects.all().filter(course_code=code)

                    if reg_id:
                        for reg in reg_id:
                            cbt.objects.filter(course_title=title, course_code=code).update(course=reg.reg_id, examiner=user_id)
                    cbt_info = cbt.objects.all().filter(course_title=title, course_code=code)
                    if cbt_info:
                        for cbt_ in cbt_info:
                            questions.objects.create(cbt_id=cbt_.id).DoesNotExist

            messages.success(request, ('Course Added successfully!'))
            return redirect('course_setup')
        else:
            messages.error(request, ('Course fails to be added!'))
            return redirect('course_setup')

    else:
        form = courseAddForm()
        context = {
            'form':form
        }
    return render(request, 'recordApp/course_setup.html', context=context)

@login_required
def displayCourses(request):
    courses = course_register.objects.all()
    return render(request, 'recordApp/view_courses.html', {'courses':courses})

@login_required
def editCourse(request, course_id):
    course = get_object_or_404(course_register, reg_id=course_id)
    if request.method == 'POST':
        form = courseEditForm(request.POST, instance=course)
        if form.is_valid():
            with transaction.atomic():
                form_save = form.save(commit=False)
                instructor = form.cleaned_data['instructor']
                user = User.objects.all().filter(username=instructor)
                if user:
                    for profile in user:
                        form_save.user_id = profile.id
                        form_save.save()
            messages.success(request, (f'{form_save.course_code} successfully updated!'))
            return HttpResponsePermanentRedirect(reverse('course_details', args=(course_id,)))
        else:
            messages.error(request, ('Course fails to update!'))
            return HttpResponsePermanentRedirect(reverse('edit_course', args=(course_id,)))
    else:
        form = courseEditForm(instance=course)
    return render(request, 'recordApp/edit_course.html', {'form':form})

@login_required
def courseDetails(request, course_id):
    course_details = course_register.objects.all().filter(reg_id=course_id)
    return render(request, 'recordApp/course_details.html',{'details':course_details})

@login_required
def deleteCourse(request, course_id):
    reg_course=course_register.objects.all().filter(reg_id=course_id)
    if reg_course:
        for course in reg_course:
            id = course.course
            # course_Model = course_model.
    
    if request.user.is_superuser:
        messages.success(request, ('Course successfully deleted!'))
        return redirect('view_course')
    elif request.user.is_staff:
        messages.success(request, ('Course successfully deleted!'))
        return redirect('course_setup')

@login_required
def cbtReg(request, user_id):
    course_info = course_model.objects.filter(user_id=user_id)
    if course_info:
        for courses in course_info: 
            info = course_register.objects.filter(instructor=courses.user.username)
            context = {
                'all_profile':info
            }
            return render(request, 'recordApp/cbt_reg.html', context=context)

@login_required
def cbtDetails(request, user_id):
    course = get_object_or_404(course_register, reg_id=user_id)
    cbt_id = get_object_or_404(cbt, course_id = user_id)
    if request.method == 'POST':
        reg_form = reg_cbt(request.POST or None, instance=cbt_id)
        course_details_form = course_details(request.POST or None, instance=course)
        if reg_form.is_valid() and course_details_form.is_valid():
            reg_form.save()
            course_details_form.save()
            messages.success(request, ('Successfully Updated!'))
            return HttpResponsePermanentRedirect(reverse('view_questions', args=(cbt_id.course.reg_id,)))
        else:
            messages.error(request, ('Internal Error!'))
            return HttpResponsePermanentRedirect(reverse('test_details', args=(user_id,)))
    
    else:
        reg_form = reg_cbt(instance=cbt_id)
        course_details_form = course_details(instance=course)
        query = questions.objects.all().filter(cbt_id=cbt_id)
        if query:
            for x in query:
                course_title = x.cbt.course_title
                course_id = x.cbt.course_id
                course_code = x.cbt.course_code
                {
                'course_title':course_title,
                'course_id':course_id, 
                'course_code': course_code,}
        return render(request, 'recordApp/cbt_form.html', {
            'reg_form':reg_form,
            'course_details_form':course_details_form,
            'course_id':course_id, 
        })

@login_required
def cbtQuestions(request, user_id):
    cbt_id = get_object_or_404(cbt, course_id = user_id)
    if request.method == 'POST':
        quest_form = question_form(request.POST or None)
        if quest_form.is_valid():
            with transaction.atomic():
                form = quest_form.save(commit=False)
                form.cbt = cbt_id
                form.save()
            messages.success(request, ('Question Successfully Added!'))
            return HttpResponsePermanentRedirect(reverse('test_questions', args=(user_id,)))
        else:
            messages.error(request, ('Internal Error!'))
            return HttpResponsePermanentRedirect(reverse('test_questions', args=(user_id,)))
       
    else:
        quest_form = question_form(request.POST or None)
        quest_agg = questions.objects.all().filter(cbt_id=cbt_id).count
        query = questions.objects.all().filter(cbt_id=cbt_id)
        if query:
            for x in query:
                course_title = x.cbt.course_title
                course_id = x.cbt.course_id
                course_code = x.cbt.course_code
    return render(request, 'recordApp/cbt_questions.html', {
        'questions':quest_form,
        'course_title':course_title,
        'course_id':course_id, 
        'quest_agg':quest_agg,
        'course_code': course_code,
    })

# id_user = ''
@login_required
def viewQuestions(request, user_id):
    user_info = cbt.objects.all().filter(course_id=user_id)
    if user_info:
        for user in user_info:
            id = user.id
            # global id_user
            all_questions = questions.objects.filter(cbt_id=id)
            cbt_query = cbt.objects.filter(id=id)
            if cbt_query:
                for query in cbt_query:
                    course_id = query.course_id
                    # user = course_id
                    print(course_id)
    return render(request, 'recordApp/view_questions.html', {
        'all_questions':all_questions,
        'id':course_id
        })

# id_cbt = ''
@login_required
def editQuestions(request, user_id):
    
    cbt_id = get_object_or_404(questions, id=user_id)
    cbt_data = questions.objects.all().filter(id=user_id)
    # for id in cbt_data:
    #     global id_cbt
    #     id_cbt = id.cbt.id
    #     print(id_cbt)
    if request.method == "POST":
        quest_form = question_form(request.POST or None, instance=cbt_id)
        if quest_form.is_valid():
            with transaction.atomic():
                quest_form.save()
                id = cbt_id.cbt.course.reg_id
                messages.success(request, ('Question Successfully Updated!'))
                return viewQuestions(request, id)

    else:
        quest_form = question_form(instance=cbt_id)
    return render(request, 'recordApp/edit_questions.html', {
        'questions':quest_form,
    })

@login_required
def cbtTest(request, test_id):
    score = 0
    course_= course_form.objects.filter(cbt_id=test_id, user_id=request.user.id)
    if course_:
        for course_info in course_:
            cbt_id = course_info.cbt_id
            unit = course_info.units
            question_data = questions.objects.filter(cbt_id=test_id)

        test_instruction = cbt.objects.only('course_code').get(id=test_id)
        if test_instruction.execution_date:
            _date = test_instruction.execution_date
            target_date_str = _date.strftime("%Y,%m,%d,%H,%M,%S")
            year,month,day,hour,minute,second=target_date_str.split(',')
            target_date = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
            date_now = datetime.now()
            time_remaining = target_date - date_now

        if not grading.objects.filter(active=True, cbt_id=cbt_id, user_id=request.user.id):
            grading.objects.create(active=True, cbt_id=cbt_id, user_id=request.user.id).DoesNotExist

        grading_ = grading.objects.filter(cbt_id=cbt_id, user_id=request.user.id)
        if grading_:
            for grading_info in grading_:
                if grading_info.active is True:
                    executed_time = grading_info.executed_time

        if request.method == 'POST':
            for question in question_data:
                selected_option = request.POST.get(str(question.id))
                if selected_option:
                    option = questions.objects.filter(answer=selected_option)
                    if option:
                        score +=1
            finished_time = time.strftime('%Y-%m-%d %H:%M: %S')
            total_score = ((int(score)/int(test_instruction.no_of_questions))*100)
            if total_score <= 39:
                grade = 'F'
            elif total_score >= 70 and not total_score > 100:
                grade = 'A'
            elif total_score >= 60 and not total_score > 69:
                grade = 'B'
            elif total_score >= 50 and not total_score > 59:
                grade = 'C'
            elif total_score >= 45 and not total_score > 49:
                grade = 'E'
            elif total_score >= 40 and not total_score > 44:
                grade = 'D'
            grading.objects.filter(active=True, cbt_id=cbt_id, user_id=request.user.id).update(score=score, active=False,finished_time=finished_time, submitted=True, unit=unit, total_score=total_score, grade=grade)
            return redirect('available_test', request.user.id)
    return render(request, 'recordApp/cbt_test.html', {
        'question_data':question_data,
        'time_remaining':time_remaining,
        'duration':test_instruction.duration,
        'executed_time':executed_time,
        'score':score
    })

# quest_data=''
# target_date = None
# date_now = None
# test_instruction_ = None
# executed_time = None
# time_remaining = None
# @login_required
# def cbtTest(request, test_id):
#     score = 0
#     course_info = course_form.objects.all().filter(course_id=test_id)
#     if course_info:
#         for course in course_info:
#             cbt_id = course.cbt.id

#             course_form_details = course_form.objects.all().filter(cbt_id=cbt_id)
#             if course_form_details:
#                 for details in course_form_details:
#                     if details.cbt_id:
#                         pass
#             global quest_data
#             question_data  = questions.objects.filter(cbt_id=cbt_id)
#             quest_data = question_data
#             if not grading.objects.filter(active=True, cbt_id=cbt_id, user_id=request.user.id):
#                 grading.objects.create(active=True, cbt_id=cbt_id, user_id=request.user.id).DoesNotExist
            
#             grading_info = grading.objects.all().filter(active=True, cbt_id=cbt_id, user_id=request.user.id)
#             if grading_info:
#                 for grade in grading_info:
#                     global executed_time
#                     executed_time_ = grade.executed_time
#                     executed_time = executed_time_
#             global test_instruction_
#             test_instruction = cbt.objects.only('course_code').get(id=cbt_id)
#             test_instruction_ = test_instruction.duration
#             if test_instruction.execution_date:
#                 _date = test_instruction.execution_date
#                 target_date_str = _date.strftime("%Y,%m,%d,%H,%M,%S")
#                 year,month,day,hour,minute,second=target_date_str.split(',')
#                 global target_date
#                 target_date_ = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
#                 target_date = target_date_
#                 global date_now
#                 date_now_ = datetime.now()
#                 date_now = date_now_
#                 global time_remaining
#                 time_remaining_ = target_date_ - date_now_
#                 time_remaining = time_remaining_
            
#             if request.method == 'POST':
#                 for question in question_data:
#                     selected_option = request.POST.get(str(question.id))
#                     if selected_option:
#                         option = questions.objects.filter(answer=selected_option)
#                         if option:
#                             score +=1
#                 finished_time = time.strftime('%Y-%m-%d %H:%M: %S')
#                 grading.objects.filter(active=True, cbt_id=cbt_id, user_id=request.user.id).update(score=score, active=False,finished_time=finished_time, submitted=True)

#     return render(request, 'recordApp/cbt_test.html', {
#         'question_data':quest_data,
#         'score':score,
#         'target_time':target_date,
#         'date_now':date_now,
#         'duration':test_instruction_,
#         'executed_time':executed_time,
#         # 'days' : f'{time_remaining.days:02}',
#         # 'hrs' : f'{time_remaining.seconds // 3600:02}',
#         # 'mins' : f'{(time_remaining.seconds % 3600) // 60:02}',
#         # 'secs' : f'{time_remaining.seconds % 60:02}',
#     })
            
# @login_required
# def cbtTestsubmit(request, test_id):
#      question_data = questions.objects.filter(cbt_id=cbt_id)
#     if request.method == 'POST':
#             for question in question_data:
#                 selected_option = request.POST.get(str(question.id))
#                 if selected_option:
#                     option = questions.objects.filter(answer=selected_option)
#                     if option:
#                         score +=1
#             finished_time = time.strftime('%Y-%m-%d %H:%M: %S')
#             grading.objects.filter(active=True, cbt_id=cbt_id, user_id=request.user.id).update(score=score, active=False,finished_time=finished_time, submitted=True)
#     return cbtTest(request, test_id)


@login_required
def courseReg(request, user_id):
    late_reg = fees_table.objects.all()
    payment = tuition_invoice_table.objects.filter(user_id=request.user.id, paid=True)
    
    
    if payment:
        if late_reg:
            for reg in late_reg:
                if reg.late_reg_approval is True:
                    inv_id = invoice_table.objects.filter(user_id=user_id, category='late_reg', status='successful', completed=True).exists()
                    if inv_id:
                        request.user.id = user_id
                        all_courses = course_register.objects.all()
                        registered_courses = course_form.objects.all().filter(user_id=user_id)
                        return render(request, 'recordApp/course_form_reg.html', {
                        'all_courses':all_courses,
                        'registered_courses':registered_courses
                    })
                    else:
                        invoice_table.objects.create(user_id=request.user.id).DoesNotExist
                        return redirect('payment_details', request.user.id, 'late_reg')
                
                else:
                    request.user.id = user_id
                    all_courses = course_register.objects.all()
                    registered_courses = course_form.objects.all().filter(user_id=user_id)
                    return render(request, 'recordApp/course_form_reg.html', {
                    'all_courses':all_courses,
                    'registered_courses':registered_courses
                })
    else:
        invoice_table.objects.create(user_id=request.user.id).DoesNotExist
        return redirect('payment_details', request.user.id, 'tuition')

@login_required
def addCourses(request, course_id):
    user_id = request.user.id
    course_info = course_form.objects.filter(course_id=course_id, user_id=user_id)
    if course_info.exists():
        course_info = course_register.objects.filter(reg_id=course_id)
        if course_info:
            for course in course_info:
                print(course.reg_id)
                course_form.objects.all().filter(course_id=course_id, user_id=user_id).update(units=course.unit, status=True)
                cbt_info = cbt.objects.filter(course_id=course_id)
                if cbt_info:
                    for cbt_id in cbt_info:
                        course_form.objects.all().filter(course_id=course_id, user_id=user_id).update(cbt_id=cbt_id)
        # pass
                
    else:
        course_form.objects.create(course_id=course_id, user_id=user_id)
        course_info = course_register.objects.filter(reg_id=course_id)
        if course_info:
            for course in course_info:
                print(course)
                course_form.objects.all().filter(course_id=course_id, user_id=user_id).update(units=course.unit, status=True)
                cbt_info = cbt.objects.filter(course_id=course_id)
                if cbt_info:
                    for cbt_id in cbt_info:
                        course_form.objects.all().filter(course_id=course_id, user_id=user_id).update(cbt_id=cbt_id)

    return courseReg(request, request.user.id)

@login_required
def removeCourses(request, course_id):
    user_id = request.user.id
    course_form.objects.filter(course_id=course_id, user_id=user_id).delete()
    return courseReg(request, request.user.id)

@login_required
def courseForm(request, user_id):
    unit = 0
    request.user.id = user_id
    id = request.user.id
    user = User.objects.all().filter(id=id)
    registered_courses = course_form.objects.all().filter(user_id=user_id)
    if registered_courses:
        reg_course = registered_courses.values()
        for reg in reg_course:
            unit += int(reg.get("units"))
        total_unit = unit
    else:
        total_unit=unit
    return render(request, 'recordApp/course_form.html', {
       'registered_courses':registered_courses,
       'total_unit':total_unit,
       'user_info':user
   })



@login_required
def availableTest(request, user_id):
    request.user.id = user_id
    id = request.user.id
    user = User.objects.all().filter(id=id)
    all_courses = course_register.objects.all()
    registered_courses = course_form.objects.all().filter(user_id=user_id)

    return render(request, 'recordApp/available_test.html', {
        'all_courses':all_courses,
       'registered_courses':registered_courses,
    })

@login_required
def confirmTest(request, test_id):
    user_id = request.user.id
    all_courses = course_register.objects.all()
    registered_courses = course_form.objects.all().filter(user_id=user_id)
    course_info = course_form.objects.all().filter(course_id=test_id, user_id=user_id)
    if course_info:
        for course in course_info:
            cbt_id = course.cbt.id
            grading_data =  grading.objects.filter(cbt_id=cbt_id, user_id=request.user.id, active=False, submitted=True)

    cbt_instruction = cbt.objects.all().filter(id=cbt_id)
    if cbt_instruction:
        for test_instruction in cbt_instruction:
            _date = test_instruction.execution_date
            target_date_str = _date.strftime("%Y,%m,%d,%H,%M,%S")
            year,month,day,hour,minute,second=target_date_str.split(',')
            target_date = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
            date_now = datetime.now()
            time_remaining = target_date - date_now

    return render(request, 'recordApp/test_confirmation.html', {
            'grading':grading_data,
            'test_id':cbt_id,
            'all_courses':course_info,
            'registered_courses':registered_courses,
            'days' : f'{time_remaining.days:02}',
            'hrs' : f'{time_remaining.seconds // 3600:02}',
            'mins' : f'{(time_remaining.seconds % 3600) // 60:02}',
            'secs' : f'{time_remaining.seconds % 60:02}',
            'target_time':target_date,
            'date_now':date_now,
    })

@login_required
def viewResult(request, user_id):
    result = grading.objects.filter(submitted=True, user_id=user_id)
    user_info = User.objects.all().filter(id=user_id)
    unit = 0
    if result:
        reg_course = result.values()
        for reg in reg_course:
            unit += int(reg.get("unit"))
        total_unit = unit
    else:
        total_unit=unit
    return render(request, 'recordApp/result.html', {
        'result_data':result,
        'user_info':user_info,
        'total_unit':total_unit,
    })
