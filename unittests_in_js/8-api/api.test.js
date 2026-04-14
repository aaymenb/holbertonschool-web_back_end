const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const url = 'http://localhost:7865/';

  it('Vérifie que le code de statut est 200', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Vérifie que le message retourné est correct', (done) => {
    request.get(url, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Vérifie que la longueur du contenu est correcte', (done) => {
    request.get(url, (error, response, body) => {
      // "Welcome to the payment system" fait 29 caractères
      expect(response.headers['content-length']).to.equal('29');
      done();
    });
  });
});
