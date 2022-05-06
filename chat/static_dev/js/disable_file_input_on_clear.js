const clearCheckbox = document.getElementById('image-clear_id');
const imageInput = document.getElementById('id_image');

clearCheckbox.addEventListener('click', () => {
    if (clearCheckbox.checked) {
        imageInput.disabled = true;
    } else {
        imageInput.disabled = false;
    }
})