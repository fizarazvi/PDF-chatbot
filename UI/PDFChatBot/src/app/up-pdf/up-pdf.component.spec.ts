import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpPdfComponent } from './up-pdf.component';

describe('UpPdfComponent', () => {
  let component: UpPdfComponent;
  let fixture: ComponentFixture<UpPdfComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpPdfComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpPdfComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
