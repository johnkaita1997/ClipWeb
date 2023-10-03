import webbrowser

from django.contrib import messages
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