from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from .forms import *
from django.contrib.auth import authenticate,login
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


def first(request):
    return HttpResponse("Welcome to Django World")

def second(request):
    return HttpResponse("my second django page")

def third(request):
    return render(request,'third.html')

def work(request):
    return render(request,'work.html')

def index(request):
    return render(request,'index.html')



def reg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        adress=request.POST.get('address')
        dob=request.POST.get('dob')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            a=registers(First_name=fname,Last_name=lname,user_name=uname,email=email,phone=phone,gender=gender,address=adress,dob=dob,password=password)
            a.save()
            return HttpResponse("registration success")
        else:
            return HttpResponse("password incorrect")

    return render(request,'registration.html')

def emp(request):
    if request.method=='POST':
        ename=request.POST.get('Employee_Name')
        email=request.POST.get('Email_id')
        cname=request.POST.get('Company_Name')
        dsgtn=request.POST.get('Designation')
        phn=request.POST.get('Phone')
        b=register(Employee_Name=ename,Email_id=email,Company_Name=cname,Designation=dsgtn,Phone=phn)
        b.save()
        return HttpResponse("registration success")
    return render(request,'employee.html')

# def login(request):
#     if request.method=='POST':
#         mail=request.POST.get('email')
#         password=request.POST.get('password')
#         c=registers.objects.all()
#         for i in c:
#           if (i.email==mail and i.password==password):
#               return HttpResponse("Login Successfull")
#         else:
#             return HttpResponse("Login Failed")
#     return render(request,'login.html')

def pro(request):
    if request.method=='POST':
        prname=request.POST.get('pname')
        price=request.POST.get('price')
        cmname=request.POST.get('cname')
        quantity=request.POST.get('quantity')
        expdate=request.POST.get('date')
        description=request.POST.get('description')
        d=register(pname=prname,price=price,cname=cmname,quantity=quantity,date=expdate,description=description)
        d.save()
        return HttpResponse("registration success")
    return render(request, 'product.html')


def upload(request):
    if request.method=='POST':
        flname=request.POST.get('filename')
        image=request.FILES.get('fileimage')
        desc=request.POST.get('description')
        z=fileupload(filename=flname,fileimage=image,description=desc)
        return HttpResponse("file upload success")
    return render(request,'upload.html')

def audi(request):
    if request.method=='POST':
        aname=request.POST.get('audioname')
        audio=request.FILES.get('audio')
        vname=request.POST.get('videoname')
        video=request.FILES.get('video')
        pname=request.POST.get('pdfname')
        pdf=request.FILES.get('pdf')
        y=audii(aname=aname,audio=audio,vname=vname,video=video,pname=pname,pdf=pdf)
        y.save()
        return HttpResponse("fileupload success")
    return render(request,'audios.html')

def state(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        state = request.POST.get('state')
        english = request.POST.get('english')
        if english == 'on':
            english = True
        else:
            english = False
        hindi = request.POST.get('hindi')
        if hindi == 'on':
            hindi = True
        else:
            hindi = False
        other = request.POST.get('other')
        if other == 'on':
            other = True
        else:
            other = False

        aa = stat(name=name, state=state, english=english, hindi=hindi, other=other)
        aa.save()
        return HttpResponse('successfully uploaded')
    return render(request, 'state.html')


def display(request):
    a=registers.objects.all()
    return render(request,'display.html',{'data':a})


def filedisplay(request):
    id=[]
    fname=[]
    fileimage=[]
    description=[]
    a1=fileupload.objects.all()
    for i in a1:
        id1=i.id
        id.append(id1)
        name=i.fname
        fname.append(name)
        img=str(i.fileimage).split('/')[-1]
        fileimage.append(img)
        des=i.description
        description.append(des)
    mylist=zip(id,fname,fileimage,description)
    return render(request,'filedisplay.html',{'data':mylist})

def myupload(request):
    id=[]
    aname=[]
    audio=[]
    vname=[]
    video=[]
    pname=[]
    pdf=[]
    a=audii.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        name=i.aname
        aname.append(name)

def update_data(request,id):
    a=registers.objects.get(id=id)
    if request.method=='POST':
        a.First_name=request.POST.get('First_name')
        a.Last_name=request.POST.get('Last_name')
        a.user_name=request.POST.get('user_name')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        # a.gender=request.POST.get('gender')
        if str(request.POST.get('gender'))=='female' or str(request.POST.get('gender'))=='male':
            a.gender=request.POST.get('gender')
        else:
            a.save()
        a.address=request.POST.get('address')
        # a.dob=request.POST.get('dob')
        if len(str(request.POST.get('dob')))>0:
            a.dob=request.POST.get('dob')
        else:
            a.save()
        a.save()
        return redirect(display)
    return render(request,'edit profile.html',{'data':a})

def update_employee(request,id):
    a=register.objects.get(id=id)
    if request.method=='POST':
        a.Employee_Name=request.POST.get('Employee_Name')
        a.Email_id=request.POST.get('Email_id')
        a.Company_Name=request.POST.get('Company_Name')
        a.Designation=request.POST.get('Designation')
        a.Phone=request.POST.get('Phone')
        a.save()
        return redirect(display)
    return render(request,'edit employee.html',{'data':a})

def delete(request,id):
    a=registers.objects.get(id=id)
    a.delete()
    return redirect(display)



# def userregistration(request):
#     if request.method=='POST':
#         a=userreg(request.POST)
#         if a.is_valid():
#             us=request.POST.get('username')
#             em=request.POST.get('email')
#             fname=request.POST.get('first_name')
#             lname=request.POST.get('last_name')
#             password=request.POST.get('password')
#             b=User.objects.create_user(username=us,email=em,first_name=fname,last_name=lname,password=password)
#             b.save()
#             return HttpResponse("authenticated user added")
#         else:
#             return HttpResponse("user not added")
#     else:
#         form=userreg()
#         return render(request,'userregister.html',{'form':form})

def userregistration(request):
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            us=form.cleaned_data['username']
            em=form.cleaned_data['email']
            fname=form.cleaned_data['first_name']
            lname=form.cleaned_data['last_name']
            password=form.cleaned_data['password']
            conf=form.cleaned_data['conf']
            if password==conf:
                b=User(username=us,email=em,first_name=fname,last_name=lname)
                b.set_password(password)
                b.save()
                return HttpResponse('Registered')
            else:
                return HttpResponse('Password does not match')
        else:
            return HttpResponse('Failed')
    else:
        form=userform()
        return render(request,'userregister.html',{'form':form})


def cust_login(request):
    if request.method=='POST':
        form=userlogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('logged successfully.')
            else:
                return HttpResponse('Invalid username or password')
        else:
            return render(request,'Invalid username or password')
    else:

        return render(request,'loginpage.html')

class login1(generic.View):
    form_class=logform
    template_name='login1.html'
    def get(self,request):  # to load the login page
        form=self.form_class  # form name
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        if request.method=='POST':
            a=logform(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=regmodel.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return HttpResponse("Login success!!!")
                else:
                    return HttpResponse("Login failed")
            return HttpResponse("Invalid Credentials")


class userregister(generic.CreateView):
    form_class = userreg
    template_name = 'user register.html'
    success_url = reverse_lazy('login1')

class loginnew1(generic.View):
    form_class=logform
    template_name='log.html'
    def get(self,request):          #to load loginpage
        form=self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        if request.method=='POST':
            a=logform1(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=User.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return HttpResponse('logged')
                else:
                    return HttpResponse('FAILED')

            return HttpResponse('INVALID')


class userregister(generic.CreateView):
    form_class = userreg
    template_name = 'user register.html'
    success_url = reverse_lazy('login1')
    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        if request.method=='POST':
            form=userreg(request.POST)
            if form.is_valid():
                us=form.cleaned_data['username']
                fn = form.cleaned_data['first_name']
                ln = form.cleaned_data['last_name']
                em = form.cleaned_data['email']
                ps = form.cleaned_data['password']
                cps = form.cleaned_data['conf']

                if ps==cps:
                    user = User(username=us, first_name=fn, last_name=ln, email=em)
                    user.set_password(ps)
                    user.save()
                    return HttpResponse('register')
                else:
                    return HttpResponse("password does not match")
            else:
                return HttpResponse("failed")



class user_login(generic.View):
    form_class=u_login
    template_name='login1.html'

    def get(self,requset):
        form=self.form_class
        return render(requset,self.template_name,{'form':form})

    def post(self,requset):
        if requset.method=='POST':
            form=u_login(requset.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(requset, username=username, password=password)

                if user is not None:
                    # login(request, user)
                    return HttpResponse('logged in successfully')
                else:
                    return HttpResponse('Invalid username or password')
            else:
                return HttpResponse('Invalid username or password')



class UserListView(generic.ListView):
    model = regmodel
    template_name = 'disp.html'
    context_object_name = 'user_list'


class re(generic.DeleteView):
    model=regmodel
    template_name='delete.html'
    success_url=reverse_lazy('disp')

class up(generic.UpdateView):
    model=regmodel
    template_name='update.html'
    fields=['name','email']
    success_url=reverse_lazy('disp')


class detail(generic.DetailView):
    model=regmodel # your model name
    template_name='detail.html'


class image_upload(generic.CreateView):
    form_class = imageform
    template_name = 'image_upload.html'
    success_url = reverse_lazy('imagedisplay')



class image_list(generic.ListView):
    model = imageupload
    template_name = 'image_display.html'
    context_object_name = 'img'

    def get(self,request):
        a=self.model.objects.all()
        return render(request,self.template_name,{'img':a})

       # return filemodel.objects.values('id','image','itemname')          # get_queryset- which is used by ListView, it determines the list of objects that you want to display.



    # filemodel.objects.value to get the values of the particular fields.

class image_delete(generic.DeleteView):
    model=imageupload
    template_name='delete_image.html'
    success_url=reverse_lazy('imagedisplay')

class image_detail(generic.DetailView):
    model=imageupload
    template_name='image_details.html'
    fields = ['item_name', 'image']


class image_update(generic.UpdateView):
    model=imageupload
    template_name='image_update.html'
    fields=['item_name','image']
    success_url=reverse_lazy('imagedisplay')

class fileclass(generic.CreateView):
    form_class=filesupload
    template_name = 'fileupload.html'
    success_url = reverse_lazy('display_file')


class display_file(generic.ListView):
    model=fileuploads_model
    template_name='display_files.html'
    context_object_name = 'file'

class deletefile(generic.DeleteView):
    model = fileuploads_model
    template_name = 'filedelete.html'
    success_url=reverse_lazy('display_file')

class detailfile(generic.DetailView):
    model = fileuploads_model
    template_name = 'file_detail.html'

class updatefile(generic.UpdateView):
    model = fileuploads_model
    template_name = 'file_update.html'
    fields = '__all__'
    success_url = reverse_lazy('display_file')


