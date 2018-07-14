from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 as _g

from django.contrib.auth.decorators import user_passes_test
from accounts.views.decorators import user_is_authenticated

from accounts.forms import EditProfileForm
from accounts.models import Profile


@user_passes_test(user_is_authenticated)
def change_first_name(request):

    user = request.user
    first_name = request.POST.get('first_name', '')

    user.first_name = first_name
    user.save()

    return JsonResponse({'first_name': first_name})


@user_passes_test(user_is_authenticated)
def change_last_name(request):

    user = request.user
    last_name = request.POST.get('last_name', '')

    user.last_name = last_name
    user.save()

    return JsonResponse({'last_name': last_name})


@user_passes_test(user_is_authenticated)
def change_email(request):

    user = request.user
    email = request.POST.get('email', '')

    user.email = email
    user.save()

    return JsonResponse({'email': email})


@user_passes_test(user_is_authenticated)
def delete_account(request):

    user = request.user

    user.is_active = False
    user.save()

    return JsonResponse({'is_active': user.is_active})


@user_passes_test(user_is_authenticated)
def edit_profil(request):
    
    context = {}

    user = request.user
    profil = _g(Profile, user=user)
    
    # Valeur initiales du formulaire
    initial = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'avatar': profil.avatar 
    }
    form = EditProfileForm(request.POST or None, initial=initial)
    context['form'] = form

    if form.is_valid():

        datas = form.cleaned_data
        first_name, last_name = datas['first_name'], datas['last_name']
        email, avatar = datas['email'], datas['avatar']

        user.first_name, user.last_name = first_name, last_name
        user.email, profil.avatar = email, avatar

        # On enregistre l'avatar sur le serveur.
        fs = FileSystemStorage()
        avatar = request.FILES['avatar']
        fs.save("users/%s" % avatar.name, avatar)

        user.save()
        profil.save()

        context['success'] = True

        return JsonResponse({"message": "Votre profil a bien été mis à jour"})
    
    return render(request, "edit_profil.html", context)
