$(document).ready(function () {
    var tooltipTriggerList = [].slice.call(
        document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    $('.toast').toast('show');
});

/**
 * Alerts the user of messages and fades into the background
 */
setTimeout(() => {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);

    if ($("#msg").length > 0) {
        alert.close();
    }
}, 3200);

$(".back-to-top-btn").click(function (e) {
    window.scrollTo(0, 0);
});