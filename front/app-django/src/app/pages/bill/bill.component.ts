import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-bill',
  templateUrl: './bill.component.html',
  styleUrls: ['./bill.component.css']
})
export class BillComponent implements OnInit {

  headers:any;

  constructor(private router: Router) { 
    this.headers = ["Numero","Tamaño","Ingrediente(s)"];
    
  }

  ngOnInit(): void {
  }

}
