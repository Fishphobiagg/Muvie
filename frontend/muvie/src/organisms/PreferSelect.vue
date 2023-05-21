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
  justify-content: center;
  align-items: center;
  height: 300px;
  gap: 10px;
  transform: rotate(-90deg);
}
</style>
