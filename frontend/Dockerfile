FROM node:20.18.1 AS builder
WORKDIR /app
COPY package.json pnpm-lock.yaml tailwind.config.js submodule-husky-hook-path.sh ./
RUN npm install -g pnpm@8.15.5 @angular/cli@18.2.12
RUN pnpm install
COPY . .
RUN ng build --project=shared-ui && ng build --base-href=/user/ --project=user

FROM nginx:alpine
WORKDIR /usr/share/nginx/user
COPY --from=builder /app/dist/user/browser ./
COPY ./projects/user/frontend/nginx.conf /etc/nginx/nginx.conf
CMD nginx -g "daemon off;"
