$(document).ready(function () {
  /**
   * Dropdowns.
   * Slides dropdown menu's for nice & smooth effect.
   * Improves the UI and makes the website more cohesive.
   */
    $(".dropdown-toggle").on("click", function (e) {
        e.preventDefault();
        let menu = $(this).next()
        if($(menu).hasClass("menu-activated")){
            $(menu).slideUp();
            $(menu).removeClass("menu-activated");
        } else {
            $(menu).slideDown();
            $(menu).addClass("menu-activated");
        }
        });
});

/**
 * Adds the navigation menu to the html document by
 * appending the nav element.
 */
var nav = $("nav");
var navHTML = `

<div class="btn navbar-toggler" data="hamburger-menu" type="button" data-bs-toggle="collapse"
    data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false"
    aria-label="Click to view drop down menu" role="navigation">
    <div class="center-svg">
        <svg class="ham hamRotate ham1" viewBox="0 0 100 100" onclick="this.classList.toggle('active')">
        <path
              class="line top"
              d="m 30,33 h 40 c 0,0 9.044436,-0.654587 9.044436,-8.508902 0,-7.854315 -8.024349,-11.958003 -14.89975,-10.85914 -6.875401,1.098863 -13.637059,4.171617 -13.637059,16.368042 v 40" />
        <path
              class="line middle"
              d="m 30,50 h 40" />
        <path
              class="line bottom"
              d="m 30,67 h 40 c 12.796276,0 15.357889,-11.717785 15.357889,-26.851538 0,-15.133752 -4.786586,-27.274118 -16.667516,-27.274118 -11.88093,0 -18.499247,6.994427 -18.435284,17.125656 l 0.252538,40" />
      </svg>
    </div>
</div>
<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <ul class="mx-sm-1 mx-auto navbar-nav">
        <li class="nav-link"><a>About</a>
        </li>
        <li class="nav-link"><a>Menu</a>
        </li>
        <li class="nav-link"><a>Reserve</a>
        </li>
        <li class="nav-link"><a>Order</a>
        </li>
        <li class="nav-link">
        <div class="dropdown">
          <a class="dropdown-toggle" href="#" role="button" id="account-dropdown" data-toggle="dropdown" aria-expanded="false">
            Account
          </a>
          <ul class="dropdown-menu" aria-labelledby="account-dropdown">
            <li><a class="dropdown-item" href="#">Sign In</a></li>
            <li><a class="dropdown-item" href="#">Sign up</a></li>
          </ul>
        </div>
        </li>
    </ul>
    <ul class="mx-auto navbar-nav nav-social d-sm-flex flex-row">
        <li class="nav-link" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Facebook"><a href="#" class="text-decoration-none" target="_blank" rel="noopener" aria-label="Click here to go to our Facebook page"><i
                                class="
                fa-brands fa-facebook-f"></i></a>
        </li>
        <li class="nav-link" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Instagram"><a href="#" class="text-decoration-none" target="_blank" rel="noopener"
                            aria-label="Click here to go to our Instagram page"><i
                                class="
                fa-brands fa-instagram"></i></a>
        </li>
        <li class="nav-link" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Twitter"><a href="#" class="text-decoration-none" target="_blank" rel="noopener"
                            aria-label="Click here to go to our Twitter page"><i
                                class="fa-brands fa-twitter"></i></a>
        </li>
        <li class="nav-link" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Call Now"><a href="tel://0209126583" class="text-decoration-none" target="_blank" rel="noopener"
                            aria-label="Click here to give us a call"><i class="fa-solid fa-phone"></i></a>
        </li>
    </ul>
</div>
`;

nav.append(navHTML);

$(window).on("scroll", function () {
  let navWrapper = nav.parent();
  if (this.window.scrollY > 50) {
    navWrapper.addClass("nav-bg");
  }
  if (this.window.scrollY < 50) {
    navWrapper.removeClass("nav-bg");
  }
});
