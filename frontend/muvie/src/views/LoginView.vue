<template>
  <div>
    <GlassCard />
    <YellowCircle />
  </div>
</template>

<script>
import GlassCard from "../atoms/GlassCard.vue";
import YellowCircle from "../atoms/YellowCircle.vue";

export default {
  name: "LoginView",
  components: {
    YellowCircle,
    GlassCard,
  },
};
</script>

<style></style>
