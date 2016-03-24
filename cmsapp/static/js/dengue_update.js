updateDengue();


/* Update Dengue data*/
function updateDengue() {
  $.ajax({
    type: "GET",
    dataType: "xml",
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
	// var cdata = area[0].getElementsByTagName("description")[0].firstChild.nodeValue;
	// cdata = $.parseHTML(cdata);

	// console.log(cdata1)
	// console.log(cdata1[5].getElementsByTagName("td")[5].innerHTML);
	// console.log(cdata1[5].getElementsByTagName("td")[7].innerHTML);
	// for (i=0;i<numberOfAreas;i++){
	// 	//Process xml data
	// 	area = weatherData.getElementsByTagName("area")[i];
	// 	weatherAbbr = area.getAttribute("forecast");
	// 	lat = area.getAttribute("lat");
	// 	lon = area.getAttribute("lon");
	// 	location = new google.maps.LatLng(lat, lon);
	// 	name = area.getAttribute("name");
	// 	weather = weatherFullNama(weatherAbbr);
	// 	weatherIcon = {
 //    		url: "http://www.nea.gov.sg/Html/Nea/images/common/weather/50px/"+weatherAbbr+".png",
 //    		scaledSize: new google.maps.Size(30, 30)
 //  		};

 //  		//Display marker
 //  		MarkersWithLabel(location, weather, weatherIcon, 10, markers_weather);

 //  		//Compose html tags
 //  		weatherDisplay += "<tr><td height</td>"+ name + "</td>" + "<td>"+ weather + "</td></tr>";

	// }
	// reflect change in html
  	$("#dengue_table").html(dengueDisplay);
}
