<template>
  <div class="slider-container">
    <VerticalSlider
      v-for="(ingredient, idx) in ingredients"
      :key="idx"
      :ingredient="ingredient"
    />
  </div>
</template>

<script>
import VerticalSlider from "../atoms/VerticalSlider.vue";

export default {
  name: "PreferSelect",
  components: {
    VerticalSlider,
  },
  data() {
    return {
      ingredients: [
        "에너지",
        "악기",
        "라이브",
        "어쿠스틱",
        "대화",
        "긍정",
        "템포",
        "장조",
        "데시벨",
        "춤",
      ],
    };
  },
};
</script>

<style>
.slider-container {
  display: flex;
  width: 56%;
  height: 400px;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  transform: rotate(-90deg);
}
</style>
