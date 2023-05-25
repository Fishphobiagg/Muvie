import Vue from "vue";
import axios from "axios";
// import VueYoutube from "vue-youtube";
// eslint-disable-next-line import/no-extraneous-dependencies
import Flicking from "@egjs/vue-flicking";
// eslint-disable-next-line import/no-extraneous-dependencies
import "@egjs/vue-flicking/dist/flicking.css";

import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.use(Flicking);

// request interceptor
axios.interceptors.request.use(
  (config) => {
    // 액세스 토큰이 로컬 스토리지에 있는 경우, 헤더에 추가
    const vuex = JSON.parse(localStorage.getItem("vuex"));
    if (vuex && vuex.loginStore) {
      const { accessToken } = vuex.loginStore;
      // eslint-disable-next-line no-param-reassign
      config.headers.Authorization = `Bearer ${accessToken}`;
    }

    // eslint-disable-next-line eqeqeq
    if (
      config.url.includes("https://content-youtube.googleapis.com/") ||
      config.url.includes(
        "https://www.googleapis.com/youtube/v3/videos?part=contentDetails"
      )
    ) {
      // eslint-disable-next-line no-param-reassign
      config.headers.Authorization = undefined;
      console.log("헤더 삭제");
      console.log(config.headers.Authorization);
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
