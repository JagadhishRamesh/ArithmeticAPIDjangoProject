from django.http import JsonResponse

def arithmetic_view(request):
    A = int(request.GET.get('A'))
    B = int(request.GET.get('B'))
    add = A + B
    diff = A - B
    product = A * B
    if B == 0:
        quotient = "undefined"
    else:
        quotient = A / B
    data = {
        "sum": add,
        "difference": diff,
        "product": product,
        "quotient": quotient
    }
    return JsonResponse(data)