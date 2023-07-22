<template>
  <div>
    <!-- Título de la página -->
    <h1>{{ titulo }}</h1>

    <!-- Tabla de PrimeVue con datos de tipoUsuarios -->
    <div class="card">
      <DataTable
        :value="tipoUsuarios"
        :paginator="true"
        :rows="10"
        paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5, 10, 25]"
        currentPageReportTemplate="Mostrando {first} a {last} de {totalRecords} tipoUsuarios"
      >
        <!-- Columnas de la tabla -->
        <Column field="tipo_usuario_id" header="ID"></Column>
        <Column field="nombre" header="Nombre"></Column>
      </DataTable>
    </div>
  </div>
  <!-- Formulario para agregar tipo de usuario -->
  <div class="card">
    <h2>Agregar Tipo de Usuario</h2>
    <div class="p-grid p-fluid">
      <div class="p-col-12 p-md-6">
        <span class="p-float-label">
          <InputText id="nombreTipoUsuario" v-model="nuevoTipoUsuario.nombre" />
          <label for="nombreTipoUsuario">Nombre</label>
        </span>
      </div>
    </div>
    <Button label="Agregar" @click="agregarTipoUsuario" />
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      titulo: "",
      tipoUsuarios: [],
      nuevoTipoUsuario: {
        nombre: "",
      },
    };
  },
  methods: {
    // Método para cargar datos de tipoUsuarios desde el servidor
    loadData() {
      axios
        .post("http://localhost:5000/tipo_usuarios")
        .then((response) => {
          this.tipoUsuarios = response.data;
          console.table(this.tipoUsuarios);
        })
        .catch((error) => {
          console.error("Error al cargar datos:", error);
        });
    },
    // Método para agregar un nuevo tipo de usuario
    agregarTipoUsuario() {
      axios
        .put("http://localhost:5000/tipo_usuario", this.nuevoTipoUsuario)
        .then((response) => {
          // Handle the response (if needed)
          // For example, you can display a success message and refresh the data table
          console.log("Tipo de usuario agregado:", response.data);
          this.loadData(); // Refresh the data table after adding a new type of user
          this.nuevoTipoUsuario = {
            tipo_usuario_id: "",
            nombre: "",
          }; // Clear the form fields after successful submission
        })
        .catch((error) => {
          console.error("Error al agregar tipo de usuario:", error);
        });
    },
  },
  mounted() {
    // Título de la página
    this.titulo = "Gestion Tipo Usuarios";
    // Cargar datos de tipoUsuarios desde el servidor al montar el componente
    this.loadData();
  },
};
</script>
