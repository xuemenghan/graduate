let zm = {
  _URL: '',
  storageStr: '',
  storage: window.localStorage,
  _DOMAINNAME: '',
  /*
   * 功能：设置本地存储
   * 参数：option：类型-Object， func：回调函数
   */
  setItem (option, func) {
    for (let c in option) {
      this.storage.setItem(this.storageStr + c, option[c])
    }
    if (func) return func()
  },

  /*
   * 功能：获取本地存储的值
   * 参数：name：存储的key
   */
  getItem (name) {
    return this.storage.getItem(this.storageStr + name)
  },
  /*
   * 功能：获取所有本地存储的值，返回值：Object
   */
  getAllItem () {
    return this.storage.valueOf()
  },

  /*
   * 功能：删除本地存储的 键名为 name的数据
   * 参数：name： 可为字符串、字符串数据
   */
  removeItem (name) {
    let type = typeof name
    if (type === 'object') {
      for (let i = 0; i < name.length; i++) {
        this.storage.removeItem(this.storageStr + name[i])
      }
    } else if (type === 'string') {
      this.storage.removeItem(this.storageStr + name)
    }
  },
  /*
   * 功能：时间戳格式化
   * 参数：nS： 时间戳， f： format-转化格式
   */
  getLocalTime: function (nS, f) {
    let format = 'YYYY-MM-DD hh:mm:ss' // 日期格式，yyyy: 年，m：月，d：天，hh：时，mm：分，ss：秒
    if (f) {
      format = f
    }

    let time
    if (nS) {
      time = new Date(nS * 1000)
    } else {
      time = new Date()
    }
    let y = time.getFullYear()
    let m = time.getMonth() + 1
    let d = time.getDate()
    let h = time.getHours()
    let mm = time.getMinutes()
    let s = time.getSeconds()

    m = m < 10 ? '0' + m : m
    d = d < 10 ? '0' + d : d
    h = h < 10 ? '0' + h : h
    mm = mm < 10 ? '0' + mm : mm
    s = s < 10 ? '0' + s : s

    let fullTime = format.replace('YYYY', y).replace('MM', m).replace('DD', d).replace('hh', h).replace('mm', mm).replace('ss', s)

    return fullTime
  }
}
export default zm
