DaFood - Documentación para el Equipo de Frontend
Descripción General

DaFood es una aplicación web diseñada para gestionar reservas y órdenes en bares y restaurantes. El backend del proyecto se ha desarrollado utilizando FastAPI, proporcionando una API RESTful que permite la autenticación de usuarios mediante JWT y la gestión de recursos como usuarios.
Endpoints Principales
Autenticación
1. Registro de Usuarios

    Endpoint: /register

    Método: POST

    Descripción: Registra un nuevo usuario en el sistema.

    Parámetros:
        name (string): Nombre del usuario.
        email (string): Correo electrónico del usuario (debe ser único).
        password (string): Contraseña del usuario.

    Ejemplo de solicitud:

    json

    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "password": "yourpassword"
    }

    Respuesta:
        201 Created: Si el registro es exitoso, retorna los detalles del usuario registrado (sin la contraseña).
        400 Bad Request: Si el correo ya está registrado.

2. Inicio de Sesión

    Endpoint: /login

    Método: POST

    Descripción: Inicia sesión en el sistema y devuelve un token JWT.

    Parámetros:
        username (string): Correo electrónico del usuario.
        password (string): Contraseña del usuario.

    Ejemplo de solicitud:

    json

{
  "username": "john.doe@example.com",
  "password": "yourpassword"
}

Respuesta:

    200 OK: Devuelve un access_token y el tipo de token (bearer).

    json

        {
          "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
          "token_type": "bearer"
        }

        401 Unauthorized: Si las credenciales son incorrectas.

Gestión de Usuarios
3. Obtener Información del Usuario Autenticado

    Endpoint: /me

    Método: GET

    Descripción: Obtiene la información del usuario actualmente autenticado.

    Encabezados:
        Authorization: Debe incluir el token JWT en el formato Bearer <token>.

    Ejemplo de solicitud:

    http

GET /me HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Respuesta:

    200 OK: Retorna los detalles del usuario autenticado.

    json

        {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com",
          "is_active": true
        }

        401 Unauthorized: Si el token no es válido o ha expirado.

Instrucciones para el Equipo de Frontend
1. Autenticación

    Almacenar el Token: Después de que un usuario inicie sesión y obtenga un access_token, este debe ser almacenado de forma segura en el frontend (puede ser en localStorage, sessionStorage, o una cookie).
    Uso del Token en Solicitudes: Para acceder a cualquier endpoint protegido, el frontend debe enviar el token en el encabezado Authorization.

2. Manejo de Errores

    Errores de Registro: Verifica el estado 400 para manejar errores como el registro de un correo ya existente.
    Errores de Autenticación: Si el backend devuelve un 401 Unauthorized, redirige al usuario a la página de inicio de sesión o muestra un mensaje de error.

3. Flujo de Trabajo Sugerido

    Inicio de Sesión: El usuario ingresa sus credenciales en el formulario de inicio de sesión.
    Almacenar Token: Si el inicio de sesión es exitoso, almacena el access_token en el frontend.
    Acceso a Recursos Protegidos: Usa el token almacenado para realizar solicitudes a los endpoints protegidos.
    Manejo de Sesiones: Monitorea la expiración del token y solicita una nueva autenticación si es necesario.

