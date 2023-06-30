from django.http import JsonResponse


def root_view(request):
    response = {"status": "ok"}
    return JsonResponse(response, status=200)
