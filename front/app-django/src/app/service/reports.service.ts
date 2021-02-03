import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ReportsService {

  baseUrl = 'http://localhost:8000/api/'

  constructor(
    private http: HttpClient
  ) { }

  reportVentasTamano(id: number){

    let url = this.baseUrl + 'get-all-sandwich-size/'

    let data = {
      "id": id,
      "name": "individual",
      "price": "200.00"
    }

    return this.http.post(url, data)


  }

}
