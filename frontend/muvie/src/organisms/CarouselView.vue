<template>
  <div class="flex-center">
    <div class="circular-slider flex-center">
      <ul class="wrapper">
        <li class="slides" style="--img-no: 1">
          <img :src="components[0].poster" alt="성분 추천 음악" />
          <div>
            <div>{{ components[0].title }}</div>
            <div>{{ components[0].artist }}</div>
            <div>{{ components[0].album }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 2">
          <img :src="components[1].poster" alt="성분 추천 음악" />
          <div>
            <div>{{ components[1].title }}</div>
            <div>{{ components[1].artist }}</div>
            <div>{{ components[1].album }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 3">
          <img :src="components[2].poster" alt="성분 추천 음악" />
          <div>
            <div>{{ components[2].title }}</div>
            <div>{{ components[2].artist }}</div>
            <div>{{ components[2].album }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 4">
          <img :src="components[3].poster" alt="성분 추천 음악" />
          <div>
            <div>{{ components[3].title }}</div>
            <div>{{ components[3].artist }}</div>
            <div>{{ components[3].album }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 5">
          <img :src="components[4].poster" alt="성분 추천 음악" />
          <div>
            <div>{{ components[4].title }}</div>
            <div>{{ components[4].artist }}</div>
            <div>{{ components[4].album }}</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "CarouselView ",
  props: {
    components: Array,
  },
};
</script>

<style>
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

/* .circular-slider {
  position: relative;
  top: 42vh;

  width: calc(50rem / 2);
  height: calc(50rem / 2);

  color: #fff;
  text-align: center;
} */

.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
}

.slides {
  list-style: none;
}

.slides img {
  margin: 5px;

  height: 100px;
  width: 100px;
}
</style>
