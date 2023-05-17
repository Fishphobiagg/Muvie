<template>
  <div>
    <div v-if="tab == 0">
      <FollowList
        :fwg="fwg"
        v-for="(fwg, idx) in following"
        :key="idx"
      ></FollowList>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import FollowList from "../atoms/FollowList.vue";

export default {
  name: "MypageView",
  data() {
    return {
      tab: 0,
      profilePhoto: null,
    };
  },
  components: {
    FollowList,
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

<style></style>
