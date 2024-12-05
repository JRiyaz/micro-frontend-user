import {
  ApplicationConfig,
  provideExperimentalZonelessChangeDetection,
} from '@angular/core';
import { provideRouter } from '@angular/router';
// import { APP_BASE_HREF } from "@angular/common";

import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    // {provide: APP_BASE_HREF, useValue: "/user/"},
    provideExperimentalZonelessChangeDetection(),
    provideRouter(routes),
    provideHttpClient(),
  ],
};
