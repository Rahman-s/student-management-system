from django.shortcuts import render,redirect
from students.models import Students 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# for create
def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_list')

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_student(request):

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        course = request.POST.get('course')

        Students.objects.create(
            name=name,
            age=age,
            course=course
        )

        return redirect('student_list')

    return render(request, 'add_student.html')

# for read
@login_required
def student_list(request):

    search_query = request.GET.get('search')

    if search_query:
        students = Students.objects.filter(name__icontains=search_query)
    else:
        students = Students.objects.all()

    paginator = Paginator(students, 5)  # 5 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'student_list.html',{
        'page_obj': page_obj,
        'search_query': search_query
    })


# for update
def update_student(request,id):
    student = Students.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()

        return redirect('student_list')

    return render(request,'update_student.html',{'student':student})

# for delete
def delete_student(request,id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect('student_list')
# Create your views here.
