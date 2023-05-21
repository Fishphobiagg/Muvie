<template>
  <div class="slider-bar">
    <input
      type="range"
      min="0"
      max="100"
      value="50"
      class="slider"
      @input="handleSliderChange"
    />
    <div class="slider-value-container">
      <p class="slider-value">{{ sliderValue }}</p>
      <p class="slider-value label">{{ ingredient }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "VerticalSlider",
  data() {
    return {
      sliderValue: 50,
    };
  },
  props: {
    ingredient: String,
  },
  methods: {
    handleSliderChange(event) {
      this.sliderValue = event.target.value / 100;
      console.log("슬라이드 바 값:", this.sliderValue);
      this.$emit("slider-change", this.sliderValue);
    },
  },
};
</script>

<style>
.slider-bar {
  display: flex;
  width: 350px;
  align-items: center;
  justify-content: space-between;
}

.slider {
  -webkit-appearance: none;
  appearance: none;
  width: 250px;
  height: 15px;
  border-radius: 20px;
  background: #fff;
  box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.1), -5px -5px 10px #fff,
    inset 4px 4px 4px rgba(0, 0, 0, 0.1);
  outline: none;
  opacity: 0.9;
  -webkit-transition: 0.2s;
  transition: opacity 0.2s;
  cursor: pointer;
  writing-mode: bt-lr;
  margin: 10px;
  overflow: hidden;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #fff;
  border: 2px solid #dfe9f3;
  box-shadow: -407px 0 0 400px #93a5cf;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #4caf50;
  cursor: pointer;
}

.slider-value-container {
  display: flex;
  width: 100px;
  justify-content: space-between;
  align-items: center;
}

.slider-value {
  transform: rotate(-270deg);
}

.label {
  width: 70px;
  height: 30px;
}
</style>
