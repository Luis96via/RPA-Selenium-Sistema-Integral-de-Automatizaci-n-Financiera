# 🤖 Sistema RPA de Procesamiento de Transacciones Financieras

## 🎯 Descripción General

**Sistema avanzado de Automatización Robótica de Procesos (RPA)** que automatiza completamente el procesamiento de transacciones financieras. Este proyecto demuestra capacidades de **nivel empresarial** combinando automatización web, resolución inteligente de captchas, integración de APIs, gestión de bases de datos y generación profesional de reportes.

## 🚀 ¿Qué Hace Este Sistema?

### 🔐 **Autenticación Automática Completa**
- **Inicia sesión automáticamente** en la web financiera
- **Resuelve captchas de forma inteligente** usando mi propia API de OCR
- **Maneja múltiples tipos de captcha**: texto, selección de imágenes y preguntas de lógica
- **Simula comportamiento humano** con patrones de escritura realistas
- **Sistema de reintentos inteligente** (6 intentos por captcha)

### 💰 **Procesamiento de Datos Financieros**
- **Extrae automáticamente** todas las transacciones de la web
- **Convierte monedas en tiempo real** usando la API de Frankfurter
- **Normaliza todo a USD** con lógica de negocio personalizada
- **Categoriza transacciones** (ingresos/gastos) automáticamente
- **Valida y limpia datos** antes del procesamiento

### 📊 **Generación de Reportes Profesionales**
- **Crea reportes en Excel (.xlsx)** con formato profesional y atractivo
- **Genera archivos XML y JSON** para integración con otros sistemas
- **Envía automáticamente** los reportes por email
- **Presentación visual elegante** tanto en reportes como en emails

## 🛠 Tecnologías y Herramientas

### **Desarrollo Propio**
- **API de OCR personalizada**: Desarrollé mi propia API para resolver captchas
- **Lógica de negocio**: Algoritmos de conversión de monedas
- **Sistema de reportes**: Generación profesional de Excel, XML y JSON

### **Automatización Web**
- **Selenium WebDriver**: Navegación y extracción automática de datos
- **Python**: Lenguaje principal para toda la automatización
- **Interacción humana realista**: Patrones de escritura y movimiento natural

### **Integración de APIs**
- **Mi API de OCR**: Para resolver captchas automáticamente
- **Frankfurter API**: Tasas de cambio en tiempo real
- **SMTP**: Envío automático de emails con reportes

### **Gestión de Datos**
- **SQLite**: Base de datos para almacenar transacciones y tasas
- **Pandas**: Procesamiento y análisis de datos financieros
- **Organización de archivos**: Estructura clara de carpetas y archivos

## 📁 Estructura del Proyecto

```
rpa-selenium/
├── rpa_extract.py          # Automatización principal (login + captchas + extracción)
├── process_data.py         # Procesamiento de datos y generación de reportes
├── captcha_solver.py       # Integración con mi API de OCR
├── exchange_rates.py       # Consumo de API de tasas de cambio
├── main.py                 # Controlador principal del flujo
├── index.html              # Interfaz web (desplegada en Netlify)
├── data/                   # Almacenamiento de datos extraídos
├── reportes/              # Reportes generados (Excel, XML, JSON)
└── README.md              # Esta documentación
```

Comando Orquestador para correr el FrotEnd en Flask y el RPA Black: python app_simple.py 

## 🔄 Flujo Completo del Sistema

### **1. Inicio de Sesión Automático**
```
🌐 Accede a la web → 📝 Ingresa credenciales → 🤖 Resuelve captchas → ✅ Sesión iniciada
```

### **2. Extracción de Datos**
```
📊 Extrae transacciones → 💱 Obtiene tasas de cambio → 💾 Guarda en archivos separados
```

### **3. Procesamiento Inteligente**
```
🔄 Convierte monedas a USD → 📈 Calcula totales → 🗄️ Almacena en base de datos
```

### **4. Generación de Reportes**
```
📋 Crea Excel profesional → 📄 Genera XML/JSON → 📧 Envía por email automáticamente
```

## 🎯 Valor de Negocio

### **Ahorro de Tiempo y Costos**
- **90% menos tiempo** en procesamiento manual
- **Eliminación de errores humanos** en datos financieros
- **Automatización completa** de reportes y envío

### **Escalabilidad**
- **Arquitectura modular** para agregar nuevas funcionalidades
- **Integración fácil** con sistemas existentes
- **Configuración flexible** para diferentes instituciones

### **Cumplimiento y Precisión**
- **Traza completa** de todas las transacciones
- **Validación de datos** en múltiples niveles
- **Reportes profesionales** para cumplimiento regulatorio

## 🚀 Cómo Usar el Sistema

### **Requisitos**
```bash
Python 3.8+
Navegador Chrome
ChromeDriver
```

### **Instalación**
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd rpa-selenium

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la automatización
python main.py
```

### **Configuración**
```python
# Actualizar credenciales en rpa_extract.py
USER_EMAIL = 'tu-email@empresa.com'
USER_PASSWORD = 'tu-contraseña'

# Configurar email en process_data.py
SMTP_SERVER = 'tu-servidor-smtp'
SMTP_PORT = 587
EMAIL_USER = 'tu-email'
EMAIL_PASSWORD = 'tu-contraseña'
```

## 📊 Características de los Reportes

### **Reporte Excel (.xlsx)**
- **Formato profesional** con branding de empresa
- **Transacciones codificadas por colores** (ingresos/gastos)
- **Estadísticas resumidas** y gráficos
- **Detalles de conversión de monedas**

### **Email Automático**
- **Diseño HTML profesional** y responsive
- **Gráficos y tablas integrados**
- **Adjuntos automáticos** de reportes
- **Presentación visual atractiva**

## 🔧 Funcionalidades Avanzadas

### **Resolución de Captchas**
- **Captchas de texto**: Reconocimiento de caracteres con mi API de OCR
- **Captchas de imágenes**: Identificación de objetos con IA
- **Captchas de lógica**: Preguntas matemáticas y culturales
- **Sistema de reintentos**: Recuperación inteligente ante fallos

### **Procesamiento de Datos**
- **Validación en tiempo real**: Limpieza y verificación de datos
- **Normalización de monedas**: Conversión automática a USD
- **Categorización automática**: Clasificación de tipos de transacción
- **Agregación de datos**: Cálculos de resumen e insights

### **Manejo de Errores**
- **Degradación elegante**: El sistema continúa ante errores no críticos
- **Logging completo**: Seguimiento detallado de errores
- **Recuperación automática**: Mecanismos de auto-reparación
- **Notificaciones claras**: Mensajes de error comprensibles

## 🎖 Logros Técnicos del Desarrollador

### **Excelencia Técnica**
- **Automatización de nivel empresarial** comparable a UiPath/Automation Anywhere
- **Integración multi-tecnología** demostrando capacidades full-stack
- **Código production-ready** con manejo robusto de errores
- **Arquitectura escalable** apta para despliegue empresarial

### **Desarrollo de APIs**
- **API de OCR propia**: Desarrollé completamente mi servicio de resolución de captchas
- **Integración de APIs externas**: Consumo eficiente de servicios de terceros
- **Lógica de negocio personalizada**: Algoritmos de conversión de monedas

### **Impacto en el Negocio**
- **Automatización end-to-end** de procesos financieros complejos
- **Reportes profesionales** que cumplen estándares de la industria
- **Solución costo-efectiva** reduciendo esfuerzo manual en 90%
- **Listo para cumplimiento** con auditorías y validación de datos

## 🤝 Sobre el Proyecto

Este proyecto demuestra capacidades avanzadas de RPA y sirve como portafolio que muestra:
- **Flujos de automatización complejos**
- **Experiencia en integración de APIs**
- **Procesamiento y análisis de datos**
- **Generación profesional de reportes**
- **Habilidades de desarrollo full-stack**

## 📞 Contacto

Para preguntas sobre esta implementación RPA o para discutir oportunidades de automatización, por favor contactar a través de la información proporcionada.

---

**Desarrollado con ❤️ usando tecnologías modernas de automatización** 
