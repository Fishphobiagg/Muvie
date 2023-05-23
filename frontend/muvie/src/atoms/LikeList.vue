<template>
  <div
    class="like_item"
    @mouseover="showButtons = true"
    @mouseleave="showButtons = false"
  >
    <div class="music-detail">
      <img
        class="album_cover"
        :src="fwg.album_cover"
        alt="앨범 커버"
        :style="{ opacity: showButtons ? '0.8' : '1' }"
      />
      <div class="music_info">
        <span class="music_name" @click="addPlaylist(fwg)">{{
          fwg.title
        }}</span>
      </div>
      <span class="artist_name">{{ fwg.artist }}</span>
    </div>
    <span
      class="play_button"
      @click="addPlaylist(fwg)"
      :style="{
        color: showButtons ? '#BDC3C7' : '#BDC3C7',
        marginRight: showButtons ? '5px' : '5px',
      }"
      v-if="showButtons"
    >
      <i class="fas fa-play"></i>
    </span>
    <span
      class="like_button"
      @click="unlike(fwg)"
      :style="{
        color: fwg.isLiked ? '#BDC3C7' : '#BDC3C7',
        marginRight: showButtons ? '5px' : '5px',
      }"
      v-if="showButtons"
    >
      <i class="fas" :class="fwg.isLiked ? 'fa fa-heart' : 'fa fa-heart-o'"></i>
    </span>
    <p class="like_count" v-if="showButtons">{{ fwg.like_count }}</p>
  </div>
</template>

<script>
export default {
  name: "LikeList",
  data() {
    return {
      showButtons: false,
    };
  },
  methods: {
    addPlaylist(fwg) {
      this.$store.dispatch("addPlaylist", fwg.id);
    },
    unlike(fwg) {
      this.$store.dispatch("unlike", fwg.id);
    },
    play(fwg) {
      this.$store.dispatch("addPlaylist", fwg.id);
      // 음악 재생 api 추가
    },
  },
  props: {
    fwg: Object,
  },
};
</script>

<style>
.like_item {
  width: 1000px;
  height: 80px;
  margin: 5px auto;
  padding: 10px 60px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.music-detail {
  height: 80px;
  display: flex;
  align-items: center;
}

.album_cover {
  width: 66px;
  height: 66px;
  background-color: white;
  border-radius: 5px;
  overflow: hidden;
  object-fit: cover;
}

.music_name {
  text-decoration: none;
  border: none;
  margin: 0 15px 0 40px;
  font-size: 25px;
  line-height: 80px;
  cursor: pointer;
  display: inline-block;
  vertical-align: middle;
}

.like_button {
  font-size: 25px;
  cursor: pointer;
  margin-right: 10px;
}

.play_button {
  font-size: 18px;
  cursor: pointer;
  margin-right: 10px;
}

.play_button i {
  display: inline-block;
  font-size: 18px;
}
</style>
