import { createContext } from "react";

//Contexto creado para la autorizacion del usuario

const AuthUser={
    auth: false,
}

export const Autorizacion = createContext(AuthUser);
