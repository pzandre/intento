const quillLabels = $("p")
const quillDivs = $("p + div")

let divArray = []

let labelArray = []
for (let j = 1; j < 3; j++) {
  if (quillDivs[j] !== undefined) {
    divArray[j-1] = quillDivs[j]
    divArray[j-1].style.display = "none"
  }
}
for (let i = 5; i < 13; i++) {
  if (quillLabels[i] !== undefined) {
    labelArray[i-5] = quillLabels[i]
    labelArray[i-5].style.display = "none"
  }
}
const br1 = document.createElement("br")
const btn1 = document.createElement("button")
btn1.innerHTML = "Adicionar outro texto-base";
btn1.classList.add("btn")
btn1.classList.add("btn-secondary")
quillLabels[4].appendChild(br1);
quillLabels[4].appendChild(btn1);
btn1.addEventListener("click", function (evt) {
  evt.preventDefault();
  btn1.style.display = "none"
  for (let k = 0; k < 4; k++) {
    labelArray[k].style.display = ""
  }
  divArray[0].style.display = ""
});
const br2 = document.createElement("br")
const btn2 = document.createElement("button")
btn2.innerHTML = "Adicionar outro texto-base";
btn2.classList.add("btn")
btn2.classList.add("btn-secondary")
quillLabels[8].appendChild(br2);
quillLabels[8].appendChild(btn2);
btn2.addEventListener("click", function (evt) {
  evt.preventDefault();
  btn2.style.display = "none"
  for (let k = 4; k < 8; k++) {
    labelArray[k].style.display = ""
  }
  divArray[1].style.display = ""
});
    // console.log(quillLabels[4])
