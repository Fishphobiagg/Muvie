<template>
  <div class="login-view">
    <GlassCard class="glasscard">
      <LoginForm></LoginForm>
    </GlassCard>
    <YellowCircle class="yellow-circle" />
    <YellowCircle class="yellow-circle1" />
    <YellowCircle class="yellow-circle2" />
    <YellowCircle class="yellow-circle3" />
    <YellowCircle class="yellow-circle4" />
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

<style>
.login-view {
  width: 100vw;
  height: 100vh;
  background: #eed0b2;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative; /* 부모 컨테이너에 position: relative; 설정 */
  overflow: hidden;
}

.glasscard {
  position: absolute;
  z-index: 100;
}

.yellow-circle {
  position: absolute;
  top: 0px;
  left: 200px;
}

.yellow-circle1 {
  position: absolute;
  bottom: 0px;
  right: 0px;
  width: 500px; /* 크기 조정 */
  height: 500px; /* 크기 조정 */
}

.yellow-circle2 {
  position: absolute;
  top: 50px;
  right: -10px;
  width: 30px;
  transform: rotate(30deg);
  height: 30px;
}

.yellow-circle3 {
  position: absolute;
  bottom: 0;
  left: 0px;
  transform: rotate(25deg);
}

.yellow-circle4 {
  position: absolute;
  top: 300px;
  right: 700px;
  width: 5px !important;
  height: 5px !important;
}

/* .yellow-circle.bottom-left {
  bottom: 20px;
  left: 20px;
} */
</style>
