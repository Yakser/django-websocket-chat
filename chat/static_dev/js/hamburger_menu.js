let x = document.getElementById("myLinks");
x.style.height = `${ x.scrollHeight }px`;
window.getComputedStyle(x, null).getPropertyValue("height");
x.style.height = "0px";


setTimeout(function() {
  x.style.display = "block";
}, 500);

x.addEventListener("transitionend", () => {
  if (x.style.height != "0px") {
      x.style.height = "auto"
  }
});

function myFunction() {
  if (x.style.height == "0px") {
    x.style.height = `${ x.scrollHeight }px`
  } else {
    x.style.height = `${ x.scrollHeight }px`;
    window.getComputedStyle(x, null).getPropertyValue("height");
    x.style.height = "0px";
  }
}