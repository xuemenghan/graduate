/**
 * jQuery extend 方法
 * @type {extend: Function}
 */
let $ = {
  copyIsArray: false,
  toString: Object.prototype.toString,
  hasOwn: Object.prototype.hasOwnProperty,
  class2type: {
    '[object Boolean]': 'boolean',
    '[object Number]': 'number',
    '[object String]': 'string',
    '[object Function]': 'function',
    '[object Array]': 'array',
    '[object Date]': 'date',
    '[object RegExp]': 'regExp',
    '[object Object]': 'object'
  },
  type: function (obj) {
    return obj == null ? String(obj) : this.class2type[this.toString.call(obj)] || 'object'
  },
  isWindow: function (obj) {
    return obj && typeof obj === 'object' && 'setInterval' in obj
  },
  isArray: Array.isArray || function (obj) {
    return this.type(obj) === 'array'
  },
  isPlainObject: function (obj) {
    if (!obj || this.type(obj) !== 'object' || obj.nodeType || this.isWindow(obj)) {
      return false
    }
    if (obj.constructor && !this.hasOwn.call(obj, 'constructor') && !this.hasOwn.call(obj.constructor.prototype, 'isPrototypeOf')) {
      return false
    }
    var key
    for (key in obj) {
    }
    return key === undefined || this.hasOwn.call(obj, key)
  },
  extend: function (deep, target, options) {
    for (let name in options) {
      let src = target[name]
      let copy = options[name]
      let clone
      if (target === copy) { continue }
      if (deep && copy && (this.isPlainObject(copy) || (this.copyIsArray = this.isArray(copy)))) {
        if (this.copyIsArray) {
          this.copyIsArray = false
          clone = src && this.isArray(src) ? src : []
        } else {
          clone = src && this.isPlainObject(src) ? src : {}
        }
        target[name] = this.extend(deep, clone, copy)
      } else if (copy !== undefined) {
        target[name] = copy
      }
    }
    return target
  }
}
export default $
