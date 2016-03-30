var currentURL = "http://localhost:8888/api/reports/";
var type = "";
var preURL;
var nextURL;
var newestDataId;


pullReports();

setInterval(checkUpdate, 5000);

function checkUpdate(){
  $.ajax({
    type: "GET",
    dataType: "json",
    url: currentURL,
    success: function(data){
      if (newestDataId != data.results[0].id) {
          $("#new-notification").html("<input class='btn btn-info col-md-4' type='button' value='New Reports Available! Click to Update!' onclick='pullReports();'>");
      }     
    }
  });
}

function pullReports() {
  var urlToRequest;

  if (type != "") {
    urlToRequest = addParameter(currentURL, "type", type, false);
  } else {
    urlToRequest = currentURL;
  }

  $.ajax({
    type: "GET",
    dataType: "json",
    url: urlToRequest,
    success: function(data){
      var html = '';
      preURL = data.previous;
      nextURL = data.next;
      newestDataId = data.results[0].id;
      $("#new-notification").html("");
      for (var x = 0; x < data.results.length; x++) {
        html += "<tr id='row" + data.results[x].id + "'>";
        html += "<th class='col-md-1'>";
        html += data.results[x].name;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].location;
        html += "</th><th class='col-md-3'>";
        html += data.results[x].description;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].type_of_assistance;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].type_of_crisis;
        html += "</th><th class='col-md-1'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-success' onClick='updateReportStatus(this.id, true)'><span class='glyphicon glyphicon-ok'></span>&nbsp;</button>"
        html += "</th><th class='col-md-1'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-danger' onClick='updateReportStatus(this.id, false)'><span class='glyphicon glyphicon-remove'></span>&nbsp;</button>"
        html += "</th></tr>";
      }
      $("#ReportContent").html(html);
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

function changeType() {
  type = $("#type-filter").val();
  console.log(type);
  pullReports();
}

function prePage(){
    currentURL = preURL;
    pullReports();
}

function nextPage(){
    currentURL = nextURL;
    pullReports();
}

function addParameter(url, parameterName, parameterValue, atStart){
    replaceDuplicates = true;
    if(url.indexOf('#') > 0){
        var cl = url.indexOf('#');
        urlhash = url.substring(url.indexOf('#'),url.length);
    } else {
        urlhash = '';
        cl = url.length;
    }
    sourceUrl = url.substring(0,cl);

    var urlParts = sourceUrl.split("?");
    var newQueryString = "";

    if (urlParts.length > 1)
    {
        var parameters = urlParts[1].split("&");
        for (var i=0; (i < parameters.length); i++)
        {
            var parameterParts = parameters[i].split("=");
            if (!(replaceDuplicates && parameterParts[0] == parameterName))
            {
                if (newQueryString == "")
                    newQueryString = "?";
                else
                    newQueryString += "&";
                newQueryString += parameterParts[0] + "=" + (parameterParts[1]?parameterParts[1]:'');
            }
        }
    }
    if (newQueryString == "")
        newQueryString = "?";

    if(atStart){
        newQueryString = '?'+ parameterName + "=" + parameterValue + (newQueryString.length>1?'&'+newQueryString.substring(1):'');
    } else {
        if (newQueryString !== "" && newQueryString != '?')
            newQueryString += "&";
        newQueryString += parameterName + "=" + (parameterValue?parameterValue:'');
    }
    return urlParts[0] + newQueryString + urlhash;
};
