from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import pymongo
import os


# Create your views here.
def index(request):
    context = {
        'title': "ממשל זמין - תרגיל"
    }
    return render(
        request,
        "HotChairs/index.html",
        context
    )


def get_organizations_list(request):
    client = pymongo.MongoClient('mongodb+srv://govavailabletask:hotchairs@hotchairs.8vnio.mongodb.net/HotChairs?retryWrites=true&w=majority')
    db = client.get_default_database()

    organization_df = pd.DataFrame({"organizationID": [1, 2], "Name": [db.name, db.name]})
    #organization_df = pd.DataFrame({"organizationID": [1, 2], "Name": ["ארגון ראשון", "ארגון שני"]})
    return JsonResponse(organization_df.to_json(orient='records'), safe=False)


def get_organization_places(request):
    org_id = int(request.GET["orgID"])
    if org_id == 1:
        place_df = pd.DataFrame({"placeID": [1, 2, 3], "Description": ["ליד החלון", "שורה אחרונה", "מאחורי הקיר"], "catchByID": [4, -1, 7]})
    else:
        place_df = pd.DataFrame({"placeID": [4], "Description": ["בכניסה למשרד"], "catchByID": [-1]})
    return JsonResponse(place_df.to_json(orient='records'), safe=False)
