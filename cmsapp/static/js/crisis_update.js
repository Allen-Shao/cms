var old_l = 0;
var new_l = 0;


pullCrisis();

setInterval(pullCrisis, 5000);

function pullCrisis() {
  var html = '';
  $.ajax({
   type: "GET",
   dataType: "json",
   url: "/api/crisis/",
   success: function(data){
    new_l = data.length;

    if (new_l != old_l) {
      for (var x = old_l; x < data.length; x++) {
          if (data[x].active){
            html += "<tr>";
            html += "<th class='col-md-2'>";
            html += data[x].type_of_crisis;
            html += "</th><th class='col-md-2'>";
            html += data[x].location;
            html += "</th><th class='col-md-3'>";
            html += data[x].description;
            html += "</th><th class='col-md-3'>";
            html += data[x].date_time;
            html += "</th></tr>";

            console.log(html);
            $("#CrisisContent").append(html);
            html = '';
          }
        }

        old_l = new_l;
      }
    }
  });
}
