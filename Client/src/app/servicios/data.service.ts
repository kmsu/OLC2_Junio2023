import { HttpClient } from '@angular/common/http';
import { Injectable, EventEmitter } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  //dolar no hace nada, solo me sirve como indicador de que es un observable. 
  //<string> podría no ir pero se usa para indicar que tipo va a manejar el servicio
  contenidoEditor$ = new EventEmitter<string>(); //Variable que almacena lo que enviare entre componentes
  contenidoConsola$ = new EventEmitter<string>(); //Variable que almacena lo que enviare entre componentes
  limpiar$ = new EventEmitter<string>();
  reporteErrore$ = new EventEmitter<string>();
  reporteTS$ = new EventEmitter<string>();
  reporteAST$ = new EventEmitter<string>();

  //Para conectar al servidor (Express)
  URL = "http://127.0.0.1:8080"

  constructor( private http:HttpClient ) { }

  //Metodos para usar con el servidor
  getAnalizador(json: any){
    return this.http.post(`${this.URL}/compilar`, json);
  }

  getAnalisis(){
    return this.http.get(`${this.URL}/salida`);
  } 

  getErrores(){
    return this.http.get(`${this.URL}/getErrores`);
  } 
 

  getTS(){
    return this.http.get(`${this.URL}/getTS`);
  } 
  
  getAST(){
    return this.http.get(`${this.URL}/getAST`);
  }
  
}
