/* eslint-disable no-param-reassign */
import axios from "axios";
import { mapState } from "vuex";

const BASE_URL = `http://127.0.0.1:8000`;

const mypageStore = {
  state: {
    followers: [],
    following: [],
    followers_count: null,
    following_count: null,
    nickname: null,
    profile_picture: null,
    userId: null,
  },
  actions: {
    getProfile({ commit }, id) {
      // 유저 데이터 가져오기
      const MYPAGE_API = `${BASE_URL}/accounts/${id}/profile`;
      console.log(MYPAGE_API);
      axios
        .get(MYPAGE_API)
        .then((res) => {
          console.log("프로필 요청");
          console.log(res);
          commit("getUserDetail", res.data);
        })
        .catch((err) => console.log(err));
    },
    follow({ commit }, id) {
      axios.post(`${BASE_URL}/accounts/${id}/follow`).then((res) => {
        console.log(res);
        commit("updateFollowState", res.following);
        // eslint-disable-next-line no-restricted-globals
        location.reload();
      });
    },
    unfollow({ commit }, id) {
      axios.delete(`${BASE_URL}/accounts/${id}/follow`).then((res) => {
        console.log(res);
        commit("updateUnfollowState", res.following);
        // eslint-disable-next-line no-restricted-globals
        location.reload();
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
    editPhoto({ commit, state }, file) {
      console.log("로컬 유저아이디");
      console.log(state);
      axios.patch(`${BASE_URL}/accounts/edit/1/`, file).then((res) => {
        console.log(res);
        console.log("프로필사진 변경 성공");
        commit("updatePhoto", file);
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
      state.userId = payload.user_proile.id;
      console.log(state);
      console.log(state.profile_picture);

      console.log("마이페이지 성공");
    },
    getPhoto(state, payload) {
      state.profile_picture_usage = payload;

      console.log(state.profile_picture_usage);
      console.log("이미지 요청 성공");
    },
    updateFollowState(state, payload) {
      state.following = payload;
      console.log("팔로잉 목록 업데이트 성공");
    },
    updateUnfollowState(state, payload) {
      state.following = payload;
      console.log("언팔로잉 목록 업데이트 성공");
    },
  },
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
    }),
  },
};

export default mypageStore;
