import { Component, OnInit } from '@angular/core';
import { SelectMultipleControlValueAccessor } from '@angular/forms';

import { Router } from '@angular/router';

import { ReportsService } from '../../service/reports.service';

@Component({
  selector: 'app-ventas-por-tamano',
  templateUrl: './ventas-por-tamano.component.html',
  styleUrls: ['./ventas-por-tamano.component.css']
})
export class VentasPorTamanoComponent implements OnInit {

  individuales: any 
  dobles: any
  triples: any
  headers = ["Numero","Tamaño", "Precio"];

  constructor(
    private router: Router,
    private service_report: ReportsService
  ) { 
    this.service_report.reportVentasTamano(1)
        .subscribe((data:any) => {
          this.individuales = data
          console.log(this.individuales)
        
        })
  }

  ngOnInit(): void {
    

    this.service_report.reportVentasTamano(2)
        .subscribe((data:any) => {
          this.dobles = data
          console.log(this.dobles)
        })
    this.service_report.reportVentasTamano(3)
        .subscribe((data:any) => {
          this.triples = data
        })
        
    
  }







}
