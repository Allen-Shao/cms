// Include JQuery on HTML using:
// <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>

var old_l = 0;
var new_l = 0;

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
    new_l = data.results.length;

    if (new_l != old_l) {
      for (var x = old_l; x < new_l; x++) {
            html = "";
            // html += "<div class='row'>";
            // html += "<div class='col-md-2'>";
            // html += data[x].name;
            // html += "</div>";
            // html += "<div class='col-md-2'>";
            // html += data[x].location;
            // html += "</div>";
            // html += "<div class='col-md-3'>";
            // html += data[x].description;
            // html += "</div>";
            // html += "<div class='col-md-3'>";
            // html += data[x].type_of_assistance;
            // html += "</div>";
            // html += "<div class='col-md-2'>";
            // html += data[x].type_of_crisis;
            // html += "</div>";
            // html += "</div>";
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

            console.log(html);
            $("#AJAXcontent").append(html);
          }

          old_l = new_l;
        }

      }
    });
}
