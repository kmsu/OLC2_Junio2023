import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './paginas/home/home.component';
import { ReporteASTComponent } from './paginas/reporte-ast/reporte-ast.component';
import { ReporteErroresComponent } from './paginas/reporte-errores/reporte-errores.component';
import { ReporteTSComponent } from './paginas/reporte-ts/reporte-ts.component';
import { AnalisisComponent } from './paginas/analisis/analisis.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  //Mas paginas de navegacion
  { path: 'reporteAST', component: ReporteASTComponent }, 
  { path: 'reporteErrores', component: ReporteErroresComponent }, 
  { path: 'reporteTS', component: ReporteTSComponent },
  { path: 'analisis', component: AnalisisComponent }, 
  //para que lo que no este definido se redirija a home en cualquier otro caso
  { path: '**', pathMatch: 'full', redirectTo: 'home' } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
