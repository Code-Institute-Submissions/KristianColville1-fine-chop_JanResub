$(document).ready(function () {
    /**
     * Set a timer and display these images on the home page and iterate 
     * through them. Called using iterateSlideShow function.
     */
    let timeToDisplay = 10000;

    let slideshow = $("#home-bg-slideshow");
    const urls = [
        "../static/img/home-page/home-2.webp",
        "../static/img/home-page/home-3.webp",
        "../static/img/home-page/home-4.webp",
        "../static/img/home-page/home-1.webp",
    ];

    let index = 0;
    let transition = function () {
        var url = urls[index];
        slideshow.css("background", "url(" + url + ") no-repeat center center");
        slideshow.css("background-size", "cover");
        index++;
        if (index > urls.length - 1) {
            index = 0;
        }
    };

    const iterateSlideShow = function () {
        transition();
        slideshow.fadeIn("slow", function () {
            setTimeout(function () {
                slideshow.fadeOut("fast", iterateSlideShow);
            }, timeToDisplay);
        });
    };

    iterateSlideShow();
});
