document.addEventListener("DOMContentLoaded", function () {
    var blockCounter = 1; // Contador para identificar de manera única cada bloque
    var listaBloques = [];
  
    // Función para crear un nuevo bloque y su correspondiente ítem
    function createNewBlock(content, strategy) {
      var bloques = document.querySelector(".bloquesCreados");
  
      // Crear nuevo bloque
      var newBlock = document.createElement("div");
      var blockId = blockCounter; // Crear un ID único para el bloque
      newBlock.id = blockId;
      newBlock.classList.add("block");
      newBlock.innerHTML = `
          <h2>Bloque ${blockCounter}</h2>
          <div class="markdown-content" id="${blockId}-content"></div> <!-- Contenedor para contenido Markdown -->
          <div class="markdown-strategy" id="${blockId}-strategy"></div> <!-- Contenedor para estrategias Markdown -->
      `;
  
      // Añadir bloque al contenedor
      bloques.appendChild(newBlock);
  
      // Crear correspondiente ítem con botones de configuración
      var newItem = document.createElement("div");
      newItem.classList.add("item");
      newItem.dataset.blockId = blockId; // Añadir un atributo de datos para almacenar el ID del bloque
      newItem.innerHTML = `
          <span>Bloque ${blockCounter}</span>
          <button class="config-button" onclick="editBlock('${blockId}')">Editar</button>
          <button class="config-button" onclick="deleteBlock('${blockId}')">Eliminar</button>
      `;
  
      // Añadir ítem al contenedor
      document.getElementById("blockItems").appendChild(newItem);
  
      // Incrementar el contador para el próximo bloque
      blockCounter++;
      listaBloques.push(newBlock);
  
      // Actualizar el contenido del bloque con información Markdown y en los divs específicos
      markDownBlock();
  
      // Actualizar los divs program-content y strategies con la información de los bloques
    }
  
    function markDownBlock() {
      for (var i = 0; i < listaBloques.length; i++) {
        var block = listaBloques[i];
  
        /* contenido de los bloques */
        var textContent = block.querySelector(`#${i}-content`).value;
        var textLearning = block.querySelector(`#${i}-strategy`).value;
  
        var converter = new showdown.Converter();
  
        /* contenido de los bloques en html*/
        var htmlContent = converter.makeHtml(textContent);
        var htmlLearning = converter.makeHtml(textLearning);
  
        /* targets */
        var contentMarkdownBlock = document.createElement('div');
        var learningMarkdownBlock = document.createElement('div');
  
        contentMarkdownBlock.innerHTML = htmlContent;
        learningMarkdownBlock.innerHTML = htmlLearning;
  
        var targetContent = document.getElementById('program-content');
        var targetLearning = document.getElementById('strategies');
  
        targetContent.appendChild(contentMarkdownBlock);
        targetLearning.appendChild(learningMarkdownBlock);
      }
    }
  });
  