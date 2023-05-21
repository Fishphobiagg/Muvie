<template>
  <div>
    <GlassCard>
      <SignupForm @open-modal="handleModal" />
    </GlassCard>
    <YellowCircle />
    <ModalAtom :isModalOpen="isModalOpen" @close-modal="closeModal">
      <h2>모달 내용</h2>
      <p>취향 선택</p>
      <button @click="confirmModal">확인</button>
      <button @click="closeModal">지금 안하기</button>
    </ModalAtom>
  </div>
</template>

<script>
import GlassCard from "../atoms/GlassCard.vue";
import YellowCircle from "../atoms/YellowCircle.vue";
import SignupForm from "../organisms/SignupForm.vue";
import ModalAtom from "../atoms/ModalAtom.vue";

export default {
  name: "SignupView",
  components: {
    GlassCard,
    SignupForm,
    YellowCircle,
    ModalAtom,
  },
  data() {
    return {
      isModalOpen: false,
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
    },
    confirmModal() {
      // 확인 버튼 클릭에 대한 로직을 처리합니다.
      console.log("확인 버튼 클릭");
    },
  },
};
</script>

<style></style>
