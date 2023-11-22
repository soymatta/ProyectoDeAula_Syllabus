document.addEventListener('DOMContentLoaded', function() {
    var modalidadAsignatura = document.getElementById('idModalidadPresencial');
    var modalidad = modalidadAsignatura.getAttribute('data-modalidad');
    if (modalidad === 'presencial') {
        modalidadAsignatura.innerHTML += '<p>X</p>';
    } else if (modalidad === 'pre') {
        modalidadAsignatura = document.getElementById('idModalidadTIC');
        if (modalidadAsignatura) {
            modalidadAsignatura.innerHTML += '<p>X</p>';
        }
    } else if (modalidad === 'virtual') {
        modalidadAsignatura = document.getElementById('idModalidadVirtual');
        if (modalidadAsignatura) {
            modalidadAsignatura.innerHTML += '<p>X</p>';
        }
    }

    var tipoAsignatura = document.getElementById('typeAsignatura')
    var tipo = tipoAsignatura.getAttribute('data-tipo')

    if(tipo === 'teorica' ){
        tipoAsignatura = document.getElementById('idAsignaturaTeorica')
        tipoAsignatura.innerHTML += '<p>X</p>';
    }

    if(tipo === 'teorico-practica'){
        tipoAsignatura = document.getElementById('idAsignaturaTeoricoPractica')
        tipoAsignatura.innerHTML += '<p>X</p>';
    }

    if(tipo ===  'practica'){
        tipoAsignatura = document.getElementById('idAsignaturaPractica')
    }

});