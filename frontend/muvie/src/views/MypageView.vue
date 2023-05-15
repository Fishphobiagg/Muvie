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
  components: {
    FollowList,
  },
};
</script>

<style></style>
