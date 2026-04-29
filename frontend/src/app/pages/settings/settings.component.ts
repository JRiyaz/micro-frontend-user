import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ThemeService, NotificationService } from 'ui-shared';
import { inject } from '@angular/core';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <div
      class="min-h-screen bg-slate-50 dark:bg-dark-base p-6 sm:p-8 relative overflow-hidden"
    >
      <div class="max-w-3xl mx-auto relative z-10">
        <!-- Header -->
        <div class="mb-8">
          <a
            routerLink="/dashboard"
            class="inline-flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white font-bold uppercase tracking-widest mb-4 transition-colors"
          >
            <svg
              class="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 19l-7-7 7-7"
              ></path>
            </svg>
            Back to Dashboard
          </a>
          <h1
            class="text-2xl sm:text-3xl font-black tracking-tight text-slate-900 dark:text-white"
          >
            Account Settings
          </h1>
          <p class="text-slate-500 dark:text-slate-400 text-sm mt-1">
            Manage your profile, preferences and security.
          </p>
        </div>

        <!-- Tabs -->
        <div
          class="flex gap-1 mb-8 bg-white dark:bg-white/[0.03] border border-slate-200 dark:border-white/[0.06] rounded-xl p-1 overflow-x-auto shadow-sm dark:shadow-none"
        >
          <button
            *ngFor="let tab of tabs"
            (click)="activeTab.set(tab.id)"
            class="px-4 py-2.5 text-xs font-bold uppercase tracking-widest rounded-lg transition-all whitespace-nowrap"
            [class.bg-primary]="activeTab() === tab.id"
            [class.text-white]="activeTab() === tab.id"
            [class.shadow-lg]="activeTab() === tab.id"
            [class.text-slate-500]="activeTab() !== tab.id"
            [class.dark:text-slate-400]="activeTab() !== tab.id"
            [class.hover:text-slate-900]="activeTab() !== tab.id"
            [class.dark:hover:text-white]="activeTab() !== tab.id"
          >
            {{ tab.label }}
          </button>
        </div>

        <!-- Profile Tab -->
        <div *ngIf="activeTab() === 'profile'" class="space-y-6">
          <div
            class="bg-white dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-none"
          >
            <h3
              class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-widest mb-6"
            >
              Profile Information
            </h3>
            <div class="flex flex-col sm:flex-row items-start gap-6 mb-6">
              <div class="relative group">
                <img
                  src="https://ui-avatars.com/api/?name=Riyaz+Khan&background=3b429f&color=fff&size=80"
                  class="w-20 h-20 rounded-2xl border border-primary/30"
                />
                <div
                  class="absolute inset-0 bg-black/50 rounded-2xl opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity cursor-pointer"
                >
                  <svg
                    class="w-5 h-5 text-white"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"
                    ></path>
                    <circle cx="12" cy="13" r="3"></circle>
                  </svg>
                </div>
              </div>
              <div class="flex-1 w-full">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label
                      class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-2"
                      >First Name</label
                    >
                    <input
                      type="text"
                      value="Riyaz"
                      class="w-full bg-slate-50 dark:bg-dark-base/50 border border-slate-200 dark:border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
                    />
                  </div>
                  <div>
                    <label
                      class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-2"
                      >Last Name</label
                    >
                    <input
                      type="text"
                      value="Khan"
                      class="w-full bg-slate-50 dark:bg-dark-base/50 border border-slate-200 dark:border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="space-y-4">
              <div>
                <label
                  class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-2"
                  >Email</label
                >
                <input
                  type="email"
                  value="riyaz@company.com"
                  class="w-full bg-slate-50 dark:bg-dark-base/50 border border-slate-200 dark:border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
                />
              </div>
              <div>
                <label
                  class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-2"
                  >Role</label
                >
                <input
                  type="text"
                  value="Lead Developer"
                  disabled
                  class="w-full bg-slate-100 dark:bg-dark-base/30 border border-slate-200 dark:border-white/[0.06] rounded-xl px-4 py-3 text-sm text-slate-500 cursor-not-allowed"
                />
              </div>
            </div>
            <button
              class="mt-6 px-6 py-2.5 bg-primary text-white rounded-xl font-bold text-sm hover:bg-primary-hover transition-all"
            >
              Save Changes
            </button>
          </div>
        </div>

        <!-- Appearance Tab -->
        <div *ngIf="activeTab() === 'appearance'" class="space-y-6">
          <div
            class="bg-white dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-none"
          >
            <h3
              class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-widest mb-6"
            >
              Theme
            </h3>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div
                *ngFor="let theme of themes"
                class="bg-slate-50 dark:bg-white/[0.03] border rounded-xl p-4 cursor-pointer transition-all hover:scale-[1.02]"
                [class.border-primary]="
                  themeService.currentTheme() === theme.id
                "
                [class.border-slate-200]="
                  themeService.currentTheme() !== theme.id
                "
                [class.dark:border-white/[0.08]]="
                  themeService.currentTheme() !== theme.id
                "
                (click)="themeService.setTheme(theme.id)"
              >
                <div
                  class="h-16 rounded-lg mb-3"
                  [style.background]="theme.preview"
                ></div>
                <p class="text-sm font-bold text-slate-900 dark:text-white">
                  {{ theme.name }}
                </p>
                <p
                  class="text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider mt-0.5"
                >
                  {{ theme.desc }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Security Tab -->
        <div *ngIf="activeTab() === 'security'" class="space-y-6">
          <div
            class="bg-white dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-none"
          >
            <h3
              class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-widest mb-6"
            >
              Change Password
            </h3>
            <div class="space-y-4 max-w-md">
              <div>
                <label
                  class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-2"
                  >Current Password</label
                >
                <input
                  type="password"
                  placeholder="••••••••"
                  class="w-full bg-slate-50 dark:bg-dark-base/50 border border-slate-200 dark:border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
                />
              </div>
              <div>
                <label
                  class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-2"
                  >New Password</label
                >
                <input
                  type="password"
                  placeholder="Min. 8 characters"
                  class="w-full bg-slate-50 dark:bg-dark-base/50 border border-slate-200 dark:border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
                />
              </div>
              <div>
                <label
                  class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-2"
                  >Confirm Password</label
                >
                <input
                  type="password"
                  placeholder="Re-enter password"
                  class="w-full bg-slate-50 dark:bg-dark-base/50 border border-slate-200 dark:border-white/[0.08] rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
                />
              </div>
              <button
                class="px-6 py-2.5 bg-primary text-white rounded-xl font-bold text-sm hover:bg-primary-hover transition-all"
              >
                Update Password
              </button>
            </div>
          </div>
          <div
            class="bg-white dark:bg-white/[0.04] border border-red-500/20 rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-none"
          >
            <h3
              class="text-sm font-bold text-red-400 uppercase tracking-widest mb-2"
            >
              Danger Zone
            </h3>
            <p class="text-xs text-slate-500 dark:text-slate-400 mb-4">
              Once you delete your account, there is no going back.
            </p>
            <button
              class="px-6 py-2.5 bg-red-500/10 border border-red-500/30 text-red-400 rounded-xl font-bold text-sm hover:bg-red-500/20 transition-all"
            >
              Delete Account
            </button>
          </div>
        </div>

        <!-- Notifications Tab -->
        <div *ngIf="activeTab() === 'notifications'" class="space-y-6">
          <div
            class="bg-white dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-none"
          >
            <h3
              class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-widest mb-6"
            >
              Notification Behavior
            </h3>

            <div class="space-y-8">
              <!-- Do Not Disturb -->
              <div
                class="flex items-center justify-between p-4 bg-slate-50 dark:bg-white/[0.02] border border-slate-200 dark:border-white/[0.06] rounded-xl"
              >
                <div class="flex items-center gap-3">
                  <div
                    class="w-10 h-10 rounded-xl bg-amber-500/10 flex items-center justify-center text-amber-500"
                  >
                    <svg
                      class="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                      ></path>
                    </svg>
                  </div>
                  <div>
                    <h4
                      class="text-sm font-bold text-slate-900 dark:text-white"
                    >
                      Do Not Disturb
                    </h4>
                    <p
                      class="text-xs text-slate-500 dark:text-slate-400 mt-0.5"
                    >
                      Mute all toast notifications while keeping them in
                      history.
                    </p>
                  </div>
                </div>
                <button
                  (click)="
                    notificationService.updateConfig({
                      dnd: !notificationService.config().dnd,
                    })
                  "
                  class="w-11 h-6 rounded-full transition-colors relative"
                  [class.bg-primary]="notificationService.config().dnd"
                  [class.bg-slate-300]="!notificationService.config().dnd"
                  [class.dark:bg-white/10]="!notificationService.config().dnd"
                >
                  <div
                    class="absolute top-1 left-1 w-4 h-4 bg-white rounded-full transition-transform shadow-sm"
                    [class.translate-x-5]="notificationService.config().dnd"
                  ></div>
                </button>
              </div>

              <!-- Duration -->
              <div>
                <div class="flex justify-between items-center mb-3">
                  <label
                    class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em]"
                    >Display Duration</label
                  >
                  <span class="text-xs font-mono text-primary font-bold"
                    >{{ notificationService.config().duration / 1000 }}s</span
                  >
                </div>
                <input
                  type="range"
                  min="2000"
                  max="10000"
                  step="500"
                  [value]="notificationService.config().duration"
                  (input)="updateDuration($event)"
                  class="w-full h-1.5 bg-slate-200 dark:bg-white/10 rounded-lg appearance-none cursor-pointer accent-primary"
                />
                <div
                  class="flex justify-between mt-2 text-[10px] text-slate-400 font-medium"
                >
                  <span>2s</span>
                  <span>5s</span>
                  <span>10s</span>
                </div>
              </div>

              <!-- Placement -->
              <div>
                <label
                  class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-4"
                  >On-Screen Placement</label
                >
                <div class="grid grid-cols-2 gap-3">
                  <button
                    *ngFor="let pos of placements"
                    (click)="
                      notificationService.updateConfig({ placement: pos.id })
                    "
                    class="p-4 border rounded-xl flex flex-col items-center gap-3 transition-all"
                    [class.border-primary]="
                      notificationService.config().placement === pos.id
                    "
                    [class.bg-primary/5]="
                      notificationService.config().placement === pos.id
                    "
                    [class.border-slate-200]="
                      notificationService.config().placement !== pos.id
                    "
                    [class.dark:border-white/10]="
                      notificationService.config().placement !== pos.id
                    "
                  >
                    <div
                      class="w-16 h-12 bg-slate-100 dark:bg-white/5 rounded border border-slate-200 dark:border-white/10 relative overflow-hidden"
                    >
                      <div
                        class="absolute w-3 h-3 bg-primary rounded-sm shadow-[0_0_8px_rgba(109,116,255,0.5)]"
                        [style.top]="pos.id.startsWith('top') ? '4px' : 'auto'"
                        [style.bottom]="
                          pos.id.startsWith('bottom') ? '4px' : 'auto'
                        "
                        [style.left]="pos.id.endsWith('left') ? '4px' : 'auto'"
                        [style.right]="
                          pos.id.endsWith('right') ? '4px' : 'auto'
                        "
                      ></div>
                    </div>
                    <span
                      class="text-[10px] font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400"
                      >{{ pos.label }}</span
                    >
                  </button>
                </div>
              </div>

              <!-- Urgent Toggle -->
              <div
                class="flex items-center justify-between p-4 bg-slate-50 dark:bg-white/[0.02] border border-slate-200 dark:border-white/[0.06] rounded-xl"
              >
                <div>
                  <h4 class="text-sm font-bold text-slate-900 dark:text-white">
                    Persistent Urgent Alerts
                  </h4>
                  <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                    Keep urgent notifications on screen until manually
                    dismissed.
                  </p>
                </div>
                <button
                  (click)="
                    notificationService.updateConfig({
                      urgentStick: !notificationService.config().urgentStick,
                    })
                  "
                  class="w-11 h-6 rounded-full transition-colors relative"
                  [class.bg-primary]="notificationService.config().urgentStick"
                  [class.bg-slate-300]="
                    !notificationService.config().urgentStick
                  "
                  [class.dark:bg-white/10]="
                    !notificationService.config().urgentStick
                  "
                >
                  <div
                    class="absolute top-1 left-1 w-4 h-4 bg-white rounded-full transition-transform shadow-sm"
                    [class.translate-x-5]="
                      notificationService.config().urgentStick
                    "
                  ></div>
                </button>
              </div>
            </div>

            <div
              class="mt-8 pt-6 border-t border-slate-200 dark:border-white/[0.06]"
            >
              <button
                (click)="testUrgent()"
                class="px-5 py-2.5 bg-rose-500/10 border border-rose-500/20 text-rose-500 rounded-xl font-bold text-xs hover:bg-rose-500/20 transition-all uppercase tracking-widest"
              >
                Test Urgent Alert
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [],
})
export class SettingsComponent {
  activeTab = signal('profile');

  tabs = [
    { id: 'profile', label: 'Profile' },
    { id: 'appearance', label: 'Appearance' },
    { id: 'notifications', label: 'Notifications' },
    { id: 'security', label: 'Security' },
  ];

  placements: { id: any; label: string }[] = [
    { id: 'top-left', label: 'Top Left' },
    { id: 'top-right', label: 'Top Right' },
    { id: 'bottom-left', label: 'Bottom Left' },
    { id: 'bottom-right', label: 'Bottom Right' },
  ];

  themes = [
    {
      id: 'void-blue',
      name: 'Void Blue',
      desc: 'Default dark',
      preview: 'linear-gradient(135deg, #0a0b1e, #16193b, #3b429f)',
    },
    {
      id: 'emerald',
      name: 'Emerald',
      desc: 'Lush green',
      preview: 'linear-gradient(135deg, #022c22, #064e3b, #10b981)',
    },
    {
      id: 'rose',
      name: 'Rose',
      desc: 'Vibrant red',
      preview: 'linear-gradient(135deg, #2e1022, #4e1434, #f43f5e)',
    },
    {
      id: 'obsidian',
      name: 'Obsidian',
      desc: 'Sleek purple',
      preview: 'linear-gradient(135deg, #0f172a, #334155, #a855f7)',
    },
  ];

  notificationService = inject(NotificationService);

  constructor(public themeService: ThemeService) {}

  updateDuration(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.notificationService.updateConfig({ duration: parseInt(value, 10) });
  }

  testUrgent() {
    this.notificationService.notify(
      'error',
      'System Alert',
      'This is an urgent persistent notification that will stay until you close it.',
      true,
    );
  }
}
