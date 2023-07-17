$(document).ready(function () {
    var table = $('#tableUsers').DataTable({
        dom: 'Blfrtip',
        buttons: [
            'copy', 'excel', {
                extend: 'pdfHtml5',
                orientation: 'landscape',
                pageSize: 'LEGAL'
            }
        ]
    });

    $('#tableUsers tbody').on('click', 'tr', function () {
        var data = table.row(this).data();
        displayModal("delete", data);

    });
});

function displayModal(which, data) {
    if(which == 'delete'){
        $('#modal_body').html(prepareHTML(data));
        $('#modal_title').html("Registry from: <b>" + data[1] + "</b>")
        $('#ModalModify').modal('show');
    }else if(which == 'add'){
        $('#ModalAdd').modal('show');
    }else if(which == 'update'){
        document.getElementById("formid2").value = document.getElementById("spanid").innerText;
        $('formid2').prop("disabled", true);
        document.getElementById("formuser2").value = document.getElementById("spanuser").innerText;
        document.getElementById("formpassword2").value = document.getElementById("spanpassword").innerText;
        document.getElementById("formworker2").checked = checkUncheck(document.getElementById("spanworker").innerText);
        document.getElementById("formstudent2").checked = checkUncheck(document.getElementById("spanstudent").innerText);
        document.getElementById("formincomes2").value = document.getElementById("spanincomes").innerText;
        $('#ModalUpdate').modal('show');
    }
}

function prepareHTML(data) {
    str = "id: <b><span id=\"spanid\">" + data[0] + "</span></b>\n<br>" +
        "user: <b><span id=\"spanuser\">" + data[1] + "</span></b>\n<br>" +
        "password: <b><span id=\"spanpassword\">" + data[2] + "</span></b>\n<br>" +
        "worker: <b><span id=\"spanworker\">" + data[3] + "</span></b>\n<br>" +
        "student: <b><span id=\"spanstudent\">" + data[4] + "</span></b>\n<br>" +
        "incomes: <b><span id=\"spanincomes\">" + data[5] + "</span></b>\n<br>";
    return str;
}

function deleteRegistry(){
    
}

function functionupdate(){
    
}

function checkUncheck(value){
    if(value == "1"){
        return true;
    }else if(value == "0"){
        return false;
    }
}