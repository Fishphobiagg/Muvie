<template>
  <div>
    <div class="slider-container">
      <VerticalSlider
        ref="VerticalSlider"
        v-for="(ingredient, idx) in ingredients"
        :key="idx"
        :idx="idx"
        :ingredient="ingredient"
        @slider-change="handleSliderChange($event, idx)"
      />
    </div>
    <div class="button-container">
      <button class="preference-button" @click="confirmModal(myPreference)">
        확인
      </button>
      <button class="preference-button" @click="closeModal">나중에 하기</button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
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
        "데시벨",
        "춤",
      ],
      ingredientsTitle: [
        "energy",
        "instrumentalness",
        "liveness",
        "acousticness",
        "speechiness",
        "valence",
        "tempo",
        "loudness",
        "danceability",
      ],
      preferences: {
        energy: 0.5,
        instrumentalness: 0.5,
        liveness: 0.5,
        acousticness: 0.5,
        speechiness: 0.5,
        valence: 0.5,
        tempo: 80.0,
        mode: 0.5,
        loudness: 50.0,
        danceability: 0.5,
      },
    };
  },
  methods: {
    confirmModal(myPreference) {
      console.log("확인 버튼 클릭");
      // eslint-disable-next-line eqeqeq
      console.log("제출");
      console.log(myPreference);
      this.$store.dispatch("submitPreference", myPreference);
      this.$emit("close-modal");
    },
    closeModal() {
      console.log("모달 닫기");
      this.$emit("close-modal");
    },
  },
  computed: mapState({
    myPreference: (state) => state.preferenceStore.myPreference,
  }),
};
</script>

<style>
.slider-container {
  display: flex;
  width: 66%;
  height: 400px;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  transform: rotate(-90deg);
}

.button-container > button {
  position: relative;
  margin: 20px;
  padding: 13px 30px;
  background: white;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  text-decoration: none;
  border: none;
  z-index: 900;
  transition: transform 0.3s;
}

.button-container > button:hover {
  color: white;
  background: rgba(218, 138, 114, 0.8);
  letter-spacing: 2px;
  cursor: pointer;
}

.button-container > button:active {
  transform: scale(1.1);
}
</style>
