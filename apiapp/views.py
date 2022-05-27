from django.shortcuts import render
import requests
from . models import APIData
from . import api_test


def index(request):
    x_val = api_test.name_list
    y_val = api_test.home_list
    #print(x_val,y_val)
    for i in range(0,2):
        data = x_val
        dataa = y_val
        return render(request,'index.html',{'data':data,'dataa':dataa})
        
