import { useState } from "react";

import "./App.css";
import PageRoutes from "./routes/PageRoutes";
import { Autorizacion } from "./context/AuthContext";

function App() {
  const [autenticado, setAutenticado] = useState("");

  return (
    <>
      <Autorizacion.Provider value={{ autenticado, setAutenticado }}>
        <PageRoutes />
      </Autorizacion.Provider>
    </>
  );
}

export default App;
