<template>
  <div class="like_item">
    <div class="music-detail">
      <img
        class="album_cover"
        :src="`${fwg.album_cover}`"
        alt="앨범 커버"
      />
      <span class="music_name" @click="navigateToProfile(fwg.id)">{{
        fwg.title
      }} </span>
    </div>
    <!-- <span class="like"></span> -->
    
    <span
      class="like_button"
      @click="followAction(fwg)"
      :class="{ following: fwg.is_followed }"
    > ♡ 
    {{fwg.like_count}}
    </span>
  </div>
</template>

<script>
export default {
  name: "LikeList",
  data() {
    return {
      buttonMsg: "재생",
    };
  },
  methods: {
    navigateToProfile(userId) {
      this.$router.push({ name: "Profile", params: { userId } });
    },
    followAction(fwg) {
      if (fwg.is_followed) {
        // 이미 재생 목록에 있는 경우의 동작
        this.$store.dispatch("unfollow", fwg.id);
      } else {
        // 재생목록에 추가할 경우의 동작
        this.$store.dispatch("follow", fwg.id);
      }
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
  /* background-color: transparent; */
  margin: 0 15px 0 40px;
  font-size: 25px;
  line-height: 80px;
  cursor: pointer;
  display: inline-block;
  vertical-align: middle;
}

.follow-button {
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
</style>
