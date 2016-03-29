
pullDecisions();

setInterval(pullDecisions, 5000);

function pullDecisions() {
  var html = '';
  $.ajax({
   type: "GET",
   dataType: "json",
   url: "http://localhost:8888/api/decisions/",
   success: function(data){
    length = data.results.length;

      for (var x = 0; x < length; x++) {
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

            
          // }
        }
        $("#DecisionsContent").html(html);
    }
  });
}
