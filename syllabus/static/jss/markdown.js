document.addEventListener('DOMContentLoaded', function() {
  JustificationRun();
  competencesRun();
  learningsRun();
  methodologyRun();
  bibliographyRun();
  firstEvaluationRun();
  secondEvaluationRun();
  thirdEvaluationRun();
});

function JustificationRun() {
  var text = document.getElementById('JustificationText').value,
      target = document.getElementById('justification'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function competencesRun() {
  var text = document.getElementById('competencesText').value,
      target = document.getElementById('competences'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function learningsRun() {
  var text = document.getElementById('learningsText').value,
      target = document.getElementById('learning_results'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function methodologyRun() {
  var text = document.getElementById('methodologyText').value,
      target = document.getElementById('methodology'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function bibliographyRun() {
  var text = document.getElementById('bibliographyText').value,
      target = document.getElementById('bibliography'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function firstEvaluationRun(){
  var text = document.getElementById('firstEvaluationText').value,
      target = document.getElementById('firstEvaluation'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function secondEvaluationRun(){
  var text = document.getElementById('secondEvaluationText').value,
      target = document.getElementById('secondEvaluation'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function thirdEvaluationRun(){
  var text = document.getElementById('thirdEvaluationText').value,
      target = document.getElementById('thirdEvaluation'),
      converter = new showdown.Converter();

  var html = converter.makeHtml(text);
  html = processMarkdownLineBreaks(html);
  target.innerHTML = html;
}

function processMarkdownLineBreaks(html) {
  var blocks = html.split(/<\/?(?:div|p)>/);
  var processedBlocks = blocks.map(function (block) {
      return block.trim() ? processMarkdownLineBreak(block) + '<br>' : '';
  });
  return processedBlocks.join('');
}

function processMarkdownLineBreak(block) {
  return block.replace(/\n/g, '<br>');
}