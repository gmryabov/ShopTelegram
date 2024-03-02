let subMenu = false;
let active = true;

function credit() {
    const infoCredit = document.querySelector("#credit-info");
    const overlay = document.querySelector("#overlay");
    infoCredit.style.transform = "translate(0, 0)"
    overlay.style.opacity = "1";
    overlay.style.display = "block";
    overlay.style.zIndex = "999";
}

function closeCredit() {
    const infoCredit = document.querySelector("#credit-info");
    const overlay = document.querySelector("#overlay");
    infoCredit.style.transform = "translate(-150%, 0px)"
    overlay.style.opacity = "0";
    overlay.style.zIndex = "-999";
}

function closeMenu(main) {
    const bar = document.getElementsByClassName("bar-bottom")[0];
    let link = document.getElementsByClassName("link active")[0];
    bar.style.transform = "translateY(95vh)";
    link.classList.remove("active")
    let link_inner = main.getElementsByClassName("link")[0];
    link_inner.classList.add("active")
}

function menuItems(menuItem) {
    const catalog = document.getElementById("categories");
    const contact = document.getElementById("contact_inner");
    let cart = document.getElementById("cart_inner");
    const menu_items = {"catalog": catalog, "cart": cart, "contact": contact};
    const main = document.getElementById("main")
    const subCategories = document.querySelector(`.sub-categories`);
    let sub_cat = subCategories.querySelectorAll('.sub-categories > *');
    const backSub = subCategories.querySelector('.sub-back');
    const bar = document.getElementsByClassName("bar-bottom")[0];
    if (subMenu) {
        sub_cat.forEach((element)  => {
            subMenu = false;
            element.style.opacity = "0";
            element.style.zIndex = "0";
            setTimeout(() => {element.style.display = "none"}, 400)
        });
        backSub.style.opacity = "0";
        backSub.style.zIndex = "0";
        backSub.style.display = "none"
    }

    let link = document.getElementsByClassName("link active")[0];
    let check_item = menuItem.getElementsByClassName("link")[0].classList.contains('active');
    const link_inner = menuItem.getElementsByClassName("link")[0];
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

    for (let key in menu_items) {
        if (key === menuItem.id) {
            menu_items[key].style.opacity = "1"
            menu_items[key].style.zIndex = "100"
        }
        else {
            menu_items[key].style.opacity = "0"
            menu_items[key].style.zIndex = "0"
        }
    }
}

function choose(catItem) {
    const catalog = document.getElementById("categories");
    const subCategories = document.querySelector(`.sub-categories`);
    const backSub = subCategories.querySelector('.sub-back');
    let sub_cat = subCategories.querySelectorAll('.sub-categories > *');
    sub_cat.forEach((element)  => {
        if (element.classList.contains(`${catItem.id}`)) {
            element.style.display = "flex"
            element.style.opacity = "1";
            element.style.zIndex = "100";
            backSub.style.display = "flex"
        } else {
            if (element.classList.contains(`sub-back`)) {
                backSub.style.display = "flex"
                backSub.style.opacity = "1";
                backSub.style.zIndex = "100";

                catalog.style.opacity = "0";
                catalog.style.zIndex = "0";

                subMenu = true;
            } else {
            element.style.display = "none"
            }
        }
    });
}

function backToCat() {
    const catalog = document.getElementById("categories");
    const subCategories = document.querySelector(`.sub-categories`);
    let sub_cat = subCategories.querySelectorAll('.sub-categories > *');
    const backSub = subCategories.querySelector('.sub-back');
    sub_cat.forEach((element)  => {
        element.style.opacity = "0";
        element.style.zIndex = "0";
    });
    backSub.style.opacity = "0";
    backSub.style.zIndex = "0";

    catalog.style.opacity = "1";
    catalog.style.zIndex = "100";
}

function setImage(productImage) {
    const mainImage = document.getElementsByClassName("product-pic")[0]
    mainImage.src = productImage.src
    let images = document.querySelectorAll(".product-image")
    images.forEach(imag => {
        if (imag === productImage){
            imag.classList.add('active')
        } else {
            imag.classList.remove('active')
        }
    })
}

function subChoose(subItem) {
    let subItemTitle = subItem.innerHTML
    // console.log(subItemTitle)

    let arr = document.querySelectorAll(`.sub-prod`)
    console.log(arr)
    arr.forEach(elem => {
        console.log(elem)
        if (elem.id === subItemTitle) {
            console.log(elem)
        }
    })
}