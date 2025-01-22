import { Routes } from '@angular/router';
import { NotFoundComponent } from './not-found.component';
import { AppComponent } from './app.component';

export const USER_ROUTES: Routes = [
  {
    path: 'carousel',
    title: 'Carousel',
    loadComponent: () => import('./carousel.component'),
  },
  {
    path: 'model',
    title: 'Model',
    loadComponent: () => import('./model.component'),
  },
  {
    path: '**',
    title: 'Not Found',
    component: NotFoundComponent,
  },
  {
    path: '',
    title: 'Home',
    component: AppComponent,
  },
];

export const routes: Routes = [
  {
    path: 'example',
    title: 'Example',
    loadComponent: () => import('./sample.component'),
  },

  ...USER_ROUTES,
];
