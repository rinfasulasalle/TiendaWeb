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
        <Column header="Acciones" :exportable="false"></Column>
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
              @click="eliminarTipoUsuario(slotProps.data)"
            />
          </template>
        </Column>
      </DataTable>
    </div>

    <!-- Edit Dialog -->
    <Dialog
      v-model:visible="showEditDialog"
      header="Editar Tipo de Usuario"
      :modal="true"
    >
      <div class="p-fluid">
        <div class="p-field">
          <label for="editTipoUsuarioID">ID</label>
          <InputText
            id="editTipoUsuarioID"
            v-model="editTipoUsuario.tipo_usuario_id"
            :disabled="true"
          />
        </div>
        <div class="p-field">
          <label for="editNombreTipoUsuario">Nombre</label>
          <InputText
            id="editNombreTipoUsuario"
            v-model="editTipoUsuario.nombre"
          />
        </div>
        <br />
      </div>
      <div class="p-dialog-footer">
        <Button label="Cancelar" severity="danger" @click="cancelarEdicion" />
        <Button label="Enviar" severity="success" @click="enviarEdicion" />
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
      tipoUsuarios: [],
      nuevoTipoUsuario: {
        nombre: "",
      },
      showEditDialog: false,
      editTipoUsuario: {
        tipo_usuario_id: "",
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
    // Método para abrir el diálogo de edición y cargar los datos del tipo de usuario
    openEditDialog(tipoUsuario) {
      this.editTipoUsuario = { ...tipoUsuario };
      this.showEditDialog = true;
    },

    // Método para cancelar la edición y cerrar el diálogo
    cancelarEdicion() {
      this.showEditDialog = false;
    },

    // Método para enviar los cambios de edición
    enviarEdicion() {
      const dataToUpdate = {
        tipo_usuario_id: this.editTipoUsuario.tipo_usuario_id,
        nombre: this.editTipoUsuario.nombre,
      };
      axios
        .patch("http://localhost:5000/tipo_usuario", dataToUpdate)
        .then((response) => {
          // Handle the response (if needed)
          // For example, you can display a success message and refresh the data table
          console.log("Tipo de usuario editado:", response.data);
          this.loadData(); // Refresh the data table after editing a type of user
          this.showEditDialog = false; // Close the dialog after successful submission
        })
        .catch((error) => {
          console.error("Error al editar tipo de usuario:", error);
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
