<template>
  <div>
    <GlassCard>
      <SignupForm></SignupForm>
    </GlassCard>
    <YellowCircle />
  </div>
</template>

<script>
import GlassCard from "../atoms/GlassCard.vue";
import YellowCircle from "../atoms/YellowCircle.vue";
import SignupForm from "../organisms/SignupForm.vue";

export default {
  name: "LoginView",
  components: {
    GlassCard,
    SignupForm,
    YellowCircle,
  },
};
</script>

<style></style>
