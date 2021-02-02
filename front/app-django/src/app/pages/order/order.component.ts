import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  headers = ["Número","Tamaño","Ingredientes"];
  size=["Grande","Medio","Pequeño"];
  ingredients = ["Jamon","Champiñones","Pimenton","Doble queso"];

  rows =[
    {
      "Número":"1",
      "Tamaño":"Pequeño",
      "Ingredientes":["Salami"," Chorizo"]
    },
    {
      "Número":"2",
      "Tamaño":"Grande",
      "Ingredientes":"Salchica"
    },
    {
      "Número":"3",
      "Tamaño":"Mediano",
      "Ingredientes":"Chorizo"
    }
  ];

  agregar(){
    this.rows.push({"Número":"3","Tamaño":"Mediano","Ingredientes":"Chorizo"})
  }

}
