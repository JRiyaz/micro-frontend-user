import { inject, Injectable } from '@angular/core';

import { User } from './user';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private readonly apiUrl = 'https://jsonplaceholder.typicode.com/users';

  // constructor(private readonly http: HttpClient) {}
  http: HttpClient | undefined;

  constructor() {
    this.http = inject(HttpClient);
  }

  getUsers(): Observable<User[]> {
    return this.http!.get<User[]>(this.apiUrl);
  }
}
