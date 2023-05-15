// import router from "@/router";
import axios from "axios";

const userId = localStorage.getItem("user_id");
const BASE_URL = `http://127.0.0.1:8000/accounts/${userId}/profile`;

const loginStore = {
  state: {},
  mutations: {},
  actions: {
    // login({ commit }, loginObj) {
    //   axios
    //     .post(BASE_URL, loginObj)
    //     .then((res) => {
    //       console.log(res.data);
    //       const accessToken = res.data.token.access;
    //       localStorage.setItem("access_token", accessToken);
    //       const refreshToken = res.data.token.refresh;
    //       localStorage.setItem("refresh_token", refreshToken);
    //       axios.defaults.headers.common.Authorization = `Bearer ${accessToken}`;
    //       commit("loginSuccess", res.data.user);
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },
    getProfile() {
      axios.get(BASE_URL);
    },
  },
};

export default loginStore;
