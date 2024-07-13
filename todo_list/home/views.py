# Create your views here.
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

from home.models import Task


def home(request):
    # context = {'success' = False}
    if request.method == "POST":

        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        # context =  { 'success' = True}
    return render(request ,'index.html' )
    
def tasks(request):
    allTasks =  Task.objects.all()
    print(allTasks)
    for item in allTasks:
        print(item.taskTitle)
    context = {'tasks':allTasks}
    return render(request ,'tasks.html',context)

def delete_row(request, row_id):
    row = get_object_or_404(Task, id=row_id)
    row.delete()
    return redirect('table')