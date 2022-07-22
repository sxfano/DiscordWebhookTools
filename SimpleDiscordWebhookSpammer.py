import requests

print("Basic Discord Webhook Spammer")

Url = input('Webhook Url:')
discord_webhook_url = '%s' % Url
Webhook_Username = input("Webhook username (optional):")
avatar = input("Avatar Url (optional):")
Message = input('Message:')
Message = {
    "content" : '%s' % Message,
    "username" : '%s' % Webhook_Username,
    "avatar_url": '%s' % avatar,
}
print("Sent")
while True:
     requests.post(discord_webhook_url, data=Message)