from django.shortcuts import render

# Create your views here.
def registration_low(request):
    html = "registration-low.html"
    return render(request, html, {})

def registration_medium(request):
    html = "registration-medium.html"
    return render(request, html, {})

def registration_high(request):
    html = "registration-high.html"
    return render(request, html, {})
def registration_mixed(request):
    html = "registration-mixed.html"
    return render(request, html, {})
def preference_panel(request):
    html = "preference-panel.html"
    return render(request, html, {})
