
import "./App.css";
import RouterPrincipal from "./router/RouterPrincipal";
import { useState } from "react";

import PageRoutes from "./routes/PageRoutes";
import { Autorizacion } from "./context/AuthContext";

function App() {
  const [autenticado, setAutenticado] = useState("");

  return (
    <>
      <div className="App">
          <RouterPrincipal />
      </div>
     <Autorizacion.Provider value={{ autenticado, setAutenticado }}>
        <PageRoutes />
      </Autorizacion.Provider>     
    </>
  );
}

export default App;
