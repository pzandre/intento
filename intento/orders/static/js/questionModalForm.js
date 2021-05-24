const alternatives = {'A': '&#9398;', 'B': '&#9399', 'C': '&#9400', 'D': '&#9401', 'E': '&#9402'};
const modalBefore = $("#exampleModal").html(); // save modal HTML before modifications

$(".previewModal").click(function () {
  let questionContent = document.getElementsByClassName('ql-editor'); // gets quilljs input
  for (let i = 0; i < questionContent.length; i++) {
    let paragraph = questionContent.item(i);
    let textfieldId = paragraph.parentElement.id;
    if (alternatives[textfieldId.slice(-1)]  == undefined) {
      document.getElementById('modal-question').innerHTML += '<p class="modal-text-fields">' + paragraph.innerHTML + '<hr>'
    } else {
      let questionId = textfieldId.slice(-1)
      let formattedQuestion = '<div id="alternatives"><p class="modal-text-fields">' + alternatives[questionId] + '</p> ' + paragraph.innerHTML + '</div>'
      document.getElementById('modal-question').innerHTML += formattedQuestion;
    }
  }
  $("#exampleModal").on('hidden.bs.modal', function () {
    $(this).html(modalBefore) // reset modal
  })
});