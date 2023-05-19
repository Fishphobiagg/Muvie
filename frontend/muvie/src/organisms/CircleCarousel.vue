<template>
  <div class="flex-center">
    <div class="circular-slider">
      <ul class="wrapper">
        <li class="slides" style="--img-no: 1"><img src="" alt="" /></li>
        <li class="slides" style="--img-no: 2"><img src="" alt="" /></li>
        <li class="slides" style="--img-no: 3"><img src="" alt="" /></li>
        <li class="slides" style="--img-no: 4"><img src="" alt="" /></li>
        <li class="slides" style="--img-no: 5"><img src="" alt="" /></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "CircleCarousel",
};
</script>

<style>
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.circular-slider {
  position: relative;
  top: 42vh;

  width: calc(50rem / 2);
  height: calc(50rem / 2);

  color: #fff;
  text-align: center;
}

.wrapper {
  position: absolute;

  width: 100%;
  height: 100%;
  border: 1px solide crimson;
  border-radius: 50%;

  transform: rotateZ(0deg);
  transition: 1s ease;
}

.slides {
  position: absolute;
  left: 0;
  transform: rotateZ(calc(360deg / 5 * var(--imga-no)))
    translateY(calc(50rem / 2));
  transform-origin: calc(50rem / 2);
  width: 16vw;

  cursor: pointer;
}
.slides img {
  width: 100%;
  border-radius: 50%;
  transform: rotateZ(calc(360 / 5 * var(--imga-no))) scale(var(--scale, 0.8));

  object-fit: cover;
  transition: 0.4s ease;
}

.slides img:hover {
  --scale: 1;
}
</style>
