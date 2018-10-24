from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "What is broken can be reforge",
                "message": "- Riven"}
        return data
    
class AboutPageView (TemplateView):
    template_name = "resume.html"

class ContactPageView (TemplateView):
    template_name = "contactInfo.html"


