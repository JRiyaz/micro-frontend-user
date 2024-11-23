import { Component } from "@angular/core";
import { RouterLink, RouterOutlet } from "@angular/router";

@Component({
  selector: "app-root",
  imports: [RouterOutlet, RouterLink],
  template: `
    <ul class="nav">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" routerLink="/">Active</a>
      </li>

      <li class="nav-item">
        <a class="nav-link" routerLink="/example">sample</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" routerLink="/carousel">carousel</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" routerLink="/model">model</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" routerLink="/something">something</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" aria-disabled="true">Disabled</a>
      </li>
    </ul>

    <router-outlet />
  `,
  styles: [],
})
export class AppComponent {
  title = "user";
}
