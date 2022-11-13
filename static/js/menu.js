$(document).ready(function () {
    /**
     * Dropdowns.
     * Slides dropdown menu's for nice & smooth effect.
     * Improves the UI and makes the website more cohesive.
     */

    // Gets dropdowns
    const dropdowns = document.getElementsByClassName(".dropdown-menu");

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

    /**
     * Checks to see if the class allauth-wrapper exists and performs an 
     * action based on that behaviour for scrolling and adding a background
     * to the navigation menu.
     */

    let navWrapper = $(".nav-wrapper");
    let checkAllauthForm = document.getElementsByClassName("allauth-container");
    // if it does exist and there is an element with this class then add background
    if (checkAllauthForm.length != 0) {
        navWrapper.addClass("nav-bg");
    }
    window.addEventListener("scroll", function () {
        // nested condition if allauth wrapper class elements don't exist
        if (checkAllauthForm.length === 0) {
            if (this.window.scrollY > 50) {
                navWrapper.addClass("nav-bg");
            }
            if (this.window.scrollY < 50) {
                navWrapper.removeClass("nav-bg");
            }
        }
    });
    
});


