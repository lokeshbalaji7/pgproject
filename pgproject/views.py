from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,User
from .forms import PgModelform,ImageForm,RegisterForm,registeruser,RegisterUser
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import PG,PGImage,Registrations
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from .decorators import checkGroup,checkGroup1

# Create your views here.
def HomePage(request):
    return render(request,'pgapp/home.html')


def SignupPage(request):
    emptyForm =  RegisterUser()
    if request.method == 'POST':
        dataForm =  RegisterUser(request.POST)
        if dataForm.is_valid():
            user = dataForm.save()
            return redirect('login')
        else:
            return render(request, 'pgapp/signup.html', {'form': dataForm})
    return render(request, 'pgapp/signup.html', {'form': emptyForm})

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'pgapp/login.html')
    
def LogoutPage(request):
    logout(request)
    return redirect('login')

def ImageModelForm(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect after successful form submission
            return redirect('home')  
    else:
        form = ImageForm()
    return render(request, 'pgapp/imageform.html', {'form': form})


def modelform(request):
    if request.method == 'POST':
        form = PgModelform(request.POST)
        if form.is_valid():
            form.save()
            # Redirect after successful form submission
            return redirect('home')  
    else:
        form = PgModelform()
    return render(request, 'pgapp/modelform.html', {'form': form})



@login_required
def Showdata(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        # Filter PG data based on the search location
        # data=PG.objects.all()
        pg_data = PG.objects.filter(Address__icontains=search)
        pgimage_data = PGImage.objects.filter(PG_code__in=pg_data)
        return render(request, 'pgapp/show.html', {'pg_data': pg_data, 'pgimage_data': pgimage_data, 'search': search})
    else:
        pg_data = PG.objects.all()
        pgimage_data = PGImage.objects.all()
        return render(request, 'pgapp/show.html', {'pg_data': pg_data, 'pgimage_data': pgimage_data})

@login_required(login_url='login')
def complete(request,eno):
    s=PGImage.objects.get(id=eno)
    return render(request,'pgapp/complete.html',{'data':s})
    
@login_required(login_url='login')
def userregister(request,eno):
    obj = PGImage.objects.get(id=eno)
    vac=obj.vacancies
    if vac>0:
        if request.method == 'POST':
            name = request.POST['name']
            if name:  
                email = request.POST['email']
                mobile = request.POST['mobile']
                obj = PGImage.objects.get(id=eno)
                id = obj.PG_code.PG_Code
                share = obj.Sharing
                price = obj.price
                vcan=vac-1
                obj.vacancies=vcan
                obj.save()
                Registrations.objects.create(Registration_id=id,Full_name=name,Email=email,Mobile_number=mobile)
                return redirect('showdata')
            else:
                return redirect('showdata')
    else:
        return redirect('showdata')
    return render(request,'pgapp/register.html',{'obj':obj})

@checkGroup1
def showusers(request):
    data =Registrations.objects.all()
    #pg_name= PG.objects.all()

    return render(request,'pgapp/showuser.html',{'data':data})

def deleteData(request, eno):
    try:
        obj = get_object_or_404(Registrations, id=eno)
        code = obj.Registration_id
        sha = obj.sharing_person
        obj.delete()
        
        data = PGImage.objects.filter(PG_code=code)
        
        for i in data:
            if i.Sharing == sha:
                i.vacancies += 1
                i.save()
        
        return redirect('showusersurl')
    except:
        # Handle exceptions or return a proper response
        return HttpResponse("Error occurred. Object not found or other issue.")

def pglogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        validuser = authenticate(request, username=uname,password=pwd)
        if validuser != None:
            login(request,validuser)
            request.session['username'] = uname
            return redirect('showusersurl')
        else:
            return redirect('pgloginurl')
    return render(request,'pgapp/pglogin.html')


def pgsignuppage(request):
    emptyForm = registeruser()
    emptyForm1 = Group.objects.all()
    
    if request.method == 'POST':
        dataForm = registeruser(request.POST)
        if dataForm.is_valid():
            user = dataForm.save()
            group_id = request.POST.get('group')
            group = Group.objects.get(pk=group_id)
            user.groups.add(group)
            request.session['username'] = user.username
            print(user.username)
            return redirect('pgloginurl')
        else:
            return render(request, 'pgapp/pgsignup.html', {'form': emptyForm})
    return render(request, 'pgapp/pgsignup.html', {'form': emptyForm, 'form1': emptyForm1})


def pglogout(request):
    logout(request)
    return redirect('pgloginurl')
