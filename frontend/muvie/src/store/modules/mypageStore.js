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
    like_list: null,
    play_list: null,
  },
  actions: {
    getLikeList({ commit }) {
      const LIKELIST_API = `${BASE_URL}/accounts/like`;
      console.log(LIKELIST_API);
      axios
        .get(LIKELIST_API)
        .then((res) => {
          console.log("좋아요 목록 요청");
          console.log(res);
          commit("getUserLike", res.data);
        })
        .catch((err) => console.log(err));
    },
    getProfile({ commit }, id) {
      // 유저 데이터 가져오기
      const MYPAGE_API = `${BASE_URL}/accounts/${id}/profile`;
      console.log(MYPAGE_API);
      axios
        .get(MYPAGE_API)
        .then((res) => {
          console.log("프로필 요청");
          console.log(res);
          c 
        })
        .catch((err) => console.log(err));
    },
    getPlayList({ commit }) {
      const PLAYLIST_API = `${BASE_URL}/accounts/playlist`;
      console.log(PLAYLIST_API);
      axios
        .get(PLAYLIST_API)
        .then((res) => {
          console.log("재생목록 요청");
          console.log(res);
          commit("getUserPlayList", res.data);
        })
        .catch((err) => console.log(err));
    },
    like({ commit }, id) {
      axios.post(`${BASE_URL}/music/like/${id}`).then((res) => {
        console.log(res);
        commit("updateLikeState", res.like_list);
      });
    },
    unlike({ commit }, id) {
      axios.delete(`${BASE_URL}/music/like/${id}`).then((res) => {
        console.log(res);
        commit("updateLikeState", res.like_list);
      });
    },
    addPlaylist({ commit }, id) {
      axios.post(`${BASE_URL}/music/playlist/${id}`).then((res) => {
        console.log(res);
        commit("updatePlayListState");
      });
    },
    deletePlaylist({ commit }, id) {
      axios.delete(`${BASE_URL}/music/playlist/${id}`).then((res) => {
        console.log(res);
        commit("updatePlayListState");
      });
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
    getUserLike(state, payload) {
      state.like_list = payload.like_list;
      console.log(state.like_list);
      console.log("좋아요 목록  요청 성공");
    },
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
    getUserPlayList(state, payload) {
      state.play_list = payload.play_list;
      console.log(state.play_list);
      console.log("재생목록 요청 성공 뿌뿌");
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
    updateLikeState(state, payload) {
      state.like_list = payload;
      console.log("좋아요 목록 업데이트 성공 뿌뿌");
    },
    updatePlayListState(state, payload) {
      state.playlist = payload;
      console.log("재생 목록 업데이트 성공 뿌뿌");
    },
  },
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
    }),
  },
};

export default mypageStore;
