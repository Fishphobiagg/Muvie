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
  </div>
</template>

<script>
import { mapState } from "vuex";
import FollowList from "../atoms/FollowList.vue";

export default {
  name: "TabContainer",
  components: {
    FollowList,
  },
  props: {
    tab: Number,
  },
  computed: mapState({
    userId: (state) => state.loginStore.userId,
    followers: (state) => state.mypageStore.followers,
    following: (state) => state.mypageStore.following,
  }),
  created() {
    console.log("마이페이지뷰");
    if (this.userId) {
      this.$store.dispatch("getProfile", this.userId);
    }
  },
};
</script>

<style>
.tabvue {
  width: 100%;
}
</style>
