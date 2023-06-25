import { Component, OnInit } from '@angular/core';
import { DataService } from 'src/app/servicios/data.service';

@Component({
  selector: 'app-reporte-ts',
  templateUrl: './reporte-ts.component.html',
  styleUrls: ['./reporte-ts.component.css']
})
export class ReporteTSComponent implements OnInit{
  
  Reporte:Array<any> = [];

  constructor(private dataService:DataService) { }

  ngOnInit(): void {
    this.dataService.reporteTS$.subscribe(text => {
      this.Reporte = [];
      this.GetTS();
    })
  }

  GetTS(){
    this.dataService.getTS().subscribe(
      (res: any)=>{
        this.Reporte = res.reporte;
      },
      (err)=>{
        console.log(err);
      }
    )
  }
}
