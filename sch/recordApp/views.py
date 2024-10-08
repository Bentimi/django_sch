from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from recordApp.forms import courseAddForm, courseEditForm, reg_cbt, course_details
from .models import User
from recordApp.models import course_register, course_model, cbt, 


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
            return HttpResponsePermanentRedirect(reverse('test_details', args=(user_id,)))
        else:
            messages.error(request, ('Internal Error!'))
            return HttpResponsePermanentRedirect(reverse('test_details', args=(user_id,)))
    
    else:
        reg_form = reg_cbt(instance=cbt_id)
        course_details_form = course_details(instance=course)

        return render(request, 'recordApp/cbt_form.html', {
            'reg_form':reg_form,
            'course_details_form':course_details_form
        })

@login_required
def cbtQuestions(request, user_id):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'recordApp/cbt_questions.html')