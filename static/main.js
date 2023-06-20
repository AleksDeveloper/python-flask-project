// async function testJSONData() {
//     const response = await fetch('https://api.api-ninjas.com/v1/cars?model=element', {
//         method: 'GET',
//         headers: {
//             'X-Api-Key': 'ZEzlCg1B8mGFFTxttPY5Q7f0tspHHqIrxQU9KE4W'
//         },
//         contentType: 'application/json',
//         success: function(result){
//             console.log(result);
//         },
//         error: function ajaxError(jqXHR) {
//             console.error('Error: ', jqXHR.responseText);
//         },
//         mode: "no-cors",
        
//     });
//     return response.json();
// }

// console.log(testJSONData());

headerss = { 'X-Api-Key': 'ZEzlCg1B8mGFFTxttPY5Q7f0tspHHqIrxQU9KE4W'}

columnas = [{ "data": "city_mpg" },
{ "data": "class" },
{ "data": "combination_mpg" },
{ "data": "cylinders" },
{ "data": "displacement" },
{ "data": "drive" },
{ "data": "fuel_type" },
{ "data": "highway_mpg" },
{ "data": "make" },
{ "data": "model" },
{ "data": "transmission" },
{ "data": "year" }]


$(document).ready(function(){
    var url = createURL(document.getElementById('make').innerHTML,document.getElementById('model').innerHTML, 
                        document.getElementById('year').innerHTML, document.getElementById('cylinders').innerHTML,
                        document.getElementById('fuel_type').innerHTML, document.getElementById('drive').innerHTML,
                         document.getElementById('limit').innerHTML);
    console.log(url);
    var table = $('#tableCars').DataTable({
        //B parameter is for buttons, l parameter is for show entries
        dom: 'Blfrtip',
        buttons: [
            'copy', 'excel',{
                extend: 'pdfHtml5',
                orientation: 'landscape',
                pageSize: 'LEGAL'
            }
        ],
        columns: columnas,

        ajax : {
            method: 'GET',
            url: url,
            headers: headerss,
            dataSrc: function (json) {
                var data = JSON.parse(json.d);
                console.log(data);
                console.log(data.data);
                return data.data;
            },
            contentType: 'application/json',
            success: function(result){
                console.log(result);
                table.rows.add(result).draw();
            },
            error: function ajaxError(jqXHR) {
                console.error('Error: ', jqXHR.responseText);
            }
        }
    });
});


function createURL(make, model, year, cylinders, fuel_type, drive, limit){
    console.log(make, model, year, cylinders, fuel_type, drive, limit)
    url = 'https://api.api-ninjas.com/v1/cars?limit=50&model=element';
    if(make === "None" && model ==="None" && year ==="None" && cylinders ==="None" && fuel_type ==="None" && drive ==="None" && limit === "None"){
        console.log("entro")
        url = 'https://api.api-ninjas.com/v1/cars?limit=50&model=element';
    }else{
        url = 'https://api.api-ninjas.com/v1/cars?limit='+limit+"&make="+make+"&model="+model+"&year="+year+"&cylinders="+cylinders+"&fuel_type="+fuel_type+"&drive="+drive;
        console.log("CREATED THIS URL: " + url);
    }
    return url;
}
