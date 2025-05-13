# forms_app/views.py
from datetime import datetime

from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UserEForm
from pymongo import MongoClient

# establish a single client (could be module-level)
client = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
db = client[settings.MONGO_DB_NAME]
users = db["users"]  # the "users" collection


def user_eform(request):
    if request.method == "POST":
        form = UserEForm(request.POST)
        if form.is_valid():
            # grab cleaned data
            data = form.cleaned_data
            data["created_at"] = datetime.utcnow()  # timestamp
            # insert into MongoDB
            users.insert_one(data)
            return redirect("eform-success")
    else:
        form = UserEForm()
    # return render(request, "myapp/user_eform.html", {"form": form})
    return render(request, fr"D:\Riya\Eform\myapp\templates\forms_app\user_eform.html", {"form": form})
#

def success(request):
    # return render(request, "myapp/success.html")
    return render(request, fr"D:\Riya\Eform\myapp\templates\forms_app\success.html")
