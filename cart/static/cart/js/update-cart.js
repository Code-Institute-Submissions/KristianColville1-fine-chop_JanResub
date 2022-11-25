// Update quantity on click
$("a.update-link").click(function (e) {
    var form = $(".update-form");
    form.submit();
});

// Remove item from cart and reload on click
$(".remove-item").click(function (e) {
    /* collects csrf_token */
    let csrfToken = $("input[name=csrfmiddlewaretoken]").val();
    var foodID = $(this).attr("id").split("remove_")[1];
    var portion_size = $(this).data("portion_size");
    var url = `/cart/remove/${foodID}/`;
    var data = { csrfmiddlewaretoken: csrfToken, portion_size: portion_size };

    $.post(url, data).done(function () {
        location.reload();
    });
});
