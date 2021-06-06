$(document).ready(function() {
	$organizationCmb = $("#organizationCmb"), $employeesTbl = $("#employeesTbl"), $placesTbl = $("#placesTbl"), $historyTbl = $("#historyTbl"), $employeePlaceAskBtn = $("#employeePlaceAskBtn");

	OrganizationsFilling();

	function OrganizationsFilling() {
		$request = $.ajax({
			url: "get_organizations_list",
			type: "GET",
			dataType: "json"
		})
			.done(function (result) {
				// Fills the select with the organizations
				$.each($.parseJSON(result), function (index, organization) {
					$organizationCmb.append($("<option>").val(organization.id).text(organization.name));
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});
	}

	$organizationCmb.change(function () {
	    GetOrganizationPlaces($(this).find("option:selected").val())
	    GetOrganizationEmployees($(this).find("option:selected").val())
	});

	function GetOrganizationPlaces() {
		$("#placesTbl > tbody").empty();

		let params = {
			orgID: $organizationCmb.find("option:selected").val()
		}

		$request = $.ajax({
			url: "get_organization_places",
			type: "GET",
			dataType: "json",
			data: params
		})
			.done(function (result) {
				// Fills the table with the places
				$.each($.parseJSON(result), function (index, place) {
					$placesTbl.append(
					"<tr>" +
						"<td hidden organization='" + place.organization + "'>" + place.id + "</td>" +
						"<td>" + place.name + "</td>" +
						"<td catchBy=" + place.catchBy + ">" + (place.catchBy !== -1 ? "תפוס" : "פנוי") + "</td>" +
					"</tr>");
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});
	}

	function GetOrganizationEmployees() {
		$("#employeesTbl > tbody").empty();

		let params = {
			orgID: $organizationCmb.find("option:selected").val()
		}

		$request = $.ajax({
			url: "get_organization_employees",
			type: "GET",
			dataType: "json",
			data: params
		})
			.done(function (result) {
				// Fills the table with the employees
				$.each($.parseJSON(result), function (index, employee) {
					$employeesTbl.append(
					"<tr>" +
					    "<td><input type='radio' employee='" + employee.id + "' name='employees' /></td>" +
						"<td hidden organization='" + employee.organization + "'>" + employee.id + "</td>" +
						"<td>" + employee.familyName + "</td>" +
						"<td>" + employee.privateName + "</td>" +
						"<td>" + employee.identityCard + "</td>" +
						"<td placeID='" + employee.placeID + "'>" + employee.placeName + "</td>" +
					"</tr>");
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});
	}

	$employeesTbl.on("change", "input[name='employees']", function() {
	    GetEmployeeAsksHistory(parseInt($(this).attr("employee")));

	    $employeePlaceAskBtn.prop("disabled", false);
	});

	function GetEmployeeAsksHistory(employeeID) {
		$("#historyTbl > tbody").empty();

		let params = {
			employeeID: employeeID
		}

		$request = $.ajax({
			url: "get_employee_ask_history",
			type: "GET",
			dataType: "json",
			data: params
		})
			.done(function (result) {
				// Fills the table with the employee's asks history
				$.each($.parseJSON(result), function (index, history) {
					$historyTbl.append(
					"<tr>" +
						"<td hidden employee=" + history.employee + ">" + history.id + "</td>" +
						"<td>" + history.reservationTime + "</td>" +
						"<td placeID=" + history.place + ">" + history.placeName + "</td>" +
					"</tr>");
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});
	}

	$employeePlaceAskBtn.click(function() {
		alert("כפתור נלחץ");
	});
});