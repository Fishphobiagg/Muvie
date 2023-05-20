<template>
  <div class="flex-center">
    <div class="circular-slider flex-center">
      <ul class="wrapper">
        <li class="slides" style="--img-no: 1">
          <img :src="likes[0].album_cover" alt="좋아요 추천 음악" />
          <div>
            <div>{{ likes[0].title }}</div>
            <div>{{ likes[0].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 2">
          <img :src="likes[1].album_cover" alt="좋아요 추천 음악" />
          <div>
            <div>{{ likes[1].title }}</div>
            <div>{{ likes[1].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 3">
          <img :src="likes[2].album_cover" alt="좋아요 추천 음악" />
          <div>
            <div>{{ likes[2].title }}</div>
            <div>{{ likes[2].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 4">
          <img :src="likes[3].album_cover" alt="좋아요 추천 음악" />
          <div>
            <div>{{ likes[3].title }}</div>
            <div>{{ likes[3].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 5">
          <img :src="likes[4].album_cover" alt="좋아요 추천 음악" />
          <div>
            <div>{{ likes[4].title }}</div>
            <div>{{ likes[4].artist }}</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "LikesView",
  props: {
    likes: Array,
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
