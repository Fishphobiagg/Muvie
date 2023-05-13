// import router from "@/router";
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/accounts/auth";

const loginStore = {
  state: {
    userInfo: null,
    isLogin: false,
  },
  mutations: {
    // 로그인 상태 변경
    loginSuccess(state, payload) {
      this.state.userInfo = payload;
      this.state.isLogin = true;
      console.log(this.userInfo);
      console.log("로그인 성공~");
    },
    logoutSuccess() {
      this.state.userInfo = null;
      this.state.isLogin = false;
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("vuex");
      console.log("로그아웃 성공!");
    },
  },
  actions: {
    login({ commit }, loginObj) {
      axios
        .post(BASE_URL, loginObj)
        .then((res) => {
          console.log(res.data);
          const accessToken = res.data.token.access;
          localStorage.setItem("access_token", accessToken);
          const refreshToken = res.data.token.refresh;
          localStorage.setItem("refresh_token", refreshToken);
          axios.defaults.headers.common.Authorization = `Bearer ${accessToken}`;
          commit("loginSuccess", res.data.user);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  logout({ commit }) {
    commit("logoutSuccess");
    // axios.delete(BASE_URL);
  },
};

export default loginStore;
