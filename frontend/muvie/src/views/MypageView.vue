<template>
  <div>
    <div v-if="tab == 0">
      <FollowList></FollowList>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
import FollowList from "../atoms/FollowList.vue";

export default {
  name: "MypageView",
  data() {
    return {
      tab: 0,
    };
  },
  components: {
    FollowList,
  },
  computed: mapState({
    userId: (state) => state.loginStore.userId,
  }),
  mounted() {
    console.log(this.userId);
    console.log(axios.defaults);

    if (this.userId) {
      this.$store.dispatch("getProfile", this.userId);
    }
  },
};
</script>

<style></style>
