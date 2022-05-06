const changeImageLink = () => {
    const imageLink = document.querySelector('label[for="id_image"] + .base-form__field-errors + a');

    if (imageLink) {
        imageLink.innerHTML = "Посмотреть изображение";
        imageLink.target = "_blank";
        imageLink.classList.add('base-form__image-link')
    };
}

changeImageLink();