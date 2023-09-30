import requests
import json

# def get_file(request):
#     files = request.FILES.get('file', 'null')


#     params = {
#       'models': 'nudity-2.0',
#       'api_user': '139219959',
#       'api_secret': 'WSWs4TDBfXwVD57sA3jr'
#     }

#     files = {'media': open('/full/path/to/image.jpg', 'rb')}
#     r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)

#     output = json.loads(r.text)
    





# this example uses requests
import requests
import json

params = {
  'url': 'https://di1-ph.ypncdn.com/videos/201907/02/232934681/original/(m=eGM68f)(mh=SUz9AXrZbrW4-CwQ)0.jpg',
  'models': 'nudity-2.0',
  'api_user': '139219959',
  'api_secret': 'WSWs4TDBfXwVD57sA3jr'
}
r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)

output = json.loads(r.text)

print(output)