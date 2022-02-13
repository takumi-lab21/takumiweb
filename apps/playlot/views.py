from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def top(request):
    return render(request, 'playlot/top.html', {})
