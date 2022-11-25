$(document).ready(function () {
    /**
     * Set a timer and display these images on the home page and iterate
     * through them. Called using iterateSlideShow function.
     */
    let timeToDisplay = 10000;

    let slideshow = $("#home-bg-slideshow");
    const imageClasses = [
        "home-img-1",
        "home-img-2",
        "home-img-3",
        "home-img-4",
    ];

    let index = 0;
    var lastImage = '';
    let transition = function () {
        let current = imageClasses[index]
        slideshow.addClass(current);
        slideshow.removeClass(lastImage);
        lastImage = current;
        index++;
        if (index > imageClasses.length - 1) {
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
