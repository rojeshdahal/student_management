from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.objects.all()

    # Handle search
    q = request.GET.get('q')
    if q:
        students = students.filter(name__icontains=q)

    # Calculate stats
    avg_marks = students.aggregate(Avg('marks'))['marks__avg'] or 0
    top_student_obj = students.order_by('-marks').first()
    top_student = top_student_obj.name if top_student_obj else "-"

    form = StudentForm()

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        if student_id:
            # Update existing student
            student = get_object_or_404(Student, id=student_id)
            form = StudentForm(request.POST, instance=student)
        else:
            # Add new student
            form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, "students/index.html", {
        "students": students,
        "form": form,
        "avg_marks": round(avg_marks, 2) if avg_marks else 0,
        "top_student": top_student
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('index')