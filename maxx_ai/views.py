import os
from django.shortcuts import render
import requests
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from nudenet import Classifier
import urllib.request
from maxx_ai import connections

def home(request):
    return render(request, "home2.html", {})


def upload_view(request):
    return render(request, "index.html", {})

# def get_file(request):
#     pass
#     response = requests.get("http://192.168.100.42:8000/api/v1/tasks").json()
#     myurl = requests.get(response)
#     print(myurl.status_code)
#     api = [item.get("urls") for item in response]
#     for url in api:
#         print(url)
#         classifier = Classifier()
#         directory, filename = os.path.split(url)
#         print(filename)
#         file_path = os.path.join("media", filename)  # File path within the "media" folder
#         urllib.request.urlretrieve(url, file_path)
#         path = "C:/Users/Asus/Desktop/code/Python/maxx_ai/media/"
#         images_preds = classifier.classify([path + filename], batch_size= 4)
#         for images_pred, value in images_preds.items():
#             safe = value.get('safe')
#             unsafe = value.get('unsafe')
#             if(safe>unsafe):
#                 print("Good to go")
#             else:
#                 print("Ohhh Shit!!")
#     return HttpResponse("File processed successfully!" )


def get_file(request):
    result_list = []  # List to store the filename and result
    pass
    response = requests.get("http://192.168.100.42:8000/api/v1/tasks").json()
    api_urls = [item.get("urls") for item in response]
    print(api_urls)
    for api in api_urls:

        classifier = Classifier()
        data = request.FILES.get('file')
        directory, filename = os.path.split(api)
        file_path = os.path.join("media", filename)  # File path within the "media" folder
        print(filename)
        urllib.request.urlretrieve(api, file_path)
        print(os.listdir())
        data = str(data)
        path = "C:/Users/Asus/Desktop/code/Python/maxx_ai/media/"
        images_preds = classifier.classify(path + filename)
        classifier.classify([path + filename], batch_size= 4)
        for images_pred, value in images_preds.items():
            safe = value.get('safe')
            unsafe = value.get('unsafe')
            if(safe>unsafe):
                print("Good to go")
                result = 1
            else:
                print("Ohhh Shit!!")
                result = 0
            result_list.append((filename, result))  # Append the filename and result as a tuple
    connections.process_results(result_list)
    return HttpResponse("File processed successfully!")



