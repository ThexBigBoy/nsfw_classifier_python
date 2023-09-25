
import os
from django.shortcuts import redirect, render
from maxx_ai import settings
from maxx_ai.models import UploadedFile
from maxx_ai.forms import FileUploadForm
from django.shortcuts import render


def home(request):
    return render(request, "home2.html", {})


def upload_view(request):
    return render(request, "index.html", {})
    
# def upload_view(request):
#     if request.user.is_authenticated:
#         return render(request, "TikTok/upload.html", {})
#     else:
#         return redirect('home')
        




def upload_file(request):
    if request.method == 'POST':
        form = UploadedFile()
        form.desc = request.POST['desc']
        form.file = request.FILES.get('file', 'null')
        if form is not None:
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    current_user = request.user
    context = {"name": current_user }
    return render(request, 'maxx_ai/home2.html', {'form': form}, context)






def nsfw_detect_view(request):
    return render(request, 'nsfw_detection/upload.html', {})

def nsfw_detect(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            image_path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(image_path, 'wb') as f:
                f.write(image.read())

            nsfw_score, sfw_score = detect_nsfw(image_path)
            os.remove(image_path)  # Remove the uploaded image

            context = {
                'nsfw_score': nsfw_score,
                'sfw_score': sfw_score
            }
            return render(request, 'nsfw_detection/result.html', context)
    return render(request, 'nsfw_detection/detect.html')



