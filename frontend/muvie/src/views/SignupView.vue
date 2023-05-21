<template>
  <div>
    <GlassCard>
      <SignupForm @open-modal="handleModal" />
    </GlassCard>
    <YellowCircle />
    <ModalAtom :isModalOpen="isModalOpen">
      <h2>음악 취향</h2>
      <PreferSelect @close-modal="closeModal" />
    </ModalAtom>
  </div>
</template>

<script>
import GlassCard from "../atoms/GlassCard.vue";
import YellowCircle from "../atoms/YellowCircle.vue";
import SignupForm from "../organisms/SignupForm.vue";
import PreferSelect from "../organisms/PreferSelect.vue";
import ModalAtom from "../atoms/ModalAtom.vue";

export default {
  name: "SignupView",
  components: {
    GlassCard,
    SignupForm,
    YellowCircle,
    ModalAtom,
    PreferSelect,
  },
  data() {
    return {
      isModalOpen: false,
      formData: {},
    };
  },
  methods: {
    handleModal() {
      console.log("모달 오픈");
      this.isModalOpen = true;
    },
    closeModal() {
      console.log("모달 닫기");
      this.isModalOpen = false;
      this.$router.push("/login");
    },
  },
};
</script>

<style></style>
