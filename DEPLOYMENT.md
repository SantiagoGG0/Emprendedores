# Deployment AWS Elastic Beanstalk - Guía Paso a Paso

## Preparación Local

### 1. Instalar AWS EB CLI
```powershell
pip install awsebcli
```

### 2. Configurar AWS Credentials
Opción A - AWS CLI (recomendado):
```powershell
pip install awscli
aws configure
# Ingresa: Access Key ID, Secret Access Key, Region (us-east-2), Output format (json)
```

Opción B - Variables de entorno:
```powershell
$env:AWS_ACCESS_KEY_ID="tu-access-key"
$env:AWS_SECRET_ACCESS_KEY="tu-secret-key"
$env:AWS_DEFAULT_REGION="us-east-2"
```

## Deployment Completo

### 3. Inicializar EB (primera vez)
```powershell
# Desde directorio del proyecto
cd C:\Users\santi\Desktop\suluhisho

# Inicializar EB
eb init

# Responde:
# - Region: 18) us-east-2 (Ohio)
# - Application name: suluhisho
# - Platform: Python
# - Platform branch: Python 3.13
# - CodeCommit: N
# - SSH: Y (para debug)
```

### 4. Crear Environment y Deployar
```powershell
# Crear environment (toma 5-10 min)
eb create suluhisho-env

# Espera a que complete...
```

### 5. Configurar Variables de Entorno
```powershell
# SECRET_KEY - genera uno nuevo:
eb setenv SECRET_KEY="django-insecure-CAMBIA-ESTO-POR-UNO-SEGURO-$(Get-Random)"

# Database (si usas PostgreSQL RDS):
# eb setenv DATABASE_URL="postgresql://user:pass@host:5432/dbname"

# Allowed hosts (el dominio que te da AWS):
eb setenv ALLOWED_HOSTS=".elasticbeanstalk.com,.amazonaws.com"

# Admin credentials (opcional, usa defaults si no configuras):
# eb setenv DJANGO_ADMIN_USERNAME="admin" DJANGO_ADMIN_EMAIL="admin@example.com" DJANGO_ADMIN_PASSWORD="secure-password"
```

### 6. Abrir Aplicación
```powershell
eb open
```

## Actualizaciones Futuras

### Deployar Cambios
```powershell
# Después de hacer cambios en código:
eb deploy

# Ver logs si hay problemas:
eb logs

# Ver status:
eb status

# SSH al servidor (para debug):
eb ssh
```

## Base de Datos

### Opción A: SQLite (default, solo para testing)
- Ya configurado, funciona automáticamente
- **NO recomendado para production real** (se pierde al redeploy)

### Opción B: PostgreSQL RDS (recomendado production)
```powershell
# Crear RDS desde AWS Console:
# 1. RDS > Create database > PostgreSQL
# 2. Free tier o production según necesidad
# 3. Anotar: endpoint, port, username, password, database name

# Configurar en EB:
eb setenv DATABASE_URL="postgresql://username:password@endpoint:5432/dbname"
```

Luego agregar a `suluhisho_platform/settings/production.py`:
```python
import dj_database_url

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ['DATABASE_URL'])
    }
```

Y agregar a `requirements/production.txt`:
```
dj-database-url==2.2.0
```

## Media Files (S3)

Para subir archivos usuarios (media/):

1. Crear S3 bucket desde AWS Console
2. Agregar a requirements:
   ```
   django-storages[s3]==1.14.5
   ```
3. Descomentar config S3 en `production.py`
4. Configurar env vars:
   ```powershell
   eb setenv AWS_STORAGE_BUCKET_NAME="suluhisho-media"
   eb setenv AWS_S3_REGION_NAME="us-east-2"
   ```

## Troubleshooting

### Ver Logs
```powershell
eb logs
```

### Reiniciar App
```powershell
eb ssh
sudo systemctl restart web
```

### Verificar Variables
```powershell
eb printenv
```

### Rollback a Versión Anterior
```powershell
eb deploy --version <version-label>
```

## Comandos Útiles

```powershell
# Ver todos los environments
eb list

# Cambiar environment activo
eb use suluhisho-env

# Terminar environment (CUIDADO: elimina todo)
eb terminate suluhisho-env

# Escalar (cambiar instance type o número)
eb scale 2  # 2 instancias
```

## Checklist Final

- [ ] Código commiteado (si usas git)
- [ ] Requirements actualizados
- [ ] SECRET_KEY configurado (nuevo, seguro)
- [ ] ALLOWED_HOSTS configurado
- [ ] Database configurada (RDS o SQLite temporal)
- [ ] Variables de entorno seteadas (`eb printenv` para verificar)
- [ ] Media storage configurado (S3) si necesitas uploads
- [ ] Dominio custom configurado (Route 53) - opcional
- [ ] HTTPS configurado (Certificate Manager) - opcional
- [ ] Migrations aplicadas automáticamente en deploy
- [ ] Admin user creado automáticamente

## Costos Estimados AWS

- **Free Tier:** 750 hrs/mes EC2 t2.micro (12 meses) = $0
- **Después Free Tier:** ~$20-30/mes (t2.micro, 1 instancia)
- **Con RDS:** +$15-20/mes (db.t3.micro)
- **Con S3:** ~$1-5/mes (depende uploads)

## Siguientes Pasos

1. Deploy inicial: `eb create suluhisho-env`
2. Configurar variables: `eb setenv ...`
3. Verificar: `eb open`
4. Login admin: `/admin/` con credenciales configuradas
5. Test admin dashboard: `/admin-dashboard/`
