const buttonHome = document.querySelector('.btn_footer');
buttonHome.addEventListener('click', function() {
    window.location.href = 'speakUs.html'; 
});

const boschItem = document.getElementById("bosch");
boschItem.addEventListener('click', function(){
  window.location.href = './landingpage/carregamento_bosch.html';
});

const dewaltItem = document.getElementById("dewalt");
dewaltItem.addEventListener('click', function(){
  window.location.href = './landingpage/carregamento_dewalt.html';
});

const makitatItem = document.getElementById("makita");
makitatItem.addEventListener('click', function(){
  window.location.href = './landingpage/carregamento_makita.html';
});

const skilltItem = document.getElementById("skil");
skilltItem.addEventListener('click', function(){
  window.location.href = './landingpage/carregamento_skil.html';
});



// // Obter o elemento do ícone com o id "adm_ref"
// const admRef = document.getElementById("adm_ref");
// admRef.addEventListener('click', function() {
//   window.location.href = './adm.html';  // Substitua pelo caminho da página para a qual deseja navegar
// });
