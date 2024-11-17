import { Component, OnInit } from "@angular/core";
import { UserService } from "./user.service";
import { CommonModule } from "@angular/common";

@Component({
  selector: "app-carousel",
  standalone: true,
  imports: [CommonModule],
  template: `
    <table class="table m-3">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">User-Name</th>
          <th scope="col">Email</th>
          <th scope="col">Phone</th>
        </tr>
      </thead>
      <tbody>
        @for (user of this.userService.users(); track $index) {
          <tr>
            <th scope="row">{{ user.id }}</th>
            <td>{{ user.name }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.phone }}</td>
          </tr>
        } @empty {
          <td colspan="4">No users found ...</td>
        }
      </tbody>
    </table>
  `,
  styles: ``,
})
export class CarouselComponent implements OnInit {
  constructor(public userService: UserService) {}

  ngOnInit() {
    this.userService.getUsers();
  }
}
