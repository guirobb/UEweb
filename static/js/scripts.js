function enableEditCompany(ident, name)
{
    // console.log(ident, name)
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);
    let el3 = document.getElementById(`save_btn-${ident}`);
    let el4 = document.getElementById(`delete_btn-${ident}`);
    let el5 = document.getElementById(`edit_btn-${ident}`);
    let el6 = document.getElementById(`discardEditCompany_btn-${ident}`);

    el.classList.remove("hidden");
    el2.classList.add("hidden");
    el3.classList.remove("hidden");
    el4.classList.add("hidden");
    el5.classList.add("hidden");
    el6.classList.remove("hidden");
}

function saveChangesCompany(ident){
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);
    let el3 = document.getElementById(`save_btn-${ident}`);
    let el4 = document.getElementById(`delete_btn-${ident}`);
    let el5 = document.getElementById(`edit_btn-${ident}`);
    let el6 = document.getElementById(`discardEditCompany_btn-${ident}`);

    el.classList.add("hidden");
    el2.classList.remove("hidden");
    el3.classList.add("hidden");
    el4.classList.remove("hidden");
    el5.classList.remove("hidden");
    el6.classList.add("hidden");
}