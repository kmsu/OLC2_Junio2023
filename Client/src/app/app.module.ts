import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ComponentesModule } from './componentes/componentes.module';
import { PaginasModule } from './paginas/paginas.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
     //SE IMPORTA PARA TENER ACCESO GLOBAL
     ComponentesModule,
     PaginasModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
