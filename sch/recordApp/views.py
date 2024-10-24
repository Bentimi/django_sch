from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponse
from recordApp.forms import courseAddForm, courseEditForm, reg_cbt, course_details, question_form, test_form
from .models import User
from recordApp.models import course_register, course_model, cbt, questions, course_form
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template



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
    print(f'Test ID: {test_id}')
    score = 0
    course_info =  course_form.objects.all().filter(course_id=test_id)
    if course_info:
        for course in course_info:
            print(course.cbt.id)
            cbt_id = course.cbt.id
            course_form_details = course_form.objects.all().filter(cbt_id=cbt_id)
            if course_form_details:
                for details in course_form_details:
                    print(details.cbt_id)
                    if details.cbt_id:
                        listing = 0
                        question_data = questions.objects.filter(cbt_id=details.cbt_id)
                        listing +=1
                        if request.method == 'POST':
                            for question in question_data:
                                selected_option = request.POST.get(str(question.id))
                                if selected_option:
                                    option = questions.objects.filter(answer=selected_option)
                                    if option:
                                        score +=1


                        return render(request, 'recordApp/cbt_test.html',
                                    {
                                        'question_data':question_data,
                                        'score':score,
                                        'listing':listing
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

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('Error rendering PDF', status=500)
#     return response

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
    return render(request, 'recordApp/course_form.html', {
       'registered_courses':registered_courses,
       'total_unit':total_unit,
       'user_info':user
   })



@login_required
def avaliableTest(request, user_id):
    request.user.id = user_id
    id = request.user.id
    user = User.objects.all().filter(id=id)
    all_courses = course_register.objects.all()
    registered_courses = course_form.objects.all().filter(user_id=user_id)

    return render(request, 'recordApp/available_test.html', {
        'all_courses':all_courses,
       'registered_courses':registered_courses,
    })