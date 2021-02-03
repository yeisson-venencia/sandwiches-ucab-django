import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, NgForm, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { $ } from 'protractor';
import { OrderService } from '../../service/order.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  headers:any;
  rows:any = [];
  checkout = false;
  private sizeSelected: String = '';
  private ingredientSelected: String = '';
  size:any[]=[];
  ingredients:any[] =[];

  constructor(private router: Router, private orderService:OrderService) { 
    this.headers = ["Numero","Tamaño","Ingredientes"];
    orderService.getSize().subscribe((data:any) =>{
      this.orderService.sizeArray = data;
      for(let i of data){
        this.size.push(i.name);
      }      
    });
    orderService.getIngredient().subscribe((data:any)=>{
      this.orderService.ingredientArray = data;
      for(let i of data){
        this.ingredients.push(i.name);
      }
      /* console.log(this.orderService.sizeArray); */
            
    });
  }

  ngOnInit(): void {
    
  }

  addSandwich(){
    let inputElement:any = document.getElementsByTagName("input");
    let ing =[];
    for(let i of inputElement){
      if(i.value != 0 && i.value > 0){
        let x = i.value + " "+ i.getAttribute('id');
        ing.push([x]);
        console.log(ing);
        
      }
    }
    this.rows.push({"Numero":"1","Tamaño":this.sizeSelected,"Ingredientes":ing});   
    
    
  }

  payBill(){
    let obj = this.orderService.payBill(this.rows);
    

    this.orderService.postOrder(obj).subscribe((data)=>{
      console.log(data);
      
    })
  }
  
  selectSize(event:any){
    this.sizeSelected = event.target.value;
    
  }

  selectIngredient(event:any){
    this.ingredientSelected = event.target.value;
    
  }

  goBack(){
    this.router.navigate(['/home'])

  }

  toggle(){
    this.checkout = !this.checkout;
  }

}
