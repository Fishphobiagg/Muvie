/* eslint-disable no-param-reassign */
import axios from "axios";

const mypageStore = {
  state: {
    followers: [],
    following: [],
    followers_count: null,
    following_coun: null,
  },
  // computed: mapState({
  //   userId: (state) => state.loginStore.userId,
  // }),
  actions: {
    getProfile({ commit }, id) {
      const BASE_URL = `http://127.0.0.1:8000/accounts/${id}/profile`;

      axios
        .get(BASE_URL)
        .then((res) => {
          console.log(res.data.user_profile);
          console.log(res.data.detail);
          commit("getUserDetail", res.data);
        })
        .catch((err) => console.log(err));
    },
  },
  mutations: {
    // 마이페이지 데이터 저장
    getUserDetail(state, payload) {
      state.followers = payload.detail.followers;
      state.following = payload.detail.following;
      state.followers_count = payload.detail.followers_count;
      state.followers_count = payload.detail.followers_count;

      console.log(state);

      console.log("마이페이지 성공");
    },
  },
};

export default mypageStore;
