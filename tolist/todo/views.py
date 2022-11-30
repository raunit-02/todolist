from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def todolist(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    form = TodoForm()
    page = {
        'forms': form,
        "list": item_list,
        'title': "TO DO LIST",
    }
    return render(request, 'todolist.html', page)
    
@login_required(login_url='/login')
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed")
    return redirect('todolist')
