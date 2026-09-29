// Endereço do PocketBase. Usa o host acessado no navegador ou 127.0.0.1 como fallback.
const host = window.location.hostname || '127.0.0.1';
window.pb = new PocketBase(`http://${host}:8090`);