# -*- encoding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from common.utilities import split_filepath

from domain.models import UserAccount
from presentation.forms import EditProfileForm, NoAutoFillPasswordChangeForm, EmailChangeForm

@login_required
def view_my_writeroom(request):
    return render(request, 'accounts/writeroom.html', {})

# USER PROFILE #########################################################################################################

@login_required
def view_my_profile(request):
    return _view_user_profile(request, request.user)


def view_user_profile_by_id(request, user_uid):
    user = get_object_or_404(UserAccount, user_uid=user_uid)
    return _view_user_profile(request, user)


def view_user_profile_by_url_name(request, url_name):
    user = get_object_or_404(UserAccount, url_name=url_name)
    return _view_user_profile(request, user)


def _view_user_profile(request, user):
    #publications = Publication.objects.filter(created_by=user)
    #return render(request, 'accounts/profile.html', {'profile_user':user, 'publications':publications})
    return render(request, 'accounts/profile.html', {'profile_user':user, })


# ACCOUNT SETTINGS #####################################################################################################

@login_required
def edit_my_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(user, request.POST, request.FILES)
        if form.is_valid():
            user.name = form.cleaned_data['name']
            user.url_name = form.cleaned_data['url_name']
            user.bio = form.cleaned_data['bio']
            user.website_url = form.cleaned_data['website_url']
            user.facebook_url = form.cleaned_data['facebook_url']
            user.twitter_url = form.cleaned_data['twitter_url']
            user.save()

            avatar = form.cleaned_data['avatar']
            if avatar:
                (root, name, ext) = split_filepath(avatar.name)
                user.avatar.save('avatar.%s' % ext, avatar)

            messages.success(request, u'บันทึกการเปลี่ยนแปลงเรียบร้อย')
            return redirect('edit_my_profile')

    else:
        form = EditProfileForm(user, initial={
            'avatar':user.avatar,
            'name':user.name,
            'url_name':user.url_name,
            'bio':user.bio,
            'website_url':user.website_url,
            'facebook_url':user.facebook_url,
            'twitter_url':user.twitter_url,
        })

    return render(request, 'accounts/settings/settings_profile.html', {'form':form})


@login_required
def edit_my_account(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'email':
            email_form = EmailChangeForm(request.POST)
            if email_form.is_valid():
                # TODO Send confirmation email again
                request.user.email = email_form.cleaned_data['email']
                request.user.save()

                messages.success(request, u'เปลี่ยนอีเมลเรียบร้อย')
                return redirect('edit_my_account')

            else:
                password_form = NoAutoFillPasswordChangeForm(request.user)

        elif request.POST.get('submit') == 'email':
            password_form = NoAutoFillPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                request.user.set_password(password_form.cleaned_data['new_password1'])
                request.user.save()

                messages.success(request, u'เปลี่ยนรหัสผ่านเรียบร้อย')
                return redirect('edit_my_account')

            else:
                email_form = EmailChangeForm(initial={'email':request.user.email})
        else:
            raise Http404

    else:
        email_form = EmailChangeForm(initial={'email':request.user.email})
        password_form = NoAutoFillPasswordChangeForm(request.user)

    return render(request, 'accounts/settings/settings_account.html', {'email_form':email_form, 'password_form':password_form})