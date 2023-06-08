import { Injectable, EventEmitter } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  //dolar no hace nada, solo me sirve como indicador de que es un observable. 
  //<string> podría no ir pero se usa para indicar que tipo va a manejar el servicio
  contenidoEditor$ = new EventEmitter<string>(); //Variable que almacena lo que enviare entre componentes
  contenidoConsola$ = new EventEmitter<string>(); //Variable que almacena lo que enviare entre componentes
  
  constructor() { }
}
