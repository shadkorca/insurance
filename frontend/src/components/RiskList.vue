<template lang="pug">
  #app
    .card(v-for="risk in risks")
      .card-header
        button.btn.btn-clear.float-right(@click="deleteRisk(risk)")
        .card-title
        .card-subtitle
      .card-body
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'risk-list',
  computed: mapGetters(['risks']),
  methods: {
    deleteRisk (risk) {
      // Вызываем действие 'deleteRisk' из нашего хранилища, которое
      // попытается удалить заметку из нашех базы данных, отправив запрос к API
      this.$store.dispatch('deleteRisk', risk)
    }
  },
  beforeMount () {
    // Перед тем как загрузить страницу, нам нужно получить список всех
    // имеющихся заметок. Для этого мы вызываем действие 'getRisks' из
    // нашего хранилища
    this.$store.dispatch('getRisks')
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
