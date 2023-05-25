<template>
  <div class="circle-out">
    <div class="circle"></div>
  </div>
</template>

<script>
export default {};
</script>

<style>
body {
  background: #eed0b2;
  height: 100vh;
  width: 100vw;
}

.circle-out {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  /* background: #349fb3; */
  background: #F5F5F5;
  width: 300px;
  height: 300px;
}
.circle {
  /* transform: rotate( 150deg ); */
  /* background: linear-gradient(#0097D1 0%, #00a2b3 10%, #00536c 50%, #004040 100%); */
  background: linear-gradient(
    #fed780 0%,
    #f9da95 10%,
    #fab976 50%,
    #c6816e 100%
  );
  border-radius: 50%;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.circle:before {
  content: "";
  position: absolute;
  width: 250px;
  height: 250px;
  border-radius: 50%;
  /* background: linear-gradient(#56d1e9 10%, #006a7b 50%, #00404e 100%); */
  background: linear-gradient(#fff1d3 0%, #fab876 50%, #da8a72 100%);
  transform: rotateZ("45deg");
  filter: blur(15px);
}
</style>
