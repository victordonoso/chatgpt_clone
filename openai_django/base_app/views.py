from django.shortcuts import render
from django.http import JsonResponse
from .oai_queries import get_completion

def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    return render(request, 'query.html')
