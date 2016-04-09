var currentURL = baseUrl + "/api/reports/";
var type = "";
var preURL;
var nextURL;
var newestDataId = 0;

pullReports();

setInterval(checkUpdate, 5000);

/**
 * Check if there are new reports to show. If there are, show a button to update the reports
 */
function checkUpdate() {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: currentURL,
        success: function (data) {
            if (data.count > 0 && newestDataId < data.results[0].id) {
                $("#new-notification").html("<input class='btn btn-info col-md-4' type='button' value='New Reports Available! Click to Update!' onclick='pullReports();'>");
            }
        }
    });
}

/**
 * Pull new reports from the backend
 */
function pullReports() {
    var urlToRequest;

    if (type != "") {
        urlToRequest = addParameter(currentURL, "type", type, false);
    } else {
        urlToRequest = currentURL;
    }

    $.ajax({
        type: "GET",
        dataType: "json",
        url: urlToRequest,
        success: function (data) {
            var html = '';
            preURL = data.previous;
            nextURL = data.next;
            if (data.count > 0) {
                newestDataId = data.results[0].id;
            } else {
                newestDataId = 0;
            }
            $("#new-notification").html("");
            for (var x = 0; x < data.results.length; x++) {
                html += "<tr id='row" + data.results[x].id + "'>";
                html += "<td class='col-md-1'>";
                html += data.results[x].name;
                html += "</td><td class='col-md-2'>";
                html += data.results[x].location;
                html += "</td><td class='col-md-3'>";
                html += data.results[x].description;
                html += "</td><td class='col-md-2'>";
                html += data.results[x].type_of_assistance;
                html += "</td><td class='col-md-2'>";
                html += data.results[x].type_of_crisis;
                html += "</td><td class='col-md-1'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-success' onClick='updateReportStatus(this.id, true)'><span class='glyphicon glyphicon-ok'></span>&nbsp;</button>"
                html += "</td><td class='col-md-1'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-danger' onClick='updateReportStatus(this.id, false)'><span class='glyphicon glyphicon-remove'></span>&nbsp;</button>"
                html += "</td></tr>";
            }
            $("#ReportContent").html(html);
            if (preURL == null) {
                $("#prepage").attr("class", "disabled");
            }
            else {
                $("#prepage").attr("class", "active");
            }
            if (nextURL == null) {
                $("#nextpage").attr("class", "disabled");
            }
            else {
                $("#nextpage").attr("class", "active");
            }

        }
    });
}

/**
 * Updating the status of the report to efficiently mange the reports
 *
 * @param reportID unique ID of the report
 * @param newStatus the new status to be updated
 */
function updateReportStatus(reportID, newStatus) {
    var csrf_token = getCookie("csrftoken");
    var dataToPost = {"status": newStatus}
    $.ajax({
        url: currentURL + reportID + "/",
        headers: {"X-CSRFToken": csrf_token},
        data: JSON.stringify(dataToPost),
        method: "PATCH",
        contentType: 'application/json',
        dataType: "json",
        success: function (data) {
            pullReports();
            console.log("Report status updated");
        }
    });
}

/**
 * Filter the reports by the required type of crisis
 */
function changeType() {
    type = $("#type-filter").val();
    console.log(type);
    pullReports();
}

/**
 * Pagination -- Go to the previous page
 */
function prePage() {
    currentURL = preURL;
    pullReports();
}

/**
 * Pagination -- Go to the next page
 */
function nextPage() {
    currentURL = nextURL;
    pullReports();
}
