import os
from django.shortcuts import render
import requests
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from nudenet import Classifier
import urllib.request


import json
from flask import Flask, jsonify, request
app = Flask(__name__)

from maxx_ai import connections


def home(request):
    return render(request, "home2.html", {})
def upload_view(request):
    return render(request, "index.html", {})


def get_file(request):
    result_list = []
    # test = [
    # { 'urls': 'C:/Users/Asus/Desktop/IMG/Capture.PNG'},
    # { 'urls': 'C:/Users/Asus/Desktop/IMG/IMG_4729.JPEG'},
    # { 'urls': 'C:/Users/Asus/Desktop/IMG/306124018_492664422321467_4280235543073674243_n.jpg'}
    # ]
    # print(test)
    pass
    # response = test
    # response = requests.get("http://192.168.100.42:8000/api/v1/tasks").json()



    response = requests.get("https://api.slingacademy.com/v1/sample-data/photos").json()
    # response_dict = json.loads(response)
    photos_array = response["photos"]
    api_urls = [photo["url"] for photo in photos_array]
    # api_urls = [item.get("url") for item in response]
    # print(api_urls)
    for api in api_urls:
        classifier = Classifier()
        directory, filename = os.path.split(api)
        file_path = os.path.join("media", filename)
        urllib.request.urlretrieve(api, file_path)
        path = "C:/Users/Asus/Desktop/code/Python/maxx_ai/media/"
        images_preds = classifier.classify(path + filename)
        classifier.classify([path + filename], batch_size= 4)
        for images_pred, value in images_preds.items():
            safe = value.get('safe')
            unsafe = value.get('unsafe')
            if(safe>unsafe):
                # print("Good to go")
                result = "safe"
            else:
                # print("Ohhh Shit!!")
                result = "not_safe"
            result_list.append((filename, result))
    connections.process_results(result_list)
    # print(result_list)
    # res = result_list
    # return res
    # return HttpResponse(res)    
    return HttpResponse("File processed successfully!")



