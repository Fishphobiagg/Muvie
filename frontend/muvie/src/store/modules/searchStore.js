/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const searchStore = {
  state: {
    searchedList: null,
  },
  actions: {
    getSearchList({ commit }, keyword) {
      axios
        .get(`${BASE_URL}/music/search/${keyword}`)
        .then((res) => {
          console.log("검색 결과 가져오기");
          console.log(res.data.data);
          commit("updateSearchedList", res.data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // like({ commit }, id) {
    //   axios.post(`${BASE_URL}/music/like/${id}`).then((res) => {
    //     console.log(res);
    //     commit("updateSearchedList", res.like_list);
    //   });
    // },
    // unlike({ commit }, id) {
    //   axios.delete(`${BASE_URL}/music/like/${id}`).then((res) => {
    //     console.log(res);
    //     commit("updateSearchedList", res.like_list);
    //   });
    // },
  },
  mutations: {
    getSearchedList(state, payload) {
      state.searchedList = payload;
      console.log("검색 결과 불러오기");
    },
    updateSearchedList(state, payload) {
      state.searchedList = payload;
      console.log("검색 결과에 반영");
    },
  },
};

export default searchStore;
