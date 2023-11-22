document.addEventListener('DOMContentLoaded', function() {
    var tipoAsignatura = document.getElementById('idModalidadPresencial');
    var tipo = tipoAsignatura.getAttribute('data-tipo');
    if (tipo === 'presencial') {
        console.log('hola')
        tipoAsignatura.innerHTML += '<p>X</p>';
    } else if (tipo === 'presencial-tic') {
        console.log('hola')
        tipoAsignatura = document.getElementById('idModalidadTIC');
        if (tipoAsignatura) {
            tipoAsignatura.innerHTML += '<p>X</p>';
        }
    } else if (tipo === 'virtual') {
        console.log('hola')
        tipoAsignatura = document.getElementById('idModalidadVirtual');
        if (tipoAsignatura) {
            tipoAsignatura.innerHTML += '<p>X</p>';
        }
    }
});