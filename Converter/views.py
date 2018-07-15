from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'Converter/index.min.html', context={'lenResult': '', 'wgtResult':'', 'volResult':'', 'curResult':''})

def convLength(request):
    if(request.method == 'POST'):
        src = request.POST['src']
        dest = request.POST['dest']
        num = request.POST['val']
        num = float(num)
        res = num
        if(src == 'src-feet' and dest == 'dest-feet'):
            res = num
        if(src == 'src-feet' and dest == 'dest-inch'):
            res = num*12
        if(src == 'src-feet' and dest == 'dest-metre'):
            res = num/3.3
        if(src == 'src-inch' and dest == 'dest-feet'):
            res = num/12
        if(src == 'src-inch' and dest == 'dest-inch'):
            res = num
        if(src == 'src-inch' and dest == 'dest-metre'):
            res = num*0.0254
        if(src == 'src-metre' and dest == 'dest-feet'):
            res = num*3.3
        if(src == 'src-metre' and dest == 'dest-inch'):
            res = num*39.37
        if(src == 'src-metre' and dest == 'dest-metre'):
            res = num
        return JsonResponse({'res': res})

def convWeight(request):
    if(request.method == 'POST'):
        src = request.POST['src']
        dest = request.POST['dest']
        num = request.POST['val']
        num = float(num)
        res = num
        if(src == 'src-pound' and dest == 'dest-pound'):
            res = num
        if(src == 'src-pound' and dest == 'dest-kg'):
            res = num*0.4535
        if(src == 'src-kg' and dest == 'dest-pound'):
            res = num*2.204
        if(src == 'src-kg' and dest == 'dest-kg'):
            res = num
        return JsonResponse({'res': res})

def convVolume(request):
    if(request.method == 'POST'):
        src = request.POST['src']
        dest = request.POST['dest']
        num = request.POST['val']
        num = float(num)
        res = num
        if(src == 'src-cuMt' and dest == 'dest-cuMt'):
            res = num
        if(src == 'src-cuMt' and dest == 'dest-l'):
            res = num*1000
        if(src == 'src-l' and dest == 'dest-cuMt'):
            res = num/1000
        if(src == 'src-l' and dest == 'dest-l'):
            res = num
        return JsonResponse({'res': res})

def convCurrency(request):
    if(request.method == 'POST'):
        src = request.POST['src']
        dest = request.POST['dest']
        num = request.POST['val']
        num = float(num)
        res = num
        if(src == 'src-dollar' and dest == 'dest-dollar'):
            res = num
        if(src == 'src-dollar' and dest == 'dest-rupee'):
            res = num*67.659
        if(src == 'src-rupee' and dest == 'dest-dollar'):
            res = num/67.659
        if(src == 'src-rupee' and dest == 'dest-rupee'):
            res = num
        return JsonResponse({'res': res})
