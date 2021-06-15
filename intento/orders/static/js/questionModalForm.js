const alternatives = {'A': '&#9398;', 'B': '&#9399', 'C': '&#9400', 'D': '&#9401', 'E': '&#9402'};
const modalBefore = $("#exampleModal").html(); // save modal HTML before modifications
const biblioRef1 = document.getElementById('id_bibliographic_reference_1');
const biblioRef2 = document.getElementById('id_bibliographic_reference_2');
const biblioRef3 = document.getElementById('id_bibliographic_reference_3');
const refArray = [biblioRef1, biblioRef2, biblioRef3];

const questionArray = [
                       // Had to hardcode the question inputs, since they have the same class names as Answer inputs
                       'quill-id_base_text_1', 'quill-id_base_text_2', 'quill-id_base_text_3',
                       'quill-id_question_statement', 'quill-id_answer_A', 'quill-id_answer_B',
                       'quill-id_answer_C', 'quill-id_answer_D', 'quill-id_answer_E'
                      ];

let editorArray1 = [];
questionArray.forEach(function (value) {
  editorArray1.push(document.getElementById(value));    // Save Inputs DOM info on the array
});

let qlArray = [];

$(".previewModal").click(function () {
  editorArray1.forEach(value => qlArray.push(value.getElementsByClassName('ql-editor')[0].innerHTML));  // gets quilljs input inner HTML
  for (let i = 0; i < qlArray.length; i++) {
    let paragraph = qlArray[i];
    let textfieldId = '';
    if (i > 3) {
      textfieldId = editorArray1[i].outerHTML.split('div id="quill-id_answer_')[1].split('"')[0];
      // Get last digit of question array fields (for question alternatives will be A, B, C, D and E)
    }
    if (alternatives[textfieldId] == undefined) {
      if (i < refArray.length && refArray[i] !== undefined) {
        document.getElementById('modal-question').innerHTML += '<p class="modal-text-fields">' + paragraph + '</p><p style="text-align: end;"><em>' + refArray[i].value + '</em></p></br>';
      } else {
        document.getElementById('modal-question').innerHTML += '<p class="modal-text-fields">' + paragraph;
      }
    } else {
      paragraph = paragraph.replaceAll('<p>', '<p style="margin-top: -40px; margin-left: 30px; margin-bottom: 30px;">');
      // I'm inserting inline Css momentanely, but it'll be declared a class for this
      // TODO: Declare class and make css style
      document.getElementById('modal-question').innerHTML += '<div id="alternatives"><p class="modal-text-fields">'
      + alternatives[textfieldId] + '</p>' + paragraph;
    }
  }
  $("#exampleModal").on('hidden.bs.modal', function () {
    $(this).html(modalBefore); // reset modal
    qlArray = [];              // reset array
  });
});