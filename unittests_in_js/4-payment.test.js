const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  it('should use a stub for Utils.calculateNumber and spy on console.log', () => {
    // 1. Création du stub : on remplace le comportement de calculateNumber
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    
    // 2. Création du spy sur console.log
    const consoleSpy = sinon.spy(console, 'log');

    // 3. Exécution de la fonction
    sendPaymentRequestToApi(100, 20);

    // 4. Vérifications
    // On vérifie que le stub a été appelé avec les bons arguments
    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    
    // On vérifie que la console affiche bien le résultat forcé par le stub
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

    // 5. Restauration du stub et du spy (crucial !)
    stub.restore();
    consoleSpy.restore();
  });
});
