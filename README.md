# 🐾 API Test Automation - Swagger PetStore

Proyecto de automatización de pruebas API desarrollado con Python y Pytest utilizando la API pública Swagger PetStore.

## 📋 Objetivo

Validar el correcto funcionamiento de los endpoints del módulo de mascotas (Pet) mediante pruebas automatizadas que cubren operaciones CRUD, validaciones de respuestas, escenarios positivos y negativos, generación de reportes HTML y logging detallado.

---

## 🛠️ Tecnologías Utilizadas

- Python 3.14
- Pytest
- Requests
- Pytest-Check
- Pytest-HTML
- Logging
- Swagger PetStore API

API utilizada:

https://petstore.swagger.io/

Documentación Swagger:

https://petstore.swagger.io/

---

## 📂 Estructura del Proyecto

```text
Proyecto-final/
│
├── pages/
│   └── pet_api_page.py
│
├── tests/
│   └── test_pets.py
│
├── utils/
│   └── logger.py
│
├── reports/
│   └── ui_api_report.html
│
├── conftest.py
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Casos de Prueba Implementados

### Escenarios Positivos

### ✅ Crear Mascota

- Método: POST
- Valida código HTTP 200
- Valida ID generado
- Valida nombre de mascota
- Valida estado

### ✅ Consultar Mascota

- Método: GET
- Consulta una mascota previamente creada
- Valida código HTTP 200
- Valida información retornada

### ✅ Actualizar Mascota

- Método: PUT
- Actualiza nombre y estado
- Valida persistencia de los cambios

### ✅ Eliminar Mascota

- Método: DELETE
- Elimina una mascota existente
- Valida respuesta del endpoint

---

### Escenarios Negativos

### ✅ Consultar Mascota Inexistente

- Método: GET
- Consulta un ID inexistente
- Valida código HTTP 404
- Valida mensaje "Pet not found"

---

## 🔗 Encadenamiento de Peticiones

Se implementó un flujo completo utilizando fixtures de Pytest:

```text
CREATE PET
      ↓
GET PET
      ↓
UPDATE PET
      ↓
DELETE PET
```

Cada prueba utiliza datos generados dinámicamente para garantizar independencia entre ejecuciones.

---

## 📊 Reportes HTML

Generar reporte:

```bash
py -m pytest -v --html=reports/ui_api_report.html --self-contained-html
```

El reporte incluye:

- Estado de cada prueba
- Tiempo de ejecución
- Logs generados durante la ejecución
- Resumen general de resultados

---

## 📝 Logging

Se implementó un sistema de logging para registrar:

- Datos enviados a la API
- Respuestas recibidas
- IDs generados dinámicamente
- Validaciones realizadas
- Escenarios de error

Ejemplo:

```text
===== CREATE PET =====
ID: 275517
Name: Beethoven
Status: available
Response: {...}
======================
```

---

## ▶️ Ejecución del Proyecto

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar todas las pruebas

```bash
py -m pytest -v
```

### Ejecutar pruebas con reporte HTML

```bash
py -m pytest -v --html=reports/ui_api_report.html --self-contained-html
```

---

## 📌 Cobertura de la Consigna

| Requisito | Estado |
|------------|---------|
| API pública | ✅ |
| GET | ✅ |
| POST | ✅ |
| DELETE | ✅ |
| Validación Status Code | ✅ |
| Validación JSON | ✅ |
| Escenarios positivos | ✅ |
| Escenarios negativos | ✅ |
| Encadenamiento de peticiones | ✅ |
| Logging | ✅ |
| Reporte HTML | ✅ |

---

## 👨‍💻 Autor

Carlos Aparicio

QA Engineer | Manual Testing | API Testing | Automation Testing

GitHub: https://github.com/CarlosE-Aparicio
