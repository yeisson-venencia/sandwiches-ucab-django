import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, NgForm, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { $ } from 'protractor';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  headers:any;
  rows:any;
  private sizeSelected: String = '';
  private ingredientSelected: String = '';
  numero:Number=-1;
  ingredients = ['Salchicha','Queso','Champiñones','Jamon','Peperoni']

  constructor(private router: Router) { 
    this.headers = ["Numero","Tamaño","Ingrediente(s)"];
    
  }

  ngOnInit(): void {
    
  }

  addSandwich(){
    let inputElement:any = document.getElementsByTagName("input");
     
    for(let i of inputElement){
      console.log('ID: '+ i.getAttribute('id'));
      console.log('Valor: '+ i.value);
      
    }
    
  }
  
  selectSize(event:any){
    this.sizeSelected = event.target.value;
    console.log(this.sizeSelected);
    
  }

  selectIngredient(event:any){
    this.ingredientSelected = event.target.value;
    console.log(this.ingredientSelected);
    
  }

  goBack(){
    this.router.navigate(['/home'])

  }

}
