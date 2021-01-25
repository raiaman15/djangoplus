## DJANGO-STARTER

### DEVELOPMENT SETUP
**Deleting Development Setup**
`docker-compose -f dc-local.yml down -v`

**Creating Development Setup**
`docker-compose -f dc-local.yml up --build`

### PRODUCTION SETUP
**Deleting Production Setup**
`docker-compose -f dc-production.yml down -v`

**Creating Prod Setup**
`docker-compose -f dc-production.yml up -d --build`

### PRODUCTION SSL SETUP
**Deleting Production Setup**
`docker-compose -f dc-ssl-production.yml down -v`

**Creating Prod Setup**
`docker-compose -f dc-ssl-production.yml up -d --build`

### USEFUL DOCKER COMMANDS
**Execute Command in Docker Container**
`docker-compose exec <container_name> <command>`

**Deletes all Docker components unused presently (DON'T TRY IF NOT SURE)**
`docker system prune -a`

*NOTE: Volumes persist unless deleted explicitly with "docker-compose -f <yml filename> down -v" where -v flag is for deleting the volume.*

### Reference URLs
- https://docs.docker.com/compose/django/
- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

*NOTE: This is a starter template for django (version 3.1.5)*
*NOTE: You must update the compose/ssl_production/nginx/domain_ssl_cert.pem file with the file generated for your domain. You can generate it from Cloudflare or any other provider.*
*NOTE: You must update the compose/ssl_production/nginx/domain_ssl_private_key.key file with the file generated for your domain. You can generate it from Cloudflare or any other provider.*