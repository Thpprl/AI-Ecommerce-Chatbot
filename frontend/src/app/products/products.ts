import { Component, OnInit, signal, ViewEncapsulation } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  description: string;
}

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './products.html',
  styleUrl: './products.css',  
  encapsulation: ViewEncapsulation.None 

})
export class ProductsPage implements OnInit {
  products = signal<Product[]>([]);

  constructor(private router: Router) {}

  ngOnInit() {
    this.loadProducts();
  }

loadProducts() {
  this.products.set([
    {
      id: 1,
      name: 'A1990 A1953 Battery MacBook Pro 15"',
      price: 75.99,
      image: 'https://www.freedomcomputerservice.net/upload/id0005824/%E0%B9%81%E0%B8%9A%E0%B8%95%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B8%B5%E0%B9%88-MacBook(ORIGINAL)-A1953-Macbook-PRO-RETINA-15-MODEL-A1990-%E0%B8%9B%E0%B8%B5-2018--2019.jpg',
      description: 'Battery MacBook Pro 15 inch (2018-2019) 7400mAh ⭐ 3.9'
    },
    {
      id: 2,
      name: 'Under Desk Mount Holder for Mac Studio',
      price: 25.99,
      image: 'https://m.media-amazon.com/images/I/61lCthip6tL._AC_UF350,350_QL50_.jpg',
      description: 'ที่ยึด Mac Studio ใต้โต๊ะ ⭐ 4.0'
    },
    {
      id: 3,
      name: 'Laptop Skin Sticker Pink Letters',
      price: 11.85,
      image: 'https://m.media-amazon.com/images/I/61rsMQgeAsL.jpg',
      description: 'สติ๊กเกอร์ Laptop ลายตัวอักษรสีชมพู ⭐ 4.1'
    },
    {
      id: 4,
      name: 'Anime Girls Sticker Pack 50pcs',
      price: 5.99,
      image: 'https://m.media-amazon.com/images/I/81VTcEFv7GL._AC_UF894,1000_QL80_.jpg',
      description: 'สติ๊กเกอร์อนิเมะ 50 ชิ้น ⭐ 4.2'
    },
    {
      id: 5,
      name: 'Dell Inspiron Battery 39DY5',
      price: 36.79,
      image: 'https://nextplay.co.th/wp-content/uploads/2022/01/39DY5-06.jpg',
      description: 'แบตเตอรี่ Dell Inspiron ⭐ 4.5'
    },
    {
      id: 6,
      name: 'Ghost Rock Band Sticker',
      price: 3.97,
      image: 'https://i.ebayimg.com/images/g/w5gAAOSwb1Rjo1SC/s-l1200.jpg',
      description: 'สติ๊กเกอร์วง Ghost ⭐ 4.5'
    },
    {
      id: 7,
      name: '65W HP USB-C Charger',
      price: 22.88,
      image: 'https://th-media.apjonlinecdn.com/catalog/product/1/P/1P3K6AA-1_T1681807481.png',
      description: 'ที่ชาร์จ HP USB-C ⭐ 4.5'
    },
    {
      id: 8,
      name: '90W Dell Laptop Charger',
      price: 36.99,
      image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ--piv1jH3zmxC9bBUBRhPu_ClsY3WUA5mwA&s',
      description: 'Adapter Dell 90W ⭐ 4.6'
    },
  ]);
}

  goToInquiry() {
    this.router.navigate(['/inquiry']);
  }
}

