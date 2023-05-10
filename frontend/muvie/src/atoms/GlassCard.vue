<template>
  <div>
    <div class="container">
      <div class="card">
        <div class="content"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  bottom: 0;
  min-height: 100vh;
}
.container {
  /* 임시 위치 */
  position: fixed;
  bottom: 0%;
  left: 0;
  /* position: relative;
  display: flex;
  justify-content: center;
  align-items: center; */
  max-width: 1200px;
  flex-wrap: wrap;
  z-index: 1;
}
.container .card {
  position: relative;
  width: 700px;
  height: 500px;
  margin: 30px;
  box-shadow: 20px 20px 50px rgb(0, 0, 0, 0.5);
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.1);
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top: 1px solid rgb(255, 255, 255, 0.5);
  border-left: 1px solid rgb(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);
}

.container .card .content h2 {
  color: rgba(218, 138, 114);
  pointer-events: none;
}
</style>
