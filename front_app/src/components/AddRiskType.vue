<template>
  <v-container>
    <v-layout text-xs-start wrap top mb-5>
      <v-flex class="justify-start" xs4 offset-xs2>
        <h2 class="headline font-weight-bold">Add new risk type</h2>
          <v-form ref="form" lazy-validation>
            <v-text-field
              v-model="name"
              :rules="nameRules"
              label="add new type risk"
              required
            ></v-text-field>
          </v-form>
          <v-btn @click="submitForm">Add type</v-btn>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import { Risk } from "../api/risks"
  import RiskTypes from '@/components/RiskTypes'
  // import router from "../router/index"

  export default {
      name: 'add_risk_type',
      data: () => ({
          name: '',
          nameRules: [v => !!v || 'Name is required'],
          info: null,
          posts: null
      }),

      methods: {
          clearForm() {
              this.$refs.form.reset()
          },
          submitForm(event) {
              if (this.$refs.form.validate()) {
                  this.$store.dispatch('createRisk', { name: this.name })
                  this.clearForm()
                  event.preventDefault()
              }
          },
      }
  }
</script>

<style>

</style>
