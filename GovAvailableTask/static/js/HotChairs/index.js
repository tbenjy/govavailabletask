$(document).ready(function() {
	$organizationCmb = $("#organizationCmb"), $employeesTbl = $("#employeesTbl"), $placesTbl = $("#placesTbl"), $employeePlaceAskBtn = $("#employeePlaceAskBtn");

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
		$("#placesTbl > tbody").empty();
		$("#employeesTbl > tbody").empty();

		let params = {
			orgID: $(this).find("option:selected").val()
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
						"<td hidden organization=" + employee.organization + ">" + employee.id + "</td>" +
						"<td>" + employee.familyName + "</td>" +
						"<td>" + employee.privateName + "</td>" +
						"<td>" + employee.employeeID + "</td>" +
						"<td>" + "בית" + "</td>" +
					"</tr>");
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});

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
						"<td hidden>" + place.placeID + "</td>" +
						"<td>" + place.Description + "</td>" +
						"<td>" + (place.catchByID !== -1 ? "תפוס" : "פנוי") + "</td>" +
					"</tr>");
				});
			})
			.fail(function (err) {
				alert($(err.responseText).filter("title").text());
			});
	});

	$employeePlaceAskBtn.click(function() {
		alert("כפתור נלחץ");
	});
});