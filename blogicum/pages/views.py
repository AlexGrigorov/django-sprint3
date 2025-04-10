from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html')


def rules(request):
    return render(render, 'pages/rules.html')
