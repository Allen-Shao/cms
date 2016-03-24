updateWeather();

/* Update 2-hour weather nowcast*/
function updateWeather() {
  $.ajax({
    type: "GET",
    dataType: "xml",
    url: "http://www.nea.gov.sg/api/WebAPI?dataset=2hr_nowcast&keyref=781CF461BB6606AD0308169EFFAA8231021BA33828C73DAE",
    success: updateWeatherInHome,
    error: function(error) {
      console.log(error);
    }
  });
}

function weatherFullNama(weatherAbbr){
	switch (weatherAbbr){
		case "BR":
			return "Mist";
			break;
		case "CL":
			return "Cloudy";
			break;
		case "DR":
			return "Dizzle";
			break;
		case "FA":
			return "Fair";
			break;
		case "FG":
			return "Fog";
			break;
		case "FN":
			return "Fair";
			break;
		case "FW":
			return "Fair & Warm";
			break;
		case "HG":
			return "Heavy Thundery Showers with Gusty Winds";
			break;
		case "HR":
			return "Heavy Rain";
			break;
		case "HS":
			return "Heavy Showers";
			break;
		case "HT":
			return "Heavy Thundery Showers";
			break;
		case "HZ":
			return "Haze";
			break;
		case "LH":
			return "Slightly Haze";
			break;
		case "LR":
			return "Light Rain";
			break;
		case "LS":
			return "Light Showers";
			break;
		case "OC":
			return "Overcast";
			break;
		case "PC":
			return "Partly Cloudy";
			break;
		case "PN":
			return "Partly Cloudy";
			break;
		case "PS":
			return "Passing Showers";
			break;
		case "RA":
			return "Moderate Rain";
			break;
		case "SH":
			return "Showers";
			break;
		case "SK":
			return "Strong Winds, Showers";
			break;
		case "SN":
		    return "Snow";
		    break;
		case "SR":
		    return "Strong Winds, Rain";
		    break;
		case "SS":
			return "Snow Showers";
			break;
		case "SU":
			return "Sunny";
			break;
		case "SW":
			return "Strong Winds";
			break;
		case "TL":
			return "Thundery Showers";
			break;
		case "WC":
			return "Windy, Cloudy";
			break;
		case "WD":
			return "Windy";
			break;
		case "WF":
			return "Windy, Fair";
			break;
		case "WR":
			return "Windy, Rain";
			break;
		case "WS":
			return "Windy, Showers";
			break;
	}

}



function updateWeatherInHome(weatherData) {
	var numberOfAreas = 47;
	var area, lat, lon, weatherAbbr, weather, name, location;
	var weatherIcon;
	var i;
	var weatherDisplay = "";
	for (i=0;i<numberOfAreas;i++){
		//Process xml data
		area = weatherData.getElementsByTagName("area")[i];
		weatherAbbr = area.getAttribute("forecast");
		lat = area.getAttribute("lat");
		lon = area.getAttribute("lon");
		location = new google.maps.LatLng(lat, lon);
		name = area.getAttribute("name");
		weather = weatherFullNama(weatherAbbr);
		weatherIcon = {
    		url: "http://www.nea.gov.sg/Html/Nea/images/common/weather/50px/"+weatherAbbr+".png",
    		scaledSize: new google.maps.Size(30, 30)
  		};

  		//Display marker
  		MarkersWithLabel(location, weather, weatherIcon, 10);

  		//Compose html tags
  		weatherDisplay += "<tr><td height</td>"+ name + "</td>" + "<td>"+ weather + "</td></tr>";

	}
	// reflect change in html
  	$("#weather_table").html(weatherDisplay);
}





