from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .discord import send_discord_message

@login_required
@permission_required('greenlight.can_use_greenlight', raise_exception=True)
def greenlight_view(request):
    if request.method == 'POST':
        color = request.POST.get('color')
        if color:
            send_discord_message(color)
        return redirect('greenlight')
    return render(request, 'greenlight/greenlight.html')
