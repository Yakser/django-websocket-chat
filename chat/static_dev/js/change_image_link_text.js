const imageLink = document.querySelector('label[for="id_image"] + a');

if (imageLink) {
    imageLink.innerHTML = "Посмотреть изображение";
    imageLink.target = "_blank";
};