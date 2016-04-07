var url = baseUrl + "/api/decisions/";

pullDecisions();

setInterval(pullDecisions, 5000);

/**
 * Display the crises on the dashboard of the Decision Maker
 */
function pullDecisions() {
  var html = '';
  $.ajax({
    type: "GET",
    dataType: "json",
    url: url,
    success: function(data){
      length = data.results.length;
      html = "";

      for (var x = 0; x < length; x++) {
        html += "<tr>";
        html += "<th class='col-md-2'>";
        html += data.results[x].type_of_crisis;
        html += "</th><th class='col-md-6'>";
        html += data.results[x].description;
        html += "</th><th class='col-md-3'>";
        html += data.results[x].date_time;
        html += "</th><th class='col-md-1'>";
        html += "<button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-danger' onClick='updateDecisionStatus(this.id, false)'><span class='glyphicon glyphicon-remove'></span>&nbsp;</button>"
        html += "</th></tr>";
      }

      $("#DecisionsContent").html(html);
    }
  });
}

/**
 * Update the status of the decision to manage the cases effectively
 *
 * @param decisionID
 * @param newStatus
 */
function updateDecisionStatus(decisionID, newStatus) {

  var csrf_token = getCookie("csrftoken");
  var dataToPost = {"active": newStatus}
  $.ajax({
    url: url + decisionID + "/",
    headers: {"X-CSRFToken": csrf_token},
    data: JSON.stringify(dataToPost),
    method: "PATCH",
    contentType: 'application/json',
    dataType: "json",
    success: function(data) {
      pullDecisions();
      console.log("Decision status updated");
    }
  });
}
