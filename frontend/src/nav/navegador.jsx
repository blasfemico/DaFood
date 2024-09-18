import NavStyle from "./nav.module.css";
import React, { useEffect, useRef } from "react";

export const Navegador = () => {
  const navRef = useRef(null);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 50) {
        navRef.current.classList.add(NavStyle.scrolled);
      } else {
        navRef.current.classList.remove(NavStyle.scrolled);
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <nav className={NavStyle.NavContainer} ref={navRef}>
      <ul className={NavStyle.NavUl}>
        <h1>
          <b className={NavStyle.TittleColor}>Da</b>Food
        </h1>
        <li className={NavStyle.NavLi}>
          <a href="#" id="border-button" className={NavStyle.NavA}>
            Home
          </a>
        </li>
        <li className={NavStyle.NavLi}>
          <a href="#" id="border-button" className={NavStyle.NavA}>
            Sobre nosotros
          </a>
        </li>
        <li className={NavStyle.NavLi}>
          <a href="#" id="border-button" className={NavStyle.NavA}>
            Referencias
          </a>
        </li>
        <li className={NavStyle.LoginRegisterContainer}>
          <li className={NavStyle.NavLi} id="LoginUser">
            <a href="#" id="LoginUser" className={NavStyle.NavAFirst1}>
              Iniciar Sesion
            </a>
          </li>
          <li className={NavStyle.NavLi} id="LoginUser">
            <a href="#Form" id="LoginUser" className={NavStyle.NavAFirst}>
              Registrarse
            </a>
          </li>
        </li>
      </ul>
    </nav>
  );
};
