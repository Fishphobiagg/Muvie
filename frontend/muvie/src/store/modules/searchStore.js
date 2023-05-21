/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const mainStore = {
  state: {
    searchedList : null,
  },
  actions: {
    getSearchList({ commit }, keyword) {
      axios
        .get(`${BASE_URL}/music/search/${keyword}`)
        .then((res) => {
          console.log("검색 결과 가져오기");
          console.log(res.data);
          commit("getSearchedList", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mutations: {
    getSearchedList(state, payload) {
      state.searchedList = payload;
      console.log("성분추천 불러오기");
    },
  },
};

export default mainStore;
