<template>
  <div class="like_item">
    <div class="music-detail">
      <img
        class="album_cover"
        :src="`${fwg.album_cover}`"
        alt="앨범 커버"
      />
      <span class="music_name" @click="playMusic(fwg.id)">{{
        fwg.title
      }} </span>
      <span class="artist_name">{{fwg.artist}}</span>
    </div>
    <!-- <span class="like"></span> -->
    <div class='like'>
      <span class='like_button'>♡</span>
      <span class="like_count">{{fwg.like_count}}</span>
    </div>
      <span class="delete"></span>

  </div>
</template>

<script>
export default {
  name: "PlayList",
  data() {
    return {
      buttonMsg: "재생",
    };
  },
  methods: {
    playMusic(musicId) {
      console.log('음악 재생 요청')
    },
    deletePlaylist(musicId){
      console.log('플레이리스트 삭제 요청')
      this.$store.dispatch('deletePlaylist', musicId)
    }
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
  /* background-color: transparent; */
  margin: 0 15px 0 40px;
  font-size: 25px;
  line-height: 80px;
  cursor: pointer;
  display: inline-block;
  vertical-align: middle;
}

.like-button {
  height: 40px;
  width: 80px;
  font-size: 15px;
  border: none;
  border-radius: 9px;
  cursor: pointer;
  color: white;
}

.following {
  background-color: lightgray !important;
  color: black !important;
}

.delete {
  position: relative;
  width: 20px;
  height: 20px;
}

.delete::before,
.delete::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 2px;
  height: 10px;
  background-color: #000;
  transform: translate(-50%, -50%) rotate(45deg);
}

.delete::after {
  transform: translate(-50%, -50%) rotate(-45deg);
}

</style>
