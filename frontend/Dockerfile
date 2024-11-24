FROM node:20.18.1 AS builder
WORKDIR /app
COPY package.json pnpm-lock.yaml tailwind.config.js ./
RUN npm install -g pnpm@8.15.5
RUN npm install -g @angular/cli@19.0.1
RUN pnpm install
COPY . .
RUN ng build --project=user

FROM registry.access.redhat.com/ubi8/nginx-120
COPY ./projects/shell/nginx.conf "${NGINX_CONF_PATH}"
COPY --from=builder /app/dist/user /usr/share/nginx/html2/user/
CMD nginx -g "daemon off;"