import React from "react";
import Bodystyle from "./body.module.css";
import { Contacts } from "./Contacts/Contacts";
import { Info } from "./Info/Info";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUtensils } from "@fortawesome/free-solid-svg-icons";
import { faMugSaucer } from "@fortawesome/free-solid-svg-icons";
import { faBeerMugEmpty } from "@fortawesome/free-solid-svg-icons";

export const Body = () => {
  return (
    <div className={Bodystyle.BodyContainer}>
      <div className={Bodystyle.DescriptionContainer}>
        <h1>
          Bienvenido a <b className={Bodystyle.TittleColor}>Da</b>Food
        </h1>

        <h5>
          Sofward de gestion para
          <b className={Bodystyle.TittleColor}> restaurantes </b> y
          <b className={Bodystyle.TittleColor}> negocios </b>
          gastronomicos
        </h5>
        <Info />

        <div className={Bodystyle.IconContainer}>
          <div className={Bodystyle.Icons}>
            <FontAwesomeIcon icon={faUtensils} className={Bodystyle.Icon} />
            <p>Restaurantes</p>
          </div>
          <div className={Bodystyle.Icons}>
            <FontAwesomeIcon icon={faMugSaucer} className={Bodystyle.Icon} />
            <p>Cafeterias</p>
          </div>
          <div className={Bodystyle.Icons}>
            <FontAwesomeIcon icon={faBeerMugEmpty} className={Bodystyle.Icon} />
            <p>Bares</p>
          </div>
        </div>
      </div>
      <Contacts />
    </div>
  );
};
