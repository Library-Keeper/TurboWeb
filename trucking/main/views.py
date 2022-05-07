from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def feedback(request):
    return render(request, 'main/feedback.html')
