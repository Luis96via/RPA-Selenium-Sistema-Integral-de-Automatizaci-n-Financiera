# 🚀 Deploy RPA - Sistema Integral de Automatización Financiera

## 📋 Resumen del Proyecto

Este es un sistema RPA completo que automatiza:
- 🤖 Login y extracción de datos web con Selenium
- 🔐 Resolución de captchas con OCR personalizado
- 💱 Integración con APIs de tasas de cambio
- 💾 Almacenamiento en MySQL
- 📊 Generación de reportes (Excel, XML, JSON)
- 📧 Envío automático de emails
- 🌐 Interfaz web moderna

## 🎯 Opciones de Deploy

### ✅ **PythonAnywhere (RECOMENDADO - GRATIS)**
- ✅ Selenium compatible
- ✅ MySQL incluido
- ✅ Flask web apps
- ✅ Sin tarjeta de crédito
- ✅ 512MB RAM, 1GB almacenamiento

### 🚀 **Railway (GRATIS $5/mes)**
- ✅ Soporte completo Python
- ✅ Base de datos incluida
- ✅ Deploy automático

### 🌐 **Heroku (PAGO)**
- ✅ Python/Selenium compatible
- ✅ PostgreSQL incluido
- ❌ Sin plan gratuito

## 🚀 Deploy en PythonAnywhere

### **Paso 1: Crear cuenta**
1. Ve a [PythonAnywhere](https://www.pythonanywhere.com/)
2. Click "Create a Beginner account"
3. Registro con email (sin tarjeta)

### **Paso 2: Subir código**
```bash
# En PythonAnywhere Console
git clone https://github.com/tuusuario/rpa-selenium.git
cd rpa-selenium
```

### **Paso 3: Configuración automática**
```bash
# Ejecutar script de configuración
chmod +x setup_pythonanywhere.sh
./setup_pythonanywhere.sh
```

### **Paso 4: Configurar base de datos**
1. Ve a "Databases" en PythonAnywhere
2. Crear BD: `finanzas_rpa`
3. Usuario: tu username
4. Contraseña: la que configures

### **Paso 5: Variables de entorno**
Crear archivo `.env`:
```env
EMAIL_USER=tu_correo@gmail.com
EMAIL_PASS=tu_password_aplicacion
EMAIL_TO=luis96via@gmail.com,luisdev96via@gmail.com
```

### **Paso 6: Configurar aplicación web**
1. Ve a "Web" en PythonAnywhere
2. "Add a new web app"
3. Flask + Python 3.9
4. Source: `/home/tuusuario/rpa-selenium`
5. WSGI: usar archivo `wsgi.py`

### **Paso 7: Editar WSGI**
Reemplazar contenido con:
```python
#!/usr/bin/env python3
import sys
import os

path = '/home/tuusuario/rpa-selenium'
if path not in sys.path:
    sys.path.append(path)

os.environ['PYTHONPATH'] = path

from app_simple import app as application
```

### **Paso 8: Reiniciar**
- Ve a "Web" > "Reload"

## 🌐 URL de la aplicación
`https://tuusuario.pythonanywhere.com`

## ✅ Verificación del Deploy

### **1. Interfaz web**
- ✅ Carga la página principal
- ✅ Botones funcionan
- ✅ Terminal muestra logs

### **2. RPA funcional**
- ✅ Login automático
- ✅ Resolución de captchas
- ✅ Extracción de datos
- ✅ Generación de reportes
- ✅ Envío de emails

### **3. Base de datos**
- ✅ Conexión MySQL
- ✅ Tablas creadas
- ✅ Datos almacenados

## 🔧 Troubleshooting

### **Error de Chrome/Selenium**
```bash
# Verificar Chrome instalado
which chromium-browser

# Verificar ChromeDriver
ls -la chromedriver
chmod +x chromedriver
```

### **Error de dependencias**
```bash
pip3 install --user --upgrade pip
pip3 install --user -r requirements.txt
```

### **Error de base de datos**
- Verificar credenciales en `process_data.py`
- Asegurar que la BD existe
- Verificar permisos de usuario

### **Error de permisos**
```bash
chmod 755 data/
chmod 755 reportes/
chmod +x chromedriver
```

## 📊 Monitoreo

### **Logs de aplicación**
- PythonAnywhere > Web > Log files
- Console de PythonAnywhere

### **Estado del RPA**
- Terminal en la interfaz web
- Logs en tiempo real

## 🔒 Seguridad

### **Variables de entorno**
- ✅ Credenciales en `.env`
- ✅ No en código fuente
- ✅ Archivo `.env` en `.gitignore`

### **Base de datos**
- ✅ Usuario específico para la app
- ✅ Contraseña segura
- ✅ Permisos mínimos

## 📈 Escalabilidad

### **Plan gratuito**
- ✅ 512MB RAM
- ✅ 1GB almacenamiento
- ✅ 1 aplicación web
- ✅ Base de datos MySQL

### **Plan Hacker ($5/mes)**
- ✅ Más recursos
- ✅ Múltiples aplicaciones
- ✅ Dominio personalizado

## 🆘 Soporte

### **Documentación**
- `deploy_instructions.md` - Instrucciones detalladas
- `README.md` - Documentación del proyecto

### **Logs y debugging**
- PythonAnywhere Console
- Web > Log files
- Terminal de la interfaz web

### **Contacto**
- Revisar logs antes de contactar
- Incluir mensajes de error específicos
- Describir pasos que causan el problema

---

**¡Tu RPA estará funcionando online en minutos! 🎉** 