/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const mainStore = {
  state: {
    componentsRecommends: null,
    userRecommends: null,
    likeRecommends: null,
  },
  actions: {
    getComponentsRecommends({ commit }) {
      axios
        .get(`${BASE_URL}/accounts/recommend/components`)
        .then((res) => {
          console.log("성분추천 가져오기");
          console.log(res.data);
          commit("getComponents", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getUserRecommends({ commit }) {
      axios
        .get(`${BASE_URL}/accounts/recommend/user`)
        .then((res) => {
          console.log("유저추천 가져오기");
          console.log(res.data);
          commit("getUser", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getLikeRecommends({ commit }) {
      axios
        .get(`${BASE_URL}/accounts/recommend/like`)
        .then((res) => {
          console.log("좋아요추천 가져오기");
          console.log(res.data);
          commit("getLike", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mutations: {
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
