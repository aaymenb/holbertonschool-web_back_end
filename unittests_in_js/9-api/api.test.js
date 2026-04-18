const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const url = 'http://localhost:7865/';

  it('Vérifie le code de statut (200)', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Vérifie le message de bienvenue', (done) => {
    request.get(url, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  const baseUrl = 'http://localhost:7865/cart/';

  it('Retourne 200 quand :id est un nombre', (done) => {
    request.get(`${baseUrl}12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('Retourne 404 quand :id n\'est pas un nombre (ex: hello)', (done) => {
    request.get(`${baseUrl}hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('Retourne 404 quand :id contient des lettres et chiffres (ex: a12)', (done) => {
    request.get(`${baseUrl}a12`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
