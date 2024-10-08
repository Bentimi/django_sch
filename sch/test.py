# import random
# sample = random.randint(10000, 99999)
# print(f'22{sample}')

# import time
# tt = time.strftime('%y',)
# print(tt)

# print(time.gmtime())

# print('Hello!')

# import hashlib
# import os

# salt = input('Enter password: ')
# password = salt.encode('utf-8')
# # salt  = os.urandom(16)


# hashed_password = hashlib.sha256(password).hexdigest()

# unhashed_password = hashlib.sha256(password).hexdigest()

# print(f'''
#         Salt: {salt}
#         Password: {password}
#         SHA-256 Hashed password: {hashed_password}
# ''')

# if hashed_password == salt:
#     print("Logged In")
# else:
#     print('error')


# import bcrypt

# pwd = input('password: ')
# password = pwd.encode('utf-8')

# hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# print(f'Hashed Password: {hashed_password}')

# login = input('Password: ')
# login_pwd = login.encode('utf-8')

# if bcrypt.checkpw(login_pwd, hashed_password):
#     print('Correct!')
# else:
#     print('Error!')


username = 'Bennie'
first_name = 'Benjamin'
last_name = 'Ogunkunle'
cont = (username, first_name, last_name)
if username!='' and first_name!='' and last_name!='':
    print(cont)
else:
    print('Invalid!')


"""
def admissionReg(request):
    

    if request.method == "POST":
        form = registrationForm(request.POST)
        student = request.POST['is_registered']
        # confirmation_form = confirmationForm(request.POST)

        # if form.is_valid() and student is True:
            # reg = form.save(commit=False)
            # form_id = form.id
            # users_status.objects.filter(user_id = form_id).update(student=True)
            # reg.save()
            # status.save()
            # confirmation_form.save()
            # confirmation = confirmation_form.save(commit=False)
            # confirmation.student = True
            # confirmation.save()
                # student_confirmation = con
                # student_confirmation.save()
        if form.is_valid() and (student == True):
            form_id = form.id
            users_status.objects.filter(user_id = form_id).update(student=True)
            form.save()
            messages.success(request, ('Candidate Successfully Registered!'))
            return redirect('admission_login')
        else:
            messages.error(request, ('please correct the error below.'))
            return redirect('admission_reg')
    else:
        form = registrationForm()
        # confirmation_form = confirmationForm()
        context = {
            'reg_form':form,
            # 'confirmation' : confirmation_form
        }
        return render(request, 'admissionApp/registration.html', context=context)
"""