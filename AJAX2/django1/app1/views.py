from django.http import JsonResponse
from django.shortcuts import render
from app1.forms import inputform
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def perm3(s3):
    list3=[]
    c1=s3[0:1]
    c2=s3[1:2]
    c3=s3[2:3]
    list3.append(c1+c2+c3)
    list3.append(c1+c3+c2)
    list3.append(c2+c1+c3)
    list3.append(c2+c3+c1)
    list3.append(c3+c1+c2)
    list3.append(c3+c2+c1)
    return list3

def perm4(s4):
    c1=s4[0:1]
    c2=s4[1:2]
    c3=s4[2:3]
    c4=s4[3:4]
    list4=[]
    part1=c1
    part2=c2+c3+c4
    info1=perm3(part2)
    for i in range(0,len(info1)):
        list4.append(part1+info1[i])
    part1=c2
    part2=c1+c3+c4
    info1=perm3(part2)
    for i in range(0,len(info1)):
        list4.append(part1+info1[i])

    part1=c3
    part2=c1+c2+c4
    info1=perm3(part2)
    for i in range(0,len(info1)):
        list4.append(part1+info1[i])
    part1=c4
    part2=c1+c2+c3
    info1=perm3(part2)
    for i in range(0,len(info1)):
        list4.append(part1+info1[i])
    return list4

def home(request):
    form1 = inputform()
    return render(request,'app1/index.html',{'form':form1})

def api1(request):
    result1=[]
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            in1=data.get("input")
            len1=len(in1)
            if len1==3:
                result1=perm3(in1)
            if len1==4:
                result1=perm4(in1)
            return JsonResponse({'param1':result1})
    else:
        return JsonResponse({'Error':'Form Invalid'})

@csrf_exempt
def api2(request):
    if request.method=="POST":
        return JsonResponse({"status":"API Working"})