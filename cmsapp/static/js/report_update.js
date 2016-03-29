var report_old_l = 0;
var report_new_l = 0;
var currentURL = "http://localhost:8888/api/reports/";
pullReports();

setInterval(pullReports, 5000);

function pullReports() {
  var html = '';
  $.ajax({
    type: "GET",
    dataType: "json",
    url: currentURL,
    success: function(data){
      report_new_l = data.results.length;

      if (report_new_l != report_old_l) {
        for (var x = report_old_l; x < report_new_l; x++) {
          html = "";
          html += "<tr id='row" + data.results[x].id + "'>";
          html += "<th class='col-md-2'>";
          html += data.results[x].name;
          html += "</th><th class='col-md-2'>";
          html += data.results[x].location;
          html += "</th><th class='col-md-3'>";
          html += data.results[x].description;
          html += "</th><th class='col-md-3'>";
          html += data.results[x].type_of_assistance;
          html += "</th><th class='col-md-2'>";
          html += data.results[x].type_of_crisis;
          html += "</th><th class='col-md-1'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-danger' onClick='updateReportStatus(this.id)'><span class='glyphicon glyphicon-trash'></span>&nbsp;</button>"
          html += "</th></tr>";

          $("#ReportContent").append(html);
        }

        report_old_l = report_new_l;
      }
    }
  });
}

function updateReportStatus(reportID, newStatus) {
  var csrf_token = getCookie("csrftoken");
  var dataToPost = {"status": newStatus}
  $.ajax({
    url: "http://localhost:8888/api/reports/"+reportID+"/",
    headers: {"X-CSRFToken": csrf_token},
    data: JSON.stringify(dataToPost),
    method: "PATCH",
    contentType: 'application/json',
    dataType: "json",
    success: function(data) {
      console.log("Report status updated");
    }
  });

  // $("#row" + reportID).remove();
  // refresh the reports after removal
  pullReports();
}
