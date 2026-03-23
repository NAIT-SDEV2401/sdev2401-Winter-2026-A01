from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

# get our current time mixin
from core.mixins import CurrentTimeMixin


class HomePageView(CurrentTimeMixin, TemplateView):
    template_name = "web/home.html"

    # let's say in a template view
    # you wanted to pass a description
    # to the context.
    # this is the same as what you'd pass in
    # render.
    def get_context_data(self, **kwargs):
        # calling get_context_data from the super class.
        context = super().get_context_data(**kwargs)
        breakpoint()
        context["title"] = "Super LMS"
        context["description"] = "Our awesome lms system."
        return context

    # with a template view you no longer need to define
    # a get with no context
    # def get(self, request):
    #     return render(request, self.template_name)
