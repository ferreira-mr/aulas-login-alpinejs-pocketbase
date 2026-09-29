document.addEventListener('alpine:init', () => {
  // Alpine.data registra um componente que o HTML encontra por x-data="loginApp".
  Alpine.data('loginApp', () => ({
    email: '',
    senha: '',
    erro: '',
    carregando: false,

    init() {
      // Se o aluno já entrou antes, o SDK ainda pode ter um token válido salvo.
      if (window.pb.authStore.isValid) {
        window.location.replace('logado.html');
      }
    },

    async entrar() {
      this.erro = '';
      this.carregando = true;

      try {
        // Envia as credenciais para a coleção Auth users do PocketBase.
        await window.pb.collection('users').authWithPassword(this.email, this.senha);

        // Depois que o SDK salva o login, abrimos a página do aluno.
        window.location.href = 'logado.html';
      } catch (erro) {
        // Uma mensagem simples evita mostrar detalhes técnicos ao aluno.
        this.erro = 'E-mail ou senha inválidos. Confira também se o PocketBase está rodando.';
      } finally {
        this.carregando = false;
      }
    },
  }));
});