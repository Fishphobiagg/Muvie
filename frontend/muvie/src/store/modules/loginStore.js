/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/accounts/login/";

const loginStore = {
  state: {
    userInfo: null,
    isLogin: false,
    userId: null,
    accessToken: null,
    refreshToken: null,
  },
  actions: {
    // 로그인
    login({ commit }, loginObj) {
      axios
        .post(BASE_URL, loginObj)
        .then((res) => {
          console.log(axios.defaults);
          commit("loginSuccess", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mutations: {
    // 로그인 성공 후 상태 변경
    loginSuccess(state, payload) {
      state.userInfo = payload.user;

      state.isLogin = true;

      state.userId = payload.user.id;

      state.accessToken = payload.token.access;
      state.refreshToken = payload.token.refresh;
      console.log("로그인 성공~");
    },
    updateNickname(state, payload) {
      state.userInfo.nickname = payload;
      console.log("로컬스토리지 닉네임 변경");
    },
    updatePhoto(state, payload) {
      state.userInfo.profile_picture = payload;
      console.log("로컬스토리지 프사 변경");
    },
  },
};

export default loginStore;
