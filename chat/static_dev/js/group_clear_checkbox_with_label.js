
const groupClearCheckboxWithLabel = () => {
    const imageInput = document.getElementById('id_image');

    const checkbox = document.getElementById('image-clear_id');

    const label = document.querySelector('label[for="image-clear_id"]');
    label.textContent = 'Очистить?';

    const block = document.createElement('div');
    block.classList.add('clear-image-block');
    block.insertAdjacentElement('afterbegin', label);
    block.insertAdjacentElement('beforeend', checkbox);

    imageInput.insertAdjacentElement('beforebegin', block);

    // удаляет <br>, сгенерированный Django
    imageInput.parentElement.children[3].remove();
}

groupClearCheckboxWithLabel();
