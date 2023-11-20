// main.js
const showdown = require('showdown');
const converter = new showdown.Converter();
const text = '# Hello, Markdown!';
const html = converter.makeHtml(text);
console.log(html);


