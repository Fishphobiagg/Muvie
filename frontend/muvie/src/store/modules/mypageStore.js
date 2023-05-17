/* eslint-disable no-param-reassign */
import axios from "axios";

const mypageStore = {
  state: {
    followers: [],
    following: [],
    followers_count: null,
    following_count: null,
    profile_picture: null,
    profile_picture_usage: null,
  },
  actions: {
    getProfile({ commit }, id) {
      const BASE_URL = `http://127.0.0.1:8000`;

      // 유저 데이터 가져오기
      const MYPAGE_API = `${BASE_URL}/accounts/${id}/profile`;
      console.log(MYPAGE_API);
      axios
        .get(MYPAGE_API)
        .then((res) => {
          console.log("프로필 요청");
          commit("getUserDetail", res.data);

          // 유저(본인) 프로필사진 가져오기
          if (res.data.user_profile.profile_picture) {
            const PHOTO_API = `${BASE_URL}/${res.data.user_profile.profile_picture}`;
            console.log(PHOTO_API);
            axios
              .get(PHOTO_API, {
                responseType: "arraybuffer",
              })
              .then((response) => {
                const image = new Blob([response.data], { type: "image/jpeg" });
                const imageUrl = URL.createObjectURL(image);
                commit("getPhoto", imageUrl);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        })
        .catch((err) => console.log(err));
    },
  },
  mutations: {
    getUserDetail(state, payload) {
      state.followers = payload.detail.followers;
      state.following = payload.detail.following;
      state.followers_count = payload.detail.followers_count;
      state.following_count = payload.detail.following_count;
      state.profile_picture = payload.user_profile.profile_picture;

      console.log("마이페이지 성공");
    },
    getPhoto(state, payload) {
      state.profile_picture_usage = payload;

      console.log(state.profile_picture_usage);
      console.log("이미지 요청 성공");
    },
  },
};

export default mypageStore;
