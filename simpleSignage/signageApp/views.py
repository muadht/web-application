from django.shortcuts import render, redirect, get_object_or_404
from .forms import AssetForm
from .models import Asset
from .forms import ScreenForm
from .models import Screen
import uuid

# Home view
def home_view(request):
    form = AssetForm()
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'signageApp/home.html', context)
  
### Asset view ###
#create Asset view
def create_asset_view(request):
    form = AssetForm()
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    context = {
        'form': form
    }
    return render(request, 'signageApp/asset_form.html', context)
  
# Read view
def asset_list_view(request):
    assets = Asset.objects.all()
    context = {
        'assets': assets
    }
    return render(request, 'signageApp/asset_list.html', context)

# Update view
def update_asset_view(request, pk):
    asset = get_object_or_404(Asset, file_id=pk)
    form = AssetForm(instance=asset)
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list.html')
    context = {
        'form': form
    }
    return render(request, 'signageApp/asset_form.html', context) 

# Delete view
def delete_asset_view(request, pk):
    asset = Asset.objects.get(file_id=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, 'signageApp/asset_confirm_delete.html', {'asset': asset})

### Screen view ###
# Create view
def create_screen_view(request):
    if request.method == 'POST':
        form = ScreenForm(request.POST)
        if form.is_valid():
            screen = form.save(commit=False)
            screen.screen_resolution = '1920x1080'  # Default resolution
            screen.screen_orientation = 'Landscape'  # Default orientation
            screen.screen_status = 'Active'  # Default status
            screen.save()
            return redirect('screen_list')  # Redirect to a list view or any other view
    else:
        form = ScreenForm()
    return render(request, 'signageApp/screen_form.html', {'form': form})

# Read view
def screen_list_view(request):
    screens = Screen.objects.all()
    context = {
        'screens': screens
    }
    return render(request, 'signageApp/screen_list.html', context)

# Update view
def update_screen_view(request, pk):
    screen = Screen.objects.get(screen_id=pk)
    form = ScreenForm(instance=screen)
    if request.method == 'POST':
        form = ScreenForm(request.POST, instance=screen)
        if form.is_valid():
            form.save()
            return redirect('screen_list')
    context = {
        'form': form
    }
    return render(request, 'signageApp/screen_form.html', context)

# Delete view
def delete_screen_view(request, pk):
    screen = Screen.objects.get(screen_id=pk)
    if request.method == 'POST':
      screen.delete()
      return redirect('screen_list')
    return render(request, 'signageApp/screen_confirm_delete.html', {'screen': screen})

# Screen Display view
# def screen_display_view(request, screen_path):
#     screen = Screen.objects.get(screen_path=screen_path)
#     context = {
#         'screen': screen
#     }
#     return render(request, 'signageApp/screen_display.html', context)

# views.py

def screen_display_view(request, screen_path):
    screen = get_object_or_404(Screen, screen_path=screen_path)
    context = {
        'screen': screen,
        'screen_path': screen.screen_path
    }
    return render(request, 'signageApp/screen_display.html', context)