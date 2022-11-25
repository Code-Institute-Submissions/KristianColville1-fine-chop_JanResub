// Update quantity on click
$(".update-link").click(function (e) {
    var form = $(this).prev(".update-form");
    form.submit();
});

// Remove item from cart and reload on click
$(".remove-item").click(function (e) {
    var csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    var itemId = $(this).attr("id").split("remove_")[1];
    var size = $(this).data("size");
    var url = `/cart/remove/${itemId}`;
    var data = { csrfmiddlewaretoken: csrfToken, size: size };

    $.post(url, data).done(function () {
        location.reload();
    });
});
