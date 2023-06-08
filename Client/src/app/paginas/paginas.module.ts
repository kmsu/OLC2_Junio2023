import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ComponentesModule } from '../componentes/componentes.module';
import { HomeComponent } from './home/home.component';
import { ReporteASTComponent } from './reporte-ast/reporte-ast.component';
import { ReporteErroresComponent } from './reporte-errores/reporte-errores.component';
import { ReporteTSComponent } from './reporte-ts/reporte-ts.component';
import { AnalisisComponent } from './analisis/analisis.component';



@NgModule({
  declarations: [
    HomeComponent,
    ReporteASTComponent,
    ReporteErroresComponent,
    ReporteTSComponent,
    AnalisisComponent
  ],
  imports: [
    CommonModule,
    ComponentesModule
  ]
})
export class PaginasModule { }
