import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReporteErroresComponent } from './reporte-errores.component';

describe('ReporteErroresComponent', () => {
  let component: ReporteErroresComponent;
  let fixture: ComponentFixture<ReporteErroresComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ReporteErroresComponent]
    });
    fixture = TestBed.createComponent(ReporteErroresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
