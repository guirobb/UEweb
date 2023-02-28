function enableEditCompany(ident, name)
{
    console.log(ident, name)
    let el = document.getElementById(`edit_name-${ident}`);
    let el2 = document.getElementById(`label_name-${ident}`);

    el.classList.remove("hidden");
    el2.classList.add("hidden");
}