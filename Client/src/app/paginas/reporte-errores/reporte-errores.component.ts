import { Component, OnInit } from '@angular/core';
import { DataService } from 'src/app/servicios/data.service';

@Component({
  selector: 'app-reporte-errores',
  templateUrl: './reporte-errores.component.html',
  styleUrls: ['./reporte-errores.component.css']
})
export class ReporteErroresComponent implements OnInit {

  Reporte:Array<any> = [];

  constructor(private dataService: DataService ) { }

  ngOnInit(): void {
    this.dataService.reporteErrore$.subscribe(text => {
      this.Reporte = [];
      this.GetErrores();
    })
  }
 
  ngOnDestroy() {
    
  }
 
  GetErrores(){
    this.dataService.getErrores().subscribe(
      (res: any)=>{
        this.Reporte = res.valores;
      },
      (err)=>{
        console.log(err);
      }
    )
  }
}