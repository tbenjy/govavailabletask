from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd


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
    organization_df = pd.DataFrame({"organizationID": [1, 2], "Name": ["ארגון ראשון", "ארגון שני"]})
    return JsonResponse(organization_df.to_json(orient='records'), safe=False)


def get_organization_places(request):
    org_id = int(request.GET["orgID"])
    if org_id == 1:
        place_df = pd.DataFrame({"placeID": [1, 2, 3], "Description": ["ליד החלון", "שורה אחרונה", "מאחורי הקיר"], "X_Y": ["(3,6)", "(78,54)", "(8,9)"], "catchByID": [4, -1, 7], "catchByName": ["משה", "", "אבנר"]})
    else:
        place_df = pd.DataFrame({"placeID": [4], "Description": ["בכניסה למשרד"], "X_Y": ["(100,200)"], "catchByID": [-1], "catchByName": [""]})
    return JsonResponse(place_df.to_json(orient='records'), safe=False)
