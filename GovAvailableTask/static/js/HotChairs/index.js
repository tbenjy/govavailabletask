$(document).ready(function() {
	let $organizationCmb = $("#organizationCmb"),
		$employeesTbl = $("#employeesTbl"), $placesTbl = $("#placesTbl"), $historyTbl = $("#historyTbl"),
		$employeePlaceAskBtn = $("#employeePlaceAskBtn"), $freePlaceDiv = $("#freePlaceDiv"),
		$freePlaceCmb = $("#freePlaceCmb"), $dialogOkBtn = $("#dialogOkBtn"), $dialogCancelBtn = $("#dialogCancelBtn");

	// Fills the list of organizations in the beginning
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
		$employeePlaceAskBtn.prop("disabled", true);
		$("#historyTbl > tbody").empty();

		$organizationCmb.prop("disabled", true);
		// Fills the tables of places and employees that belong to the organization
		GetOrganizationPlaces()
		GetOrganizationEmployees()
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
						"<td place_id='" + employee.placeID + "'>" + employee.placeName + "</td>" +
					"</tr>");
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			})
			.always(function () {
				$organizationCmb.prop("disabled", false);
			});
	}

	$employeesTbl.on("change", "input[name='employees']", function() {
		// Fills the table of the employee's reservations' history
		GetEmployeeAsksHistory(parseInt($(this).attr("employee")));
	});

	function GetEmployeeAsksHistory(employeeID) {
		$("#employeesTbl *").prop("disabled", true);
		$employeePlaceAskBtn.prop("disabled", true);
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
						"<td place_id=" + history.place + ">" + history.placeName + "</td>" +
					"</tr>");
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			})
			.always(function () {
				$("#employeesTbl *").prop("disabled", false);
				$employeePlaceAskBtn.prop("disabled", false);
			});
	}

	$freePlaceDiv.dialog({
		modal: true,
		autoOpen: false,
		open: function(event, ui) {
			// Fills the list of the organization's free places
			FreePlacesFilling();
		},
		close: function(event, ui) {
			$dialogOkBtn.prop("disabled", true);
		}
	});

	function FreePlacesFilling() {
		$freePlaceCmb.empty();
		$freePlaceCmb.append($("<option hidden>").text("בחר אחד מהמקומות הבאים"));

		let params = {
			orgID: $organizationCmb.find("option:selected").val()
		}

		$request = $.ajax({
			url: "get_free_places_list",
			type: "GET",
			dataType: "json",
			data: params
		})
			.done(function (result) {
				// Fills the select with the free places
				let currentPlace = parseInt($("input[name='employees']:checked").closest("tr").find("td[place_id]").attr("place_id"))
				if (currentPlace !== -1)
					$freePlaceCmb.append($("<option>").val(-1).text("בית"));
				$.each($.parseJSON(result), function (index, place) {
					$freePlaceCmb.append($("<option>").val(place.id).text(place.name));
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});
	}

	$employeePlaceAskBtn.click(function() {
		$freePlaceDiv.dialog("open");
	});

	$dialogCancelBtn.click(function() {
		$freePlaceDiv.dialog("close");
	});

	$freePlaceCmb.change(function() {
		$dialogOkBtn.prop("disabled", false);
	});

	$dialogOkBtn.click(function() {
		let $employee = $("input[name='employees']:checked"),
			$oldPlace = $employee.closest("tr").find("td[place_id]"),
			$newPlace = $freePlaceCmb.find("option:selected");

		let employeeID = parseInt($employee.attr("employee")),
			oldPlaceID = parseInt($oldPlace.attr("place_id")),
			newPlaceID = parseInt($newPlace.val())

		let params = {
			employeeID: employeeID,
			oldPlaceID: oldPlaceID,
			newPlaceID: newPlaceID
		}

		$.ajax({
		    async: false,
			url: "update_employee_place",
			data: params
		})
			.done(function (result) {
				// Updates the employee with the new place's ID and name
				$oldPlace.attr("place_id", $newPlace.val())
				$oldPlace.text($newPlace.text())
				// Refresh the table of the organization's places
				GetOrganizationPlaces();
				// If the new place isn't the home
				if (newPlaceID !== -1)
					// Refresh the table of the employee's history
					GetEmployeeAsksHistory(employeeID)
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});

		$freePlaceDiv.dialog("close");
	});
});

$(document).ajaxStart(function() {
	$(document.body).css({"cursor": "wait"});
}).ajaxStop(function() {
	$(document.body).css({"cursor": "default"});
});