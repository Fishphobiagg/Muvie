<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/signup">Signup</router-link> |
      <router-link to="/mypage">Mypage</router-link> |
      <router-link to="/main">Main</router-link> |
    </nav>
    <router-view />
    <YoutubePlayer />
  </div>
</template>

<script>
import YoutubePlayer from "./organisms/YoutubePlayer.vue";

export default {
  name: "App",
  components: {
    YoutubePlayer,
  },
};
</script>

<style>
@import "./assets/css/global.css";
@font-face {
  font-family: "appleGothic";
  src: url("assets/AppleGothic.ttf");
}

body {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  margin: 0px;
  padding: 0px;
}

#app {
  font-family: "appleGothic", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  list-style: none;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
