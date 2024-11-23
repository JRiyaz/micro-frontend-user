import { Injectable, signal, WritableSignal } from "@angular/core";

import { User } from "./user";
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: "root",
})
export class UserService {
  private readonly apiUrl = "https://jsonplaceholder.typicode.com/users";
  users: WritableSignal<User[]> = signal([]);

  constructor(private readonly http: HttpClient) {}

  getUsers() {
    this.http
      .get<User[]>(this.apiUrl)
      .subscribe((users) => this.users.set(users));
  }
}
