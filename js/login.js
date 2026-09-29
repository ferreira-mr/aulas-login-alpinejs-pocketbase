// Etapa 3: a mesma página agora consulta o servidor para autenticar.
function loginComPocketBase() {
  return {
    email: '',
    senha: '',
    erro: '',
    carregando: false,

    async entrar() {
      this.erro = '';
      this.carregando = true;

      try {
        // O PocketBase confere as credenciais na coleção Auth users.
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