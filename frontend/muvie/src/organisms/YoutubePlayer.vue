<template>
  <div id="player">
    <img
      v-if="albumCover"
      class="albumCover"
      :src="albumCover"
      alt="앨범 커버"
    />
    <i v-else class="fa-sharp fa-solid fa-music" style="color: gray"></i>
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

    <div class="detail-and-bar">
      <div class="song-detail">
        <span id="song-title" ref="songTitleRef">{{ title }}</span>
        <span id="song-artist">{{ artist }}</span>
      </div>
      <div class="progress-bar">
        <div class="progress" :style="{ width: `${progress}%` }"></div>
      </div>
    </div>
    <i v-if="isPlaying" @click="stopPlayer" class="fas fa-pause"></i>
    <i v-else @click="startPlayer()" class="fas fa-play"></i>
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
      title: (state) => state.playerStore.title,
      artist: (state) => state.playerStore.artist,
    }),
  },
  methods: {
    startPlayer() {
      this.$store.dispatch("startPlayerState");
      const { youtubeIframe } = this.$refs;
      if (youtubeIframe) {
        youtubeIframe.src = this.videoId; // iframe의 src를 빈 문자열로 설정하여 멈추기
      }
      console.log("하단바로 시작 요청");
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
      // 페이지 새로고침 시 실행되는 동작
      console.log("페이지 새로고침됨");
      this.$store.dispatch("stopPlayerState");
    },
    startTextAnimation() {
      const songTitleElement = this.$refs.songTitleRef;
      const containerWidth = songTitleElement.offsetWidth;
      const textWidth = songTitleElement.scrollWidth;
      if (textWidth > containerWidth) {
        const animationDuration = textWidth / 50; // 원하는 속도로 조정
        songTitleElement.style.animationDuration = `${animationDuration}s`;
        songTitleElement.classList.add("scrolling-text");
      }
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
    this.startTextAnimation();
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
.scrolling-text-container {
  width: 53%;
  overflow: hidden;
  position: relative;
  padding-right: 100px;
}

.scrolling-text {
  white-space: nowrap;
  position: absolute;
  animation: scrollText linear infinite;
  animation-duration: 10s;
}

@keyframes scrollText {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-100%);
  }
}

.albumCover {
  width: 66px;
  height: 66px;
  background-color: white;
  border-radius: 5px;
  overflow: hidden;
  object-fit: cover;
  margin-right: 50px;
}

.fa-sharp {
  border: 1px solid rgba(0, 0, 0, 0.1);
  padding: 17px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

#player {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 12%;
  background-color: #eef3f7c4;
  box-shadow: 0px 55px 15px 50px rgba(50, 88, 130, 0.22);
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
  z-index: 3;
}

#player i {
  margin-right: 10px;
  cursor: pointer;
}

#player i.fas.fa-play {
  font-size: 2em; /* 2배 크기로 설정 */
  color: white; /* 색상 변경 */
  filter: drop-shadow(0 0px 12px rgba(172, 184, 204, 205));
}

#player i.fa-pause {
  font-size: 2em; /* 2배 크기로 설정 */
  color: white; /* 색상 변경 */
  filter: drop-shadow(0 0px 30px rgba(172, 184, 204, 405));
}

.detail-and-bar {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* 수정된 부분 */
  justify-content: center;
  width: 60%;
  margin-left: 30px;
}

.progress-bar {
  /* filter: drop-shadow(0 11px 6px rgba(172, 184, 204, 0.45)); */
  height: 10px;
  width: 90%;
  background-color: #d0d8e6;
  display: inline-block;
  border-radius: 10px;
  margin-bottom: 70px;
}

.progress {
  height: inherit;
  background-color: #a3b3ce;
  border-radius: 10px;
  transition: width 0.3s linear;
}

.song-detail {
  height: 30px;
  margin-bottom: 10px;
  margin-top: 5px;
  padding-top: 70px;
  text-align: right;
  font-size: 17px;
}

#song-title {
  margin-right: 300px;
  margin-left: 20px;
  font-weight: 700;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

#song-artist {
  margin-right: 40px;
  margin-left: 20px;
  font-size: 15px;
  color: #858fa5;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>
