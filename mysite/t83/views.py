from django.shortcuts import render
from .models import T83

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    list = T83.objects.order_by('t83_num')[:90]
    list01 = T83.objects.order_by('t83_num')[0:5]
    list06 = T83.objects.order_by('t83_num')[5:10]
    list11 = T83.objects.order_by('t83_num')[10:15]
    list16 = T83.objects.order_by('t83_num')[15:20]
    list21 = T83.objects.order_by('t83_num')[20:25]
    list26 = T83.objects.order_by('t83_num')[25:30]
    list31 = T83.objects.order_by('t83_num')[30:35]
    list36 = T83.objects.order_by('t83_num')[35:40]
    list41 = T83.objects.order_by('t83_num')[40:45]
    list46 = T83.objects.order_by('t83_num')[45:50]
    list51 = T83.objects.order_by('t83_num')[50:55]
    list56 = T83.objects.order_by('t83_num')[55:60]
    list61 = T83.objects.order_by('t83_num')[60:64] # 4
    list65 = T83.objects.order_by('t83_num')[64:69]
    list70 = T83.objects.order_by('t83_num')[69:74] # 5
    list75 = T83.objects.order_by('t83_num')[74:79]
    list80 = T83.objects.order_by('t83_num')[79:83]

    context = {'list': list
    ,'list01': list01
    ,'list06': list06
,'list11': list11
,'list16': list16
,'list21': list21
,'list26': list26
,'list31': list31
,'list36': list36
,'list41': list41
,'list46': list46
,'list51': list51
,'list56': list56
,'list61': list61
,'list65': list65
,'list70': list70
,'list75': list75
,'list80': list80


    ,}


    return render(request, 't83/index.html', context)
