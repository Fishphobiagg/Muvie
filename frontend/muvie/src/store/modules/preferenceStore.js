/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/music/component";

const preferenceStore = {
  state: {
    myPreference: [],
  },
  actions: {
    submitPreference(_, preference) {
      axios
        .post(BASE_URL, preference)
        .then((res) => {
          console.log("음악성분 수정 요청 완료");
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getPreference() {
      axios
        .get(BASE_URL)
        .then((res) => {
          console.log("음악성분 조회");
          console.log(res.data);
          this.$refs.verticalSlider.setValue(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mutations: {
    // 로그인 성공 후 상태 변경
    getIngredients(state, payload) {
      state.myPreference = payload;
      console.log("성분 조회 성공");
    },
  },
};

export default preferenceStore;
