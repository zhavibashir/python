const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnsOpenModal = document.querySelectorAll(".show-modal");
const btnNewNote = document.querySelector(".add_btn");
const btnSubmit = document.querySelector(".modal-btn");

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

const displayNote = function (result) {
  const html = `<div class="note">
        <h3 class="title">${result.title}</h3>
        <p class="content">${result.content}</p>
        <span class="date">${result.date}</span>
      </div>`;
  $(".container:first").prepend(html);
};

btnNewNote.addEventListener("click", openModal);

btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  // console.log(e.key);

  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});

// add new note functionality
const titleInput = document.querySelector(".title-input");
const contentInput = document.querySelector(".content-input");
$(btnSubmit).click(function (e) {
  console.log("clicked");
  e.preventDefault();
  if (titleInput.value !== "" && contentInput.value !== "") {
    $.ajax({
      data: { title: titleInput.value, content: contentInput.value },
      type: "POST",
      url: "add/",
      success: function (result) {
        displayNote(result);
        closeModal();
      },
    });
  }
});

// search functionality
$(".search-input").keyup(function () {
  const text = $(".search-input").val();
  $.ajax({
    type: "POST",
    data: { title: text },
    url: "search/",
    success: function (results) {
      console.log(results);
      $(".container").html("");
      results.notes.reverse();
      results.notes.forEach((result) => {
        console.log(typeof result.date);
        displayNote(result);
      });
    },
  });
});

// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }
// const csrftoken = getCookie("csrftoken");
// console.log(csrftoken);
