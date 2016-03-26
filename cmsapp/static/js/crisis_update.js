var crisis_old_l = 0;
var crisis_new_l = 0;
pullDecisions();

setInterval(pullDecisions, 5000);

function pullDecisions() {
  var html = '';
  $.ajax({
   type: "GET",
   dataType: "json",
   url: "http://localhost:8888/api/decisions/",
   success: function(data){
    crisis_new_l = data.results.length;

    if (crisis_new_l != crisis_old_l) {
      for (var x = crisis_old_l; x < crisis_new_l; x++) {
        html = "";
          // if (data[x].active){
            html += "<tr>";
            html += "<th class='col-md-2'>";
            html += data.results[x].type_of_crisis;
            html += "</th><th class='col-md-2'>";
            html += data.results[x].description;
            html += "</th><th class='col-md-3'>";
            html += data.results[x].date_time;
            html += "</th></tr>";

            $("#DecisionsContent").append(html);
          // }
        }

        crisis_old_l = crisis_new_l;
      }
    }
  });
}
