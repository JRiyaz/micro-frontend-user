import { Injectable, signal, WritableSignal } from "@angular/core";

import { User } from "./user";
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: "root",
})
export class UserService {
  private apiUrl = "https://jsonplaceholder.typicode.com/users";
  users: WritableSignal<User[]> = signal([]);

  constructor(private http: HttpClient) {}

  getUsers() {
    this.http
      .get<User[]>(this.apiUrl)
      .subscribe((users) => this.users.set(users));
  }
}
