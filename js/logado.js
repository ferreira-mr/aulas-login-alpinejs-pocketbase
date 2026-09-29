document.addEventListener('alpine:init', () => {
  Alpine.data('paginaLogado', () => ({
    usuario: null,

    init() {
      // Sem login válido, voltamos ao formulário antes de mostrar o conteúdo.
      if (!window.pb.authStore.isValid) {
        window.location.replace('login.html');
        return;
      }

      // O SDK guarda o registro do aluno junto ao token de autenticação.
      this.usuario = window.pb.authStore.record;
    },

    sair() {
      // Limpa o token salvo neste navegador e encerra o fluxo da interface.
      window.pb.authStore.clear();
      window.location.href = 'login.html';
    },
  }));
});