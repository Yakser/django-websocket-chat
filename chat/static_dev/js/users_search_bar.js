const searchBar = document.getElementById("users_search");
const users = document.querySelectorAll(".item");

searchBar.addEventListener('input', (e) => {
    const barValue = searchBar.value;
    for (let i = 0; i < users.length; i++) {
        const user = users[i];
        const name = user.getAttribute('value');
        if (!name.includes(barValue)) {
            user.style.display = 'none';
        } else {
            user.style.display = 'flex';
        }
    }
});