/* eslint-disable no-param-reassign */
import axios from "axios";

// const BASE_URL = `http://127.0.0.1:8000`;

const playerStore = {
  state: {
    videoId: null,
    duration: null,
  },
  actions: {
    playMusic({ commit }, { title, artist }) {
      console.log(title, artist);
      const searchRequest = axios.get(
        `https://content-youtube.googleapis.com/youtube/v3/search?q=${title}${artist}&part=snippet&maxResults=1&type=video&key=${process.env.VUE_APP_YOUTUBE_APIKEY}`
      );

      searchRequest
        .then((res) => {
          console.log("비디오 아이디");
          const { videoId } = res.data.items[0].id;
          console.log(videoId);
          commit("setVideoId", videoId);

          const durationRequest = axios.get(
            `https://www.googleapis.com/youtube/v3/videos?part=contentDetails&maxResults=1&id=${videoId}&key=${process.env.VUE_APP_YOUTUBE_APIKEY}`
          );

          durationRequest
            // eslint-disable-next-line no-shadow
            .then((res) => {
              const { duration } = res.data.items[0].contentDetails;
              console.log(duration);
              commit("setDuration", duration);
            })
            .catch((error) => {
              console.error("API 요청 에러:", error);
            });
        })
        .catch((error) => {
          console.error("API 요청 에러:", error);
        });
    },
  },
  mutations: {
    setVideoId(state, payload) {
      state.videoId = payload;
      console.log("비디오 아이디 전달");
    },
    setDuration(state, payload) {
      const numbersOnly = payload.match(/\d+/g).map(Number);
      const sec = numbersOnly[0] * 60 + numbersOnly[1];
      state.duration = sec;
      console.log("비디오 길이 전달", state.duration);
    },
  },
};

export default playerStore;
