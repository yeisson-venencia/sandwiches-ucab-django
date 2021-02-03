import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './pages/home/home.component';
import { NopagefoundComponent } from './pages/nopagefound/nopagefound.component';
import { OrderComponent } from './pages/order/order.component';
import { BillComponent } from './pages/bill/bill.component';
import { ReportsComponent } from './pages/reports/reports.component';
import { VentasPorTamanoComponent } from './pages/ventas-por-tamano/ventas-por-tamano.component';

const routes: Routes = [

  { path: 'home', component: HomeComponent },
  { path: 'order',component: OrderComponent },
  { path: 'bill',component: BillComponent },
  { path: 'reports',component: ReportsComponent },
  { path: 'ventasportamano',component: VentasPorTamanoComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: '**', component: NopagefoundComponent }

];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot( routes )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
