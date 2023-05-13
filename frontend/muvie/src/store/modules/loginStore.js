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
    },
  },
  actions: {
    login(dispatch, loginObj) {
      axios.post(BASE_URL, loginObj).then((res) => {
        console.log(res.data);
        console.log(res.data);
        const accessToken = res.data.token.access;
        localStorage.setItem("access_token", accessToken);
        const refreshToken = res.data.token.refresh;
        localStorage.setItem("refresh_token", refreshToken);
        axios.defaults.headers.common.Authorization = `Bearer ${accessToken}`;
        this.$store.commit("loginSuccess", res.data.user);
      });
    },
  },
  logout() {
    this.$store.commit("logoutSuccess");
    axios.delete(BASE_URL);
  },
};

export default loginStore;
