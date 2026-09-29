// Etapa 4: a segunda página confirma a sessão antes de mostrar o aluno.
function paginaLogada() {
  return {
    usuario: null,
    verificando: true,

    async init() {
      // isValid olha apenas o token salvo e seu prazo de validade.
      if (!window.pb.authStore.isValid) {
        window.location.replace('login.html');
        return;
      }

      try {
        // authRefresh confirma o token com o PocketBase e atualiza o usuário.
        await window.pb.collection('users').authRefresh();
        this.usuario = window.pb.authStore.record;
      } catch (erro) {
        window.pb.authStore.clear();
        window.location.replace('login.html');
      } finally {
        this.verificando = false;
      }
    },

    sair() {
      window.pb.authStore.clear();
      window.location.replace('login.html');
    },
  };
}