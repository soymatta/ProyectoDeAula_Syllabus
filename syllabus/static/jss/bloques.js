// Contenido del script.js
document.addEventListener('DOMContentLoaded', function () {
  var blockCounter = 1;  // Contador para identificar de manera única cada bloque

  // Función para crear un nuevo bloque y su correspondiente ítem
  function createNewBlock(content, strategy) {
      var accordionBody = document.querySelector('.accordion-body');

      // Crear nuevo bloque
      var newBlock = document.createElement('div');
      var blockId = 'block' + blockCounter;  // Crear un ID único para el bloque
      newBlock.id = blockId;
      newBlock.classList.add('block');
      newBlock.innerHTML = `
          <h2>Bloque ${blockCounter}</h2>
          <div class="markdown-content" id="${blockId}-content"></div> <!-- Contenedor para contenido Markdown -->
          <div class="markdown-strategy" id="${blockId}-strategy"></div> <!-- Contenedor para estrategias Markdown -->
      `;

      // Añadir bloque al contenedor
      accordionBody.appendChild(newBlock);

      // Crear correspondiente ítem con botones de configuración
      var newItem = document.createElement('div');
      newItem.classList.add('item');
      newItem.dataset.blockId = blockId;  // Añadir un atributo de datos para almacenar el ID del bloque
      newItem.innerHTML = `
          <br>
          <span>Bloque ${blockCounter}</span>
          <button class="btn btn-secondary ms-4" onclick="editBlock('${blockId}')">Editar</button>
          <button class="btn-close ms-4" onclick="deleteBlock('${blockId}')"></button>
      `;

      // Añadir ítem al contenedor
      document.getElementById('blockItems').appendChild(newItem);

      // Incrementar el contador para el próximo bloque
      blockCounter++;

      // Actualizar el contenido del bloque con información Markdown y en los divs específicos
      updateBlockContent(blockId, content, strategy);

      // Actualizar los divs program-content y strategies con la información de los bloques
      updateProgramContentAndStrategies();
  }

  // Función para manejar el evento de hacer clic en "Crear bloque"
  function handleCreateBlock() {
      var content = document.getElementById('content-text').value;
      var strategy = document.getElementById('learning-text').value;
      var editBlockId = document.getElementById('editBlockId').value;

      if (editBlockId) {
          // Si hay un ID de bloque para editar, realiza la lógica de edición aquí
          // Puedes usar la función updateBlockContent con el ID del bloque y los nuevos valores
          updateBlockContent(editBlockId, content, strategy);

          // Restablecer el ID de bloque para editar
          document.getElementById('editBlockId').value = '';
      } else {
          // Si no hay un ID de bloque para editar, crea un nuevo bloque
          createNewBlock(content, strategy);
      }

      // Cerrar el modal
      var modal = new bootstrap.Modal(document.getElementById('exampleModal'));
      modal.hide();
  }

  // Asignar la función handleCreateBlock al botón "Crear bloque" del modal
  document.getElementById('createBlockBtn').addEventListener('click', handleCreateBlock);
});

// Función para editar un bloque
function editBlock(blockId) {
  // Obtener el contenido actual del bloque
  var contentDiv = document.getElementById(`${blockId}-content`);
  var strategyDiv = document.getElementById(`${blockId}-strategy`);
  var currentContent = contentDiv.innerHTML;
  var currentStrategy = strategyDiv.innerHTML;

  // Prellenar los textareas del modal con el contenido actual del bloque
  document.getElementById('content-text').value = currentContent;
  document.getElementById('learning-text').value = currentStrategy;

  // Abrir el modal de edición
  var editModal = new bootstrap.Modal(document.getElementById('exampleModal'));
  editModal.show();

  // Guardar el ID del bloque actual que se está editando
  document.getElementById('editBlockId').value = blockId;
}

// Función para eliminar un bloque
function deleteBlock(blockId) {
  // Obtener el bloque y su ítem correspondiente
  var block = document.getElementById(blockId);
  var item = document.querySelector(`.item[data-block-id="${blockId}"]`);

  // Eliminar el bloque y su ítem
  if (block && item) {
      block.remove();
      item.remove();
  }

  // Actualizar los divs program-content y strategies con la información de los bloques
  updateProgramContentAndStrategies();
}

// Función para actualizar el contenido del bloque con información Markdown
function updateBlockContent(blockId, content, strategy) {
  var contentDiv = document.getElementById(`${blockId}-content`);
  var strategyDiv = document.getElementById(`${blockId}-strategy`);

  // Actualizar el contenido de los contenedores Markdown en el bloque sin convertir a HTML
  contentDiv.textContent = content;
  strategyDiv.textContent = strategy;
}


// Función para actualizar los divs program-content y strategies con la información de los bloques
function updateProgramContentAndStrategies() {
  var programContentDiv = document.getElementById('program-content');
  var strategiesDiv = document.getElementById('strategies');

  // Obtener todos los bloques creados
  var blocks = document.querySelectorAll('.block');

  // Recorrer los bloques y extraer su contenido Markdown
  var programContentMarkdown = '';
  var strategiesMarkdown = '';
  blocks.forEach(function (block) {
      var contentDiv = block.querySelector('.markdown-content');
      var strategyDiv = block.querySelector('.markdown-strategy');

      // Agregar contenido Markdown al total
      programContentMarkdown += contentDiv.innerHTML + '<br>';

      // Agregar estrategias Markdown al total
      strategiesMarkdown += strategyDiv.innerHTML + '<br>';
  });

  // Convertir el contenido y las estrategias de Markdown a HTML
  var converter = new showdown.Converter();
  var programContentHtml = converter.makeHtml(programContentMarkdown);
  var strategiesHtml = converter.makeHtml(strategiesMarkdown);

  // Actualizar el contenido de los divs program-content y strategies
  programContentDiv.innerHTML = programContentHtml;
  strategiesDiv.innerHTML = strategiesHtml;
}