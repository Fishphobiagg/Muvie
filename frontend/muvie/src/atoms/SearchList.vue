<template>
  <div class="like_item" @mouseover="showButtons = true" @mouseleave="showButtons = false">
    <div class="music-detail">
      <img class="album_cover" :src="item.album_cover" alt="앨범 커버" :style="{ opacity: showButtons ? '0.8' : '1' }" />
      <div class="music_info">
        <span class="music_name" @click="addPlaylist(item)">{{ truncateTitle(item.title) }}</span>
      </div>
      <span class="artist_name">{{ item.artist }}</span>
    </div>
    <span class="play_button" @click="addPlaylist(item)" :style="{ color: showButtons ? '#BDC3C7' : '#BDC3C7', marginRight: showButtons ? '5px' : '5px' }" v-if="showButtons" >
      <i class="fas fa-play"></i>
    </span>
    <span class="like_button" @click="unlike(item)" :style="{ color: item.isLiked ? '#BDC3C7' : '#BDC3C7', marginRight: showButtons ? '5px' : '5px' }" v-if="showButtons">
      <i class="fas" :class="item.isLiked ? 'fa fa-heart' : 'fa fa-heart-o'"></i>
    </span>
      <p class="like_count" v-if="showButtons">{{item.like_count}}</p>
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
      const maxLength = 42;
      if (title.length > maxLength) {
        return title.substring(0, maxLength) + "...";
      }
      return title;
    }
    },
    addPlaylistAndPlayMusic(item) {
      this.$store.dispatch("addPlaylist", item.id);
      console.log('재생은 아직')
    },
    like(item) {
      this.$store.dispatch("like", item.id)
    },
    unlike(item) {
      this.$store.dispatch("unlike", item.id);
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
  position: relative;
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

.music_info {
  width: 500px;
  display: flex;
  flex-direction: column;
}

.music_name {
  text-decoration: none;
  border: none;
  margin-right: 10px;
  font-size: 20px;
  line-height: 40px;
  cursor: pointer;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  text-align: left;
}

.artist_name {
  font-size: 16px;
  line-height: 30px;
}

.play_button,
.like_button {
  font-size: 16px;
  cursor: pointer;
}

.play_button i,
.like_button i {
  display: inline-block;
  font-size: 18px;
  color: #BDC3C7;
}

.fa-heart {
  color: #BDC3C7;
}

.fa-heart-o {
  color: #BDC3C7;
}

.like_count {
  color: #BDC3C7;
  margin-right: 5px;
}

.user_option {
  display: flex;
  flex-direction: row;
  align-items: center;
  position: absolute; /* Add absolute positioning */
  top: 50%; /* Position it in the middle vertically */
  right: 0; /* Position it at the right edge */
  transform: translateY(-50%); /* Adjust vertical alignment */
}

</style>