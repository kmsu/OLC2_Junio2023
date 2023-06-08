import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReporteASTComponent } from './reporte-ast.component';

describe('ReporteASTComponent', () => {
  let component: ReporteASTComponent;
  let fixture: ComponentFixture<ReporteASTComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ReporteASTComponent]
    });
    fixture = TestBed.createComponent(ReporteASTComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
