$(document).ready(function() {
    $organizationCmb = $("#organizationCmb"), $placesTbl = $("#placesTbl");

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
                        "<td>" + place.X_Y + "</td>" +
                        "<td>" + (place.catchByID !== -1 ? "תפוס" : "פנוי") + "</td>" +
                        "<td hidden>" + place.catchByID + "</td>" +
                        "<td>" + place.catchByName + "</td>" +
                    "</tr>");
				});
			})
			.fail(function (err) {
			    alert($(err.responseText).filter("title").text());
			});
    });
});