var url = baseUrl + "/api/decisions/";

pullDecisions();

setInterval(pullDecisions, 5000);

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
        html += "</th><th class='col-md-8'>";
        html += data.results[x].description;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].date_time;
        html += "</th></tr>";
      }

      $("#DecisionsContent").html(html);
    }
  });
}
