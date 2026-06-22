# Suluhisho Platform

**Plataforma de Ideación para Emprendedores en Territorios Vulnerables de Colombia**

Sistema web progresivo (PWA) diseñado para guiar a emprendedores de poblaciones vulnerables a través de un recorrido estructurado de 7 pasos de ideación, validación y desarrollo de propuestas de valor.

---

## 📋 Características Principales

- **7 Módulos Secuenciales de Ideación**
  1. Ikigai del Emprendedor
  2. Diario de Campo (Observación territorial)
  3. Mapa de Empatía + POV
  4. Jobs To Be Done (JTBD)
  5. Brainstorming + SCAMPER
  6. Value Proposition Canvas
  7. Entrevistas de Validación

- **Accesibilidad y Contexto**
  - Diseño mobile-first (PWA)
  - Soporte offline (Service Workers + IndexedDB)
  - Entrada multimodal (texto, voz, imágenes)
  - Lenguaje simple adaptado a baja alfabetización
  - Contexto territorial (PDET, zonas rurales, urbano periférico)

- **Validación y Acompañamiento**
  - Validación automática por módulo
  - Sistema de progreso secuencial (no se puede saltar pasos)
  - Dashboard para facilitadores/mentores
  - Asignación de facilitadores a emprendedores

---

## 🛠️ Stack Tecnológico

- **Backend:** Django 6.0 + Django REST Framework
- **Database:** PostgreSQL 16 (SQLite para desarrollo)
- **Storage:** S3-compatible (AWS S3 / Cloudflare R2)
- **Task Queue:** Celery + Redis
- **Frontend:** HTMX + Tailwind CSS (sin frameworks JS pesados)
- **Offline:** Service Workers (Workbox)

---

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.13+
- PostgreSQL 16 (opcional, usa SQLite por defecto en desarrollo)
- Redis (opcional, necesario para Celery)

### Opción 1: Instalación Local

1. **Clonar el repositorio**
```bash
git clone <repo-url>
cd suluhisho
```

2. **Crear y activar entorno virtual**
```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements/base.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Aplicar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Inicializar datos básicos (opcional)**
```bash
python manage.py loaddata fixtures/modules.json
```

8. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

Accede a:
- **Aplicación:** http://localhost:8000
- **Admin:** http://localhost:8000/admin

### Opción 2: Docker Compose (Recomendado)

1. **Asegúrate de tener Docker y Docker Compose instalados**

2. **Construir y ejecutar**
```bash
docker-compose up --build
```

Esto levantará:
- Django app (puerto 8000)
- PostgreSQL (puerto 5432)
- Redis (puerto 6379)
- Celery worker
- Celery beat

3. **Ejecutar migraciones**
```bash
docker-compose exec web python manage.py migrate
```

4. **Crear superusuario**
```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 📁 Estructura del Proyecto

```
suluhisho/
├── core/                      # Modelos centrales (Module, ModuleProgress, ValidationRule)
├── entrepreneurs/             # Usuarios (User, EntrepreneurProfile, FacilitatorProfile)
├── deliverables/              # Entregables polimórficos (Text, Voice, Image)
├── media_handling/            # Manejo de archivos multimedia (transcripción, thumbnails)
├── modules/                   # 7 módulos de ideación
│   ├── ikigai/
│   ├── field_diary/
│   ├── empathy/
│   ├── jtbd/
│   ├── ideation/
│   ├── value_prop/
│   └── validation/
├── suluhisho_platform/
│   ├── settings/
│   │   ├── base.py           # Configuración base
│   │   ├── production.py     # Configuración de producción
│   │   └── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── static/                    # Archivos estáticos (CSS, JS, imágenes)
├── templates/                 # Templates HTML
├── media/                     # Archivos subidos por usuarios
├── requirements/
│   ├── base.txt              # Dependencias base
│   └── production.txt        # Dependencias de producción
├── .env                       # Variables de entorno (no versionar)
├── .env.example               # Ejemplo de variables de entorno
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── README.md
```

---

## 🗄️ Modelos Principales

### `entrepreneurs.User`
Usuario personalizado con soporte para:
- Tipo de usuario (emprendedor, facilitador, admin)
- Autenticación por teléfono (para baja alfabetización)
- Perfiles relacionados (EntrepreneurProfile, FacilitatorProfile)

### `core.Module`
Representa uno de los 7 pasos:
- Orden secuencial
- Instrucciones y descripciones
- Tiempo estimado
- Reglas de validación

### `core.ModuleProgress`
Rastrea el progreso de cada usuario por módulo:
- Estado (no iniciado, en progreso, completado, bloqueado)
- Porcentaje de completitud
- Validación pasada
- Notas del facilitador

### `deliverables.Deliverable` (Polimórfico)
Entregables de cada módulo:
- **TextDeliverable:** Datos estructurados (JSON)
- **VoiceDeliverable:** Audio + transcripción opcional
- **ImageDeliverable:** Fotos + thumbnails

---

## 🔧 Comandos Útiles

### Gestión de Base de Datos
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos de ejemplo
python manage.py loaddata fixtures/modules.json
```

### Gestión de Archivos Estáticos
```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Limpiar archivos estáticos antiguos
python manage.py collectstatic --clear --noinput
```

### Celery (Procesamiento Asíncrono)
```bash
# Iniciar worker
celery -A suluhisho_platform worker --loglevel=info

# Iniciar beat (tareas programadas)
celery -A suluhisho_platform beat --loglevel=info

# Monitorear tareas
celery -A suluhisho_platform events
```

### Testing
```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests de una app específica
python manage.py test core

# Con cobertura
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 🌍 Variables de Entorno

Ver `.env.example` para la lista completa. Las principales son:

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `SECRET_KEY` | Clave secreta de Django | `django-insecure-...` |
| `DEBUG` | Modo debug (True/False) | `False` |
| `DJANGO_ENV` | Entorno (development/production) | `production` |
| `DB_NAME` | Nombre de la base de datos | `suluhisho_db` |
| `DB_USER` | Usuario de PostgreSQL | `postgres` |
| `DB_PASSWORD` | Contraseña de PostgreSQL | `***` |
| `DB_HOST` | Host de la base de datos | `localhost` |
| `REDIS_URL` | URL de Redis | `redis://localhost:6379/0` |
| `AWS_ACCESS_KEY_ID` | AWS Access Key (para S3) | `***` |
| `AWS_SECRET_ACCESS_KEY` | AWS Secret Key | `***` |
| `AWS_STORAGE_BUCKET_NAME` | Nombre del bucket S3 | `suluhisho-media` |

---

## 📝 Roadmap de Desarrollo

### ✅ Fase 1: Fundamentos (Completado)
- [x] Estructura de proyecto Django
- [x] Modelos de usuarios (User, EntrepreneurProfile, FacilitatorProfile)
- [x] Modelos core (Module, ModuleProgress, ValidationRule, Example)
- [x] Modelos de entregables polimórficos
- [x] Configuración de settings (base + production)
- [x] Docker Compose
- [x] Migraciones iniciales

### 🚧 Fase 2: Módulos de Ideación (En Progreso)
- [ ] Módulo 1: Ikigai (formularios + validación)
- [ ] Módulo 2: Diario de Campo
- [ ] Módulo 3: Mapa de Empatía + POV
- [ ] Módulo 4: JTBD Canvas
- [ ] Módulo 5: Brainstorming + SCAMPER
- [ ] Módulo 6: Value Proposition Canvas
- [ ] Módulo 7: Entrevistas de Validación

### 📋 Fase 3: Sistema Multimodal
- [ ] Captura de voz (MediaRecorder API)
- [ ] Upload de imágenes con compresión
- [ ] Generación de thumbnails (Celery)
- [ ] Transcripción de audio (Whisper API - opcional)
- [ ] Almacenamiento en S3

### 🎨 Fase 4: Frontend y UX
- [ ] Templates base con HTMX
- [ ] Dashboard de emprendedor
- [ ] Dashboard de facilitador
- [ ] Vistas de módulos (genéricas + específicas)
- [ ] Sistema de progreso visual
- [ ] Diseño mobile-first (Tailwind)
- [ ] PWA (Service Worker + manifest)

### 🔒 Fase 5: Offline y Sincronización
- [ ] Service Worker con Workbox
- [ ] Persistencia en IndexedDB
- [ ] Sincronización en background
- [ ] Resolución de conflictos
- [ ] Indicadores de estado de conexión

### 👥 Fase 6: Sistema de Mentorship
- [ ] Asignación de facilitadores
- [ ] Notificaciones (email + WhatsApp - opcional)
- [ ] Sistema de comentarios en entregables
- [ ] Override manual de validación
- [ ] Reportes de progreso

### 🚀 Fase 7: Deploy y Producción
- [ ] CI/CD (GitHub Actions)
- [ ] Deploy a Railway/Render/DigitalOcean
- [ ] Configuración de S3/R2
- [ ] Monitoring (Sentry)
- [ ] Backups automatizados
- [ ] Documentación de usuario

---

## 🧪 Testing

El proyecto incluye tests unitarios, de integración y end-to-end.

```bash
# Ejecutar todos los tests
python manage.py test

# Tests con cobertura
coverage run manage.py test
coverage report
coverage html  # genera reporte HTML en htmlcov/

# Tests específicos
python manage.py test core.tests.test_models
python manage.py test entrepreneurs
```

---

## 🤝 Contribución

Este proyecto está diseñado para el contexto colombiano de emprendimiento en territorios vulnerables.

### Guías de Contribución
1. Fork el proyecto
2. Crea una rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Estándares de Código
- **Python:** PEP 8 (usar `black` y `flake8`)
- **Django:** Seguir convenciones de Django
- **Commits:** Mensajes descriptivos en español
- **Documentación:** Docstrings en español para modelos y funciones principales

---

## 📄 Licencia

[Por definir]

---

## 📧 Contacto

Para preguntas sobre el proyecto o colaboración, contacta a: [correo@ejemplo.com]

---

## 🙏 Agradecimientos

Este proyecto se basa en metodologías validadas de emprendimiento territorial:
- **Ikigai** (concepto japonés adaptado)
- **Double Diamond** (British Design Council)
- **Lean Startup** (Eric Ries)
- **Design Thinking** (Stanford d.school)
- **Jobs To Be Done** (Clayton Christensen)
- **Value Proposition Canvas** (Alexander Osterwalder)

Diseñado específicamente para el contexto colombiano de Programas de Desarrollo con Enfoque Territorial (PDET) y comunidades en post-conflicto.
