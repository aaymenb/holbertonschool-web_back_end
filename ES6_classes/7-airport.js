export default class Airport {
  constructor(name, code) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
    this._code = code;
  }

  get code() {
    return this._code;
  }

  set code(newcode) {
    if (typeof newcode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this.__code = newcode;
  }

  get name() {
    return this._name;
  }

  set name(newname) {
    if (typeof newname !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newname;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
