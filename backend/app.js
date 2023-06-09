
var express = require('express');
var morgan = require('morgan');
var cors = require("cors");
var corsOptions = { origin: true, OptionsSuccessStatus: 200 };
var app= express();

app.use(morgan('dev')); //me muestra en consola que acción hizo el servidor
app.use(express.json());
app.use(cors(corsOptions));//conexion a angular
app.use(express.urlencoded({extended: true}));

var puerto = 8080;
var gramatica = require('./Analizador_Sintactico.py');

app.listen(8080, function () {
    console.log('app nueva escuchando en el puerto 8080');
})

var resultado = '';
var reportError;
var reporteTS;
var reporteAST;
var analisis;// =  gramatica.parse(req.body.dato);
app.post('/editor', function(req, res) {
  if(analisis!=null){
    analisis.clearAll();
  }
  analisis =  gramatica.parse(req.body.dato);
  resultado = analisis.getConsola(); 
  reportError = analisis.getErrores();
  reporteTS = analisis.getReporteTS();
  reporteAST = analisis.dibujarAST();
  //resultado = gramatica.parse(req.body.dato);
  /*
  resultado = '';
  for(let var1 of analisis){
    resultado += var1 + "\n";
  }*/

  res.json({resul: resultado})
})


app.get('/getAnalisis', function(req, res) {
    res.json({analisis: resultado})
})

app.get('/getErrores',function(req, res){
  res.json({reporte: reportError})
})

app.get('/getTS',function(req, res){
  res.json({reporte: reporteTS})
})

app.get('/getAST',function(req, res){
  res.json({reporte: reporteAST})
})