from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student

def home(request):
    status = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('home')
    else:
        form = StudentForm()
    # put render outside 'else' block, so user can see the error messages
    return render(request, 'absent/index.html', {'form': form, 'students': Student.objects.all(), 'status': status })

