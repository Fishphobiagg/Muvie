<template>
  <div>
    <div v-if="tab == 0">
      <FollowList></FollowList>
    </div>
  </div>
</template>

<script>
import FollowList from "../atoms/FollowList.vue";

export default {
  name: "MypageView",
  data() {
    return {
      tab: 0,
    };
  },
  // computed: {
  //   getId() {
  //     // eslint-disable-next-line no-undef
  //     console.log(this.$store.state.userId);
  //     // eslint-disable-next-line no-undef
  //     return this.$store.state.mypageStore.userId;
  //   },
  // },
  components: {
    FollowList,
  },
  created() {
    const Id = this.$store.state.loginStore.userId;
    console.log(typeof Id);
    this.$store.dispatch("getProfile");
  },
  // created() {
  //   const save = localStorage.getItem("vuex");
  //   console.log(save);
  //   // this.$store.dispatch("getProfile");
  // },
};
</script>

<style></style>
