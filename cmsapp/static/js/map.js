function initMap() {
  // create map
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: {lat: 1.354241, lng: 103.819417}
  });

  // psi icon
  var psiIcon = {
    url: "http://cdn8.staztic.com/app/a/2742/2742678/psi-malaysia-haze-5-l-140x140.png",
    // url: "http://10.27.161.249:8888/static/images/psi_marker_40.png",
    scaledSize: new google.maps.Size(40, 40)
  };

  // create marker
  // var marker = new MarkerWithLabel({
  //   position: {lat: 1.354241, lng: 103.819417},
  //   map: map,
  //   draggable: false,
  //   labelContent: "59",
  //   icon: psiIcon
  // });

  var rNO = new google.maps.Marker({
    position: {lat: 1.41803, lng: 103.82000},
    map: map,
    title: 'Hello World!',
    icon: psiIcon
  });

  var rCE = new google.maps.Marker({
    position: {lat: 1.35735, lng: 103.82000},
    map: map,
    title: 'Hello World!',
    icon: psiIcon
  });

  var rEA = new google.maps.Marker({
    position: {lat: 1.35735, lng: 103.94000},
    map: map,
    title: 'Hello World!',
    icon: psiIcon
  });

  var rWE = new google.maps.Marker({
    position: {lat: 1.35735, lng: 103.70000},
    map: map,
    title: 'Hello World!',
    icon: psiIcon
  });

  var rSO = new google.maps.Marker({
    position: {lat: 1.29587, lng: 103.82000},
    map: map,
    title: 'Hello World!',
    icon: psiIcon
  });

  // create dengue cluster
  var dengueKmlLayer = new google.maps.KmlLayer({
    url: 'https://data.gov.sg/dataset/e7536645-6126-4358-b959-a02b22c6c473/resource/c1d04c0e-3926-40bc-8e97-2dfbb1c51c3a/download/denguecluster.kml',
    map: map
  });
}
