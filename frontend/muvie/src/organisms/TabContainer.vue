<template>
  <div class="tabvue">
    <div v-if="tab == 0">
      <FollowList
        :fwg="fwg"
        v-for="(fwg, idx) in following"
        :key="idx"
      ></FollowList>
    </div>
    <div v-if="tab == 1">
      <FollowList
        :fwg="fwg"
        v-for="(fwg, idx) in followers"
        :key="idx"
      ></FollowList>
    </div>
        <div v-if="tab == 2">
      <LikeList
        :fwg="fwg"
        v-for="(fwg, idx) in like_list"
        :key="idx"
      ></LikeList>
    </div>
        <div v-if="tab == 3">
      <PlayList
        :fwg="fwg"
        v-for="(fwg, idx) in play_list"
        :key="idx"
      ></PlayList>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import FollowList from "../atoms/FollowList.vue";
import LikeList from "../atoms/LikeList.vue";
import PlayList from '../atoms/PlayList.vue';

export default {
  name: "TabContainer",
  components: {
    FollowList,
    LikeList,
    PlayList,
  },
  props: {
    tab: Number,
  },
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
      followers: (state) => state.mypageStore.followers,
      following: (state) => state.mypageStore.following,
      like_list: (state) => state.mypageStore.like_list,
      play_list: (state) => state.mypageStore.play_list,
    }),
    paramId() {
      return this.$route.params.userId;
    },
  },
  watch: {
    paramId(newId) {
      if (newId) {
        console.log("워치 파라미터");
        this.$store.dispatch("getProfile", newId);
      }
    },
  },
  created() {
    console.log("마이페이지뷰");
    console.log(this.paramId);
    if (this.paramId) {
      this.$store.dispatch("getProfile", this.paramId);
      this.$store.dispatch("getLikeList");
      this.$store.dispatch("getPlayList");
    }
  },
};
</script>

<style>
.tabvue {
  width: 100%;
}
</style>
