// Importamos React Router:
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import { CssBaseline } from "@mui/material";
import { Experimental_CssVarsProvider as CssVarsProvider } from "@mui/material/styles";
import "../index.css";
import MiniDrawer from "../components/Drawer";
import Articulo from "../components/Articulo";
import Home from "../components/Home";
import Deposito from "../components/Deposito";
import Stock from "../components/Stock";
import Mantenimiento from "../components/Mantenimiento";

const RouterPrincipal = () => {
  return (
    <BrowserRouter>
      <CssBaseline />
      <Routes>
        <Route path="/" element={<MiniDrawer />}>
          <Route path="/" element={<Home />} />
          <Route path="/articulo" element={<Articulo />} />
          <Route path="/deposito" element={<Deposito />} />
          <Route path="/mantenimiento" element={<Mantenimiento />} />
          <Route path="/stock" element={<Stock />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default RouterPrincipal;
