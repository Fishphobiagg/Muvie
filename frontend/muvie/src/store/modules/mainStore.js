/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/";

const mainStore = {
  state: {
    componentsRecommends: null,
    userRecommends: null,
    likeRecommends: null,
  },
  actions: {
    // 추천 데이터 가져오기
    getComponentsRecommends({ commit }) {
      axios
        .get(`${BASE_URL}/recommend/components`)
        .then((res) => {
          commit("getComponents", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getUserRecommends({ commit }) {
      axios
        .get(`${BASE_URL}/recommend/user`)
        .then((res) => {
          commit("getUser", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getLikeRecommends({ commit }) {
      axios
        .get(`${BASE_URL}/recommend/like`)
        .then((res) => {
          commit("getLike", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mutations: {
    // 로그인 성공 후 상태 변경
    getComponents(state, payload) {
      state.componentsRecommends = payload;
      console.log("성분추천 불러오기");
    },
    getUser(state, payload) {
      state.userRecommends = payload;
      console.log("유저추천 불러오기");
    },
    getLike(state, payload) {
      state.likeRecommends = payload;
      console.log("좋아요추천 불러오기");
    },
  },
};

export default mainStore;
