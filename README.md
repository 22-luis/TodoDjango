# 📁 Estructura de una App Django RESTful
```bash
mi_proyecto/
├── manage.py
│   # Script principal para ejecutar comandos de Django (runserver, migrate, etc.)
│
├── mi_proyecto/
│   ├── __init__.py
│   ├── settings.py           # Configuración global del proyecto (BD, apps, middleware, etc.)
│   ├── urls.py               # Enrutamiento global del proyecto
│   ├── asgi.py               # Configuración ASGI (para websockets, async)
│   └── wsgi.py               # Configuración WSGI (para servidores como Gunicorn)
│
└── productos/                # App específica para gestionar productos
    ├── __init__.py
    ├── admin.py              # Registro de modelos en el panel de administración
    ├── apps.py               # Configuración interna de la app
    ├── urls.py               # Rutas específicas de la app (ej: /api/productos/)
    ├── migrations/
    │   ├── __init__.py
    │   └── # Archivos generados automáticamente para crear/modificar tablas
    │
    ├── models/               # 🧱 Modelos (representan tablas en la base de datos)
    │   ├── __init__.py
    │   └── producto.py       # Modelo Producto con sus campos y relaciones
    │
    ├── serializers/          # 🔄 Serializadores (transforman modelos <-> JSON)
    │   ├── __init__.py
    │   └── producto.py       # ProductoSerializer para validación y representación de datos
    │
    ├── views/                # 👁️‍🗨️ Vistas (reciben peticiones y devuelven respuestas)
    │   ├── __init__.py
    │   └── producto.py       # ProductoViewSet para operaciones CRUD sobre productos
    │
    ├── permissions/          # 🔐 Permisos personalizados
    │   ├── __init__.py
    │   └── producto.py       # Ej: solo admins pueden eliminar productos
    │
    ├── repositories/         # 📦 Lógica de acceso a datos (opcional pero útil)
    │   ├── __init__.py
    │   └── producto_repository.py  # Consultas reutilizables para productos
    │
    └── tests/                # 🧪 Pruebas automatizadas
        ├── __init__.py
        └── test_producto.py  # Test unitarios/funcionales del modelo o la vista
```
