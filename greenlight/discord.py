import requests
from django.conf import settings

WEBHOOK_URL = getattr(settings, 'GREENLIGHT_DISCORD_WEBHOOK', '')

MESSAGES = {
    'green': '🟢 **GREEN ALERT!** All clear.',
    'yellow': '🟡 **YELLOW ALERT!** Be ready.',
    'red': '🔴 **RED ALERT!** Action needed!'
}

def send_discord_message(color):
    content = MESSAGES.get(color, 'Unknown alert')
    if WEBHOOK_URL:
        requests.post(WEBHOOK_URL, json={'content': content})
