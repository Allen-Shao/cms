//Markers function
/**
 * Make a marker on the map along with a label
 * @param location the location of the marker
 * @param labelText text to be displayed on the label
 * @param markerIcon icon for the marker
 * @param size size of the text
 * @param markers_type
 * @constructor
 */
function MarkersWithLabel(location, labelText, markerIcon, size, markers_type) {
    var label = new MapLabel({
        text: labelText,
        position: location,
        map: null,
        fontSize: size,
        align: 'center'
    });
    var marker = new google.maps.Marker({
        position: location,
        map: null,
        icon: markerIcon
    });
    marker.bindTo('map', label);
    marker.bindTo('position', label);
    marker.setDraggable(false);
    marker.clickable = false;
    //Display only psi by default
    if (size == 30) {
        marker.setMap(map);
    }
    markers_type.push(marker);
}

/**
 * Display the markers on the map
 *
 * @param markers_type list of all the markers
 */
function showMarkers(markers_type) {
    var i;
    for (i = 0; i < markers_type.length; i++) {
        markers_type[i].setMap(map);
    }
}

/**
 * Hide the markers on the map
 *
 * @param markers_type list of all the markers
 */
function hideMarkers(markers_type) {
    var i;
    for (i = 0; i < markers_type.length; i++) {
        markers_type[i].setMap(null);
    }
}

/**
 * Toggling the map to the weather section
 */
function weatherButtonClicked() {
    //display weather markers
    showMarkers(markers_weather);
    //hide psi markers and dengue kml
    hideMarkers(markers_psi);
    dengueKmlLayer.setMap(null);
}

/**
 * Toggling the map to the PSI section
 */
function psiButtonClicked() {
    //display weather markers
    showMarkers(markers_psi);
    //hide psi markers and dengue kml
    hideMarkers(markers_weather);
    dengueKmlLayer.setMap(null);
}

/**
 * Showing the dengue hotspots and toggling off the weather and psi section
 */
function dengueButtonClicked() {
    //display weather markers
    dengueKmlLayer.setMap(map);
    //hide psi markers and dengue kml
    hideMarkers(markers_psi);
    hideMarkers(markers_weather);
}

var map, psiIcon;

var northLatLng;
var centralLatLng;
var eastLatLng;
var westLatLng;
var southLatLng;

var markers_weather = [];
var markers_psi = [];
var dengueKmlLayer;

/**
 * Initializing the map
 */
function initMap() {
    // create map
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: new google.maps.LatLng(1.354241, 103.82000),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        streetViewControl: false,
        scrollwheel: false
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


    //create dengue cluster
    dengueKmlLayer = new google.maps.KmlLayer({
        url: "https://ref.data.gov.sg/common/Handler.ashx?ThemeName=DENGUE_CLUSTER&Format=kml&MetaDataID=228454",
        // url: 'https://data.gov.sg/dataset/e7536645-6126-4358-b959-a02b22c6c473/resource/c1d04c0e-3926-40bc-8e97-2dfbb1c51c3a/download/denguecluster.kml',
        map: null
    });
}

initMap();
