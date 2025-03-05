from django.shortcuts import render
from django.views import generic
from .models import About
# Create your views here.

def about_me(request):
    """
    Display an individual :model:`about.AboutMe`.

    **Context**

    ``about``
        An instance of :model:`about.AboutMe`.

    **Template:**

    :template:`about/about_me.html`
    """

    about = About.objects.all().order_by("updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
   )
