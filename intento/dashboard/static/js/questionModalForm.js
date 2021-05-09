$(function () {
 $(".teste").click(function () {
     let questionForm1 = $('[id^="quill-id"]').each(function (index) {
      let previewQuestion = $(this).html();
      document.getElementById('modal-question').innerHTML = previewQuestion;
     })
 })
});
