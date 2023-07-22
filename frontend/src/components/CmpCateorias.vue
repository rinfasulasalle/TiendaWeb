<template>
  <div>
    <!-- Título de la página -->
    <h1>{{ titulo }}</h1>

    <!-- Tabla de PrimeVue con datos de categorías -->
    <div class="card datatable-container">
      <DataTable
        :value="categorias"
        :paginator="true"
        :rows="10"
        paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5, 10, 25]"
        currentPageReportTemplate="Mostrando {first} a {last} de {totalRecords} categorías"
      >
        <!-- Columnas de la tabla -->
        <Column field="id_categoria" header="ID"></Column>
        <Column field="nombre" header="Nombre"></Column>
        <!-- Custom slot for actions buttons in each row -->
        <Column :exportable="false" style="min-width: 8rem">
          <template #body="slotProps">
            <Button
              icon="pi pi-pencil"
              class="mr-2"
              @click="openEditDialog(slotProps.data)"
            />
            <Button
              icon="pi pi-trash"
              severity="danger"
              @click="eliminarCategoria(slotProps.data)"
            />
          </template>
        </Column>
      </DataTable>
    </div>
    <!-- Formulario para agregar categoría -->
    <div class="card form-container">
      <h2>Agregar Categoría</h2>
      <div class="p-grid p-fluid">
        <div class="p-col-12 p-md-6">
          <span class="p-float-label">
            <InputText id="nombreCategoria" v-model="nuevaCategoria.nombre" />
            <label for="nombreCategoria">Nombre</label>
          </span>
        </div>
      </div>
      <Button label="Agregar" @click="agregarCategoria" />
    </div>
    <!-- Edit Dialog -->
    <Dialog
      v-model:visible="showEditDialog"
      header="Editar Categoría"
      :modal="true"
    >
      <div class="p-fluid">
        <div class="p-field">
          <label for="editCategoriaID">ID</label>
          <InputText
            id="editCategoriaID"
            v-model="editCategoria.id_categoria"
            :disabled="true"
          />
        </div>
        <div class="p-field">
          <label for="editNombreCategoria">Nombre</label>
          <InputText id="editNombreCategoria" v-model="editCategoria.nombre" />
        </div>
        <br />
      </div>
      <div class="p-dialog-footer">
        <Button label="Cancelar" severity="danger" @click="cancelarEdicion" />
        <Button label="Enviar" severity="success" @click="enviarEdicion" />
      </div>
    </Dialog>
    <!-- Confirmation Dialog -->
    <Dialog
      v-model:visible="showDeleteDialog"
      header="Confirmar Eliminación"
      :modal="true"
    >
      <div class="p-dialog-body">
        ¿Está seguro de que desea eliminar el registro {{ deleteId }}?
      </div>
      <br />
      <div class="p-dialog-footer">
        <Button label="Cancelar" @click="cancelarEliminacion" />
        <Button
          label="Aceptar"
          @click="eliminarRegistro"
          class="p-button-danger"
        />
      </div>
    </Dialog>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      titulo: "",
      categorias: [],
      nuevaCategoria: {
        nombre: "",
      },
      showEditDialog: false,
      editCategoria: {
        id_categoria: "",
        nombre: "",
      },
      showDeleteDialog: false,
      deleteId: null,
    };
  },
  methods: {
    // Método para cargar datos de categorías desde el servidor
    loadData() {
      axios
        .post("http://127.0.0.1:5000/categorias")
        .then((response) => {
          this.categorias = response.data;
          console.table(this.categorias);
        })
        .catch((error) => {
          console.error("Error al cargar datos:", error);
        });
    },
    // Método para agregar una nueva categoría
    agregarCategoria() {
      axios
        .put("http://127.0.0.1:5000/categoria", this.nuevaCategoria)
        .then((response) => {
          // Handle the response (if needed)
          // For example, you can display a success message and refresh the data table
          console.log("Categoría agregada:", response.data);
          this.loadData(); // Refresh the data table after adding a new category
          this.nuevaCategoria = {
            id_categoria: "",
            nombre: "",
          }; // Clear the form fields after successful submission
        })
        .catch((error) => {
          console.error("Error al agregar categoría:", error);
        });
    },
    // Método para abrir el diálogo de edición y cargar los datos de la categoría
    openEditDialog(categoria) {
      this.editCategoria = { ...categoria };
      this.showEditDialog = true;
    },

    // Método para cancelar la edición y cerrar el diálogo
    cancelarEdicion() {
      this.showEditDialog = false;
    },

    // Método para enviar los cambios de edición
    enviarEdicion() {
      const dataToUpdate = {
        id_categoria: this.editCategoria.id_categoria,
        nombre: this.editCategoria.nombre,
      };
      axios
        .patch("http://127.0.0.1:5000/categoria", dataToUpdate)
        .then((response) => {
          // Handle the response (if needed)
          // For example, you can display a success message and refresh the data table
          console.log("Categoría editada:", response.data);
          this.loadData(); // Refresh the data table after editing a category
          this.showEditDialog = false; // Close the dialog after successful submission
        })
        .catch((error) => {
          console.error("Error al editar categoría:", error);
        });
    },
    // Método para abrir el diálogo de confirmación de eliminación
    eliminarCategoria(categoria) {
      this.deleteId = categoria.id_categoria;
      this.showDeleteDialog = true;
    },

    // Método para cancelar la eliminación y cerrar el diálogo de confirmación
    cancelarEliminacion() {
      this.showDeleteDialog = false;
      this.deleteId = null;
    },

    // Método para enviar la solicitud de eliminación al servidor
    eliminarRegistro() {
      const idToDelete = this.deleteId;
      console.log(idToDelete);
      // Assuming your endpoint supports DELETE requests with JSON data
      axios
        .delete(`http://127.0.0.1:5000/categoria`, {
          data: { id_categoria: idToDelete },
        })
        .then((response) => {
          // Handle the response (if needed)
          // For example, you can display a success message and refresh the data table
          console.log("Registro eliminado:", response.data);
          this.loadData(); // Refresh the data table after deleting a record
          this.showDeleteDialog = false; // Close the dialog after successful deletion
          this.deleteId = null; // Reset the deleteId property
        })
        .catch((error) => {
          console.error("Error al eliminar el registro:", error);
          this.showDeleteDialog = false; // Close the dialog on error
          this.deleteId = null; // Reset the deleteId property
        });
    },
  },
  mounted() {
    // Título de la página
    this.titulo = "Gestión de Categorías";
    // Cargar datos de categorías desde el servidor al montar el componente
    this.loadData();
  },
};
</script>

<style>
.form-container {
  max-width: 300px;
  margin: 0 auto;
}
.datatable-container {
  max-width: 800px;
  margin: 0 auto;
}
</style>
