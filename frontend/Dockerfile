FROM node:20.18.1 AS builder
WORKDIR /app
COPY package.json pnpm-lock.yaml tailwind.config.js submodule-husky-hook-path.sh ./
RUN npm install -g pnpm@9.14.2 @angular/cli@19.1.2
RUN pnpm install
COPY . .
RUN ng build --project=shared-ui && ng build --base-href=/user/ --project=user-service

FROM nginx:stable-alpine3.21
WORKDIR /usr/share/nginx/user
COPY --from=builder /app/dist/user-service/browser ./
COPY ./projects/user-service/frontend/nginx.conf /etc/nginx/nginx.conf
CMD nginx -g "daemon off;"
