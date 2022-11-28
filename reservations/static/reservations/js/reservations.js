$('#id_guest_amount').val(2)

$("#id_guest_amount").change(function () {
    if ($(this).val() > 15) {
        $(this).val(15);
    }
    if ($(this).val() < 2) {
        $(this).val(2);
    }
});

var today = new Date();
var dd = String(today.getDate()).padStart(2, "0");
var mm = String(today.getMonth() + 1).padStart(2, "0");
var yyyy = today.getFullYear();

today = yyyy + "-" + mm + "-" + dd;
$("#id_date").attr("min", today);