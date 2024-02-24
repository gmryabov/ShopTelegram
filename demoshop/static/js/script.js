const infoCredit = document.querySelector("#credit-info");
const overlay = document.querySelector("#overlay");
let subMenu = false;
const subCategories = document.querySelector(`.sub-categories`);
let sub_cat = subCategories.querySelectorAll('.sub-categories > *');
const backSub = subCategories.querySelector('.sub-back');

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

let active = true;
const main = document.getElementById("main")

const bar = document.getElementsByClassName("bar-bottom")[0];
const catalog = document.getElementById("categories");
const contact = document.getElementById("contact_inner");
let cart = document.getElementById("cart_inner");

// var barItems = document.getElementsByClassName("bar-items")[0]


function closeMenu(main) {
    let link = document.getElementsByClassName("link active")[0];
    bar.style.transform = "translateY(95vh)";
    link.classList.remove("active")
    let link_inner = main.getElementsByClassName("link")[0];
    link_inner.classList.add("active")
}

const menu_items = {"catalog": catalog, "cart": cart, "contact": contact};

function menuItems(menuItem) {
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
    sub_cat.forEach((element)  => {
        element.style.opacity = "0";
        element.style.zIndex = "0";
    });
    backSub.style.opacity = "0";
    backSub.style.zIndex = "0";

    catalog.style.opacity = "1";
    catalog.style.zIndex = "100";
}




const mainImage = document.getElementsByClassName("product-pic")[0]
const heBlock = document.getElementsByClassName("product-swipper")[0]
console.log(heBlock.style.height)
heBlock.style.height = `${mainImage.height}px`
function setImage(productImage) {
    let productPic = document.querySelectorAll(".product-pic")
    let picArr = Array.from(productPic)
    let images = document.querySelectorAll(".product-image")
    let arr = Array.from(images)
    images.forEach(image => {
        let activeImage = document.querySelector(".product-image.active")
        // mainImage.src = activeImage.src
        if (activeImage !== productImage) {
            activeImage.classList.remove("active")
            productImage.classList.add("active")

            let idx = arr.indexOf(productImage)

            picArr.forEach(cadr => {
                cadr.classList.remove("active")
            })
            picArr[idx].classList.add("active")
            // console.log(picArr[picArr.length-1])
            // picArr[idx-1].style.transform = `translate(${-115}%, 0)`
            // picArr[idx].style.transform = `translate(${0}%, 0)`
        }
    })

}
