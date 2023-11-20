function JustificationRun() {
  var text = document.getElementById('JustificationText').value,
      target = document.getElementById('justification'),
      converter = new showdown.Converter();

  // Convertir el texto de Markdown a HTML
  var html = converter.makeHtml(text);

  // Procesar los bloques de Markdown para manejar mejor los saltos de línea
  html = processMarkdownLineBreaks(html);

  // Actualizar el contenido del div de destino
  target.innerHTML = html;
}

function competencesRun() {
  var text = document.getElementById('competencesText').value,
      target = document.getElementById('competences'),
      converter = new showdown.Converter();

  // Convertir el texto de Markdown a HTML
  var html = converter.makeHtml(text);

  // Procesar los bloques de Markdown para manejar mejor los saltos de línea
  html = processMarkdownLineBreaks(html);

  // Actualizar el contenido del div de destino
  target.innerHTML = html;
}

function learningsRun() {
  var text = document.getElementById('learningsText').value,
      target = document.getElementById('learning_results'),
      converter = new showdown.Converter();

  // Convertir el texto de Markdown a HTML
  var html = converter.makeHtml(text);

  // Procesar los bloques de Markdown para manejar mejor los saltos de línea
  html = processMarkdownLineBreaks(html);

  // Actualizar el contenido del div de destino
  target.innerHTML = html;
}

function methodologyRun() {
  var text = document.getElementById('methodologyText').value,
      target = document.getElementById('methodology'),
      converter = new showdown.Converter();

  // Convertir el texto de Markdown a HTML
  var html = converter.makeHtml(text);

  // Procesar los bloques de Markdown para manejar mejor los saltos de línea
  html = processMarkdownLineBreaks(html);

  // Actualizar el contenido del div de destino
  target.innerHTML = html;
}

function bibliographyRun() {
  var text = document.getElementById('bibliographyText').value,
      target = document.getElementById('bibliography'),
      converter = new showdown.Converter();

  // Convertir el texto de Markdown a HTML
  var html = converter.makeHtml(text);

  // Procesar los bloques de Markdown para manejar mejor los saltos de línea
  html = processMarkdownLineBreaks(html);

  // Actualizar el contenido del div de destino
  target.innerHTML = html;
}

function processMarkdownLineBreaks(html) {
  // Dividir el HTML en bloques de Markdown
  var blocks = html.split(/<\/?(?:div|p)>/);

  // Filtrar y agregar <br> según sea necesario
  var processedBlocks = blocks.map(function (block) {
      return block.trim() ? processMarkdownLineBreak(block) + '<br>' : '';
  });

  // Unir los bloques procesados nuevamente en HTML
  return processedBlocks.join('');
}

function processMarkdownLineBreak(block) {
  // Procesar los saltos de línea en bloques de Markdown
  return block.replace(/\n/g, '<br>');
}