import { Component, OnInit } from '@angular/core';
import { DataService } from 'src/app/servicios/data.service';

@Component({
  selector: 'app-reporte-ast',
  templateUrl: './reporte-ast.component.html',
  styleUrls: ['./reporte-ast.component.css']
})
export class ReporteASTComponent implements OnInit {
  
  Ast:string = '';

  constructor(private dataService:DataService) { }

  ngOnInit(): void {
    this.dataService.reporteAST$.subscribe(text => {
      this.Ast = '';
      this.GetAST();
    })
  }

  GetAST(){
    this.dataService.getAST().subscribe(
      (res: any)=>{
        this.Ast = res.reporte;
      },
      (err)=>{
        console.log(err);
      }
    )
  }

}
