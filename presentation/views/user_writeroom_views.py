# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@login_required
def view_user_writeroom(request):
    return render(request, 'user/user_writeroom.html', {})


@login_required
def start_new_writing(request):
    return render(request, 'user/user_writeroom_edit.html', {})