/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const searchStore = {
  state: {
    searchedList: null,
    userList: null,
  },
  actions: {
    getSearchList({ commit }, keyword) {
      axios
        .get(`${BASE_URL}/music/search/${keyword}`)
        .then((res) => {
          console.log("검색 결과 가져오기");
          console.log(res.data.data);
          commit("getSearchedList", res.data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getUserList({commit}, keyword){
      axios
      .get(`${BASE_URL}/accounts/search/${keyword}`)
      .then((res) => {
        console.log("유저 검색 결과 가져오기");
        console.log(res.data.data)
        commit("getUserList", res.data.data)
      })
    }
  },
  mutations: {
    getSearchedList(state, payload) {
      state.searchedList = payload;
      console.log("검색 결과 불러오기");
    },
    getUserList(state, payload) {
      state.userList = payload;
      console.log("유저 검색 결과 불러오기");
      
    },
  },
};

export default searchStore;
