from bson import json_util
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import logging

from HotChairs.Classes.History import History
from HotChairs.Classes.Organizations import Organizations
from HotChairs.Classes.Employees import Employees
from HotChairs.Classes.Places import Places
from HotChairs.Classes.Log import Log


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
    try:
        organizations = Organizations()

        organizations_list = organizations.get_all_organizations()

        # Returns a list of all organizations
        return JsonResponse(json_util.dumps(organizations_list), safe=False)
    except Exception as ex:
        log = Log()
        log.add_message(logging.getLevelName(logging.ERROR), str(ex))


def get_organization_employees(request):
    try:
        org_id = int(request.GET["orgID"])
        employees = Employees()

        employees_list = employees.get_employees_by_organization(org_id)
        for employee in employees_list:
            employee.update(employees.get_employee_place(employee))

        # Returns a list of all organization's employees
        return JsonResponse(json_util.dumps(employees_list), safe=False)
    except Exception as ex:
        log = Log()
        log.add_message(logging.getLevelName(logging.ERROR), str(ex))


def get_organization_places(request):
    try:
        org_id = int(request.GET["orgID"])
        places = Places()

        places_list = places.get_places_by_organization(org_id)

        # Returns a list of all organization's places
        return JsonResponse(json_util.dumps(places_list), safe=False)
    except Exception as ex:
        log = Log()
        log.add_message(logging.getLevelName(logging.ERROR), str(ex))


def get_employee_ask_history(request):
    try:
        employee_id = int(request.GET["employeeID"])
        history = History()

        history_list = history.get_history_by_employee(employee_id)
        for history_row in history_list:
            history_row.update(history.get_place_name_of_history(history_row))

        # Returns a list of all organization's places
        return JsonResponse(json_util.dumps(history_list), safe=False)
    except Exception as ex:
        log = Log()
        log.add_message(logging.getLevelName(logging.ERROR), str(ex))


def get_free_places_list(request):
    try:
        org_id = int(request.GET["orgID"])
        places = Places()

        places_list = places.get_free_places_by_organization(org_id)

        # Returns a list of all organization's places
        return JsonResponse(json_util.dumps(places_list), safe=False)
    except Exception as ex:
        log = Log()
        log.add_message(logging.getLevelName(logging.ERROR), str(ex))


def update_employee_place(request):
    try:
        employee_id = int(request.GET["employeeID"])
        old_place_id = int(request.GET["oldPlaceID"])
        new_place_id = int(request.GET["newPlaceID"])

        places = Places()
        if new_place_id != -1:
            # Put the employee in the selected
            places.update_employee_of_the_place(new_place_id, employee_id)
            history = History()
            # Writes the reservation in the history
            history.insert_new_place_of_employee(employee_id, new_place_id)

        # Removes the employee from his previous place
        places.update_employee_of_the_place(old_place_id, -1)
        return HttpResponse()
    except Exception as ex:
        log = Log()
        log.add_message(logging.getLevelName(logging.ERROR), str(ex))
