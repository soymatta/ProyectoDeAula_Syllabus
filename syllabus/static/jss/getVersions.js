document.addEventListener('DOMContentLoaded', function() {
    const changesUpdate = document.getElementById('changesTableBody');
    const changes = changesUpdate.getAttribute('data-changes');
    const versionsData = JSON.parse(changes);

    // Obtener el último cambio
    const lastVersion = versionsData[versionsData.length - 1];

    // Formatear la fecha en DD-MM-YYYY
    const formattedDate = new Date(lastVersion.update_date).toLocaleDateString('es-ES');

    // Mostrar la fecha en el div
    const dateActualizacion = document.getElementById('dateActualizacion');
    
    // Verificar si el elemento existe antes de intentar establecer su contenido
    if (dateActualizacion) {
        dateActualizacion.textContent = formattedDate;
    }

    // Mostrar los últimos cinco cambios en la tabla
    const lastFiveVersions = versionsData.slice(-5);

    lastFiveVersions.forEach(version => {
        // Crear una fila
        const row = document.createElement('tr');

        // Formatear la fecha en DD-MM-YYYY
        const formattedDate = new Date(version.update_date).toLocaleDateString('es-ES');

        // Crear celdas para cada propiedad
        const dateCell = document.createElement('td');
        dateCell.textContent = formattedDate;
        row.appendChild(dateCell);

        const descriptionCell = document.createElement('td');
        descriptionCell.textContent = version.description;
        row.appendChild(descriptionCell);

        const userCell = document.createElement('td');
        userCell.textContent = version.user_name;
        row.appendChild(userCell);

        // Agregar la fila a la tabla
        changesUpdate.appendChild(row);
    });
});