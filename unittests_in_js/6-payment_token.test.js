const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should return a successful response when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        // On appelle done() pour dire à Mocha que le test est fini et réussi
        done();
      })
      .catch((error) => {
        // En cas d'erreur, on passe l'erreur à done pour faire échouer le test
        done(error);
      });
  });
});
