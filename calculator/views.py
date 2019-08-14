from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'calculator/index.html')


def calculator(request):
    c = ''
    if request.method == 'POST':
        a = request.POST.get('n1')
        b = request.POST.get('n2')
        c = int(a) + int(b)
    return render(request, 'calculator/calculator.html', {'result':c})


