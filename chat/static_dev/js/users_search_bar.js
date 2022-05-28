const searchBar = document.querySelector(".search-bar");
const items = document.querySelectorAll(".item");

searchBar.addEventListener('input', (e) => {
    const barValue = searchBar.value;
    for (let i = 0; i < items.length; i++) {
        const item = items[i];
        const value = item.getAttribute('value');
        if (!value.includes(barValue) || barValue == NaN) {
            item.style.display = 'none';
        } else {
            item.style.display = 'flex';
        }
    }
});