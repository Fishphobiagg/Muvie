<template>
  <div class="slider">
    <h2 class="slider-nickname">
      {{ nickname || "익명의 유저" }}님과 비슷한 유저 추천
    </h2>
    <div class="slide-track">
      <div
        class="slide"
        v-for="(user, index) in users"
        :key="index"
        :style="`--img-no: ${index + 1}`"
      >
        <img
          class="user-slide-img"
          :src="`http://127.0.0.1:8000/${user.profile_picture}`"
          alt="추천 유저"
        />
        <div>
          <div class="user-slide-nickname">{{ user.nickname }}</div>
        </div>
      </div>
      <!-- 추가: 원래 슬라이드를 복제하여 오른쪽에 추가 -->
      <div
        class="slide"
        v-for="(user, index) in users"
        :key="index + 5"
        :style="`--img-no: ${index + 1}`"
      >
        <img
          class="user-slide-img"
          :src="`http://127.0.0.1:8000/${user.profile_picture}`"
          alt="추천 유저"
        />
        <div>
          <div>{{ user.nickname }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "UsersView",
  props: {
    users: Array,
  },
  computed: {
    ...mapState({
      nickname: (state) =>
        localStorage.getItem("vuex")
          ? state.loginStore.userInfo.nickname
          : "익명의 유저",
    }),
  },
};
</script>

<style>
.slider {
  background-color: transparent;
  box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.125);
  height: 900px;
  margin: auto;
  overflow: hidden;
  position: relative;
  width: 960px;
}

.slider-nickname {
  margin-bottom: 60px;
}
.slide-track {
  animation: scroll 15s linear infinite;
  display: flex;
  height: 600px;
  width: calc(250px * 10); /* 변경: 슬라이드 개수에 맞게 수정 */
}

.slide {
  height: 100px;
  width: 250px;
  flex: 0 0 250px; /* 변경: 슬라이드 너비 설정 */
}

.user-slide-img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
}
.user-slide-nickname {
  margin-top: 10px;
  font-size: 20px;
  font-weight: 700;
}
@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(
      calc(-250px * 5)
    ); /* 변경: 원래 슬라이드 개수에 맞게 수정 */
  }
}
</style>
