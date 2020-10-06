from django.shortcuts import render
def index(request):
    return render(request,"index.html")
# Create your views here.
def form_submit(request):
    print("got Post Info......")
    print(request.POST)
    name = request.POST['name']
    location = request.POST['location']
    stack = request.POST['stack']
    student = request.POST['student']
    comment = request.POST['comment']
    user_list = {
        "name_on_template": name,
        "location_on_template":location,
        "stack_on_template":stack,
        "student_on_template":student,
        "comment_on_template":comment,
    }
    return render(request,"result.html",user_list)