/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/accounts/auth";

const loginStore = {
  state: {
    userInfo: null,
    isLogin: false,
    userId: null,
  },
  actions: {
    // 로그인
    login({ commit }, loginObj) {
      axios
        .post(BASE_URL, loginObj)
        .then((res) => {
          commit("loginSuccess", res.data.user);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mutations: {
    // 로그인 성공 후 상태 변경
    loginSuccess(state, payload) {
      state.userInfo = payload;
      state.isLogin = true;
      state.userId = payload.id;
      console.log("로그인 성공~");
    },
  },
};

export default loginStore;
