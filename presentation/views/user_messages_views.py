# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@login_required
def view_user_messages(request):
    return render(request, 'user/user_messages.html', {})