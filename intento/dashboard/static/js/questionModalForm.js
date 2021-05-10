const alternatives = ['A', 'B', 'C', 'D', 'E'];

$(".previewModal").click(function () {
  let modalBefore = $("#exampleModal").html(); // save modal HTML before modifications
  let questionContent = document.getElementsByClassName('ql-editor'); // gets quilljs input
  for (let i = 0; i < questionContent.length; i++) {
    let paragraph = questionContent.item(i);
    let textfieldId = paragraph.parentElement.id;
    if (alternatives.indexOf(textfieldId.slice(-1)) == -1) {
      document.getElementById('modal-question').innerHTML += '<p class="modal-text-fields">' + paragraph.innerHTML + '<hr>'
    } else {
      questionId = textfieldId.slice(-1)
      formattedQuestion = '<p class="modal-text-fields">' + questionId + ') ' + '</p>' + paragraph.innerHTML
      document.getElementById('modal-question').innerHTML += formattedQuestion;
    }
  }
  $("#exampleModal").on('hidden.bs.modal', function () {
    $(this).html(modalBefore) // reset modal
  })
});