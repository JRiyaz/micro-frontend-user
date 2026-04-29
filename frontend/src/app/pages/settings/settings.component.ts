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
      class="min-h-screen bg-slate-50 dark:bg-dark-base p-4 sm:p-8 relative overflow-hidden flex items-center justify-center"
    >
      <div
        class="w-full max-w-3xl relative z-10 flex flex-col h-[90vh] max-h-[850px]"
      >
        <!-- Header (Fixed) -->
        <div class="mb-6 flex-shrink-0">
          <a
            routerLink="/dashboard"
            class="inline-flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white font-bold uppercase tracking-widest mb-3 transition-colors"
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

        <!-- Navigation Tabs (Fixed) -->
        <div
          class="flex w-full bg-white dark:bg-white/[0.03] border border-slate-200 dark:border-white/[0.06] rounded-xl p-1 shadow-sm dark:shadow-none mb-6 flex-shrink-0"
        >
          <button
            *ngFor="let tab of tabs"
            (click)="activeTab.set(tab.id)"
            class="flex-1 px-2 py-2.5 text-[10px] sm:text-xs font-bold uppercase tracking-widest rounded-lg transition-all flex items-center justify-center gap-2 text-center"
            [class.bg-primary]="activeTab() === tab.id"
            [class.text-white]="activeTab() === tab.id"
            [class.shadow-lg]="activeTab() === tab.id"
            [class.text-slate-500]="activeTab() !== tab.id"
            [class.dark:text-slate-400]="activeTab() !== tab.id"
            [class.hover:text-slate-900]="activeTab() !== tab.id"
            [class.dark:hover:text-white]="activeTab() !== tab.id"
          >
            <span
              *ngIf="tab.icon"
              [innerHTML]="tab.icon"
              class="w-4 h-4 hidden sm:block"
            ></span>
            <span class="truncate">{{ tab.label }}</span>
          </button>
        </div>

        <!-- Tab Content (Scrollable) -->
        <div class="flex-1 overflow-y-auto pr-2 custom-scrollbar min-h-0">
          <div class="pb-8">
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
                  class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4"
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
                    <p class="text-xs font-bold text-slate-900 dark:text-white">
                      {{ theme.name }}
                    </p>
                    <p
                      class="text-[9px] text-slate-500 dark:text-slate-400 uppercase tracking-wider mt-0.5"
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

                <div class="space-y-6">
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

                  <!-- Urgent Stick -->
                  <div
                    class="flex items-center justify-between p-4 bg-slate-50 dark:bg-white/[0.02] border border-slate-200 dark:border-white/[0.06] rounded-xl"
                  >
                    <div class="flex items-center gap-3">
                      <div
                        class="w-10 h-10 rounded-xl bg-rose-500/10 flex items-center justify-center text-rose-500"
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
                            d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 00-2 2zm10-10V7a4 4 0 00-8 0v4h8z"
                          ></path>
                        </svg>
                      </div>
                      <div>
                        <h4
                          class="text-sm font-bold text-slate-900 dark:text-white"
                        >
                          Urgent Persistence
                        </h4>
                        <p
                          class="text-xs text-slate-500 dark:text-slate-400 mt-0.5"
                        >
                          Critical alerts stay on screen until manually
                          dismissed.
                        </p>
                      </div>
                    </div>
                    <button
                      (click)="
                        notificationService.updateConfig({
                          urgentStick:
                            !notificationService.config().urgentStick,
                        })
                      "
                      class="w-11 h-6 rounded-full transition-colors relative"
                      [class.bg-primary]="
                        notificationService.config().urgentStick
                      "
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

                  <!-- Duration -->
                  <div
                    class="p-4 bg-slate-50 dark:bg-white/[0.02] border border-slate-200 dark:border-white/[0.06] rounded-xl"
                  >
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
                  <div
                    class="p-4 bg-slate-50 dark:bg-white/[0.02] border border-slate-200 dark:border-white/[0.06] rounded-xl"
                  >
                    <label
                      class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-[0.15em] block mb-4"
                      >On-Screen Placement</label
                    >
                    <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
                      <button
                        *ngFor="let pos of placements"
                        (click)="
                          notificationService.updateConfig({
                            placement: pos.id,
                          })
                        "
                        class="p-3 border rounded-xl flex flex-col items-center gap-2 transition-all"
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
                          class="w-full aspect-[4/3] bg-slate-100 dark:bg-white/5 rounded border border-slate-200 dark:border-white/10 relative overflow-hidden"
                        >
                          <div
                            class="absolute w-2.5 h-2.5 bg-primary rounded-sm shadow-[0_0_8px_rgba(109,116,255,0.5)]"
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
                          class="text-[9px] font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400 text-center"
                          >{{ pos.label }}</span
                        >
                      </button>
                    </div>
                  </div>
                </div>

                <div
                  class="mt-8 pt-6 border-t border-slate-200 dark:border-white/[0.06] flex gap-3"
                >
                  <button
                    (click)="testUrgent()"
                    class="flex-1 px-5 py-2.5 bg-rose-500/10 border border-rose-500/20 text-rose-500 rounded-xl font-bold text-xs hover:bg-rose-500/20 transition-all uppercase tracking-widest"
                  >
                    Test Urgent
                  </button>
                  <button
                    (click)="
                      notificationService.success(
                        'System Check',
                        'All modules are operating normally.'
                      )
                    "
                    class="flex-1 px-5 py-2.5 bg-green-500/10 border border-green-500/20 text-green-500 rounded-xl font-bold text-xs hover:bg-green-500/20 transition-all uppercase tracking-widest"
                  >
                    Test Standard
                  </button>
                </div>
              </div>
            </div>

            <!-- Workspaces Tab -->
            <div
              *ngIf="activeTab() === 'workspaces'"
              class="space-y-6 animate-fade-in"
            >
              <!-- Platform Version -->
              <div class="flex flex-col items-center justify-center mb-4">
                <div
                  class="bg-primary/10 border border-primary/20 px-4 py-1.5 rounded-full flex items-center gap-2 shadow-sm"
                >
                  <div
                    class="w-2 h-2 bg-primary rounded-full animate-pulse"
                  ></div>
                  <span
                    class="text-[10px] font-black uppercase tracking-[0.2em] text-primary"
                    >Platform v1.2.4-stable</span
                  >
                </div>
              </div>

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

                <div class="space-y-4">
                  <div
                    *ngFor="let project of projectsWithDetails; let i = index"
                    class="group relative bg-slate-50 dark:bg-white/[0.02] border border-slate-200 dark:border-white/[0.06] rounded-2xl overflow-hidden transition-all hover:border-primary/40"
                    [class.ring-2]="
                      workspaceService.selectedProjectIndex() === i
                    "
                    [class.ring-primary/30]="
                      workspaceService.selectedProjectIndex() === i
                    "
                    (click)="workspaceService.selectProject(i)"
                  >
                    <div
                      *ngIf="workspaceService.selectedProjectIndex() === i"
                      class="absolute left-0 top-0 bottom-0 w-1 bg-primary"
                    ></div>

                    <div class="p-5 flex flex-col sm:flex-row gap-5">
                      <div class="flex-shrink-0">
                        <div
                          class="w-14 h-14 rounded-2xl bg-white dark:bg-white/5 border border-slate-200 dark:border-white/10 flex items-center justify-center text-slate-400 group-hover:text-primary transition-colors shadow-sm"
                        >
                          <svg
                            class="w-7 h-7"
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
                      </div>

                      <div class="flex-1 min-w-0">
                        <div class="flex items-center justify-between mb-2">
                          <h4
                            class="text-base font-black text-slate-900 dark:text-white truncate flex items-center gap-2"
                          >
                            {{ project.name }}
                            <span
                              *ngIf="
                                workspaceService.selectedProjectIndex() === i
                              "
                              class="text-[9px] bg-primary text-white px-1.5 py-0.5 rounded uppercase font-bold"
                              >Active</span
                            >
                          </h4>
                          <span class="flex items-center gap-1.5">
                            <span
                              class="w-2 h-2 rounded-full"
                              [class.bg-green-400]="
                                project.status === 'running'
                              "
                              [class.bg-red-400]="project.status === 'error'"
                            ></span>
                            <span
                              class="text-[10px] font-bold uppercase tracking-widest text-slate-500 dark:text-slate-400"
                              >{{ project.status }}</span
                            >
                          </span>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-4">
                          <div class="space-y-1">
                            <p
                              class="text-[9px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest"
                            >
                              Address
                            </p>
                            <p
                              class="text-xs font-mono text-slate-700 dark:text-slate-300"
                            >
                              {{ project.ip }}
                            </p>
                          </div>
                          <div class="space-y-1">
                            <p
                              class="text-[9px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest"
                            >
                              Port
                            </p>
                            <p
                              class="text-xs font-mono text-slate-700 dark:text-slate-300"
                            >
                              {{ project.port }}
                            </p>
                          </div>
                          <div class="space-y-1">
                            <p
                              class="text-[9px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest"
                            >
                              Version
                            </p>
                            <p
                              class="text-xs font-mono text-slate-700 dark:text-slate-300"
                            >
                              v{{ project.version }}
                            </p>
                          </div>
                          <div class="space-y-1">
                            <p
                              class="text-[9px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest"
                            >
                              Protocol
                            </p>
                            <p
                              class="text-xs font-mono text-slate-700 dark:text-slate-300"
                            >
                              HTTP/1.1
                            </p>
                          </div>
                        </div>

                        <!-- Services List -->
                        <div
                          class="mt-4 pt-4 border-t border-slate-200/50 dark:border-white/5"
                        >
                          <p
                            class="text-[9px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest mb-2"
                          >
                            Active Services
                          </p>
                          <div class="flex flex-wrap gap-2">
                            <div
                              *ngFor="let svc of project.services"
                              class="px-2 py-1 bg-primary/5 dark:bg-primary/10 border border-primary/20 rounded-lg text-[9px] font-bold text-primary uppercase tracking-tight"
                            >
                              {{ svc }}
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div
                      class="px-5 py-2.5 bg-slate-100 dark:bg-white/[0.03] border-t border-slate-200 dark:border-white/[0.06] flex justify-between items-center"
                    >
                      <span class="text-[9px] text-slate-500 font-medium italic"
                        >Last heartbeat: {{ project.lastSeen }}</span
                      >
                      <div class="flex items-center gap-3">
                        <button
                          class="text-[10px] font-bold text-primary uppercase hover:underline"
                        >
                          Re-ping
                        </button>
                        <button
                          class="text-[10px] font-bold text-slate-500 uppercase hover:text-slate-900 dark:hover:text-white transition-colors"
                        >
                          Logs
                        </button>
                      </div>
                    </div>
                  </div>
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

      /* Custom Scrollbar */
      .custom-scrollbar::-webkit-scrollbar {
        width: 6px;
      }
      .custom-scrollbar::-webkit-scrollbar-track {
        background: transparent;
      }
      .custom-scrollbar::-webkit-scrollbar-thumb {
        background: rgba(109, 116, 255, 0.2);
        border-radius: 10px;
        transition: background 0.3s ease;
      }
      .custom-scrollbar::-webkit-scrollbar-thumb:hover {
        background: rgba(109, 116, 255, 0.4);
      }

      .custom-scrollbar {
        scrollbar-width: thin;
        scrollbar-color: rgba(109, 116, 255, 0.2) transparent;
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
      desc: 'Deep Space',
      preview: 'linear-gradient(135deg, #060714, #111333, #6d74ff)',
    },
    {
      id: 'emerald',
      name: 'Emerald',
      desc: 'Deep Jungle',
      preview: 'linear-gradient(135deg, #020d0a, #06241c, #10b981)',
    },
    {
      id: 'rose',
      name: 'Rose',
      desc: 'Crimson Velvet',
      preview: 'linear-gradient(135deg, #0d0408, #260c19, #f43f5e)',
    },
    {
      id: 'obsidian',
      name: 'Obsidian',
      desc: 'Midnight Orchid',
      preview: 'linear-gradient(135deg, #080511, #180f31, #a855f7)',
    },
    {
      id: 'gold',
      name: 'Gold',
      desc: 'Warm Luxury',
      preview: 'linear-gradient(135deg, #14120a, #35301b, #d4af37)',
    },
  ];

  notificationService = inject(NotificationService);
  workspaceService = inject(WorkspaceService);

  get projectsWithDetails() {
    const versions = ['1.2.4', '1.1.2', '1.0.0'];
    return this.workspaceService.subProjects().map((p, i) => ({
      ...p,
      ip: `192.168.1.${10 + i}`,
      version: p.name.includes('Shell')
        ? '1.2.4'
        : versions[i % versions.length],
      lastSeen: i === 0 ? 'Live' : `${i * 2 + 1} mins ago`,
      services: p.services || ['Core Module'],
    }));
  }

  constructor(public themeService: ThemeService) {}

  updateDuration(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.notificationService.updateConfig({ duration: parseInt(value, 10) });
  }

  testUrgent() {
    this.notificationService.notify(
      'error',
      'Security Breach',
      'Detected unauthorized access attempt from IP 192.168.1.45',
      true,
    );
  }
}
