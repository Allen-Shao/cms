var old_length = 0;
var new_length = 0;
pullDecisions();

setInterval(pullDecisions, 5000);

function pullDecisions() {
  var html = '';
  $.ajax({
   type: "GET",
   dataType: "json",
   url: "http://localhost:8888/api/decisions/",
   success: function(data){
    new_length = data.results.length;

    if (new_length != old_length) {
      for (var x = old_length; x < new_length; x++) {
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

        old_length = new_length;
      }
    }
  });
}
