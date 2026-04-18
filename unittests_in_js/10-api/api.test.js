const request = require('request');
const { expect } = require('chai');

describe('Index & Cart pages', () => {
  const url = 'http://localhost:7865/';

  it('GET / returns correct message', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('GET /cart/:id returns 404 for invalid id', (done) => {
    request.get(`${url}cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available Payments', () => {
  it('GET /available_payments returns correct object structure', (done) => {
    request.get('http://localhost:7865/available_payments', (error, response, body) => {
      const expected = {
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      };
      // On parse le body car request retourne une string par défaut
      expect(JSON.parse(body)).to.deep.equal(expected);
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
});

describe('Login', () => {
  it('POST /login returns welcome message', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      json: true,
      body: { userName: 'Betty' }
    };
    request.post(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});
