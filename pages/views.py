from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    context = {
        'name': 'AIDREN FEROSE PASCUA',
        'student_id': '2023-05561',
    }
    return render(request, 'about.html', context)
