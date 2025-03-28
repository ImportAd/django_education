from django.shortcuts import render
from django.views.generic import TemplateView

# from django.http import HttpResponse


# def home_page_view(request):
#     return HttpResponse("Hompage")


def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "8-800-555-35-35"
        return context
