import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <div class="min-h-screen bg-[#0a0b1e] p-6 sm:p-8 relative overflow-hidden">

      <div class="max-w-3xl mx-auto relative z-10">
        <!-- Header -->
        <div class="mb-8">
          <a routerLink="/dashboard" class="inline-flex items-center gap-2 text-xs text-slate-400 hover:text-white font-bold uppercase tracking-widest mb-4 transition-colors">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
            Back to Dashboard
          </a>
          <h1 class="text-2xl sm:text-3xl font-black tracking-tight text-white">Account Settings</h1>
          <p class="text-slate-400 text-sm mt-1">Manage your profile, preferences and security.</p>
        </div>

        <!-- Tabs -->
        <div class="flex gap-1 mb-8 bg-white/[0.03] border border-white/[0.06] rounded-xl p-1 overflow-x-auto">
          <button *ngFor="let tab of tabs" (click)="activeTab.set(tab.id)"
                  class="px-4 py-2.5 text-xs font-bold uppercase tracking-widest rounded-lg transition-all whitespace-nowrap"
                  [class.bg-[#6d74ff]]="activeTab() === tab.id"
                  [class.text-white]="activeTab() === tab.id"
                  [class.shadow-lg]="activeTab() === tab.id"
                  [class.text-slate-500]="activeTab() !== tab.id"
                  [class.hover:text-white]="activeTab() !== tab.id">
            {{ tab.label }}
          </button>
        </div>

        <!-- Profile Tab -->
        <div *ngIf="activeTab() === 'profile'" class="space-y-6">
          <div class="bg-white/[0.04] border border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8">
            <h3 class="text-sm font-bold text-white uppercase tracking-widest mb-6">Profile Information</h3>
            <div class="flex flex-col sm:flex-row items-start gap-6 mb-6">
              <div class="relative group">
                <img src="https://ui-avatars.com/api/?name=Riyaz+Khan&background=3b429f&color=fff&size=80" class="w-20 h-20 rounded-2xl border border-[#6d74ff]/30">
                <div class="absolute inset-0 bg-black/50 rounded-2xl opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity cursor-pointer">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><circle cx="12" cy="13" r="3"></circle></svg>
                </div>
              </div>
              <div class="flex-1 w-full">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2">First Name</label>
                    <input type="text" value="Riyaz" class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all">
                  </div>
                  <div>
                    <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2">Last Name</label>
                    <input type="text" value="Khan" class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all">
                  </div>
                </div>
              </div>
            </div>
            <div class="space-y-4">
              <div>
                <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2">Email</label>
                <input type="email" value="riyaz@company.com" class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all">
              </div>
              <div>
                <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2">Role</label>
                <input type="text" value="Lead Developer" disabled class="w-full bg-[#0a0b1e]/30 border border-white/[0.06] rounded-xl px-4 py-3 text-sm text-slate-500 cursor-not-allowed">
              </div>
            </div>
            <button class="mt-6 px-6 py-2.5 bg-[#6d74ff] text-white rounded-xl font-bold text-sm hover:bg-[#5a61e6] transition-all">Save Changes</button>
          </div>
        </div>

        <!-- Appearance Tab -->
        <div *ngIf="activeTab() === 'appearance'" class="space-y-6">
          <div class="bg-white/[0.04] border border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8">
            <h3 class="text-sm font-bold text-white uppercase tracking-widest mb-6">Theme</h3>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div *ngFor="let theme of themes"
                   class="bg-white/[0.03] border rounded-xl p-4 cursor-pointer transition-all hover:scale-[1.02]"
                   [class.border-[#6d74ff]]="selectedTheme() === theme.id"
                   [class.border-white/[0.08]]="selectedTheme() !== theme.id"
                   (click)="selectedTheme.set(theme.id)">
                <div class="h-16 rounded-lg mb-3" [style.background]="theme.preview"></div>
                <p class="text-sm font-bold text-white">{{ theme.name }}</p>
                <p class="text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">{{ theme.desc }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Security Tab -->
        <div *ngIf="activeTab() === 'security'" class="space-y-6">
          <div class="bg-white/[0.04] border border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8">
            <h3 class="text-sm font-bold text-white uppercase tracking-widest mb-6">Change Password</h3>
            <div class="space-y-4 max-w-md">
              <div>
                <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2">Current Password</label>
                <input type="password" placeholder="••••••••" class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all">
              </div>
              <div>
                <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2">New Password</label>
                <input type="password" placeholder="Min. 8 characters" class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all">
              </div>
              <div>
                <label class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.15em] block mb-2">Confirm Password</label>
                <input type="password" placeholder="Re-enter password" class="w-full bg-[#0a0b1e]/50 border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-2 focus:ring-[#6d74ff]/50 transition-all">
              </div>
              <button class="px-6 py-2.5 bg-[#6d74ff] text-white rounded-xl font-bold text-sm hover:bg-[#5a61e6] transition-all">Update Password</button>
            </div>
          </div>
          <div class="bg-white/[0.04] border border-red-500/20 rounded-2xl p-6 sm:p-8">
            <h3 class="text-sm font-bold text-red-400 uppercase tracking-widest mb-2">Danger Zone</h3>
            <p class="text-xs text-slate-400 mb-4">Once you delete your account, there is no going back.</p>
            <button class="px-6 py-2.5 bg-red-500/10 border border-red-500/30 text-red-400 rounded-xl font-bold text-sm hover:bg-red-500/20 transition-all">Delete Account</button>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: []
})
export class SettingsComponent {
  activeTab = signal('profile');
  selectedTheme = signal('void-blue');

  tabs = [
    { id: 'profile', label: 'Profile' },
    { id: 'appearance', label: 'Appearance' },
    { id: 'security', label: 'Security' },
  ];

  themes = [
    { id: 'void-blue', name: 'Void Blue', desc: 'Default dark', preview: 'linear-gradient(135deg, #0a0b1e, #16193b, #3b429f)' },
    { id: 'midnight', name: 'Midnight', desc: 'Pure dark', preview: 'linear-gradient(135deg, #0f0f0f, #1a1a2e, #16213e)' },
    { id: 'ocean', name: 'Ocean', desc: 'Deep blue', preview: 'linear-gradient(135deg, #0d1b2a, #1b263b, #415a77)' },
  ];
}
