<template>
  <div id="player">
    <!-- <img
      class="album_cover"
      :src="album_cover"
      alt="앨범 커버"
    /> -->
    <iframe
      ref="youtubeIframe"
      width="100"
      height="90"
      :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`"
      frameborder="0"
      allow="autoplay; encrypted-media"
      allowfullscreen
      :style="{ display: 'none' }"
    ></iframe>
    <i @click="stopPlayer" class="fas fa-play"></i>
    <i class="fa-solid fa-pause"></i>
    <div class="progress-bar">
      <div class="progress" :style="{ width: `${progress}%` }"></div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "YoutubePlayer",
  data() {
    return {
      progress: 0, // 막대기의 길이를 나타내는 변수
      timer: null, // 타이머 변수
    };
  },
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
      clearInterval(this.timer); // 타이머 멈춤
      this.progress = 100; // 막대기의 길이를 최대로 설정하여 이동을 멈춥니다.
    },
    startTimer() {
      console.log("스타트 타이머");
      this.progress = 0; // 막대기의 길이 초기화
      this.timer = setInterval(
        this.updateProgress,
        (this.duration * 1000) / 100
      ); // duration 동안 100번에 걸쳐서 updateProgress 메서드 호출
    },
    updateProgress() {
      if (this.progress >= 100) {
        // 막대기가 이미 최대 길이에 도달한 경우
        clearInterval(this.timer); // 타이머 멈춤
        return; // 함수 종료
      }

      this.progress += 1; // 1%씩 길이 증가

      if (this.progress >= 100) {
        // 막대기가 최대 길이에 도달한 경우
        this.progress = 100; // 최대 길이로 설정
        clearInterval(this.timer); // 타이머 멈춤
        // 원하는 동작 수행
        console.log("타이머 종료"); // 예시로 콘솔에 메시지 출력
      }
    },
  },
  mounted() {
    // duration 값이 변경되면 타이머 시작
    this.$watch("duration", () => {
      this.startTimer();
    });
  },
};
</script>

<style>
#player {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 12%;
  background-color: #eef3f7;
  box-shadow: 0px -5px 15px -10px rgba(50, 88, 130, 0.22);
  text-align: center;
  display: flex; /* 요소들을 가로 방향으로 정렬하기 위해 flexbox 사용 */
  align-items: center; /* 수직 방향으로 중앙 정렬 */
  justify-content: center; /* 수평 방향으로 중앙 정렬 */
  margin-top: 50px;
}

#player i {
  margin-right: 10px;
}

#player i.fas.fa-play {
  font-size: 1.8em; /* 2배 크기로 설정 */
  color: white; /* 색상 변경 */
  filter: drop-shadow(0 18px 6px rgba(172, 184, 204, 0.45));
}

#player i.fa-pause {
  font-size: 1.8em; /* 2배 크기로 설정 */
  color: white; /* 색상 변경 */
  filter: drop-shadow(0 18px 6px rgba(172, 184, 204, 0.45));
}

.progress-bar {
  /* width: 200px;
  height: 5px;
  background-color: red;
  margin: 10px auto;
  position: relative; */
  height: 6px;
  width: 70%;
  background-color: #d0d8e6;
  display: inline-block;
  border-radius: 10px;
  /* filter: drop-shadow(0 11px 6px rgba(172, 184, 204, 0.45)); */
}

.progress {
  height: inherit;
  background-color: #a3b3ce;
  border-radius: 10px;
  transition: width 0.3s linear;
}
</style>
