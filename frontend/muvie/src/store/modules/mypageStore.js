// import axios from "axios";
// import Vue from "vue";
// import Vuex from "vuex";
// import { useStore } from "vuex";
// import { computed } from "vue";

// const { userId } = localStorage.getItem("vuex");

// Vue.use(Vuex);

const mypageStore = {
  state: {
    followers: null,
    following: null,
  },
  mutations: {},
  actions: {
    getProfile() {
      const Id = this.$store.state.loginStore.userId;
      console.log(Id);
      const BASE_URL = `http://127.0.0.1:8000/accounts/${Id}/profile`;

      // axios.get(BASE_URL).then((res) => {
      //   console.log(res.data);
      // });
      console.log(BASE_URL);
      console.log("에러");
    },
  },
};

export default mypageStore;
