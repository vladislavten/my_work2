const uploadButton = document.getElementById('uploadButton');
const fileInput = document.getElementById('fileInput');

uploadButton.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        // You can use AJAX or fetch to send the file to the server and save it in the 'images' directory
        // For simplicity, we'll just log the file name for now
        console.log('File uploaded:', file.name);
    }
});
