import { Routes } from "@angular/router";
import { SampleComponent } from "./sample.component";
import { NotFoundComponent } from "./not-found.component";
import { AppComponent } from "./app.component";

export const USER_ROUTES: Routes = [
  {
    path: "carousel",
    title: "Carousel",
    loadComponent: () =>
      import("./carousel.component").then((x) => x.CarouselComponent),
  },
  {
    path: "model",
    title: "Model",
    loadComponent: () =>
      import("./model.component").then((x) => x.ModelComponent),
  },
  {
    path: "**",
    title: "Not Found",
    component: NotFoundComponent,
  },
  {
    path: "",
    title: "Home",
    component: AppComponent,
  },
];

export const routes: Routes = [
  {
    path: "example",
    title: "Example",
    component: SampleComponent,
  },

  ...USER_ROUTES,
];
