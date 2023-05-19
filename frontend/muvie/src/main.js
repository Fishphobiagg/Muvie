import Vue from "vue";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// request interceptor
axios.interceptors.request.use(
  (config) => {
    // 액세스 토큰이 로컬 스토리지에 있는 경우, 헤더에 추가
    const vuex = JSON.parse(localStorage.getItem("vuex"));
    if (vuex) {
      const { accessToken } = vuex.loginStore;
      // eslint-disable-next-line no-param-reassign
      config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
