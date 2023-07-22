<template>
  <CmpCateorias />
</template>

<script>
import CmpCateorias from "./components/CmpCateorias.vue";

export default {
  name: "App",
  components: {
    CmpCateorias,
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
