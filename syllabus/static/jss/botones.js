function exportarAPDF() {
    // Obtener la lista de elementos que deseas exportar
    var elementos = document.querySelectorAll('.elemento-exportar');

    // Crear un contenedor temporal para almacenar los elementos a exportar
    var contenedor = document.createElement('div');

    // Clonar y agregar cada elemento al contenedor
    elementos.forEach(function (elemento) {
        contenedor.appendChild(elemento.cloneNode(true));
    });

    // Llamar a la función html2pdf con el contenido del contenedor
    html2pdf(contenedor);
}


function aplicarNegrita() {
    var editor = document.getElementById('JustificationText');
    var seleccion = window.getSelection().toString();

    // Verifica si hay texto seleccionado
    if (seleccion !== '') {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `__${seleccion}__`);
        editor.innerHTML = nuevoContenido;
    } else {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `__type here__`);
        editor.innerHTML = nuevoContenido;
    }
}


function aplicarCursiva() {
    var editor = document.getElementById('JustificationText');
    var seleccion = window.getSelection().toString();

    // Verifica si hay texto seleccionado
    if (seleccion !== '') {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `_${seleccion}_`);
        editor.innerHTML = nuevoContenido;
    } else {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `_type here_`);
        editor.innerHTML = nuevoContenido;
    }
}

function aplicarEnlace() {
    var editor = document.getElementById('JustificationText');
    var seleccion = window.getSelection().toString();

    // Verifica si hay texto seleccionado
    if (seleccion !== '') {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `[${seleccion}](${seleccion})`);
        editor.innerHTML = nuevoContenido;
    } else {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `[Link](type link)`);
        editor.innerHTML = nuevoContenido;
    }
}



function aplicarImg() {
    var editor = document.getElementById('JustificationText');
    var seleccion = window.getSelection().toString();

    // Verifica si hay texto seleccionado
    if (seleccion !== '') {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `![${seleccion}](${seleccion})`);
        editor.innerHTML = nuevoContenido;
    } else {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `![Link](type link)`);
        editor.innerHTML = nuevoContenido;
    }
}

function aplicarListas() {
    var editor = document.getElementById('JustificationText');
    var seleccion = window.getSelection().toString();
    var contenidoActual = document.getElementById('JustificationText').innerHTML;
    // Verifica si hay texto seleccionado
    if (seleccion !== '') {
        var nuevoContenido = editor.innerHTML.replace(seleccion, `>-${seleccion}`);
        editor.innerHTML = nuevoContenido;
    } else if (seleccion !== '>-' + seleccion) {
        var contenidoActual = document.getElementById('JustificationText').innerHTML;

        // Agregar un encabezado con #
        var nuevoContenido = '>' + contenidoActual;

        // Actualizar el contenido del div
        document.getElementById('JustificationText').innerHTML = nuevoContenido;
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