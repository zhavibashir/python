var chat = document.getElementById("chat");
chat.scrollTop = chat.scrollHeight - chat.clientHeight;

console.log("hello world");

$(document).ready(function () {
  setInterval(function () {
    $.ajax({
      type: "GET",
      url: "/messages",
      success: function (results) {
        results.messages[0].forEach(function (result) {
          const html = `<div class="messages" id="chat">
          <div class="time">today</div>
          <div class="message sender">${result.text}</div>`;
          $(".messages").prepend(html);
        });

        results.messages[1].forEach(function (result) {
          const html = `<div class="messages" id="chat">
            <div class="time">today</div>
            <div class="message">${result.text}</div>`;
          $(".messages").prepend(html);
        });
      },
    });
  }, 500);
});
