console.log("Prueba JS");

document.addEventListener('DOMContentLoaded', function () {
    const inputElement = document.getElementById('floatingInput');
    const labelElement = document.getElementById('labelText');

    inputElement.addEventListener('input', function () {
        labelElement.style.display = (inputElement.value === '') ? 'block' : 'none';
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('floatingPassword');
    const passwordLabel = document.getElementById('labelPassword');

    passwordInput.addEventListener('input', function () {
        passwordLabel.style.display = (passwordInput.value === '') ? 'block' : 'none';
    });
});