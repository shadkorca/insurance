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
          <v-btn @click="submitForm">
            Add type
          </v-btn>
          <v-btn @click="clearForm">Clear</v-btn>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import { Risk } from "../api/risks"
  import RiskTypes from '@/components/RiskTypes'
  // import router from "../router/index"

  export default {
      name: 'add_risk',
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
          submitForm() {
              if (this.$refs.form.validate()) {
                  console.log(this.name)
                  // this.posts = Risk.create({ name: this.name })

                  // router.push({
                  //   name: 'add_risk',
                  //   params: {
                  //       items: this.name
                  //   }
                  // })

                  // console.log(RiskTypes.items)

                  Risk.create({ name: this.name }).then(data => {
                      this.posts = data
                      console.log(data)
                  })
                  // console.log(this.posts)

                  // working
                  // this.info = Policy.createPolicy({ name: this.name, risk_type_id: 1 })
                  // working
                  // this.info = Policy.listPolicies()
              }
          },
      }
  }
</script>

<style>

</style>
