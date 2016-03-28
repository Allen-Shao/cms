// Include JQuery on HTML using:
// <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
var report_old_l = 0;
var report_new_l = 0;


// $("#AJAXreports").append("<table class='table table-striped'><tbody id='AJAXcontent'></tbody></table>");

pullReports();

setInterval(pullReports, 5000);

function pullReports() {
  var html = '';
  $.ajax({
  type: "GET",
  dataType: "json",
  url: "http://localhost:8888/api/reports/",
  success: function(data){
  report_new_l = data.results.length;

  if (report_new_l != report_old_l) {
    for (var x = report_old_l; x < report_new_l; x++) {
          html = "";
          html += "<tr>";
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
          html += "</th></tr>";

          $("#ReportContent").append(html);
        }

        report_old_l = report_new_l;
      }
    }
  });
}
