document.addEventListener("DOMContentLoaded", () => {
    const $boton = document.querySelector("#btnCrearPdf");
    
    $boton.addEventListener("click", () => {
        const $elementoParaConvertir = document.querySelector("#DivExportar");

        html2pdf()
            .set({ jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' } })
            .from($elementoParaConvertir)
            .save()
            .catch(err => console.log(err));
    });
});

function exportarAPDF() {
    var element = document.getElementById('DivExportar');

    // Opciones de configuración para html2pdf
    var opt = {
        margin: 10,
        filename: 'documento.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    // Llama a html2pdf con las opciones
    html2pdf(element, opt);
}


function aplicarNegrita() {
    // Verificar si hay un textArea activo
    if (activeTextArea) {
        // Obtener el contenido actual del textArea activo
        var contenidoActual = activeTextArea.value;

        // Obtener la selección actual del editor en el textArea activo
        var selectedText = contenidoActual.substring(activeTextArea.selectionStart, activeTextArea.selectionEnd);

        // Verificar si hay texto seleccionado
        if (selectedText !== "") {
            // Agregar el texto en negrita a la selección
            var newText = contenidoActual.substring(0, activeTextArea.selectionStart) +
                "**" + selectedText + "**" +
                contenidoActual.substring(activeTextArea.selectionEnd);

            // Reemplazar el contenido del textArea activo con el nuevo texto
            activeTextArea.value = newText;
        } else {
            // Si no hay texto seleccionado, agregar los caracteres de negrita alrededor del cursor
            var cursorPosition = activeTextArea.selectionStart;
            var newText = contenidoActual.substring(0, cursorPosition) +
                "**Type here**" +
                contenidoActual.substring(cursorPosition);

            // Reemplazar el contenido del textArea activo con el nuevo texto
            activeTextArea.value = newText;

            // Mover el cursor al medio de los caracteres de negrita
            activeTextArea.setSelectionRange(cursorPosition + 2, cursorPosition + 2);
        }
    }
}

function aplicarCursiva() {
    // Verificar si hay un textArea activo
    if (activeTextArea) {
        // Obtener el contenido actual del textArea activo
        var contenidoActual = activeTextArea.value;

        // Obtener la selección actual del editor en el textArea activo
        var selectedText = contenidoActual.substring(activeTextArea.selectionStart, activeTextArea.selectionEnd);

        // Verificar si hay texto seleccionado
        if (selectedText !== "") {
            // Agregar el texto en negrita a la selección
            var newText = contenidoActual.substring(0, activeTextArea.selectionStart) +
                "*" + selectedText + "*" +
                contenidoActual.substring(activeTextArea.selectionEnd);

            // Reemplazar el contenido del textArea activo con el nuevo texto
            activeTextArea.value = newText;
        } else {
            // Si no hay texto seleccionado, agregar los caracteres de negrita alrededor del cursor
            var cursorPosition = activeTextArea.selectionStart;
            var newText = contenidoActual.substring(0, cursorPosition) +
                "*Type here*" +
                contenidoActual.substring(cursorPosition);

            // Reemplazar el contenido del textArea activo con el nuevo texto
            activeTextArea.value = newText;

            // Mover el cursor al medio de los caracteres de negrita
            activeTextArea.setSelectionRange(cursorPosition + 2, cursorPosition + 2);
        }
    }
}

function aplicarImg() {
    // Verificar si hay un textArea activo
    if (activeTextArea) {
        // Obtener el contenido actual del textArea activo
        var contenidoActual = activeTextArea.value;

        // Obtener la selección actual del editor en el textArea activo
        var selectedText = contenidoActual.substring(activeTextArea.selectionStart, activeTextArea.selectionEnd);

        // Insertar la estructura de imagen alrededor del texto seleccionado o en el cursor
        var newText = contenidoActual.substring(0, activeTextArea.selectionStart) +
            "![texto alternativo](URL_de_la_imagen)" +
            contenidoActual.substring(activeTextArea.selectionEnd);

        // Reemplazar el contenido del textArea activo con el nuevo texto
        activeTextArea.value = newText;

        // Si no hay texto seleccionado, seleccionar "texto alternativo"
        if (selectedText === "") {
            var cursorPosition = activeTextArea.selectionStart + 2;
            activeTextArea.setSelectionRange(cursorPosition, cursorPosition + 13); // Selecciona "texto alternativo"
        }
    }
}

function aplicarEnlace() {
    // Verificar si hay un textArea activo
    if (activeTextArea) {
        // Obtener el contenido actual del textArea activo
        var contenidoActual = activeTextArea.value;

        // Obtener la selección actual del editor en el textArea activo
        var selectedText = contenidoActual.substring(activeTextArea.selectionStart, activeTextArea.selectionEnd);

        // Insertar la estructura de enlace alrededor del texto seleccionado o en el cursor
        var newText = contenidoActual.substring(0, activeTextArea.selectionStart) +
            "[" + selectedText + "](URL_del_enlace)" +
            contenidoActual.substring(activeTextArea.selectionEnd);

        // Reemplazar el contenido del textArea activo con el nuevo texto
        activeTextArea.value = newText;

        // Si no hay texto seleccionado, seleccionar "texto del enlace"
        if (selectedText === "") {
            var cursorPosition = activeTextArea.selectionStart + 1;
            activeTextArea.setSelectionRange(cursorPosition, cursorPosition + 15); // Selecciona "texto del enlace"
        }
    }
}

function aplicarListas() {
    // Verificar si hay un textArea activo
    if (activeTextArea) {
        // Obtener el contenido actual del textArea activo
        var contenidoActual = activeTextArea.value;

        // Obtener la selección actual del editor en el textArea activo
        var selectedText = contenidoActual.substring(activeTextArea.selectionStart, activeTextArea.selectionEnd);

        // Verificar si hay texto seleccionado
        if (selectedText !== "") {
            // Insertar la estructura de lista alrededor del texto seleccionado
            var newText = contenidoActual.substring(0, activeTextArea.selectionStart) +
                "- " + selectedText +
                contenidoActual.substring(activeTextArea.selectionEnd);

            // Reemplazar el contenido del textArea activo con el nuevo texto
            activeTextArea.value = newText;
        } else {
            // Si no hay texto seleccionado, agregar un elemento de lista en la posición actual del cursor
            var cursorPosition = activeTextArea.selectionStart;
            var beforeCursor = contenidoActual.substring(0, cursorPosition);
            var afterCursor = contenidoActual.substring(cursorPosition);

            // Verificar si el cursor está al inicio de una línea o al principio del texto
            var isNewLine = cursorPosition === 0 || beforeCursor.charAt(cursorPosition - 1) === '\n';

            // Agregar el elemento de lista en la posición actual del cursor
            var newText = beforeCursor +
                (isNewLine ? "" : "\n") +
                "- " +
                (isNewLine ? "" : " ") +
                afterCursor;

            // Reemplazar el contenido del textArea activo con el nuevo texto
            activeTextArea.value = newText;

            // Mover el cursor al final del nuevo elemento de lista
            activeTextArea.setSelectionRange(cursorPosition + (isNewLine ? 2 : 3), cursorPosition + (isNewLine ? 2 : 3));
        }
    }
}




function showHeaderMenu() {
    var headerMenu = document.getElementById("headerMenu");
    headerMenu.style.display = "block";
}

function hideHeaderMenu() {
    var headerMenu = document.getElementById("headerMenu");
    headerMenu.style.display = "none";
}

// Variable para almacenar el textArea activo
var activeTextArea;

// Función para establecer el textArea activo
function setActiveTextArea(textArea) {
    activeTextArea = textArea;
}

// Función para agregar encabezados en sintaxis Markdown al textArea activo
function addHeader(level) {
    // Verificar si hay un textArea activo
    if (activeTextArea) {
        // Obtener el ID del textArea activo
        var textAreaId = activeTextArea.id;

        // Obtener el contenido actual del textArea activo
        var contenidoActual = activeTextArea.value;

        // Obtener la selección actual del editor en el textArea activo
        var selectedText = contenidoActual.substring(activeTextArea.selectionStart, activeTextArea.selectionEnd);

        // Agregar el encabezado correspondiente a la selección
        var newText = contenidoActual.substring(0, activeTextArea.selectionStart) +
            "#".repeat(level) + selectedText +
            contenidoActual.substring(activeTextArea.selectionEnd);

        // Reemplazar el contenido del textArea activo con el nuevo texto
        activeTextArea.value = newText;
    }
}



function guardarEnBaseDeDatos() {
    var update_date = new Date().toISOString(); // Obtén la fecha actual en formato ISO
    var description = document.getElementById('descriptionInput').value; // Ajusta el ID según tu formulario
    var user_id = document.getElementById('userIdInput').value; // Ajusta el ID según tu formulario
    var syllabus_id = document.getElementById('syllabusIdInput').value; // Ajusta el ID según tu formulario

    fetch('/guardarDiv', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            update_date: update_date,
            description: description,
            user_id: user_id,
            syllabus_id: syllabus_id
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensaje || data.error);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}