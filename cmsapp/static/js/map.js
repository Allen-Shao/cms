//PSI Markers function
function MarkersWithLabel(location, labelText, markerIcon, size){
  var label = new MapLabel({
          text: labelText,
          position: location,
          map: map,
          fontSize: size,
          align: 'center'
  });
  var marker = new google.maps.Marker({
          position: location,
          map: map,
          icon: markerIcon
  });
  marker.bindTo('map', label);
  marker.bindTo('position', label);
  marker.setDraggable(false);
}


var map, psiIcon;

var northLatLng;
var centralLatLng;
var eastLatLng;
var westLatLng;
var southLatLng;


function initMap() {
  // create map
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: new google.maps.LatLng(1.354241, 103.82000),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });

  // psi icon
  psiIcon = {
    url: "http://cdn8.staztic.com/app/a/2742/2742678/psi-malaysia-haze-5-l-140x140.png",
    scaledSize: new google.maps.Size(40, 40)
  };

  // initialize positions
  northLatLng = new google.maps.LatLng(1.41803, 103.82000);
  centralLatLng = new google.maps.LatLng(1.35735, 103.82000);
  eastLatLng = new google.maps.LatLng(1.35735, 103.94000);
  westLatLng = new google.maps.LatLng(1.35735, 103.70000);
  southLatLng = new google.maps.LatLng(1.29587, 103.82000);

  //Psi Markers
  // MarkersWithLabel(northLatLng, "120");
  // MarkersWithLabel(centralLatLng, "130");
  // MarkersWithLabel(eastLatLng, "100");
  // MarkersWithLabel(westLatLng, "150");
  // MarkersWithLabel(southLatLng, "132");

  // create dengue cluster
  // var dengueKmlLayer = new google.maps.KmlLayer({
    // url: 'https://data.gov.sg/dataset/e7536645-6126-4358-b959-a02b22c6c473/resource/c1d04c0e-3926-40bc-8e97-2dfbb1c51c3a/download/denguecluster.kml',
    // map: map
  // });
}

initMap();
