import { Component, signal, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ThemeService, NotificationService, WorkspaceService } from 'ui-shared';

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
            Settings
          </h1>
          <p class="text-slate-500 dark:text-slate-400 text-sm mt-1">
            Manage your account, preferences and workspace settings.
          </p>
        </div>

        <!-- Tab Groups -->
        <div class="space-y-8">
          <!-- Navigation Tabs -->
          <div
            class="flex gap-1 bg-white dark:bg-white/[0.03] border border-slate-200 dark:border-white/[0.06] rounded-xl p-1 overflow-x-auto shadow-sm dark:shadow-none sticky top-4 z-20 backdrop-blur-md"
          >
            <button
              *ngFor="let tab of tabs"
              (click)="activeTab.set(tab.id)"
              class="px-4 py-2.5 text-xs font-bold uppercase tracking-widest rounded-lg transition-all whitespace-nowrap flex items-center gap-2"
              [class.bg-primary]="activeTab() === tab.id"
              [class.text-white]="activeTab() === tab.id"
              [class.shadow-lg]="activeTab() === tab.id"
              [class.text-slate-500]="activeTab() !== tab.id"
              [class.dark:text-slate-400]="activeTab() !== tab.id"
              [class.hover:text-slate-900]="activeTab() !== tab.id"
              [class.dark:hover:text-white]="activeTab() !== tab.id"
            >
              <span [innerHTML]="tab.icon" class="w-4 h-4"></span>
              {{ tab.label }}
            </button>
          </div>

          <!-- Tab Content -->
          <div class="mt-8">
            <!-- Profile Tab -->
            <div
              *ngIf="activeTab() === 'profile'"
              class="space-y-6 animate-fade-in"
            >
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
                  class="mt-6 px-6 py-2.5 bg-primary text-white rounded-xl font-bold text-sm hover:bg-primary-hover transition-all shadow-lg shadow-primary/20"
                >
                  Save Changes
                </button>
              </div>
            </div>

            <!-- Security Tab -->
            <div
              *ngIf="activeTab() === 'security'"
              class="space-y-6 animate-fade-in"
            >
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

            <!-- Appearance Tab -->
            <div
              *ngIf="activeTab() === 'appearance'"
              class="space-y-6 animate-fade-in"
            >
              <div
                class="bg-white dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-none"
              >
                <h3
                  class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-widest mb-6"
                >
                  Application Theme
                </h3>
                <div
                  class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4"
                >
                  <div
                    *ngFor="let theme of themes"
                    class="bg-slate-50 dark:bg-white/[0.03] border rounded-xl p-4 cursor-pointer transition-all hover:scale-[1.02] relative group overflow-hidden"
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
                      class="h-20 rounded-lg mb-3 shadow-inner"
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
                    <div
                      *ngIf="themeService.currentTheme() === theme.id"
                      class="absolute top-2 right-2 w-5 h-5 bg-primary text-white rounded-full flex items-center justify-center"
                    >
                      <svg
                        class="w-3 h-3"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="3"
                          d="M5 13l4 4L19 7"
                        ></path>
                      </svg>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Notifications Tab -->
            <div
              *ngIf="activeTab() === 'notifications'"
              class="space-y-6 animate-fade-in"
            >
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
                      [class.dark:bg-white/10]="
                        !notificationService.config().dnd
                      "
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
                        >{{
                          notificationService.config().duration / 1000
                        }}s</span
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
                          notificationService.updateConfig({
                            placement: pos.id,
                          })
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
                            [style.top]="
                              pos.id.startsWith('top') ? '4px' : 'auto'
                            "
                            [style.bottom]="
                              pos.id.startsWith('bottom') ? '4px' : 'auto'
                            "
                            [style.left]="
                              pos.id.endsWith('left') ? '4px' : 'auto'
                            "
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

            <!-- Workspaces Tab -->
            <div
              *ngIf="activeTab() === 'workspaces'"
              class="space-y-6 animate-fade-in"
            >
              <div
                class="bg-white dark:bg-white/[0.04] border border-slate-200 dark:border-white/[0.08] backdrop-blur-md rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-none"
              >
                <div class="flex justify-between items-center mb-6">
                  <h3
                    class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-widest"
                  >
                    Project Workspaces
                  </h3>
                  <span
                    class="px-2.5 py-1 bg-green-500/10 text-green-400 text-[10px] font-black uppercase tracking-wider rounded-lg border border-green-500/20"
                  >
                    {{ workspaceService.subProjects().length }} Connected
                  </span>
                </div>

                <div class="space-y-3">
                  <div
                    *ngFor="
                      let project of workspaceService.subProjects();
                      let i = index
                    "
                    class="group flex items-center justify-between p-4 bg-slate-50 dark:bg-white/[0.02] border border-slate-200 dark:border-white/[0.06] rounded-xl hover:border-primary/30 transition-all cursor-pointer"
                    [class.ring-2]="
                      workspaceService.selectedProjectIndex() === i
                    "
                    [class.ring-primary/20]="
                      workspaceService.selectedProjectIndex() === i
                    "
                    [class.border-primary/40]="
                      workspaceService.selectedProjectIndex() === i
                    "
                    (click)="workspaceService.selectProject(i)"
                  >
                    <div class="flex items-center gap-4">
                      <div class="relative">
                        <div
                          class="w-12 h-12 rounded-xl bg-white dark:bg-white/5 border border-slate-200 dark:border-white/10 flex items-center justify-center text-slate-400 group-hover:text-primary transition-colors"
                        >
                          <svg
                            class="w-6 h-6"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="1.5"
                              d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
                            ></path>
                          </svg>
                        </div>
                        <span
                          class="absolute -top-1 -right-1 w-3.5 h-3.5 rounded-full border-2 border-white dark:border-dark-base"
                          [class.bg-green-400]="project.status === 'running'"
                          [class.bg-slate-500]="project.status === 'offline'"
                          [class.bg-red-500]="project.status === 'error'"
                        ></span>
                      </div>
                      <div>
                        <h4
                          class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2"
                        >
                          {{ project.name }}
                          <span
                            *ngIf="
                              workspaceService.selectedProjectIndex() === i
                            "
                            class="text-[9px] bg-primary text-white px-1.5 py-0.5 rounded uppercase"
                            >Active</span
                          >
                        </h4>
                        <p
                          class="text-xs text-slate-500 dark:text-slate-400 mt-0.5"
                        >
                          Port: {{ project.port || 'N/A' }} • Status:
                          {{ project.status }}
                        </p>
                      </div>
                    </div>
                    <div class="flex items-center gap-2">
                      <button
                        class="p-2 text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors"
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
                            d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
                          ></path>
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                          ></path>
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>

                <div
                  class="mt-8 p-4 bg-primary/5 border border-primary/10 rounded-xl flex items-start gap-3"
                >
                  <svg
                    class="w-5 h-5 text-primary flex-shrink-0 mt-0.5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    ></path>
                  </svg>
                  <p
                    class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed"
                  >
                    Workspaces allow you to manage different micro-frontend
                    services connected to this shell. Active workspace
                    determines the context of certain dashboard features.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [
    `
      .animate-fade-in {
        animation: fadeIn 0.3s ease-out;
      }
      @keyframes fadeIn {
        from {
          opacity: 0;
          transform: translateY(10px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
    `,
  ],
})
export class SettingsComponent {
  activeTab = signal('profile');

  tabs = [
    {
      id: 'profile',
      label: 'Profile',
      icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>',
    },
    {
      id: 'security',
      label: 'Security',
      icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 00-2 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>',
    },
    {
      id: 'appearance',
      label: 'Appearance',
      icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"></path></svg>',
    },
    {
      id: 'notifications',
      label: 'Notifications',
      icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>',
    },
    {
      id: 'workspaces',
      label: 'Workspaces',
      icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>',
    },
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
  workspaceService = inject(WorkspaceService);

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
