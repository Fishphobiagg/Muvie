<template>
  <div class="modal" v-if="isModalOpen">
    <div class="modal-content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalAtom",
  props: {
    isModalOpen: Boolean,
  },
};
</script>

<style>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 300;
}

.modal-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: white;
  border-radius: 15px;
  padding: 20px;
  width: 60%;
  min-height: 60%;
  overflow: hidden;
}
</style>
