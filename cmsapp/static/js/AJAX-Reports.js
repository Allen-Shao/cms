// Include JQuery on HTML using:
// <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>

var old_l = 0;
var new_l = 0;

$("#AJAXreports").append("<div class='container-fluid' id='AJAXcontent'></div>");

setInterval(pullReports, 3000);

function pullReports() {
  var html = '';
  $.ajax({ 
     type: "GET",
     dataType: "json",
     url: "http://localhost:8888/api/reports",
     success: function(data){        
        new_l = data.length;

        if (new_l != old_l) {
          for (var x = old_l; x < data.length; x++) {
            html += "<div class='row'>";
            html += "<div class='col-md-2'>";
            html += data[x].name;
            html += "</div>";
            html += "<div class='col-md-2'>";
            html += data[x].location;
            html += "</div>";
            html += "<div class='col-md-2'>";
            html += data[x].description;
            html += "</div>";
            html += "<div class='col-md-2'>";
            html += data[x].type_of_assistance;
            html += "</div>";
            html += "<div class='col-md-2'>";
            html += data[x].type_of_crisis;
            html += "</div>";
            html += "</div>";
            $("#AJAXcontent").append(html);
            html = '';
        }

        old_l = new_l;
    }
}
});
}