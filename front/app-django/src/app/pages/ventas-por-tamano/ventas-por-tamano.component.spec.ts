import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VentasPorTamanoComponent } from './ventas-por-tamano.component';

describe('VentasPorTamanoComponent', () => {
  let component: VentasPorTamanoComponent;
  let fixture: ComponentFixture<VentasPorTamanoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VentasPorTamanoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VentasPorTamanoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
