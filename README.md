# FastAPI Framework 

Estudio y desarrolo de API para gestión de clientes, planes, transacciones e invoices, desarrollada con **FastAPI** y **SQLModel**.

## Características

- **Clientes:** Alta, baja, modificación, listado y suscripción a planes.
- **Planes:** Gestión y asignación de planes a clientes.
- **Transacciones:** Registro y consulta de transacciones.
- **Facturación:** Creación de invoices.
- **Middleware:** Logging del tiempo de cada request.
- **Zona horaria:** Endpoint para consultar la hora local de varios países.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone 
   ```

2. **Crea un entorno virtual e instala dependencias:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   pip install -r requirements.txt
   ```

3. **Ejecuta la API:**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Accede a la documentación interactiva:**
   - [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints principales

- `GET /customers` - Lista todos los clientes
- `POST /customers` - Crea un cliente
- `PATCH /customers/{customer_id}` - Actualiza un cliente
- `DELETE /customers/{customer_id}` - Elimina un cliente
- `POST /customers/{customer_id}/plans/{plan_id}` - Suscribe un cliente a un plan
- `GET /plans` - Lista todos los planes
- `POST /transactions` - Crea una transacción
- `GET /tiempo/{iso_code}` - Devuelve la hora local de un país
- `POST /invoices` - Crea un invoice

## Uso de la base de datos SQLite

- El archivo de la base de datos se crea automáticamente.
- Puedes inspeccionarlo con el cliente de SQLite:
  ```bash
  sqlite3 db.sqlite3
  .tables

  ```



