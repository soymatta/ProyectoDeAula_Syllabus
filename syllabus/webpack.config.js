const path = require("path");

module.exports = {
  mode: "development",
  entry: "./main.js", // Ruta al archivo main.js
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "static/js"), // Ruta donde se guardará el archivo empaquetado
  },
};
