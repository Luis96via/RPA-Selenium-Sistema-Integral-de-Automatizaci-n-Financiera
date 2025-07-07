# 🤖 RPA - Sistema Integral de Automatización Financiera

## 📋 Descripción

Sistema RPA completo que automatiza la extracción, procesamiento y reporte de datos financieros con gestión dinámica de emails desde la interfaz web.

## ✨ Características Principales

### 🔄 **Automatización Completa**
- 🤖 Login automático con Selenium
- 🔐 Resolución de captchas con OCR personalizado
- 📊 Extracción de datos financieros
- 💱 Conversión de monedas con APIs
- 💾 Almacenamiento en MySQL
- 📈 Generación de reportes (Excel, XML, JSON)
- 📧 Envío automático de emails

### 📧 **Gestión Dinámica de Emails** (NUEVO)
- ⚙️ Configuración desde interfaz web
- ➕ Agregar múltiples emails destinatarios
- ✏️ Editar emails existentes
- 🗑️ Eliminar emails
- 💾 Almacenamiento en base de datos
- 🔄 Actualización en tiempo real

### 🌐 **Interfaz Web Moderna**
- 📱 Diseño responsive
- ⚡ Actualizaciones en tiempo real
- 📊 Logs en vivo
- 🎨 Interfaz moderna y intuitiva
- 📚 Documentación integrada

## 🚀 Instalación y Configuración

### **Requisitos Previos**
```bash
Python 3.8+
MySQL/MariaDB
Chrome/Chromium
```

### **1. Clonar el repositorio**
```bash
git clone https://github.com/tuusuario/rpa-selenium.git
cd rpa-selenium
```

### **2. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **3. Configurar base de datos**
```bash
# Crear base de datos MySQL
mysql -u root -p
CREATE DATABASE finanzas_rpa;
```

### **4. Configurar variables de entorno**
Crear archivo `.env`:
```env
# Configuración de base de datos
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=finanzas_rpa

# Configuración de email (solo para envío)
EMAIL_USER=tu_correo@gmail.com
EMAIL_PASS=tu_password_aplicacion

# NOTA: EMAIL_TO ya no se usa, los emails se gestionan desde la interfaz web
```

### **5. Ejecutar el sistema**
```bash
python run_system.py
```

## 📧 Gestión de Emails

### **Configuración desde la Interfaz Web**
1. Abrir la aplicación en `http://localhost:8000`
2. Hacer clic en el ícono de configuración ⚙️
3. En la sección "Emails Destinatarios":
   - ➕ **Agregar email**: Ingresar email y nombre opcional
   - ✏️ **Editar email**: Hacer clic en el botón de editar
   - 🗑️ **Eliminar email**: Hacer clic en el botón de eliminar

### **Estructura de la Base de Datos**
```sql
CREATE TABLE emails_destinatarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    nombre VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## 🔧 Uso del Sistema

### **1. Iniciar RPA**
- Hacer clic en "🚀 Iniciar RPA" en la interfaz web
- El sistema ejecutará automáticamente:
  - Login y extracción de datos
  - Procesamiento y conversión de monedas
  - Generación de reportes
  - Envío de emails a todos los destinatarios configurados

### **2. Monitorear Progreso**
- Los logs aparecen en tiempo real en la terminal
- Estado del proceso visible en la interfaz

### **3. Gestionar Emails**
- Usar el modal de configuración para agregar/editar emails
- Los cambios se guardan automáticamente en la base de datos
- Los reportes se envían a todos los emails activos

## 📁 Estructura del Proyecto

```
rpa-selenium/
├── app_simple.py              # Aplicación Flask principal
├── email_manager.py           # Gestor de emails desde BD
├── create_email_table.py      # Script para crear tabla emails
├── run_system.py              # Script para ejecutar todo
├── main_web_simple.py         # Script RPA principal
├── process_data.py            # Procesamiento de datos
├── exchange_rates.py          # API de tasas de cambio
├── templates/
│   └── index_simple.html      # Interfaz web
├── data/                      # Datos de entrada
├── reportes/                  # Reportes generados
└── requirements.txt           # Dependencias
```

## 🔌 APIs Disponibles

### **Gestión de Emails**
- `GET /api/emails` - Obtener todos los emails
- `POST /api/emails` - Agregar nuevo email
- `PUT /api/emails/<id>` - Actualizar email
- `DELETE /api/emails/<id>` - Eliminar email

### **Control RPA**
- `GET /api/status` - Estado del RPA
- `POST /api/start` - Iniciar RPA
- `POST /api/stop` - Detener RPA
- `GET /api/output` - Salida en tiempo real
- `POST /api/clear` - Limpiar salida

## 🛠️ Desarrollo

### **Agregar Nuevas Funcionalidades**
1. Modificar `app_simple.py` para nuevas rutas API
2. Actualizar `templates/index_simple.html` para la interfaz
3. Agregar estilos CSS según sea necesario

### **Modificar Procesamiento de Datos**
1. Editar `process_data.py` para cambios en el procesamiento
2. Modificar `main_web_simple.py` para cambios en el flujo RPA

## 🚀 Deploy

### **PythonAnywhere (Recomendado)**
```bash
# Clonar en PythonAnywhere
git clone https://github.com/tuusuario/rpa-selenium.git

# Ejecutar setup
chmod +x setup_pythonanywhere.sh
./setup_pythonanywhere.sh

# Configurar aplicación web
# Source: /home/tuusuario/rpa-selenium
# WSGI: app_simple.py
```

### **Railway**
```bash
# Deploy automático desde GitHub
# Configurar variables de entorno en Railway
```

## 📊 Reportes Generados

- **Excel**: `reportes/resumen_financiero.xlsx`
- **JSON**: `reportes/resumen_financiero.json`
- **XML**: `reportes/resumen_financiero.xml`

## 🔒 Seguridad

- ✅ Credenciales en variables de entorno
- ✅ Emails gestionados desde base de datos
- ✅ Validación de emails en frontend y backend
- ✅ Sanitización de datos

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama para nueva funcionalidad
3. Commit cambios
4. Push a la rama
5. Abrir Pull Request

## 📞 Soporte

- 📧 Email: luis96via@gmail.com
- 🐛 Issues: GitHub Issues
- 📖 Documentación: README.md

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

---

**Desarrollado con ❤️ por Luis Viña** 