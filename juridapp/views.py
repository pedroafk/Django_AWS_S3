from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForms

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForms

def create_student(request):
    if request.method == 'POST':
        form = StudentForms(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', id=student.id)
    else:
        form = StudentForms()
    return render(request, 'students/form.html', {'form': form})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/detail.html', {'student': student})
