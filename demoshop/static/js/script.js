var infoCredit = document.querySelector("#credit-info");
var overlay = document.querySelector("#overlay");
var subMenu = false;
var subCategories = document.querySelector(`.sub-categories`);
var sub_cat = subCategories.querySelectorAll('.sub-categories > *');
var backSub = subCategories.querySelector('.sub-back')



function isStyleEqual(element, styleProperty, value) {
  var computedStyle = window.getComputedStyle(element);
  var computedValue = computedStyle.getPropertyValue(styleProperty);
  return computedValue === value;
}


function credit() {
    infoCredit.style.transform = "translate(0, 0)"
    overlay.style.opacity = "1";
    overlay.style.display = "block";
    overlay.style.zIndex = "999";
}
function closeCredit() {
    infoCredit.style.transform = "translate(-150%, 0px)"
    overlay.style.opacity = "0";
    overlay.style.zIndex = "-999";
}

var active = true;
const main = document.getElementById("main")

var bar = document.getElementsByClassName("bar-bottom")[0]
var catalog = document.getElementById("categories")
var contact = document.getElementById("contact_inner")
var cart = document.getElementById("cart_inner")
var barItems = document.getElementsByClassName("bar-items")[0]


function closeMenu(main) {
    var link = document.getElementsByClassName("link active")[0]
    bar.style.transform = "translateY(95vh)";
    link.classList.remove("active")
    var link_inner = main.getElementsByClassName("link")[0]
    link_inner.classList.add("active")
    return;
}

var menu_items = {"catalog": catalog, "cart": cart, "contact": contact};
function menuItems(menuItem) {
    if (subMenu) {
        sub_cat.forEach((element)  => {
            subMenu = false;
            console.log(subMenu)
            element.style.opacity = "0";
            element.style.zIndex = "0";
        });
        backSub.style.opacity = "0";
        backSub.style.zIndex = "0";
    }

    var link = document.getElementsByClassName("link active")[0]
    var check_item = menuItem.getElementsByClassName("link")[0].classList.contains('active')
    var link_inner = menuItem.getElementsByClassName("link")[0]
    if (check_item) {
        active = true;
        bar.style.transform = "translateY(95vh)";
        link_inner.classList.remove("active")
        main.getElementsByClassName("link")[0].classList.add("active")
        menu_items[menuItem.id].style.opacity = "0"
        return;
    }
    link.classList.remove("active")
    link_inner.classList.add("active")
    if (active) {
        bar.style.transform = "translateY(4vh)";
    }

    for (var key in menu_items) {
        if (key === menuItem.id) {
            menu_items[key].style.opacity = "1"
            menu_items[key].style.zIndex = "100"
        }
        else {
            menu_items[key].style.opacity = "0"
            menu_items[key].style.zIndex = "0"
        }
    }
    return;
}


function choose(catItem) {
    var sub_cat = subCategories.querySelectorAll('.sub-categories > *');
    var backSub = subCategories.querySelector('.sub-back')
    console.log(backSub)
    sub_cat.forEach((element)  => {
        if (element.classList.contains(`${catItem.id}`)) {
            element.style.opacity = "1";
            element.style.zIndex = "100";
        }
    });
        backSub.style.opacity = "1";
        backSub.style.zIndex = "100";

        catalog.style.opacity = "0";
        catalog.style.zIndex = "0";

        subMenu = true;
}