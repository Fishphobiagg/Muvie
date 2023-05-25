<template>
  <div class="flex-center">
    <div class="circular-slider flex-center">
      <ul class="wrapper">
        <li class="slides" style="--img-no: 1">
          <div class="recommend_list">
          <div class="album">{{ components[0].album }}</div>
          <img class="album_cover" :src="components[0].poster" alt="성분 추천 음악" @click="addPlaylistAndPlayMusic(components[0])"/>
            <div class="title">{{ components[0].title }}</div>
            <div class="artist">{{ components[0].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 2">
          <div class="recommend_list">
            <div class="album">{{ components[1].album }}</div>
          <img class="album_cover" :src="components[1].poster" alt="성분 추천 음악" @click="addPlaylistAndPlayMusic(components[1])"/>
            <div class="title">{{ components[1].title }}</div>
            <div class="artist">{{ components[1].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 3">
          <div class="recommend_list">
           <div class="album">{{ components[2].album }}</div>
          <img class="album_cover" :src="components[2].poster" alt="성분 추천 음악" @click="addPlaylistAndPlayMusic(components[2])" />
            <div class="title">{{ components[2].title }}</div>
            <div class="artist">{{ components[2].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 4">
          <div class="recommend_list">
            <div class="album">{{ components[3].album }}</div>            
          <img class="album_cover" :src="components[3].poster" alt="성분 추천 음악" @click="addPlaylistAndPlayMusic(components[3])"/>
            <div class="title">{{ components[3].title }}</div>
            <div class="artist">{{ components[3].artist }}</div>
          </div>
        </li>
        <li class="slides" style="--img-no: 5">
          <div class="recommend_list">
            <div class="album">{{ components[4].album }}</div>
          <img class="album_cover" :src="components[4].poster" alt="성분 추천 음악" @click="addPlaylistAndPlayMusic(components[4])"/>
            <div class="title">{{ components[4].title }}</div>
            <div class="artist">{{ components[4].artist }}</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "CarouselView",
  props: {
    components: Array,
  },
  methods:{
    addPlaylistAndPlayMusic(item) {
      this.$store.dispatch("playMusic", {
        title: item.title,
        artist: item.artist,
      });
    }
  }
};

</script>

<style>

.title{
  font-size: 20px;
  font-weight: bold;
  height: 20px;

}

.artist{
  margin-top: 30px;
}

.album{
  font-size: 13px;
  height: 35px;
  display: flex;
  justify-content: center;
}

.album_cover{
  cursor: pointer;
}

.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

/* .circular-slider {
  position: relative;
  top: 42vh;

  width: calc(50rem / 2);
  height: calc(50rem / 2);

  color: #fff;
  text-align: center;
} */

.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
}

.slides {
  width: 250px;
  list-style: none;
}

.slides img {
  margin: 5px;

  height: 100px;
  width: 100px;
}
</style>
