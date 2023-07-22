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
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      titulo: "",
      tipoUsuarios: [],
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
  },
  mounted() {
    // Título de la página
    this.titulo = "Gestion Tipo Usuarios";
    // Cargar datos de tipoUsuarios desde el servidor al montar el componente
    this.loadData();
  },
};
</script>
