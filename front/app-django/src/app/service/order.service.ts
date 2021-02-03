import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  baseUrl = 'http://localhost:8000/api/'
  sizeArray = null;
  ingredientArray = null;
  
  constructor(
    private http: HttpClient
  ) { }
  
  getSize(){
    let url = this.baseUrl + 'size-list/'
    return this.http.get(url)

  }


  getIngredient(){
    let url = this.baseUrl + 'ingredient-list/'
    return this.http.get(url)
  }

  postOrder(json){
    let url = this.baseUrl + 'register-order/';
    return this.http.post(url,json);
  }

  findSize(size){    
    for(let x of this.sizeArray){
      if(size === x.name)
        return x;
    }
  }

  findIngredient(ingredient){
    for(let x of this.ingredientArray){
      if(ingredient === x.name)
        return x;
    }
  }

  payBill(orden:any){
    let body = {};
    let url = this.baseUrl + 'register-order/'
    /* let user = {};
    user["document"]="4789623";
    user["first_name"]="Jose";
    user["last_name"]="Jose";

    body["usuario"]= []
    body["usuario"].push(user); */
    body["sandwiches"] = [];
    
    for(let i of orden){
      let sandwich = {};    
      sandwich["size"] = this.findSize(i.Tamaño);
      sandwich["ingredients"] = [];
      for(let ing of i.Ingredientes){
        let aux = ing[0].split(" ");
        let ingrediente = null;
        ingrediente = this.findIngredient(aux.slice(1).join(" "));     
        ingrediente["rations"]=parseInt(aux[0]);
        sandwich["ingredients"].push(ingrediente);
      }
      body["sandwiches"].push(sandwich);
    }

    return body;

  }


}
