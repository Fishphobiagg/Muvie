<template>
  <div class="likes-flex-center">
    <div class="circular-slider flex-center">
      <div class="likes-msg">
        <p class="slider-nickname">
          {{ nickname || "익명의 유저" }}님 <br />취향맞춤음악
        </p>
      </div>
      <div class="wrapper">
        <li class="likes-slides" style="--img-no: 1">
          <img
            class="album_cover"
            :src="likes[0].album_cover"
            alt="좋아요 추천 음악"
            @click="addPlaylistAndPlayMusic(likes[0])"
          />
          <div class="likes-slides-detail">
            <div>{{ likes[0].title }}</div>
            <div>{{ likes[0].artist }}</div>
          </div>
        </li>
        <li class="likes-slides" style="--img-no: 2">
          <img
            class="album_cover"
            :src="likes[1].album_cover"
            alt="좋아요 추천 음악"
            @click="addPlaylistAndPlayMusic(likes[1])"
          />
          <div class="likes-slides-detail">
            <div>{{ likes[1].title }}</div>
            <div>{{ likes[1].artist }}</div>
          </div>
        </li>
        <li class="likes-slides" style="--img-no: 3">
          <img
            class="album_cover"
            :src="likes[2].album_cover"
            alt="좋아요 추천 음악"
            @click="addPlaylistAndPlayMusic(likes[2])"
          />
          <div class="likes-slides-detail">
            <div>{{ likes[2].title }}</div>
            <div>{{ likes[2].artist }}</div>
          </div>
        </li>
        <li class="likes-slides" style="--img-no: 4">
          <img
            class="album_cover"
            :src="likes[3].album_cover"
            alt="좋아요 추천 음악"
            @click="addPlaylistAndPlayMusic(likes[3])"
          />
          <div class="likes-slides-detail">
            <div>{{ likes[3].title }}</div>
            <div>{{ likes[3].artist }}</div>
          </div>
        </li>
        <li class="likes-slides" style="--img-no: 5">
          <img
            class="album_cover"
            :src="likes[4].album_cover"
            alt="좋아요 추천 음악"
            @click="addPlaylistAndPlayMusic(likes[4])"
          />
          <div class="likes-slides-detail">
            <div>{{ likes[4].title }}</div>
            <div>{{ likes[4].artist }}</div>
          </div>
        </li>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LikesView",
  data() {
    return {
      flickingOptions: {
        horizontal: true,
        // circular: true,
        // adaptive: true,
        // threshold: 30,
        // duration: 500,
        // ease: "ease",
        // infinite: true,
        // startIndex: 0,
        // gap: 10,
        // autoResize: true,
        // preventClickOnDrag: true,
      },
    };
  },
  props: {
    likes: Array,
  },
  methods: {
    addPlaylistAndPlayMusic(item) {
      this.$store.dispatch("saveAlbumCover", item.album_cover);
      this.$store.dispatch("playMusic", {
        title: item.title,
        artist: item.artist,
      });
      this.$store.dispatch("addPlaylist", item.id);
    },
  },
};
</script>

<style>
.title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 25px;
}

.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-bottom: 40px;
}

.likes-slides > .album_cover {
  cursor: pointer;
  width: 400px;
  height: 300px;
  border-radius: 10px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.likes-slides-detail {
  width: 400px;
  font-size: 20px;
  margin-top: auto; /* 상단 여백을 자동으로 조정하여 화면 중앙에 위치 */
}

.wrapper {
  display: flex;
  flex-direction: column; /* 컨텐츠를 세로로 정렬 */
  justify-content: center;
  align-items: center;
  height: 400px;
  z-index: 3;
  margin-top: 400px;
  margin-bottom: 700px;
}

.likes-msg {
  width: 350px;
  height: 400px;
  margin-left: 300px;
  margin-top: 100px;
}
.likes-msg > p {
  font-size: 50px;
  line-height: 1.5;
}
.likes-slides {
  list-style: none;
  margin: 10px;
}

.slides img {
  margin: 5px;

  height: 100px;
  width: 100px;
}
</style>
