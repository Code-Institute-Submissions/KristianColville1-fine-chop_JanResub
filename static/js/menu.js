$(document).ready(function () {
    /**
     * Dropdowns.
     * Slides dropdown menu's for nice & smooth effect.
     * Improves the UI and makes the website more cohesive.
     */

    // when called slides up any open dropdowns
    let slideAllDropdownsUp = () => {
        $(".dropdown-menu").each(function () {
            $(this).slideUp().removeClass("menu-activated");
        });
    };

    // if the user mouse enters
    $(".dropdown-toggle").on("mouseenter", function (e) {
        e.preventDefault();
        let menu = $(this).next();
        if ($(menu).hasClass("menu-activated")) {
            $(menu).slideUp("slow").removeClass("menu-activated");
        } else {
            slideAllDropdownsUp(); // before sliding down new menu close others up
            $(menu).slideDown("fast").addClass("menu-activated");
        }
    });

    // if the mouse leaves
    $(".dropdown-menu").on("mouseleave", function (e) {
        e.preventDefault();
        let menu = $(this);
        $(menu).slideUp().removeClass("menu-activated");
    });
});

/**
 * Opens a search bar on the bottom of the screen for mobile users
 */
const openSmallSearchBar = function () {
    if ($(".small-search").hasClass("d-none")) {
        $(".small-search").fadeIn().removeClass("d-none");
    } else {
        $(".small-search").addClass("d-none");
    }
};
