import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsolaComponent } from './consola.component';

describe('ConsolaComponent', () => {
  let component: ConsolaComponent;
  let fixture: ComponentFixture<ConsolaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ConsolaComponent]
    });
    fixture = TestBed.createComponent(ConsolaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
