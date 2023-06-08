import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReporteTSComponent } from './reporte-ts.component';

describe('ReporteTSComponent', () => {
  let component: ReporteTSComponent;
  let fixture: ComponentFixture<ReporteTSComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ReporteTSComponent]
    });
    fixture = TestBed.createComponent(ReporteTSComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
