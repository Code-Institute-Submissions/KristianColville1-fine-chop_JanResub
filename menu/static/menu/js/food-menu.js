$(document).ready(function () {
    /**
     * Secondary menu - food menu
     * adds an active class to the food menu link with the correct url
     * helps the user identify the page they are on and what menu they are
     * currently viewing
     */

    const foodMenus = [
        "starters",
        "mains",
        "noodles",
        "rices",
        "wok",
        "soups",
        "vegan",
        "salads",
        "sides",
        "drinks",
    ];
    let stringURL = location.href;
    let classToCall = "";
    for (let i = 0; i < foodMenus.length; i++) {
        if (stringURL.includes(foodMenus[i])) {
            classToCall = foodMenus[i];
            $(`.${classToCall}`).addClass("food-menu-active");
        }
    }


});