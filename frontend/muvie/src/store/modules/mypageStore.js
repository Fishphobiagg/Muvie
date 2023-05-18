/* eslint-disable no-param-reassign */
import axios from "axios";

const BASE_URL = `http://127.0.0.1:8000`;

const mypageStore = {
  state: {
    followers: [],
    following: [],
    followers_count: null,
    following_count: null,
    nickname: null,
    profile_picture: null,
  },
  actions: {
    getProfile({ commit }, id) {
      // const BASE_URL = `http://127.0.0.1:8000`;

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
    follow({ commit }, id) {
      axios.post(`${BASE_URL}/accounts/${id}/follow`).then((res) => {
        console.log(res);
        commit("updateFollowState", id);
      });
    },
    editNickname({ commit }, payload) {
      console.log(payload);
      const data = {
        nickname: payload.name,
      };
      axios
        .patch(`${BASE_URL}/accounts/edit/${payload.id}/`, data)
        .then((res) => {
          console.log(res);
          console.log("닉네임 변경 성공");
          commit("updateNickname", data.nickname);
        });
    },
    editPhoto({ commit }, payload) {
      console.log(payload);
      // eslint-disable-next-line no-restricted-syntax
      for (const key of payload.keys()) {
        console.log(key);
      }
      const data = {
        profile_picture: payload.profile_picture,
      };
      console.log(data);
      axios
        .patch(`${BASE_URL}/accounts/edit/${payload.id}/`, data)
        .then((res) => {
          console.log(res);
          console.log("프로필사진 변경 성공");
          commit("updatePhoto", data.profile_picture);
        });
    },
  },
  mutations: {
    getUserDetail(state, payload) {
      state.followers = payload.detail.followers;
      state.following = payload.detail.following;
      state.followers_count = payload.detail.followers_count;
      state.following_count = payload.detail.following_count;
      state.nickname = payload.user_profile.nickname;
      state.profile_picture = payload.user_profile.profile_picture;
      console.log(state);
      console.log(state.profile_picture);

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
