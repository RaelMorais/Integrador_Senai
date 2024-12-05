const chk = document.getElementById('dark_mode')

chk.addEventListener('change', () => {
  document.body.classList.toggle('dark')
})