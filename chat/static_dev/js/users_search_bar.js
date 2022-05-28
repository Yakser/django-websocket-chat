const searchBar = document.querySelector(".search-bar");
const users = document.querySelectorAll(".item");

console.log(searchBar)

searchBar.addEventListener('input', (e) => {
    const barValue = searchBar.value;
    for (let i = 0; i < users.length; i++) {
        const user = users[i];
        const name = user.getAttribute('value');
        if (!name.includes(barValue) || barValue == NaN) {
            user.style.display = 'none';
        } else {
            user.style.display = 'flex';
        }
    }
});