<template>
  <div class="flex-center">
    <div class="circular-slider flex-center">
      <ul class="wrapper">
        <li class="slides" style="--img-no: 1">
          <img
            :src="`http://127.0.0.1:8000/${users[0].profile_picture}`"
            alt="추천
          유저"
          />
          <div>
            <div>{{ users[0].nickname }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 2">
          <img
            :src="`http://127.0.0.1:8000/${users[1].profile_picture}`"
            alt="추천 유저"
          />
          <div>
            <div>{{ users[1].nickname }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 3">
          <img
            :src="`http://127.0.0.1:8000/${users[2].profile_picture}`"
            alt="추천 유저"
          />
          <div>
            <div>{{ users[2].nickname }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 4">
          <img
            :src="`http://127.0.0.1:8000/${users[3].profile_picture}`"
            alt="추천 유저"
          />
          <div>
            <div>{{ users[3].nickname }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 5">
          <img
            :src="`http://127.0.0.1:8000/${users[4].profile_picture}`"
            alt="추천 유저"
          />
          <div>
            <div>{{ users[4].nickname }}</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "UsersView",
  props: {
    users: Array,
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
