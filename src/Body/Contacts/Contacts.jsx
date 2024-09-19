import React from "react";
import ContactsStyle from "./Contancts.module.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faWhatsapp } from "@fortawesome/free-brands-svg-icons";
import { faInstagram } from "@fortawesome/free-brands-svg-icons";
import { faEnvelope } from "@fortawesome/free-regular-svg-icons";

export const Contacts = () => {
  return (
    <div className={ContactsStyle.ContactsContainer}>
      <h1>Contanctos</h1>
      <div className={ContactsStyle.Contacts}>
        <a href="" className={ContactsStyle.Contact}>
          <FontAwesomeIcon
            icon={faWhatsapp}
            className={ContactsStyle.ContactIcon}
          />
        </a>
        <a href="" className={ContactsStyle.Contact}>
          <FontAwesomeIcon
            icon={faInstagram}
            className={ContactsStyle.ContactIcon}
          />
        </a>
        <a href="" className={ContactsStyle.Contact}>
          <FontAwesomeIcon
            icon={faEnvelope}
            className={ContactsStyle.ContactIcon}
          />
        </a>
      </div>
    </div>
  );
};
