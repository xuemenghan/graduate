
import Vue from 'vue'
import Cookies from 'js-cookie'

const state = {
  biz: {     // 业务列表
    list: [],
    selected: parseInt(Cookies.get('bk_biz_id')) || 2
  },
  isLoadActiving: true
}

const getters = {
  bkBizId: state => state.biz.selected,
  bkBizList: state => state.biz.list
}

const actions = {
  setBizSelectedId ({commit, state}, bizId) {
    console.log(bizId)
    state.biz.selected = bizId
    Cookies.set('bk_biz_id', bizId, { expires: 30, path: '' })
    state.isLoadActiving = false
    state.isLoadActiving = true
  }
}

const mutations = {}

export default {
  state,
  getters,
  actions,
  mutations
}
