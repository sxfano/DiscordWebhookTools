import requests

webhook = input("Webhook Here: ")
requests.delete(webhook)
print("Deleted Webhook")