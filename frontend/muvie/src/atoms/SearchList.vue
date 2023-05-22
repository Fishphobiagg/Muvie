<template>
  <div class="like_item" @mouseover="showButtons = true" @mouseleave="showButtons = false">
    <div class="music-detail">
      <img class="album_cover" :src="`${item.album_cover}`" alt="앨범 커버" :style="{ opacity: showButtons ? '0.8' : '1' }"/>
      <div class="music-info">
        <div class="title-wrapper">
          <div class="title-container">
            <span class="music_name">
              {{ truncateTitle(item.title) }}
            </span>
            <span class="artist_name">{{ item.artist }}</span>
              <span class="play_button" v-if="showButtons" @click="playMusic(fwg)"><i class="fas fa-play"></i></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchList",
  data (){
    return{
      showButtons: false,
    }
  },
  props: {
    item: Object,
  },
  methods: {
    truncateTitle(title) {
      const maxLength = 50;
      if (title.length > maxLength) {
        return title.substring(0, maxLength) + "...";
      }
      return title;
    },
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

.music-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-left: 15px;
}

.title-wrapper {
  display: flex;
  align-items: center;
}

.title-container {
  display: flex;
  align-items: center;
}

.music_name {
  text-decoration: none;
  border: none;
  font-size: 16px;
  line-height: 80px;
  cursor: pointer;
  width: 500px; /* Adjust the desired width here */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: start;
}

.artist_name {
  margin-left: 10px;
  font-size: 15px;
  color: gray;
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