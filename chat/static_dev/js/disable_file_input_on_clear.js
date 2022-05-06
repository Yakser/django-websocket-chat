const disableFileInputOnClear = () => {
    const clearCheckbox = document.getElementById('image-clear_id');
    const imageInput = document.getElementById('id_image');

    clearCheckbox.addEventListener('click', () => {
        console.log(clearCheckbox.checked)
        if (clearCheckbox.checked) {
            imageInput.disabled = true;
        } else {
            imageInput.disabled = false;
        }
    })
}

disableFileInputOnClear();