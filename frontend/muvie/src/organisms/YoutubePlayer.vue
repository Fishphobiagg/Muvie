<template>
  <div id="player">
    <img class="albumCover" :src="albumCover" alt="앨범 커버" />
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
    <i v-if="isPlaying" @click="stopPlayer" class="fas fa-pause"></i>
    <i v-else @click="startPlayer()" class="fas fa-play"></i>
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
      currentVideoId: "", // 현재 동영상 id
    };
  },
  computed: {
    ...mapState({
      videoId: (state) => state.playerStore.videoId,
      duration: (state) => state.playerStore.duration,
      albumCover: (state) => state.playerStore.albumCover,
      isPlaying: (state) => state.playerStore.isPlaying,
    }),
  },
  methods: {
    // onPlayerReady(event) {
    //   console.log("플레이어 준비");
    //   if (this.isPlaying) {
    //     // 플레이어가 준비되면 소리
    //     event.target.unMute();
    //     // 상태 변경
    //     this.$store.dispatch("startPlayerState");
    //   }
    // },
    // onPlayerReady(event) {
    //   console.log("플레이어 준비");
    //   if (this.isPlaying) {
    //     console.log("플레이어 시작");
    //     console.log(event.target);
    //     event.target.playVideo(); // 플레이어 재생
    //     this.startTimer(); // 타이머 시작
    //     this.$store.dispatch("startPlayerState"); // 상태 변경
    //   }
    // },
    startPlayer() {
      this.$store.dispatch("startPlayerState");
      const { youtubeIframe } = this.$refs;
      if (youtubeIframe) {
        youtubeIframe.src = this.videoId; // iframe의 src를 빈 문자열로 설정하여 멈추기
      }
      console.log("하단바로 시작 요청");

      // console.log(event);
      // this.$store.dispatch("startPlayerState"); // 상태 변경
      // this.onPlayerReady(event);
      // console.log("플레이어 시작 요청");
    },
    stopPlayer() {
      const { youtubeIframe } = this.$refs;
      if (youtubeIframe) {
        youtubeIframe.src = ""; // iframe의 src를 빈 문자열로 설정하여 멈추기
      }
      clearInterval(this.timer); // 타이머 멈춤
      this.progress = 100; // 막대기의 길이를 최대로 설정하여 이동 멈추기
      this.$store.dispatch("stopPlayerState");
    },
    startTimer() {
      console.log("스타트 타이머");
      this.progress = 0; // 막대기 길이 초기화
      this.timer = setInterval(
        this.updateProgress,
        (this.duration * 1000) / 100
      ); // duration 동안 100번에 걸쳐서 updateProgress 메서드 호출
      this.$store.dispatch("startPlayerState");
    },
    updateProgress() {
      if (this.progress >= 100) {
        // 막대기가 이미 최대 길이에 도달한 경우
        clearInterval(this.timer); // 타이머 멈춤
        this.$store.dispatch("stopPlayerState");
        return; // 함수 종료
      }

      this.progress += 1; // 1%씩 길이 증가

      if (this.progress >= 100) {
        // 막대기가 최대 길이에 도달한 경우
        this.progress = 100; // 최대 길이로 설정
        clearInterval(this.timer); // 타이머 멈춤
        this.$store.dispatch("stopPlayerState");
        console.log("타이머 종료"); // 예시로 콘솔에 메시지 출력
      }
    },
    loadVideoById(videoId) {
      const player = document.getElementById("player");
      player.src = `https://www.youtube.com/embed/${videoId}`;
    },
    playVideo() {
      const player = document.getElementById("player");
      player.contentWindow.postMessage(
        '{"event":"command","func":"playVideo","args":""}',
        "*"
      );
    },
    reloadPage() {
      // 페이지 새로고침 시 실행되는 동작을 여기에 작성합니다.
      console.log("페이지 새로고침됨");
      this.$store.dispatch("stopPlayerState");
    },
  },
  watch: {
    $route() {
      this.reloadPage();
    },
    // isPlaying이 false면 무조건 플레이어 멈추기
    isPlaying(newValue) {
      if (!newValue) {
        console.log("플레이어 멈춰", newValue);
        this.stopPlayer();
      }
    },
    duration(newValue) {
      console.log("듀레이션 값 변경", newValue);
      const { youtubeIframe } = this.$refs;
      if (youtubeIframe) {
        console.log("듀레이션 바뀜");
        youtubeIframe.contentWindow.postMessage(
          '{"event":"command","func":"playVideo","args":""}',
          "*"
        ); // 플레이어 재생
      }
      this.startTimer(); // 타이머 시작
      this.$store.dispatch("startPlayerState"); // 상태 변경
    },
    currentVideoId(newValue) {
      if (newValue) {
        this.loadVideoById(newValue); // 동영상 로드
        this.playVideo(); // 동영상 재생
      }
    },
  },
  mounted() {
    if (!this.isPlaying) {
      console.log("새로고침됐지만 멈춰");
      this.$store.dispatch("stopPlayerState");
      const { youtubeIframe } = this.$refs;
      if (youtubeIframe) {
        youtubeIframe.src = ""; // iframe의 src를 빈 문자열로 설정하여 멈추기
      }
    }
  },
};
</script>

<style>
.albumCover {
  width: 66px;
  height: 66px;
  background-color: white;
  border-radius: 5px;
  overflow: hidden;
  object-fit: cover;
}

#player {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 12%;
  background-color: #eef3f7;
  /* opacity: 0.3; */
  box-shadow: 0px -5px 15px -10px rgba(50, 88, 130, 0.22);
  text-align: center;
  display: flex; /* 요소들을 가로 방향으로 정렬하기 위해 flexbox 사용 */
  align-items: center; /* 수직 방향으로 중앙 정렬 */
  justify-content: center; /* 수평 방향으로 중앙 정렬 */
  margin-top: 50px;
}

#player i {
  margin-right: 10px;
  cursor: pointer;
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
