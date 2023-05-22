/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/music/component";

const preferenceStore = {
  state: {
    myPreference: {
      energy: 50,
      instrumentalness: 50,
      liveness: 50,
      acousticness: 50,
      speechiness: 50,
      valence: 50,
      tempo: 50,
      mode: 50,
      loudness: 50,
      danceability: 50,
    },
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
    getPreference({ commit }) {
      axios
        .get(BASE_URL)
        .then((res) => {
          console.log("음악성분 조회");
          console.log(res.data);
          const modifiedData = { ...res.data };
          modifiedData.energy *= 100;
          modifiedData.instrumentalness *= 100;
          modifiedData.liveness *= 100;
          modifiedData.acousticness *= 100;
          modifiedData.speechiness *= 100;
          modifiedData.valence *= 100;
          modifiedData.mode *= 100;
          modifiedData.danceability *= 100;
          commit("getIngredients", modifiedData);
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
    setPreference(state, payload) {
      state.myPreference[payload.ingredient] = payload.value;
    },
  },
};

export default preferenceStore;
