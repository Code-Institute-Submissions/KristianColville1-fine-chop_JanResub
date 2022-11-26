// Disable +/- buttons outside 1-20 range
function handleInputs(foodID) {
    var currentValue = parseInt($(`#id_qty_${foodID}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 19;
    $(`#decrement-qty_${foodID}`).prop("disabled", minusDisabled);
    $(`#increment-qty_${foodID}`).prop("disabled", plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $(".qty_input");
for (var i = 0; i < allQtyInputs.length; i++) {
    var foodID = $(allQtyInputs[i]).data("item_id");
    handleInputs(foodID);
}

// Check enable/disable every time the input is changed
$(".qty_input").change(function () {
    var foodID = $(this).data("item_id");
    handleInputs(foodID);
});

// Increment quantity
$(".increment-qty").click(function (e) {
    e.preventDefault();
    var closestInput = $(this).closest(".input-group").find(".qty_input")[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var foodID = $(this).data("item_id");
    handleInputs(foodID);
});

// Decrement quantity
$(".decrement-qty").click(function (e) {
    e.preventDefault();
    var closestInput = $(this).closest(".input-group").find(".qty_input")[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var foodID = $(this).data("item_id");
    handleInputs(foodID);
});

// if user tries to manually input a number above 20
$(function () {
    $(".qty_input").keydown(function () {
        // Save the old value
        if (
            !$(this).val() ||
            (parseInt($(this).val()) <= 20 && parseInt($(this).val()) >= 0)
        )
            $(this).data("old", $(this).val());
    });
    $(".qty_input").keyup(function () {
        // Check correct, otherwise revert back to old value.
        if (
            !$(this).val() ||
            (parseInt($(this).val()) <= 20 && parseInt($(this).val()) >= 0)
        );
        else $(this).val($(this).data("old"));
    });
});

// automatically removes the amount if above 20 when user enters their cart
$(function () {
    allQtyInputs = $(".qty_input");
    for (let i = 0; i < allQtyInputs.length; i++){
        if ($(allQtyInputs[i]).val() > 20) {
            let form = $(allQtyInputs[i]).closest("form");
            $(allQtyInputs[i]).val(20);
            form.submit()
        }
    }
})