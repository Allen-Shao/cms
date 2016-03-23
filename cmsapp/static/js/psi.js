$.ajax({
  url: 'http://www.nea.gov.sg/api/WebAPI?dataset=psi_update&keyref=781CF461BB6606AD62B1E1CAA87ECA612A87DF33A3ECDC11',
  dataType: 'xml',
  type: 'GET',
  success: function (data) {
    var regions = data.childNodes[0].childNodes[2];
    var rNO = regions.childNodes[0];
    var rCE = regions.childNodes[2];
    var rEA = regions.childNodes[3];
    var rWE = regions.childNodes[4];
    var rSO = regions.childNodes[5];
    var rNOId = rNO.childNodes[0].childNodes[0].nodeValue;
    var rNOLat = rNO.childNodes[1].childNodes[0].nodeValue;
    var rNOLon = rNO.childNodes[2].childNodes[0].nodeValue;
    var rNOPSI = rNO.childNodes[3].childNodes[0].getAttribute("value");
    console.log(rNOId);
    console.log(rNOLat);
    console.log(rNOLon);
    console.log(rNOPSI);
  }
});
