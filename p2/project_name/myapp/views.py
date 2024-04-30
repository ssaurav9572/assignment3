from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import App, Task, UserProfile
from .forms import ScreenshotForm

@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'user/profile.html', {'user_profile': user_profile, 'tasks': tasks})

@login_required
def upload_screenshot(request):
    if request.method == 'POST':
        form = ScreenshotForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('user_profile')
    else:
        form = ScreenshotForm()
    return render(request, 'user/upload_screenshot.html', {'form': form})

