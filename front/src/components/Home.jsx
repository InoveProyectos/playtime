import React from "react";

function Home() {
  return (
    <section>
      <h1>Home</h1>
      <br />
      <br />
      <nav style={{ float: "inline-start", textAlignLast: "start", fontSize: "30px" }}>
        <ul>
          <li>
            <a href="#seccion1">
              <h3>¿Mostramos un dashboard?</h3>
            </a>
          </li>
          <li>
            <a href="#seccion2">
              <h3>¿Una landing sobre la empresa?</h3>
            </a>
          </li>
          <li>
            <a href="#seccion3">
              <h3>Otras opciones....</h3>
            </a>
          </li>
        </ul>
      </nav>
      <br />
    </section>
  );
}

export default Home;
