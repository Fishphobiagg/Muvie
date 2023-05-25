<template>
  <div class="carousel-wrapper">
    <div class="welcome-msg">
      {{ nickname || "익명의 유저" }} 님을 위한 <br />오늘의 음악
    </div>
    <div
      class="carousel"
      @wheel="handleWheel"
      @mousedown="handleMouseDown"
      @touchstart="handleMouseDown"
      @mousemove="handleMouseMove"
      @touchmove="handleMouseMove"
      @mouseup="handleMouseUp"
      @touchend="handleMouseUp"
      ref="carousel"
    >
      <div
        v-for="(component, index) in components"
        :key="index"
        class="carousel-item"
        :class="{ active: index === active }"
        :style="{
          transform: `translateX(${
            (index - active) * (itemWidth + spacing)
          }px) translateY(${(index - active) * (itemWidth / -2)}px) rotateZ(${
            (index - active) * 15
          }deg)`,
          zIndex: components.length - Math.abs(active - index),
          opacity: 1 - Math.abs(active - index) / components.length,
        }"
        @click="clickAnimation(index)"
      >
        <div class="carousel-box">
          <div class="image-container">
            <img :src="component.poster" alt="성분 추천 음악" />
          </div>
          <div>
            <div>{{ component.title }}</div>
            <div>{{ component.artist }}</div>
            <div>{{ component.album }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "CarouselView",
  props: {
    components: Array,
  },
  data() {
    return {
      active: 0,
      isDown: false,
      startX: 0,
      itemWidth: 180,
      spacing: 20,
    };
  },
  methods: {
    clickAnimation(index) {
      this.active = index;
    },
    handleWheel(event) {
      event.preventDefault();
      this.active += event.deltaY > 0 ? 1 : -1;
      this.active = Math.max(
        0,
        Math.min(this.active, this.components.length - 1)
      );
    },
    handleMouseDown(event) {
      this.isDown = true;
      this.startX =
        event.clientX || (event.touches && event.touches[0].clientX) || 0;
    },
    handleMouseMove(event) {
      if (!this.isDown) return;
      const x =
        event.clientX || (event.touches && event.touches[0].clientX) || 0;
      const deltaX = x - this.startX;
      const itemDelta = Math.round(deltaX / (this.itemWidth + this.spacing));
      this.active = Math.max(
        0,
        Math.min(this.active - itemDelta, this.components.length - 1)
      );
    },
    handleMouseUp() {
      this.isDown = false;
    },
  },
  computed: {
    ...mapState({
      nickname: (state) =>
        localStorage.getItem("vuex") && state.loginStore.userInfo
          ? state.loginStore.userInfo.nickname
          : "익명의 유저",
    }),
  },
};
</script>

<style>
.carousel-wrapper {
  position: relative;
  top: 20;
  width: 100%;
  height: 80vh;
  padding: 0;
  perspective: 800px;
  overflow: hidden;
  z-index: 1;
}

.carousel {
  position: relative;
  width: 100%;
  height: 40%;
  display: flex;
  align-items: center;
  justify-content: center;
  transform-style: preserve-3d;
  transition: transform 0.5s;
  cursor: grab;
  z-index: 2; /* 이미지 캐러셀을 앞으로 가져옴 */
}

.carousel-item {
  position: absolute;
  transform: translate(-50%, -50%);
  width: 250px;
  height: 350px;
  transition: transform 0.5s, opacity 0.5s, z-index 0.5s;
  z-index: 3; /* 이미지 캐러셀 요소가 다른 요소들보다 앞에 위치하도록 설정 */
}

.carousel-box {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  text-align: center;
  cursor: pointer;
  filter: brightness(0.7);
  transition: filter 0.5s;
  z-index: 2; /* 이미지 캐러셀 요소가 welcome-msg 요소 앞으로 나오도록 설정 */
}

.carousel-item.active .carousel-box {
  filter: brightness(1);
}

.image-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.carousel-box img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
  filter: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.5),
    rgba(0, 0, 0, 1)
  ) !important; /* 그라데이션을 통해 어둡게 만듦 */
}

.carousel-item.active {
  z-index: 100;
}
</style>
