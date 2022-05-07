function autoheight(element) {
    let el = document.getElementById(element);
        el.style.height = "5px";
        el.style.height = (el.scrollHeight)+"px";
}
