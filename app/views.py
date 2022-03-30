from django.shortcuts import render
import requests
import json
from requests.auth import HTTPBasicAuth
import base64


# Create your views here.


def index(request):
    response = requests.get('http://93.171.223.226/users', auth=HTTPBasicAuth('test', 'test'), headers={"Accept": "application/json"})

    #print(response.json())
    if request.method == 'POST':
        r = requests.post("http://93.171.223.226/users", auth=HTTPBasicAuth('test', 'test'), json=request.POST)
        #print(r.content)
    return render(request, 'index.html',{'datas':response.json()})

def delete(request, id):
    response = requests.delete(f'http://93.171.223.226/users/{id}', auth=HTTPBasicAuth('test', 'test'))
    print(response.content)
    response = requests.get('http://93.171.223.226/users', auth=HTTPBasicAuth('test', 'test'))
    return render(request, 'index.html',{'datas':response.json()})
