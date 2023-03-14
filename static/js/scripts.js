function enableEdit(ident, name)
{
    // console.log(ident, name)
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);
    let el3 = document.getElementById(`save_btn-${ident}`);
    let el4 = document.getElementById(`delete_btn-${ident}`);
    let el5 = document.getElementById(`edit_btn-${ident}`);
    let el6 = document.getElementById(`discardEdit_btn-${ident}`);
    let el7 = document.getElementById(`labelTaf_director-${ident}`);
    let el8 = document.getElementById(`editTafInput_director-${ident}`);

    el.classList.remove("hidden");
    el2.classList.add("hidden");
    el3.classList.remove("hidden");
    el4.classList.add("hidden");
    el5.classList.add("hidden");
    el6.classList.remove("hidden");
    el7 != undefined ? el7.classList.add("hidden") : false;
    el8 != undefined ? el8.classList.remove("hidden") : false;
}

function saveChanges(ident){
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);
    let el3 = document.getElementById(`save_btn-${ident}`);
    let el4 = document.getElementById(`delete_btn-${ident}`);
    let el5 = document.getElementById(`edit_btn-${ident}`);
    let el6 = document.getElementById(`discardEdit_btn-${ident}`);
    let el7 = document.getElementById(`labelTaf_director-${ident}`);
    let el8 = document.getElementById(`editTafInput_director-${ident}`);
    var responsable = "rr";
    el.classList.add("hidden");
    console.log(el2.innerText);
    el2.innerText=el.getElementsByClassName("form-control")[0].value;
    el2.classList.remove("hidden");
    el3.classList.add("hidden");
    el4.classList.remove("hidden");
    el5.classList.remove("hidden");
    el6.classList.add("hidden");
    el7 != undefined ? el7.classList.remove("hidden") : false;
    el8 != undefined ? el8.classList.add("hidden") : false;
    if (el8===undefined) {

    }
    else {
        responsable=el8.getElementsByClassName("form-control")[0].value;
        el7.innerText= el8.getElementsByClassName("form-control")[0].value;
    }


    let xhr = new XMLHttpRequest();
    let url = "../../update/taf";

    // open a connection
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            // Print received data from server

        }
    };

    // Converting JSON data to string
    var data = JSON.stringify({ "id": ident, "name": el.getElementsByClassName("form-control")[0].value, "responsable": responsable});

    // Sending data with the request
    xhr.send(data);

}

function saveChanges(ident){
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);
    let el3 = document.getElementById(`save_btn-${ident}`);
    let el4 = document.getElementById(`delete_btn-${ident}`);
    let el5 = document.getElementById(`edit_btn-${ident}`);
    let el6 = document.getElementById(`discardEdit_btn-${ident}`);
    let el7 = document.getElementById(`labelTaf_director-${ident}`);
    let el8 = document.getElementById(`editTafInput_director-${ident}`);
    var responsable = "rr";
    el.classList.add("hidden");
    console.log(el2.innerText);
    el2.innerText=el.getElementsByClassName("form-control")[0].value;
    el2.classList.remove("hidden");
    el3.classList.add("hidden");
    el4.classList.remove("hidden");
    el5.classList.remove("hidden");
    el6.classList.add("hidden");
    el7 != undefined ? el7.classList.remove("hidden") : false;
    el8 != undefined ? el8.classList.add("hidden") : false;
    if (el8===undefined || el8===null) {
        let xhr = new XMLHttpRequest();
        let url = "../../update/enterprise";
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
            }
        };
        var data = JSON.stringify({ "id": ident, "name": el.getElementsByClassName("form-control")[0].value});
        xhr.send(data);
        console.log("updateEnterprise")
    }
    else {
        responsable=el8.getElementsByClassName("form-control")[0].value;
        el7.innerText= el8.getElementsByClassName("form-control")[0].value;
        let xhr = new XMLHttpRequest();
        let url = "../../update/taf";
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
            }
        };
        var data = JSON.stringify({ "id": ident, "name": el.getElementsByClassName("form-control")[0].value, "responsable": responsable});
        xhr.send(data);
    }




}

function deleteStudent(id) {
    console.log(id);
    let el = document.getElementById(`student-${id}`);

    let xhr = new XMLHttpRequest();
    let url = "../../delete/student";

    // open a connection
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            // Print received data from server

        }
    };

    // Converting JSON data to string
    var data = JSON.stringify({ "id": id});

    // Sending data with the request
    xhr.send(data);
    el.classList.add("hidden");
}

function verifyStudent(student,filter) {
    return (student.taf1==filter.taf || student.taf2==filter.taf)
}

function enableEditPromo(ident, name)
{
    // console.log(ident, name)
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);
    let el3 = document.getElementById(`save_btn-${ident}`);
    let el4 = document.getElementById(`delete_btn-${ident}`);
    let el5 = document.getElementById(`edit_btn-${ident}`);
    let el6 = document.getElementById(`discardEdit_btn-${ident}`);
    let el7 = document.getElementById(`labelTaf_director-${ident}`);
    let el8 = document.getElementById(`editTafInput_director-${ident}`);

    el.classList.remove("hidden");
    el2.classList.add("hidden");
    el3.classList.remove("hidden");
    el4.classList.add("hidden");
    el5.classList.add("hidden");
    el6.classList.remove("hidden");
    el7 != undefined ? el7.classList.add("hidden") : false;
    el8 != undefined ? el8.classList.remove("hidden") : false;
}

function saveChangesPromos(ident){
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);
    let el3 = document.getElementById(`save_btn-${ident}`);
    let el4 = document.getElementById(`delete_btn-${ident}`);
    let el5 = document.getElementById(`edit_btn-${ident}`);
    let el6 = document.getElementById(`discardEdit_btn-${ident}`);
    el.classList.add("hidden");
    console.log(el2.innerText);
    el2.innerText=el.getElementsByClassName("form-control")[0].value;
    el2.classList.remove("hidden");
    el3.classList.add("hidden");
    el4.classList.remove("hidden");
    el5.classList.remove("hidden");
    el6.classList.add("hidden");


    let xhr = new XMLHttpRequest();
    let url = "../../update/promo";

    // open a connection
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            // Print received data from server

        }
    };

    // Converting JSON data to string
    console.log("aa")
    var data = JSON.stringify({ "id": ident, "annee": el.getElementsByClassName("form-control")[0].value});
    console.log("bb")
    // Sending data with the request
    xhr.send(data);

}


function deletePromo(id) {
    console.log(id);
    let el = document.getElementById(`promo-${id}`);
    let xhr = new XMLHttpRequest();
    let url = "../../delete/promo";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
        }
    };
    var data = JSON.stringify({ "id": id});
    xhr.send(data);
    el.classList.add("hidden");
}

function deleteEnterprise(id) {
    console.log(id);
    let el = document.getElementById(`company-${id}`);
    let xhr = new XMLHttpRequest();
    let url = "../../delete/enterprise";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
        }
    };
    var data = JSON.stringify({ "id": id});
    xhr.send(data);
    el.classList.add("hidden");
}

function deleteTaf(id) {
    console.log(id);
    let el = document.getElementById(`taf-${id}`);
    let xhr = new XMLHttpRequest();
    let url = "../../delete/taf";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
        }
    };
    var data = JSON.stringify({ "id": id});
    xhr.send(data);
    el.classList.add("hidden");
}
