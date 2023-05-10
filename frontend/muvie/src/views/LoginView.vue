<template>
  <div>
    <GlassCard>
      <LoginForm></LoginForm>
    </GlassCard>
    <YellowCircle />
  </div>
</template>

<script>
import GlassCard from "../atoms/GlassCard.vue";
import YellowCircle from "../atoms/YellowCircle.vue";
import LoginForm from "../organisms/LoginForm.vue";

export default {
  name: "LoginView",
  components: {
    GlassCard,
    LoginForm,
    YellowCircle,
  },
};
</script>

<style></style>
