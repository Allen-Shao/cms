var currentURL = baseUrl + "/api/requests/";

var newestDataId;
var preURL;
var nextURL;

pullRequests();

setInterval(checkUpdate, 5000);

/**
 * Check if there are new requests to show. If there are, show a button to update the requests
 */
function checkUpdate() {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: currentURL,
        success: function (data) {
            if (newestDataId != data.results[0].id) {
                console.log("appear!");
                $("#new-notification").html("<input class='btn btn-info col-md-4' type='button' value='New Requests Available! Click to Update!' onclick='pullRequests();'>");
            }
        }
    });
}

/**
 * Pull new requests from the backend
 */
function pullRequests() {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: currentURL,
        success: function (data) {
            console.log(data);
            var html = '';
            preURL = data.previous;
            nextURL = data.next;
            newestDataId = data.results[0].id;
            $("#new-notification").html("");
            console.log("disappeared");
            for (var x = 0; x < data.results.length; x++) {
                html += "<tr id='row" + data.results[x].id + "'>";
                html += "<td class='col-md-2'>";
                html += data.results[x].crisis;
                html += "</td><td class='col-md-2'>";
                html += data.results[x].resource;
                html += "</td><td class='col-md-4'>";
                html += data.results[x].description;
                html += "</td><td class='col-md-2'>";
                html += "<select id='agency" + data.results[x].id + "' class='form-control'>"
                html += agencySelect;
                html += "</select>"
                html += "</td><td class='col-md-2'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-success' onClick='updateRequestStatus(this.id)'><span class='glyphicon glyphicon-send'></span>&nbsp;</button>";
                html += "</td></tr>";
            }
            $("#RequestContent").html(html);

            if (preURL == null) {
                $("#prepage").attr("class", "disabled");
            } else {
                $("#prepage").attr("class", "active");
            }

            if (nextURL == null) {
                $("#nextpage").attr("class", "disabled");
            } else {
                $("#nextpage").attr("class", "active");
            }
        }
    });
}

/**
 * Updating the status of the request to efficiently mange the requests
 *
 * @param requestID unique ID of the request
 */
function updateRequestStatus(requestID) {
    var csrf_token = getCookie("csrftoken");
    var dataToPost = "csrfmiddlewaretoken=" + csrf_token + "&id=" + requestID + "&Agency=" + $("#agency" + requestID).val();
    $.ajax({
        url: baseUrl + "/process-requests/",
        data: dataToPost,
        method: "POST",
        contentType: 'application/x-www-form-urlencoded',
        success: function (data) {
            pullRequests();
            $("process-success").html("<div id='fastfade' class='alert alert-success'><strong>Process Succeeded!</strong></div>");
            console.log("Report status updated");
        }
    });
}

/**
 * Pagination -- Go to the previous page
 */
function prePage() {
    currentURL = preURL;
    pullRequests();
}

/**
 * Pagination -- Go to the next page
 */
function nextPage() {
    currentURL = nextURL;
    pullRequests();
}
