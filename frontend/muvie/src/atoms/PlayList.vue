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
      class="like_button"
      @click="!fwg.isLiked ? like(fwg) : unlike(fwg)"
      :style="{
        color: fwg.isLiked ? '#BDC3C7' : '#BDC3C7',
        marginRight: showButtons ? '5px' : '5px',
      }"
      v-if="showButtons"
    >
      <i class="fas" :class="fwg.isLiked ? 'fa fa-heart' : 'fa fa-heart-o'">{{fwg.like_count}}</i>
    </span>
    <span class="delete_button" @click="deletePlaylist(fwg.id)" v-if="showButtons"
      ><i class="fa fa-trash"></i
    ></span>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "PlayList",
  data() {
    return {
      showButtons: false,
      showLikes: false,
    };
  },
  methods: {
    addPlaylist(fwg) {
      this.$store.dispatch("addPlaylist", fwg.id);
    },
    playMusic(musicId) {
      console.log("음악 재생 요청");
      console.log(musicId);
    },
    deletePlaylist(musicId) {
      console.log("플레이리스트 삭제 요청");
      this.$store.dispatch("deletePlaylist", musicId);
    },
    like(fwg) {
      this.$store.dispatch("like", fwg.id);
    },
    unlike(fwg) {
      this.$store.dispatch("unlike", fwg.id);
    },
  },
  props: {
    fwg: Object,
  },
  computed: {
    ...mapState({
      liked_list: (state) => state.mypageStore.liked_list,
    }),
  },
};
</script>

<style>

.delete_button{
  cursor: pointer;
}
.music-detail {
  width: 800px;
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

.like_button {
  font-size: 16px;
  cursor: pointer;
  letter-spacing: 10px;
}

.like_button i {
  display: inline-block;
  font-size: 18px;
  color: #bdc3c7;
}

.fa-heart {
  color: #bdc3c7;
}

.fa-heart-o {
  color: #bdc3c7;
}

.like_count {
  color: #bdc3c7;
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
.like_count_tooltip {
  position: absolute;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 5px;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 999;
}

.like_count_tooltip span {
  display: block;
  margin-top: 5px;
}
</style>
