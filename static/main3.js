var key = ""

$(document).ready(function(){
    var url = document.getElementById('url').innerHTML;
    var headers = document.getElementById('headers').innerHTML;
    console.log(url);
    console.log(headers);
    console.log(document.getElementById('columns').innerHTML);
    var table = $('#tableCustom').DataTable({
        //B parameter is for buttons, l parameter is for show entries
        dom: 'Blfrtip',
        buttons: [
            document.getElementById('copy').innerHTML, document.getElementById('excel').innerHTML, document.getElementById('pdf').innerHTML
        ],
        columns: setColumns(document.getElementById('columns').innerHTML),

        ajax : {
            method: 'GET',
            url: url,
            headers: { 'X-Api-Key': headers},
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

function setColumns(columns){
    let jsonArray = [];
    columns = columns.replace(/'/g, '"');
    arrayColumns = JSON.parse(columns);

    arrayColumns.forEach(function(value) {
        let obj = { "data": value };
        jsonArray.push(obj);
    })
    console.log(jsonArray)
    return jsonArray;
}

function showAPIKey(){
    alert("Your key is: " + localStorage.getItem("API-Key"));
}

function saveAPIKey(){
    key = document.getElementById('form-APIKey').value;
    localStorage.setItem("API-Key", key)
    alert("API KEY saved.")
    console.log("saving this: " + document.getElementById('form-APIKey').value);
}

// columnas = [{ "data": "city_mpg" },
// { "data": "class" },
// { "data": "combination_mpg" },
// { "data": "cylinders" },
// { "data": "displacement" },
// { "data": "drive" },
// { "data": "fuel_type" },
// { "data": "highway_mpg" },
// { "data": "make" },
// { "data": "model" },
// { "data": "transmission" },
// { "data": "year" }]