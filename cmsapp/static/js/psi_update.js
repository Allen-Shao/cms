updatePSI();

/**
  * update psi readings
  */
function updatePSI() {
  $.ajax({
    type: "GET",
    dataType: "xml",
    url: "http://www.nea.gov.sg/api/WebAPI?dataset=psi_update&keyref=781CF461BB6606AD0308169EFFAA8231021BA33828C73DAE",
    success: updatePSIInHome,
    error: function(error) {
      console.log(error);
    }
  });
}

function updatePSIInHome(psiData) {
  // get reading from XML
  var overallReading = psiData.getElementsByTagName("region")[1].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var northReading = psiData.getElementsByTagName("region")[0].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var centralReading = psiData.getElementsByTagName("region")[2].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var eastReading = psiData.getElementsByTagName("region")[3].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var westReading = psiData.getElementsByTagName("region")[4].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');
  var southReading = psiData.getElementsByTagName("region")[5].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value');

  // compose html tags
  var psiReading = "<tr><td height</td>Overall</td>" + "<td>"+ overallReading + "</td></tr>";
  psiReading += "<tr><td>North</td>" + "<td>" + northReading + "</td></tr>";
  psiReading += "<tr><td>Central</td>" + "<td>" + centralReading + "</td></tr>";
  psiReading += "<tr><td>East</td>" + "<td>" + eastReading + "</td></tr>";
  psiReading += "<tr><td>West</td>" + "<td>" + westReading + "</td></tr>";
  psiReading += "<tr><td>South</td>" + "<td>" + southReading + "</td></tr>";

  MarkersWithLabel(northLatLng, northReading, psiIcon, 30);
  MarkersWithLabel(centralLatLng, centralReading, psiIcon, 30);
  MarkersWithLabel(eastLatLng, eastReading, psiIcon, 30);
  MarkersWithLabel(westLatLng, westReading, psiIcon, 30);
  MarkersWithLabel(southLatLng, southReading, psiIcon, 30);

  // reflect change in html
  $("#psi_table").html(psiReading);
}
