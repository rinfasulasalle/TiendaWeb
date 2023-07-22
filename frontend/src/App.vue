<template>
  <CmpUsuarios />
</template>

<script>
import CmpUsuarios from "./components/CmpUsuarios.vue";

export default {
  name: "App",
  components: {
    CmpUsuarios,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
