<template>
  <div id="player">
    <iframe
      ref="youtubeIframe"
      width="100"
      height="90"
      :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`"
      frameborder="0"
      allow="autoplay; encrypted-media"
      allowfullscreen
    ></iframe>
    <button @click="stopPlayer">Stop Player</button>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "YoutubePlayer",
  computed: {
    ...mapState({
      videoId: (state) => state.mypageStore.videoId,
      duration: (state) => state.mypageStore.duration,
    }),
  },
  methods: {
    onPlayerReady(event) {
      // 플레이어가 준비되면 소리 키기
      event.target.unMute();
    },
    stopPlayer() {
      const { youtubeIframe } = this.$refs;
      if (youtubeIframe) {
        youtubeIframe.src = ""; // iframe의 src를 빈 문자열로 설정하여 멈춥니다.
      }
    },
  },
  // mounted() {
  //   // YouTube IFrame API 스크립트를 동적으로 로드합니다.
  //   const tag = document.createElement("script");
  //   tag.src = "https://www.youtube.com/iframe_api";
  //   const firstScriptTag = document.getElementsByTagName("script")[0];
  //   firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
  // },
};
</script>
<style>
#player {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #fff;
}
</style>
