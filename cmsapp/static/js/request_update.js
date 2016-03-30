var currentURL = "http://localhost:8888/api/requests/";
// var type = "";
var newestDataId;
var preURL;
var nextURL;

pullRequests();

setInterval(checkUpdate, 5000);

function checkUpdate(){
  $.ajax({
    type: "GET",
    dataType: "json",
    url: currentURL,
    success: function(data){
      if (newestDataId != data.results[0].id) {
         console.log("appear!");
          $("#new-notification").html("<input class='btn btn-info col-md-4' type='button' value='New Requests Available! Click to Update!' onclick='pullRequests();'>");
      }
    }
  });
}

function pullRequests() {
  $.ajax({
    type: "GET",
    dataType: "json",
    url: currentURL,
    success: function(data){
      console.log(data);
      var html = '';
      preURL = data.previous;
      nextURL = data.next;
      newestDataId = data.results[0].id;
      $("#new-notification").html("");
      console.log("disappeared");
      for (var x = 0; x < data.results.length; x++) {
        html += "<tr id='row" + data.results[x].id + "'>";
        html += "<th class='col-md-2'>";
        html += data.results[x].crisis;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].resource;
        html += "</th><th class='col-md-4'>";
        html += data.results[x].description;
        html += "</th><th class='col-md-2'>";
        html += agencySelect;
        html += "</th><th class='col-md-2'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-success' onClick=''><span class='glyphicon glyphicon-send'></span>&nbsp;</button>";
        html += "</th></tr>";
      }
      $("#RequestContent").html(html);

      if (preURL == null){
        $("#prepage").attr("class", "disabled");
      }
      else{
        $("#prepage").attr("class", "active");
      }

      if (nextURL == null){
        $("#nextpage").attr("class", "disabled");
      }
      else{
        $("#nextpage").attr("class", "active");
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
      pullReports(type);
      console.log("Report status updated");
    }
  });
}

function prePage(){
    currentURL = preURL;
    pullReports();
}

function nextPage(){
    currentURL = nextURL;
    pullReports();
}
