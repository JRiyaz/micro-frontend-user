FROM node:20.18.1 AS builder
WORKDIR /app
COPY package.json pnpm-lock.yaml tailwind.config.js submodule-husky-hook-path.sh ./
RUN npm install -g pnpm@8.15.5 @angular/cli@19.0.1
RUN pnpm install
COPY . .
RUN ng build --project=shared-ui && ng build --project=user

# FROM nginx:stable-alpine3.20
# WORKDIR /usr/share/nginx/html
# COPY --from=builder /app/dist/user/browser ./user
# RUN cp -r -n ./user/* ./
# COPY ./projects/user/frontend/nginx.conf /etc/nginx/nginx.conf
# CMD nginx -g "daemon off;"
FROM registry.access.redhat.com/ubi8/nginx-120
COPY ./projects/user/frontend/nginx.conf "${NGINX_CONF_PATH}"
WORKDIR /usr/share/nginx/html2/user
COPY --from=builder /app/dist/user/browser ./
RUN cp ./* ../
CMD nginx -g "daemon off;"
