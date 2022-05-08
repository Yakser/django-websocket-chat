const Menu = () => {
  const nav = document.getElementById("js-menu-nav");

  nav.style.height = `${ nav.scrollHeight }px`;
  window.getComputedStyle(nav, null).getPropertyValue("height");
  nav.style.height = "0px";

  nav.addEventListener("transitionend", () => {
    if (nav.style.height != "0px") {
      nav.style.height = "auto"
    }
  });

  document.getElementById('js-menu-btn').addEventListener('click', () => {
    nav.classList.toggle('active');
    if (nav.classList.contains('active')) {
      nav.style.height = `${ nav.scrollHeight }px`
      nav.style.marginBlockStart = '20px';
      nav.style.opacity = '1';
    } else {
      nav.style.height = `${ nav.scrollHeight }px`;
      window.getComputedStyle(nav, null).getPropertyValue("height");
      nav.style.height = "0px";
      nav.style.marginBlockStart = '0px';
      nav.style.opacity = '0';
    }
  });
}

Menu();