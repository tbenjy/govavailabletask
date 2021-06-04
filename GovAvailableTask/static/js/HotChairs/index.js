$(document).ready(function() {
    $organizationCmb = $("#organizationCmb"), $placesTbl = $("#placesTbl"), $employeePlaceAskBtn = $("#employeePlaceAskBtn");

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
					$organizationCmb.append($("<option>").val(organization.organizationID).text(organization.Name));
				});
			})
			.fail(function (err) {
			    alert($(err.responseText).filter("title").text());
			});
    }

    $organizationCmb.change(function () {
        $("#placesTbl > tbody").empty();

        let params = {
			orgID: $(this).find("option:selected").val()
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