import { Body } from "./Body/Body";
import { Form } from "./Body/Form/Form";
import { Navegador } from "./nav/navegador";
import { AboutUs } from "./Body/About Us/AboutUs";

function App() {
  return (
    <>
      <Navegador />
      <Body />
      <Form />
      <AboutUs />
    </>
  );
}

export default App;
