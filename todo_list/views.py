from django.shortcuts import render, redirect
from .models import list
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):

    if(request.method == 'POST'):
        form = ListForm(request.POST or None)

        if(form.is_valid()):
            form.save()
            all_items = list.objects.all

            Context = { "all_items": all_items}

            messages.success(request, ('item has been added to list!'))

            return render(request, 'home.html', Context)

    else:
        all_items = list.objects.all

        Context = { "all_items": all_items}

        return render(request, 'home.html', Context)



def about(request):


    Context = {'first_name' : 'M', 'last_name' : 'e'}


    return render(request, 'about.html', Context)



def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()

    messages.success(request, ('item has been Deleted!'))

    return redirect('home')

def cross_off(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = True
    item.save()

    return redirect('home')


def uncross(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()

    return redirect('home')

def edit(request, list_id):

    if(request.method == 'POST'):
        item = list.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if(form.is_valid()):
            form.save()

            messages.success(request, ('item has been Edited!'))

            return redirect('home')

    else:
        item = list.objects.get(pk=list_id)

        Context = { "item": item}

        return render(request, 'edit.html', Context)
