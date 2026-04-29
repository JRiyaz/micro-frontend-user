import { Component, inject, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import {
  FormBuilder,
  FormGroup,
  Validators,
  ReactiveFormsModule,
} from '@angular/forms';
import { toSignal } from '@angular/core/rxjs-interop';
import { map, startWith } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, RouterModule, ReactiveFormsModule],
  template: `
    <div
      class="min-h-screen bg-slate-50 dark:bg-dark-base flex items-center justify-center p-6 relative overflow-hidden"
    >
      <div class="w-full max-w-md relative z-10">
        <div class="flex flex-col items-center mb-10">
          <a routerLink="/" class="flex items-center gap-2 mb-6">
            <div
              class="w-14 h-14 bg-gradient-to-br from-primary to-blue-500 rounded-2xl flex items-center justify-center rotate-3"
            >
              <span class="text-white font-black text-2xl">I</span>
            </div>
          </a>
          <h1
            class="text-3xl font-black tracking-tight text-slate-900 dark:text-white"
          >
            Welcome Back
          </h1>
          <p class="text-slate-500 dark:text-slate-400 text-sm mt-2">
            Sign in to your Inventory account
          </p>
        </div>

        <div
          class="bg-white dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] backdrop-blur-md p-8 rounded-3xl shadow-xl dark:shadow-2xl"
        >
          <form
            [formGroup]="loginForm"
            (ngSubmit)="onSubmit()"
            class="space-y-8"
          >
            <!-- Email Field -->
            <div class="floating-input-group">
              <input
                type="email"
                formControlName="email"
                id="login-email"
                placeholder=" "
                class="floating-input"
              />
              <label for="login-email" class="floating-label"
                >Email Address</label
              >
              <!-- Validation Error -->
              <div *ngIf="emailInvalid()" class="absolute -bottom-5 left-0">
                <span
                  *ngIf="loginForm.get('email')?.errors?.['required']"
                  class="text-[10px] text-rose-500 font-bold uppercase tracking-tight"
                  >Email is required</span
                >
                <span
                  *ngIf="loginForm.get('email')?.errors?.['email']"
                  class="text-[10px] text-rose-500 font-bold uppercase tracking-tight"
                  >Invalid email format</span
                >
              </div>
            </div>

            <!-- Password Field -->
            <div class="floating-input-group">
              <input
                type="password"
                formControlName="password"
                id="login-password"
                placeholder=" "
                class="floating-input"
              />
              <label for="login-password" class="floating-label"
                >Password</label
              >
              <!-- Validation Error -->
              <div *ngIf="passwordInvalid()" class="absolute -bottom-5 left-0">
                <span
                  *ngIf="loginForm.get('password')?.errors?.['required']"
                  class="text-[10px] text-rose-500 font-bold uppercase tracking-tight"
                  >Password is required</span
                >
                <span
                  *ngIf="loginForm.get('password')?.errors?.['minlength']"
                  class="text-[10px] text-rose-500 font-bold uppercase tracking-tight"
                  >Min 6 characters required</span
                >
              </div>
              <a
                href="#"
                class="absolute right-0 top-7 text-[10px] font-bold text-primary hover:underline uppercase tracking-widest z-10"
                >Forgot?</a
              >
            </div>

            <button
              type="submit"
              [disabled]="isFormInvalid()"
              class="w-full bg-primary disabled:opacity-50 disabled:cursor-not-allowed text-white py-3.5 rounded-xl font-black text-sm uppercase tracking-widest hover:bg-primary-hover transition-all shadow-lg shadow-primary/20"
              id="login-submit"
            >
              Sign In
            </button>
          </form>

          <div class="relative my-10">
            <div class="absolute inset-0 flex items-center">
              <div
                class="w-full border-t border-slate-200 dark:border-white/[0.08]"
              ></div>
            </div>
            <div
              class="relative flex justify-center text-[10px] uppercase font-bold tracking-widest"
            >
              <span
                class="bg-white dark:bg-dark-base px-4 text-slate-500 dark:text-slate-400"
                >Or continue with</span
              >
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3">
            <button
              class="bg-slate-50 dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] py-3 rounded-xl flex items-center justify-center gap-2 hover:bg-slate-100 dark:hover:bg-white/[0.06] transition-all text-slate-900 dark:text-white"
            >
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                <path
                  d="M12.48 10.92v3.28h7.84c-.24 1.84-.908 3.152-1.896 4.136-1.248 1.248-3.224 2.536-7.224 2.536-5.88 0-10.456-4.76-10.456-10.64s4.576-10.64 10.456-10.64c3.24 0 5.64 1.264 7.424 2.976l2.328-2.328c-1.92-1.84-4.824-3.232-8.992-3.232-7.536 0-13.728 6.12-13.728 13.64s6.192 13.64 13.728 13.64c4.104 0 7.424-1.328 9.824-3.832 2.52-2.52 3.312-6.048 3.312-8.736 0-.84-.048-1.544-.144-2.24h-12.984z"
                />
              </svg>
              <span class="text-xs font-bold uppercase tracking-tight"
                >Google</span
              >
            </button>
            <button
              class="bg-slate-50 dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] py-3 rounded-xl flex items-center justify-center gap-2 hover:bg-slate-100 dark:hover:bg-white/[0.06] transition-all text-slate-900 dark:text-white"
            >
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                <path
                  d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
                />
              </svg>
              <span class="text-xs font-bold uppercase tracking-tight"
                >GitHub</span
              >
            </button>
          </div>
        </div>

        <p class="text-center text-slate-500 dark:text-slate-400 text-xs mt-8">
          New here?
          <a
            routerLink="/user/register"
            class="text-primary font-bold uppercase tracking-widest hover:underline ml-1"
            >Create Account</a
          >
        </p>
      </div>
    </div>
  `,
  styles: [],
})
export class LoginComponent {
  private fb = inject(FormBuilder);

  loginForm: FormGroup = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
  });

  // Signal for form validity
  private formStatus = toSignal(
    this.loginForm.statusChanges.pipe(
      startWith(this.loginForm.status),
      map((status) => status === 'INVALID'),
    ),
    { initialValue: true },
  );

  isFormInvalid = computed(() => this.formStatus());

  // Signals for field validity
  emailInvalid = toSignal(
    this.loginForm.get('email')!.statusChanges.pipe(
      startWith(this.loginForm.get('email')!.status),
      map(
        () =>
          this.loginForm.get('email')!.touched &&
          this.loginForm.get('email')!.invalid,
      ),
    ),
    { initialValue: false },
  );

  passwordInvalid = toSignal(
    this.loginForm.get('password')!.statusChanges.pipe(
      startWith(this.loginForm.get('password')!.status),
      map(
        () =>
          this.loginForm.get('password')!.touched &&
          this.loginForm.get('password')!.invalid,
      ),
    ),
    { initialValue: false },
  );

  onSubmit() {
    if (this.loginForm.valid) {
      console.log('Login Form Submitted', this.loginForm.value);
    } else {
      this.loginForm.markAllAsTouched();
    }
  }
}
