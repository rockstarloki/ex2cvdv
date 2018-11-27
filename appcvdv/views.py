
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic import View

from .models import Student

class Studentfields(CreateView):
    model = Student
    fields = ["name","clas","sections"]

    template_name = "index.html"

class Save(View):
    def post(self,requrest):
        name = requrest.POST.get("name")
        clas = requrest.POST.get("clas")
        section = requrest.POST.get("sections")

        s = Student(name=name,clas=clas,sections=section)
        s.save()
        return render(requrest,"index.html",{"mes":"data Saved"})

class Showlist(ListView):
    model = Student
    template_name = "list.html"

class DeleteStudent(DeleteView):
    model = Student
    success_url = "/list/"


