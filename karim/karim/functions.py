from .settings import MEDIA_ROOT

def handle_upload_file(folder, file_name, f):
    
    file = "%s/%s/%s" % (MEDIA_ROOT, folder, file_name)
    with open(file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
