import { Routes } from '@angular/router';
import { ProductsPage } from './products/products';
import { Chatpage } from './chatpage/chatpage';

export const routes: Routes = [
  { path: '', redirectTo: '/products', pathMatch: 'full' },
  { path: 'products', component: ProductsPage },
  { path: 'inquiry', component: Chatpage },
  { path: '**', redirectTo: '/products' }
];
