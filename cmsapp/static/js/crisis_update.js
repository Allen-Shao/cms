var old_l = 0;
var new_l = 0;


pullDecisions();

setInterval(pullDecisions, 5000);

function pullDecisions() {
  var html = '';
  $.ajax({
   type: "GET",
   dataType: "json",
   url: "http://localhost:8888/api/decisions/",
   success: function(data){
    new_l = data.results.length;

    if (new_l != old_l) {
      for (var x = old_l; x < new_l; x++) {
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

            console.log(html);
            $("#DecisionsContent").append(html);
          // }
        }

        old_l = new_l;
      }
    }
  });
}
