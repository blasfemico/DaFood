import React, { useState } from "react";
import FormStyle from "../Form/Form.module.css";

export const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Aquí puedes agregar la lógica para autenticar al usuario
    if (username === "" || password === "") {
      setError("Por favor, complete todos los campos.");
      return;
    }
    // Ejemplo de autenticación simple (reemplaza esto con tu lógica real)
    if (username === "ALE" && password === "ALE") {
      alert("¡Inicio de sesión exitoso!");
      // Redirigir o hacer algo después del inicio de sesión
    } else {
      setError("Credenciales incorrectas. Intente de nuevo.");
    }
  };

  return (
    <div className="login-container">
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Usuario:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Contraseña:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p className="error">{error}</p>}
        <button type="submit" className={FormStyle.ButtonLogin}>
          Iniciar Sesión
        </button>
      </form>
    </div>
  );
};
