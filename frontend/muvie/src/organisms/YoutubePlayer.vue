<template>
  <div class="player">
    <div>플레이어</div>
  </div>
</template>

<script>

export default {
  name: "YoutubePlayer",
  methods: {
YOUTUBE_URL = `https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=25&key=${process.env.BASE_URL}`;
  }
};
</script>

<style>
.player {
  width: 100%;
  height: 30px;

}
</style>
