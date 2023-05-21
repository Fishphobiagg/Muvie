<template>
  <div>
    <GlassCard>
      <SignupForm @open-modal="handleModal" />
    </GlassCard>
    <YellowCircle />
    <ModalAtom :isModalOpen="isModalOpen" @close-modal="closeModal">
      <h2>음악 취향</h2>
      <PreferSelect />
      <div class="button-container">
        <button @click="confirmModal">확인</button>
        <button @click="closeModal">지금 안하기</button>
      </div>
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
      isModalOpen: true,
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
      console.log("확인 버튼 클릭");
    },
  },
};
</script>

<style>
.button-container > button {
  margin: 20px;
  padding: 13px 30px;
  background: white;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  text-decoration: none;
  border: none;
  z-index: 500;
  transition: transform 0.3s;
}

.button-container > button:hover {
  color: white;
  background: rgba(218, 138, 114, 0.8);
  letter-spacing: 2px;
  cursor: pointer;
}

.button-container > button:active {
  transform: scale(1.1);
}
</style>
