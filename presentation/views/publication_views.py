# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required
def view_sample_publication(request):
    return render(request, 'publication/publication_view.html', {})