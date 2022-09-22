const questionLabel = document.querySelector(".question");
const choices = document.querySelectorAll(".choices");
const next = document.querySelector(".next");

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

const getQuestion = function () {
  let re = false;
  $.ajax({
    type: "GET",
    url: "https://the-trivia-api.com/api/questions?limit=1",
    success: function (response) {
      const [data] = response;
      const answers = [data["correctAnswer"], ...data["incorrectAnswers"]];
      shuffleArray(answers);
      questionLabel.textContent = data.question;
      for (let i = 0; i < answers.length; i++) {
        choices[i].textContent = answers[i];
        if (answers[i] == data.correctAnswer) {
          var correctChoice = choices[i];
        }
      }

      const eventFunction = function () {
        re = true;
        if (this == correctChoice) {
          this.classList.add("bg-success", "text-white");
        } else {
          this.classList.add("bg-danger", "text-white");
          correctChoice.classList.add("bg-success", "text-white");
        }
      };

      const removeEvent = function () {
        re = false;
        choices.forEach((choice) => {
          choice.removeEventListener("click", eventFunction);
        });
      };

      setInterval(function () {
        if (re == true) {
          removeEvent();
        }
      }, 500);

      choices.forEach((choice) => {
        choice.addEventListener("click", eventFunction);
      });
    },
  });
};

getQuestion();

next.addEventListener("click", function () {
  choices.forEach(function (choice) {
    choice.classList.remove(
      "bg-success",
      "text-white",
      "bg-danger",
      "text-white"
    );
  });
  getQuestion();
});
