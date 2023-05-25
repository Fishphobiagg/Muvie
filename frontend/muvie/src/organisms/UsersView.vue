<template>
  <div class="user-slider">
    <div class="foruser">
      <p class="slider-nickname" style="font-weight: bold">
        {{ nickname || "익명의 유저" }}
      </p>
      <p class="slider-nickname me">님과 비슷한 유저</p>
    </div>
    <div class="slide-track">
      <div
        class="slide"
        v-for="(user, index) in users"
        :key="index"
        :style="`--img-no: ${index + 1}`"
      >
        <img
          class="user-slide-img"
          :src="`http://127.0.0.1:8000${user.profile_picture}`"
          alt="추천 유저"
          @click="navigateToProfile(user.id)"
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
          :src="`http://127.0.0.1:8000${user.profile_picture}`"
          alt="추천 유저"
          @click="navigateToProfile(user.id)"
        />
        <div>
          <div class="user-slide-nickname">{{ user.nickname }}</div>
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
  methods: {
    navigateToProfile(userId) {
      this.$router.push({ name: "Profile", params: { userId } });
    },
  },
};
</script>

<style>
.foruser {
  display: flex;
  text-align: center;
  margin-left: 40px;
  margin-bottom: 40px;
  justify-content: center; /* 화면 중앙에 정렬 */
}

.user-slider {
  background-color: transparent;
  box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.125);
  height: 900px;
  margin: 0 auto;
  overflow: hidden;
  position: relative;
  width: 100vw;
  display: flex;
  text-align: center;
  justify-content: center;
  flex-direction: column;
}

.slider-nickname {
  display: flex;
  justify-content: start;
  font-size: 40px;
  opacity: 0.9;
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
  cursor: pointer;
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
