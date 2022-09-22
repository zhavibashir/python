"use strict";
const modal = document.querySelector(".mymodal");
const modal2 = document.querySelector(".fmodal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelectorAll(".close-modal");
const btnsOpenModal1 = document.querySelector(".show-modal");
const btnsOpenModal2 = document.querySelector(".showfmodal");

const openModal1 = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};
const openModal2 = function () {
  modal2.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  const modal = this.closest(".mymodal");
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

btnsOpenModal1.addEventListener("click", openModal1);
btnsOpenModal2.addEventListener("click", openModal2);
for (let i = 0; i < btnCloseModal.length; i++)
  btnCloseModal[i].addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  // console.log(e.key);

  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});
