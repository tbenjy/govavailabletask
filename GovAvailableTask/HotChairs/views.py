import pymongo
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import logging

from HotChairs.Classes.Organizations import Organizations
from HotChairs.Classes.Employees import Employees
import pandas as pd


# Create your views here.
def index(request):
    logging.basicConfig(filename='ServerErrors.log', level=logging.ERROR)

    context = {
        'title': "ממשל זמין - תרגיל"
    }
    return render(
        request,
        "HotChairs/index.html",
        context
    )


def get_organizations_list(request):
    try:
        #organizations = Organizations()
        # Returns a list of all organizations
        #return JsonResponse(organizations.get_all_organizations(), safe=False)

        client = pymongo.MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client["HotChairs"]
        collection = db["HotChairs_organizations"]
        return JsonResponse({"id": [1, 2], "Name": ["ארגון ראשון", "ארגון שני"]}, safe=False)

    except Exception as ex:
        logging.error(ex)


def get_organization_employees(request):
    try:
        org_id = int(request.GET["orgID"])
        employees = Employees()
        # Returns a list of all organization's employees
        return JsonResponse(employees.get_employees_by_organization(org_id), safe=False)
    except Exception as ex:
        logging.error(ex)


def get_organization_places(request):
    org_id = int(request.GET["orgID"])
    if org_id == 1:
        place_df = pd.DataFrame({"placeID": [1, 2, 3], "Description": ["ליד החלון", "שורה אחרונה", "מאחורי הקיר"], "catchByID": [4, -1, 7]})
    else:
        place_df = pd.DataFrame({"placeID": [4], "Description": ["בכניסה למשרד"], "catchByID": [-1]})
    return JsonResponse(place_df.to_json(orient='records'), safe=False)
