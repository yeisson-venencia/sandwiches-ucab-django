import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  baseUrl = 'http://localhost:8000/api/'
  
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


}
