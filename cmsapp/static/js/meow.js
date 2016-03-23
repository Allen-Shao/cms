// Source from
// http://aqicn.org/city/singapore/central/


var mapCityWidgetIsLoading = null;
var aqiLevelLabels = ['no data','Good','Moderate','Unhealthy<br><span style=\'font-size:18px;\'>for Sensitive Groups</span>','Unhealthy','Very Unhealthy','Hazardous',0];
function aqiToLevel( aqi )
{
if (aqi=="-") return 0;
if (aqi<=50) return 1;
if (aqi<=100) return 2;
if (aqi<=150) return 3;
if (aqi<=200) return 4;
if (aqi<=300) return 5;
return 6;
}git
function aqicnWidgetLoaderCallback( json )
{
log("Widget loaded... ");
clearTimeout(mapCityWidgetIsLoading);
mapCityWidgetIsLoading = null;
$("#citydivmain").html(json.xxl);
$("#citydivmain").removeClass("darken");
$('#citydivouter').removeClass('citydivloading');
var aqi = $("#aqiwgtmsg").html();
$("#aqiwgtmsg").html(aqiLevelLabels[aqiToLevel(aqi)]);
try
{
var utime= json.utime.en;
$("#aqiwgtutime").html(utime[0]);
var names= json.name.en;
$("#aqiwgttitle1").html("<b>"+names[0]+"</b>: ");
$("#aqiwgttitle2").html(names[1]);
}
catch (e)
{
log("aqicnWidgetLoaderCallback. Error ",e);
}
}
function mapOnClickCityWidget( f, x )
{
/* */
if (mapCityWidgetIsLoading!=null) return;
$("#citydivmain").addClass("darken");
$('#citydivouter').addClass('citydivloading');
mapCityWidgetIsLoading = setTimeout(function(){ 
mapCityWidgetIsLoading=null;
$("#citydivmain").removeClass("darken"); 
$('#citydivouter').removeClass('citydivloading');
log("Loading widget... timeout!");
},8000);
var script = document.createElement( 'script' );
script.type = 'text/javascript';
var url = "http://sg1.aqicn.org/aqicn/cache/webwgt/@"+x+"/widget.v1.js"
try { url += "?"+_mapqk(); } catch (e) {}
script.src = url;
document.getElementsByTagName('head')[0].appendChild(script);
log("Loading widget "+x+":",url);
}
