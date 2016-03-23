 updatePSI();

 function updatePSI() {
  $.ajax({
    type: "GET",
    dataType: "xml",
    url: "http://www.nea.gov.sg/api/WebAPI?dataset=psi_update&keyref=781CF461BB6606AD0308169EFFAA8231021BA33828C73DAE",
    success: function(data){
      console.log(data.getElementsByTagName("region")[1].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value')); // Overall PSI

      console.log(data.getElementsByTagName("region")[0].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value')); // North

      console.log(data.getElementsByTagName("region")[2].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value')); // Central

      console.log(data.getElementsByTagName("region")[3].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value')); // East

      console.log(data.getElementsByTagName("region")[4].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value')); // West

      console.log(data.getElementsByTagName("region")[5].getElementsByTagName("record")[0].getElementsByTagName("reading")[0].getAttribute('value')); // South
    },
    error: function(error) {
      console.log(error);
    }
  });
}
