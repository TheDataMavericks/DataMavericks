function addMakesOfCars(){

var makesUrl = '/makes';
var makeData;

// load state drop down from Flask Route

Plotly.d3.json(makesUrl,function(error,makeData){
  if (error) {
    return console.warn(error);
};

  makeData[0].Makes.forEach(function(make) {
  Plotly.d3
      .select("#mark")
      .append('option')
      .attr('value', make)
    //   .attr('class', 'dropdown')
      .text(make)
});

})
 
}

function makePrediction() {
    $("button#predict").click(function(e){
        e.preventDefault();
        /*Get for variabes*/
        var mileage = $("#mileage").val(), year = $("#year_model").val(), make = $("#mark").val();
        var fiscal_power = $("#fiscal_power").val(), fuel_type = $("#fuel_type").val();
        /*create the JSON object*/
        // var data = {"Mileage":mileage, "Year":year_model, "Make":mark, "fiscal_power":fiscal_power, "fuel_type":fuel_type}
        var data = {"Mileage":mileage, "Year":year, "Make":make}
        // alert(data);
        /*send the ajax request*/
        $.ajax({
            method : "POST",
            url : window.location.href + 'api',
            data : $('form').serialize(),
            success : function(result){
                var json_result = JSON.parse(result);
                var price = json_result['Price'];
                swal('Estimated price is '+price+' $', '','success')
            },
            error : function(){
                console.log("error")
            }
        })
    })


}





// addUserPreferenceSelection()