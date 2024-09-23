import React, { useState } from "react";
import FormStyles from "./Form.module.css";
import { Login } from "../Login/Login";

export const Form = () => {
  const [formData, setFormData] = useState({
    email: "",
    username: "",
    password: "",
  });
  const [errors, setErrors] = useState({});

  // Manejar cambios en los campos
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Validar campos
  const validateForm = () => {
    let formErrors = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;

    if (!formData.email) {
      formErrors.email = "El correo es obligatorio";
    } else if (!emailRegex.test(formData.email)) {
      formErrors.email = "El correo no es válido";
    }

    if (!formData.username) {
      formErrors.username = "El nombre de usuario es obligatorio";
    }

    if (!formData.password) {
      formErrors.password = "La contraseña es obligatoria";
    } else if (formData.password.length < 6) {
      formErrors.password = "La contraseña debe tener al menos 6 caracteres";
    }

    setErrors(formErrors);
    return Object.keys(formErrors).length === 0;
  };

  // Manejar envío del formulario
  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      console.log("Datos enviados:", formData);
      // Aquí iría la lógica para enviar los datos al backend
    }
  };

  return (
    <form onSubmit={handleSubmit} className={FormStyles.FormContainer}>
      <div className={FormStyles.FormContent} id="Form">
        <div className={FormStyles.InfoContainer}>
          <h1>Bienvenido !</h1>
          <p>Completa el formulario para crear una cuenta</p>
          <Login />
        </div>

        <div className={FormStyles.ItemsContainer}>
          <h1>Registrarse</h1>
          <div>
            <label htmlFor="email">Correo electrónico:</label>
            <input
              className={FormStyles.FormEmail}
              autoComplete="OFF"
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
            />
            {errors.email && (
              <span className={FormStyles.SpanMsgRed}>{errors.email}</span>
            )}
          </div>

          <div>
            <label htmlFor="username">Nombre de usuario:</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
            />
            {errors.username && (
              <span className={FormStyles.SpanMsgRed}>{errors.username}</span>
            )}
          </div>

          <div>
            <label htmlFor="password">Contraseña:</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
            />
            {errors.password && (
              <span className={FormStyles.SpanMsgRed}>{errors.password}</span>
            )}
          </div>
          <div className={FormStyles.FormButtons}>
            <a href="##" className={FormStyles.ButtonRegisterContainer}>
              <button className={FormStyles.ButtonRegister} type="submit">
                Crear Usuario
              </button>
            </a>
            <a href="#" className={FormStyles.ButtonLogin}>
              Ya tengo cuenta
            </a>
          </div>
        </div>
      </div>
    </form>
  );
};
