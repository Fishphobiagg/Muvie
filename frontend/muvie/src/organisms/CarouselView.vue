<template>
  <div class="carousel-wrapper">
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
};
</script>

<style scoped>
.carousel-wrapper {
  width: 100%;
  height: 300px;
  perspective: 800px;
  overflow: hidden;
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0) 0%,
    #fff 100%
  ); /* 하얀색 그라데이션 배경 */
}

.carousel {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transform-style: preserve-3d;
  transition: transform 0.5s;
  cursor: grab;
}

.carousel-item {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 180px;
  height: 250px;
  transition: transform 0.5s, opacity 0.5s, z-index 0.5s;
}

.carousel-box {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  text-align: center;
  cursor: pointer;
}

.image-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 100%; /* 이미지의 가로 세로 비율에 따라 조정 */
  overflow: hidden;
}

.carousel-box img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지를 가로 세로 비율에 맞게 조정 */
  border-radius: 10px;
}
.carousel-item.active {
  z-index: 100;
}
</style>
