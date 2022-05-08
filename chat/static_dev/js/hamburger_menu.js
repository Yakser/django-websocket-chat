const Menu = () => {
  let x = document.getElementById("myLinks");
  x.style.height = `${ x.scrollHeight }px`;
  window.getComputedStyle(x, null).getPropertyValue("height");
  x.style.height = "0px";


  setTimeout(function () {
    x.style.display = "block";
  }, 500);

  x.addEventListener("transitionend", () => {
    if (x.style.height != "0px") {
      x.style.height = "auto"
    }
  });

  document.getElementById('js-menu').addEventListener('click', () => {
    console.log(123)
    if (x.style.height == "0px") {
      x.style.height = `${ x.scrollHeight }px`
    } else {
      x.style.height = `${ x.scrollHeight }px`;
      window.getComputedStyle(x, null).getPropertyValue("height");
      x.style.height = "0px";
    }
  });
}

Menu();