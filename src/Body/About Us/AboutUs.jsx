import React from "react";
import AboutUsStyles from "./AboutUs.module.css";

export const AboutUs = () => {
  return (
    <div className={AboutUsStyles.AboutUsContainer}>
      <div className={AboutUsStyles.Container1}>
        <h1>Sobre Nosotros</h1>
        <ul>
          <li>
            <p>
              Bienvenidos a DaFood, su solución integral para la gestión de
              restaurantes y negocios gastronómicos. Somos un equipo apasionado
              de dos amigos, Dante y Alejandro, quienes han unido sus talentos
              en programación para crear esta innovadora aplicación.
            </p>
          </li>
          <li>
            <p>
              Nuestra historia comenzó como un proyecto personal, un desafío
              para demostrar nuestras habilidades como programadores. Con Dante
              liderando el desarrollo del backend y Alejandro enfocándose en el
              frontend, hemos trabajado incansablemente para construir una
              plataforma que simplifique las operaciones diarias de los
              restaurantes y mejore la experiencia del cliente.
            </p>
          </li>
          <li>
            <p>
              En Dafoof, nuestra misión es empoderar a los dueños de negocios
              gastronómicos con herramientas eficaces y fáciles de usar,
              permitiéndoles centrarse en lo que realmente importa: ofrecer una
              experiencia culinaria excepcional. Estamos comprometidos a mejorar
              continuamente nuestra aplicación, incorporando las necesidades y
              sugerencias de nuestros usuarios.
            </p>
          </li>
          <li>
            <p>
              Creemos en la importancia de la comunidad y el trabajo en equipo,
              y estamos emocionados de ser parte de su viaje hacia el éxito.
              ¡Gracias por elegir DaFood!
            </p>
          </li>
        </ul>
      </div>
      <div className={AboutUsStyles.Container2}></div>
    </div>
  );
};
