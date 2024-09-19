import React from "react";
import InfoStyles from "./Info.module.css";

export const Info = () => {
  return (
    <div className={InfoStyles.InfoContainer}>
      <ul>
        <li>La manera fácil de llevar tu restaurante.</li>
        <li>
          Organiza todo, desde los pedidos hasta el inventario, y enfócate en lo
          que más te gusta:
        </li>
        <li>
          <b> ofrecer una gran experiencia a tus clientes</b>.
        </li>
      </ul>
    </div>
  );
};
