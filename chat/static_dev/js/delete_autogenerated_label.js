const imageLabel = document.getElementById('id_image');

if (imageLabel.parentElement) {
    const imageLabelParent = imageLabel.parentElement;
    let child = imageLabelParent.firstChild, nextChild;

    while (child) {
        nextChild = child.nextSibling;
    
        if (child.nodeType == 3) {
            imageLabelParent.removeChild(child);
        }
    
        child = nextChild;
    }
}