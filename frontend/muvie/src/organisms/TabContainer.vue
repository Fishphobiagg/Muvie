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
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
      followers: (state) => state.mypageStore.followers,
      following: (state) => state.mypageStore.following,
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
    }
  },
};
</script>

<style>
.tabvue {
  width: 100%;
}
</style>
