const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with correct arguments', () => {
    // On place un espion sur la méthode calculateNumber de l'objet Utils
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    // On vérifie si l'espion a été appelé avec les bons arguments
    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    // IMPORTANT : On restaure la fonction originale pour ne pas polluer les autres tests
    spy.restore();
  });
});
