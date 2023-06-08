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
      this.contenidoConsola = texto;
      console.log('consola: ', texto);
    })
  }
}
