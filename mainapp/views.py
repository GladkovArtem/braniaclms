#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'