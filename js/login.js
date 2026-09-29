// A mesma função foi usada na etapa 4; aqui apenas saiu do HTML.
function loginComPocketBase() {
  return {
    email: '',
    senha: '',
    erro: '',
    carregando: false,

    init() {
      // A checagem local agiliza a navegação; a outra página consulta o servidor.
      if (window.pb.authStore.isValid) {
        window.location.replace('logado.html');
      }
    },

    async entrar() {
      this.erro = '';
      this.carregando = true;

      try {
        // O PocketBase confere e-mail e senha na coleção Auth users.
        await window.pb.collection('users').authWithPassword(this.email, this.senha);
        window.location.href = 'logado.html';
      } catch (erro) {
        this.erro = 'Não foi possível entrar. Confira os dados e se o PocketBase está rodando.';
      } finally {
        this.carregando = false;
      }
    },
  };
}