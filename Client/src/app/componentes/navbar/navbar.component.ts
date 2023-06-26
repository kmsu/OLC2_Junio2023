import { Component } from '@angular/core';
import { DataService } from 'src/app/servicios/data.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {

  constructor( private dataService: DataService ) { }

  ngOnInit(): void {  }

  //Metodos directos de la barra de navegacion
  aboutInfo(){
    alert("Nombre: Kevin Samayoa \nCarnet: 200915348 \nNombre: Juan Paxtor \nCarnet: 201700470 \nOLC2")
  }

  Abrir(){
    alert("voy a cargar el archivo")
  }

  ejecutar(){
    //emito el servicio para que funcione
    this.dataService.contenidoEditor$.emit();
  }

  reporteAST(){
    this.dataService.reporteAST$.emit();
  }

  reporteError(){
    this.dataService.reporteErrore$.emit();
  }

  reporteTS(){
    this.dataService.reporteTS$.emit();
  }

  Limpiar(){
    this.dataService.limpiar$.emit("");
  }
}
