import React, { useContext, useState } from "react";
import { Autorizacion } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const { autenticado, setAutenticado } = useContext(Autorizacion);
  const [valido, setValido] = useState("Ingresa tu usuario");
  const navigate = useNavigate();

  const handlerSubmit = (e) => {
    e.preventDefault();

    const username = e.target.username.value;

    //Logica de funcionamiento para setear el valor del contexto y dar
    //autorizacion o no.
    if (username !== "admin123" || username == "") {
      setValido("Usuario Incorrecto");
      e.target.username.value = "";
      return;
    }
    //Si el susuario es correcto, automanticamente entra al dashboard
    setAutenticado(true);
    console.log(autenticado);
    autenticado ? navigate("/stock-prueba") : navigate("/");
  };

  return (
    //Formulario basico de un campo para inicio de sesion
    <>
      <form onSubmit={handlerSubmit}>
        <input type="text" name="username" placeholder="Usuario" />
        <button type="submit">Ingresar</button>
      </form>
      <h4>{valido}</h4>
    </>
  );
}
