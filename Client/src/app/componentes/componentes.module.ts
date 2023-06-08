import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from './navbar/navbar.component';
import { EditorComponent } from './editor/editor.component';
import { ConsolaComponent } from './consola/consola.component';
import { RouterModule } from '@angular/router';

import { CodemirrorModule } from '@ctrl/ngx-codemirror';
import { FormsModule } from '@angular/forms';
import { SplashScreenComponent } from './splash-screen/splash-screen.component';

@NgModule({
  declarations: [
    NavbarComponent,
    EditorComponent,
    ConsolaComponent,
    SplashScreenComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    //importar
    CodemirrorModule,
    FormsModule
  ],
  exports: [
    NavbarComponent,
    EditorComponent,
    ConsolaComponent,
    SplashScreenComponent
  ]
})
export class ComponentesModule { }
