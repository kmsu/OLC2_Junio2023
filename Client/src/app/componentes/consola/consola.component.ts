import { Component } from '@angular/core';
import { DataService } from 'src/app/servicios/data.service';

@Component({
  selector: 'app-consola',
  templateUrl: './consola.component.html',
  styleUrls: ['./consola.component.css']
})
export class ConsolaComponent {

  contenidoConsola: string = '';

  constructor( private dataService: DataService ) { }

  ngOnInit(): void {
    this.dataService.contenidoConsola$.subscribe( texto => {
      this.contenidoConsola = '';
      this.getData();
    })

    this.dataService.limpiar$.subscribe( texto => {
      this.contenidoConsola = texto;
    })
  }

  getData(){
    this.dataService.getAnalisis().subscribe(
      (res:any)=>{ //para poder retornar el incremental

        //let arreglo:Array<any> = res.analisis;
        /*
        for(let val of arreglo){
          this.contenidoConsola += "El valor de la expresion es: " + val + "\n";
        }*/
        
        this.contenidoConsola = res.consola;
      }, 
      (err)=> {
        console.log(err);
      }
    )
  }

}

