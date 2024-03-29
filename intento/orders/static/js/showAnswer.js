const labels1 = $('p');
const quillDivs1 = $('p + div');
const revisionCheckBox = document.getElementById('id_revision_approval')
const tagField = document.getElementById('id_tag');
const difficulty = document.getElementById('id_difficulty');
const bloom = document.getElementById('id_bloom_taxonomy');
const questionInfo = document.getElementById('id_question_information');
const correctAnswer = document.getElementById('id_correct_answer');
const createQstBtn = document.getElementById('create-question');
const modalButton = document.getElementById('preview-question1');

const toAnswerButton = document.createElement("button")
toAnswerButton.innerHTML = "Ir para gabarito";
toAnswerButton.classList.add("btn");
toAnswerButton.classList.add("btn-success");
toAnswerButton.classList.add("show-answer");
toAnswerButton.style.marginLeft = '4px';
modalButton.insertAdjacentElement('afterend', toAnswerButton);

for (let i = 31; i < 55; i++) {
  if (labels1[i] !== undefined) {
    labels1[i].style.display = 'none';
  };
}

for (let j = 9; j < 14; j++) {
  if (quillDivs1[j] !== undefined) {
    quillDivs1[j].style.display = 'none';
  };
}

toAnswerButton.addEventListener('click', function (evt) {
  difficulty.style.display = '';
  bloom.style.display = '';
  questionInfo.style.display = '';
  correctAnswer.style.display = '';
  revisionCheckBox.style.display = '';
  tagField.style.display = '';
  createQstBtn.style.visibility = 'visible';
  toAnswerButton.style.display = 'none';

  for (let k = 31; k < 54; k++) {
    if (labels1[k] !== undefined) {
      labels1[k].style.display = ''
    }
  }
  for (let l = 9; l < 14; l++) {
    if (quillDivs1[l] !== undefined) {
      quillDivs1[l].style.display = '';
    };
  };
});
