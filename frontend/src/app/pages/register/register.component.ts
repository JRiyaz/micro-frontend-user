import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <div class="min-h-screen bg-[#0a0b1e] flex items-center justify-center p-6 relative overflow-hidden">

      <div class="w-full max-w-xl relative z-10">
        <div class="flex flex-col items-center mb-10">
          <a routerLink="/" class="flex items-center gap-2 mb-6">
            <div class="w-14 h-14 bg-gradient-to-br from-[#6d74ff] to-blue-500 rounded-2xl flex items-center justify-center -rotate-3">
              <span class="text-white font-black text-2xl">I</span>
            </div>
          </a>
          <h1 class="text-3xl font-black tracking-tight text-white">Create Account</h1>
          <p class="text-slate-400 text-sm mt-2">Start managing your inventory today</p>
        </div>

        <div class="bg-white/[0.04] border border-white/[0.08] backdrop-blur-md p-8 sm:p-10 rounded-3xl shadow-2xl">
          <form class="grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2 px-1">First Name</label>
              <input type="text" placeholder="John"
                     class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all" id="register-firstname">
            </div>
            <div>
              <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2 px-1">Last Name</label>
              <input type="text" placeholder="Doe"
                     class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all" id="register-lastname">
            </div>
            <div class="sm:col-span-2">
              <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2 px-1">Work Email</label>
              <input type="email" placeholder="john.doe&#64;company.com"
                     class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all" id="register-email">
            </div>
            <div class="sm:col-span-2">
              <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2 px-1">Password</label>
              <input type="password" placeholder="Min. 8 characters"
                     class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all" id="register-password">
            </div>
            <div class="sm:col-span-2 flex items-center gap-2.5 px-1">
              <input type="checkbox" id="terms" class="w-4 h-4 rounded bg-[#0a0b1e] border-white/[0.15] text-[#6d74ff] focus:ring-[#6d74ff]">
              <label for="terms" class="text-[10px] text-slate-400 font-bold uppercase tracking-widest">I agree to the Terms and Data Policy</label>
            </div>
            <button type="submit"
                    class="sm:col-span-2 bg-[#6d74ff] text-white py-3.5 rounded-xl font-black text-sm uppercase tracking-widest hover:bg-[#5a61e6] transition-all mt-2" id="register-submit">
              Create My Account
            </button>
          </form>
        </div>

        <p class="text-center text-slate-400 text-xs mt-8">
          Already have an account?
          <a routerLink="/user/login" class="text-[#6d74ff] font-bold uppercase tracking-widest hover:underline ml-1">Sign In</a>
        </p>
      </div>
    </div>
  `,
  styles: []
})
export class RegisterComponent {}
