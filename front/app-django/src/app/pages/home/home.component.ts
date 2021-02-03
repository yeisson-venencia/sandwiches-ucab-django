import { Component, OnInit } from '@angular/core';

import { Router } from '@angular/router';

import { OrderService } from '../../service/order.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(
    private router: Router,
    private order_service: OrderService
  ) { }

  ngOnInit() {
  }

  hacerOrden(){
    this.order_service.getIngredient()
    .subscribe((data: any) => {
      console.log(data)
    })
    this.router.navigate(['/order'])
  }

  hacerFactura(){
    this.router.navigate(['/bill']);
  }

  reports(){
    this.router.navigate(['/reports']);
  }

}
