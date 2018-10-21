<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    .form-group
      .col-3
        label.form-label Type_name
      .col-9
        input.form-input(type="text" v-model="type_name" placeholder="Type risk name...")
    .form-group
      .col-3
        label.form-label Content_type
      .col-9
        input.form-input(v-model="content_type" rows=8 placeholder="Type of your risk...")
    .form-group
      .col-3
      .col-9
        button.btn.btn-primary(type="submit") Create
</template>

<script>
export default {
  name: 'create-risk',
  data () {
    return {
      'type_name': '',
      'content_type': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createRisk()

      // Т.к. мы уже отправили запрос на создание заметки строчкой выше,
      // нам нужно теперь очистить поля type_name и content_type
      this.type_name = ''
      this.content_type = ''

      // preventDefault нужно для того, чтобы страница
      // не перезагружалась после нажатия кнопки submit
      event.preventDefault()
    },
    createRisk () {
      // Вызываем действие 'createRisk' из хранилища, которое
      // отправит запрос на создание новой заметки к нашему API.
      this.$store.dispatch('createRisk', { type_name: this.type_name, content_type: this.content_type })
    }
  }
}
</script>
