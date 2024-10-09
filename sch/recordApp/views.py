from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from recordApp.forms import courseAddForm, courseEditForm, reg_cbt, course_details, question_form, test_form
from .models import User
from recordApp.models import course_register, course_model, cbt, questions, course_form


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
                        course_model.objects.create(user_id=user_id).DoesNotExist
                        form_save.course_model_id = user_id
                        form_save.save()
                        cbt.objects.create(course_title=title, course_code=code).DoesNotExist
                        reg_id = course_register.objects.all().filter(course_code=code)
                        if reg_id:
                            for reg in reg_id:
                                cbt.objects.all().filter(course_title=title, course_code=code).update(course=reg.reg_id, examiner=user_id)
                        
            messages.success(request, ('Course Added successfully!'))
            return redirect('course_setup')
        else:
            messages.error(request, ('Course fails to be added!'))
            return redirect('course_setup')

            # return HttpResponsePermanentRedirect(reverse('product_details', args=(prod_id,)))
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
    course_register.objects.all().filter(reg_id=course_id).delete()
    if request.user.is_superuser:
        messages.success(request, ('Course successfully deleted!'))
        return redirect('view_course')
    elif request.user.is_staff:
        messages.success(request, ('Course successfully deleted!'))
        return redirect('course_setup')

@login_required
def cbtReg(request, user_id):
    info = course_register.objects.all().filter(course_model_id=user_id)
    # user = course_model.objects.all().filter(course_id=user)
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
id_user = ''
@login_required
def viewQuestions(request, user_id):
    user_info = cbt.objects.all().filter(course_id=user_id)
    if user_info:
        for user in user_info:
            id = user.id
            global id_user
            all_questions = questions.objects.filter(cbt_id=id)
            cbt_query = cbt.objects.filter(id=id)
            if cbt_query:
                for query in cbt_query:
                    course_id = query.course_id
                    id_user = course_id
                    print(course_id)
    return render(request, 'recordApp/view_questions.html', {
        'all_questions':all_questions,
        'id':course_id
        })
id_cbt = ''
@login_required
def editQuestions(request, user_id):
    
    cbt_id = get_object_or_404(questions, id=user_id)
    cbt_data = questions.objects.all().filter(id=user_id)
    for id in cbt_data:
        global id_cbt
        id_cbt = id.cbt.id
        print(id_cbt)
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
def cbtTest(request):
     
     print(f'Hey: {str(id_cbt)}')
     print('hello')
     quest_id = questions.objects.filter(cbt_id=5)
     if request.method == 'POST':
         form = test_form(request.POST or None)
         question_data = questions.objects.all().filter(cbt_id=5)
        #  options = request.POST['options']
         if form.is_valid():
            user_answer = form.cleaned_data['answer']
            if question_data:
                for quest in question_data:
                    answer = quest.answer
                    if user_answer == answer:
                        print(f'+1 {user_answer}')
                    else:
                        print(f'+0 {user_answer}')

     else:
         
        form = test_form(request.POST)
        question_data = questions.objects.all().filter(cbt_id=5)
         
       
     return render(request, 'recordApp/cbt_test.html', {
         'form':form,
         'question_data':question_data,
         'cbt_no':id_cbt
         })

@login_required
def courseReg(request, user_id):
    request.user.id = user_id
    all_courses = course_register.objects.all()
    registered_courses = course_form.objects.all().filter(user_id=user_id)
    return render(request, 'recordApp/course_form_reg.html', {
       'all_courses':all_courses,
       'registered_courses':registered_courses
   })

@login_required
def addCourses(request, course_id):
    user_id = request.user.id
    course_info = course_form.objects.filter(course_id=course_id, user_id=user_id)
    if course_info.exists():
        pass
    else:
        course_form.objects.create(course_id=course_id, user_id=user_id)

    return courseReg(request, request.user.id)

@login_required
def removeCourses(request, course_id):
    user_id = request.user.id
    course_form.objects.filter(course_id=course_id, user_id=user_id).delete()
    return courseReg(request, request.user.id)

unit = 0
@login_required
def courseForm(request, user_id):
    request.user.id = user_id
    all_courses = course_register.objects.all()
    registered_courses = course_form.objects.all().filter(user_id=user_id)
    if registered_courses:
        reg_course = registered_courses.values()
        for reg in reg_course:
            unit = reg.get("course")
        total_unit = unit
    return render(request, 'recordApp/course_form.html', {
       'all_courses':all_courses,
       'registered_courses':registered_courses,
       'total_unit':total_unit
   })
