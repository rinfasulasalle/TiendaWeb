import { createApp } from "vue";
import App from "./App.vue";
import axios from "axios"; // Import Axios
// import
import PrimeVue from "primevue/config";

//theme
import "primevue/resources/themes/lara-dark-indigo/theme.css";
//core
import "primevue/resources/primevue.min.css";
//icons
import "primeicons/primeicons.css";
// cada componente se importa de forma separada +++++++++++++++++++++++++
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Toolbar from "primevue/toolbar";
import Dialog from "primevue/dialog";
import InputText from "primevue/inputtext";
const app = createApp(App);
app.use(PrimeVue);

// aqui agregamos el componente ******************************************
app.component("Button", Button);
app.component("DataTable", DataTable);
app.component("Column", Column);
app.component("Toolbar", Toolbar);
app.component("Dialog", Dialog);
app.component("InputText", InputText);

app.mount("#app");
