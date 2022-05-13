const clearString = (value) => {
    return value.trim().toLowerCase();
}
const search = () => {
    const input = document.getElementById('js-search');
    const listContainer = document.getElementById('js-checkboxes-list-container').firstElementChild
    const elements = listContainer.children;

    input.addEventListener('input', () => {
        const clearedValue = clearString(input.value);

        if (clearedValue.length > 0) {
            for (let element of elements) {
                if (clearString(element.textContent).includes(clearedValue)) {
                    element.style.display = 'block';
                } else {
                    element.style.display = 'none';
                }
            }
        } else {
            for (let element of elements) {
                element.style.display = 'block';
            }
        }
    })
}


search();