from django.shortcuts import render

def error_400(request, exception):
    return render(request, "blog/errors/400.html")

def error_403(request, exception):
    return render(request, "blog/errors/403.html")

def error_404(request, exception):
    return render(request, "blog/errors/404.html")

def error_500(request, exception):
    return render(request, "blog/errors/500.html")


