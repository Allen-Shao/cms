updateDengue();


/* Update Dengue data*/
function updateDengue() {
  $.ajax({
    type: "GET",
    dataType: "xml",
    // url: "https://ref.data.gov.sg/common/Handler.ashx?ThemeName=DENGUE_CLUSTER&Format=kml&MetaDataID=228454",
    // the url below is for one map request, we might use it later if we want to
    //http://www.onemap.sg/API/services.svc/mashupData?token=qo/s2TnSUmfLz+32CvLC4RMVkzEFYjxqyti1KhByvEacEdMWBpCuSSQ+IFRT84QjGPBCuz/cBom8PfSm3GjEsGc8PkdEEOEr&themeName=DENGUE_CLUSTER&otptFlds=HYPERLINK,NAME&extents=-4423.6,15672.6,69773.4,52887.4
    url: "https://data.gov.sg/dataset/e7536645-6126-4358-b959-a02b22c6c473/resource/c1d04c0e-3926-40bc-8e97-2dfbb1c51c3a/download/denguecluster.kml",
    success: updateDengueInHome,
    error: function(error) {
      console.log(error);
    }
  });
}

function updateDengueInHome(dengueData) {

  var dengueDisplay = "";
  var place;
  var numOfCases;
  var area = dengueData.getElementsByTagName("Placemark");


  for (var i=0;i<area.length;i++){
    var cdata = area[i].getElementsByTagName("description")[0].firstChild.nodeValue;
    cdata = $.parseHTML(cdata);
    place = cdata[5].getElementsByTagName("td")[5].innerHTML;
    numOfCases = cdata[5].getElementsByTagName("td")[7].innerHTML;
    if (numOfCases != 0){
      dengueDisplay += "<tr><td style='width:80%'>"+ place + "</td>" + "<td style='width:20%;' align = 'center'>"+ numOfCases + "</td></tr>";
    }
  }

  // reflect change in html
  $("#dengue_table").html(dengueDisplay);
}
