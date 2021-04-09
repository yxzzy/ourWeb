from django.shortcuts import render,redirect
# 第一个页面
def ourIndex(request):
    return render(request,'dashboard.html')
def ourIndex2(request):
    return render(request,'files.html')
def ourIndex3(request):
    return render(request,'activities.html')
# Create your views here.
