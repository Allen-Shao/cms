updatePSI();

/**
  * update psi readings
  */
function updatePSI() {
  $.ajax({
    type: "GET",
    dataType: "xml",
    url: "http://www.nea.gov.sg/api/WebAPI?dataset=psi_update&keyref=781CF461BB6606AD0308169EFFAA8231021BA33828C73DAE",
    success: updateInHome,
    error: function(error) {
      console.log(error);
    }
  });
}

function updateInHome(psiData) {
  // get reading from XML
  var overallReading = psiData.getElementsByTagName("region")[1].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var northReading = psiData.getElementsByTagName("region")[0].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var centralReading = psiData.getElementsByTagName("region")[2].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var eastReading = psiData.getElementsByTagName("region")[3].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var westReading = psiData.getElementsByTagName("region")[4].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var southReading = psiData.getElementsByTagName("region")[5].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');

  // compose html tags
  var psiReading = "<p>Overall: " + overallReading + "</p>";
  psiReading += "<p>North: " + northReading + "</p>";
  psiReading += "<p>Central: " + centralReading + "</p>";
  psiReading += "<p>East: " + eastReading + "</p>";
  psiReading += "<p>West: " + westReading + "</p>";
  psiReading += "<p>South: " + southReading + "</p>";

  // reflect change in html
  $("#weather_psi").html(psiReading);
}
