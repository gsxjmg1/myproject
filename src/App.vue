<template>
  <div id="app">
      <!-- 导航栏 -->
      <Navbar />
      <div class="main-content"></div>
      <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%; 
  background-image: url('./assets/background.jpg');
}

.main-content {
  padding-top: 50px; 
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
