<template>
  <div>
    <NavBar />
    <div class="welcome-msg">
      Hey {{ nickname }} <br />
      Welcome Back!
    </div>
    <CircleCarousel />
  </div>
</template>

<script>
import { mapState } from "vuex";
import NavBar from "../organisms/NavBar.vue";
import CircleCarousel from "../organisms/CircleCarousel.vue";

export default {
  name: "MainView",
  data() {
    return {};
  },
  components: {
    NavBar,
    CircleCarousel,
  },
  computed: {
    ...mapState({
      nickname: (state) => state.loginStore.userInfo.nickname,
    }),
  },
  created() {
    this.$store.dispatch("getComponentsRecommends");
    this.$store.dispatch("getUserRecommends");
    this.$store.dispatch("getLikeRecommends");
  },
  methods: {},
};
</script>

<style>
.welcome-msg {
  width: 500px;
  height: 200px;
  font-size: 70px;
  margin-top: 100px;
  margin-left: 80px;
  opacity: 0.7;
  text-align: left;
}
</style>
