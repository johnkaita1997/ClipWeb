import webbrowser

import clipboard
import pyperclip
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from web.models import Entries


def homepage(request):
    summarydictionary = {}
    entries = Entries.objects.all()
    print("Found found")
    print(entries)
    print("Found found")
    summarydictionary['entries'] = entries
    response = render(request, "index.html", {"summary": summarydictionary})
    return response

def deleteentry(request, id):
    Entries.objects.get(id=id).delete()
    messages.success(request, f"Entry deleted successfully")
    return redirect('homepage')


def openentry(request, url):
    try:
        print(url)
        webbrowser.open(url)
    except Exception as exception:
        messages.success(request, f"Error! {exception}")
        return redirect('homepage')


def copy(request, text):
    try:
        clipboard.copy(text)  # Copy text to clipboard using the clipboard library
        message = 'Text copied successfully!'
        success = True
    except Exception as e:
        message = str(e)
        success = False

    response_data = {
        'message': message,
        'success': success
    }
    return JsonResponse(response_data)
