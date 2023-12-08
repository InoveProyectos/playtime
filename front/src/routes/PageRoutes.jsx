import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Login from "../components/Login";
import Stockprueba from "../components/Stockprueba";
import { useContext } from "react";
import { Autorizacion } from "../context/AuthContext";

export default function PageRoutes() {
  const { autenticado } = useContext(Autorizacion);
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />

          {/* Esta ruta se habilita si se usa una barra de links, sino accede directamente al stock o menu si
          el login es autenticado */}
          <Route
            path="/stock-prueba"
            element={autenticado ? <Stockprueba /> : <Navigate to="/" />}
          />
        </Routes>
      </Router>
    </>
  );
}
