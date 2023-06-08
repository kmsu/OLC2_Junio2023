import { Component } from '@angular/core';
import { DataService } from 'src/app/servicios/data.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent {

  contenidoEditor: string = ''; //propiedad que almacena el contenido del area de texto

  constructor( private dataService: DataService ) { } //inyecto el servicio

  ngOnInit(): void {
    this.dataService.contenidoEditor$.subscribe(text => {
      //text = this.contenidoEditor;
      //console.log('desde editor: ', text);
      this.dataService.contenidoConsola$.emit(this.contenidoEditor);
    })
  }
}
