function initMap() {
  // create map
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: {lat: 1.354241, lng: 103.819417}
  });

  // create marker
  var marker = new google.maps.Marker({
    position: {lat: 1.354241, lng: 103.819417},
    map: map,
    title: 'Hello World!'
  });

  // create dengue cluster
  var dengueKmlLayer = new google.maps.KmlLayer({
    url: 'https://data.gov.sg/dataset/e7536645-6126-4358-b959-a02b22c6c473/resource/c1d04c0e-3926-40bc-8e97-2dfbb1c51c3a/download/denguecluster.kml',
    map: map
  });
}
