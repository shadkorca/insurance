<template>
  <v-container>
    <v-layout text-xs-start wrap top mb-5>
      <v-flex class="justify-start" xs5 offset-xs2>
        <h2 class="headline font-weight-bold">Add new policy</h2>
          <v-form ref="form" lazy-validation>
            <v-text-field
              v-model="name"
              :rules="nameRules"
              label="add new policy"
              required
            ></v-text-field>
          </v-form>
          <v-btn @click="submitForm">Add policy</v-btn>
          <v-btn @click="clearForm">Clear</v-btn>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  // import { Risk } from "../api/risks";
  import { Policy } from "../api/policies";

  export default {
      data: () => ({
          name: '',
          nameRules: [v => !!v || 'Name is required'],
          risks: null,
          posts: null
      }),
      watch: {
          getRisks() {
              this.info = Policy.listPolicies()
              console.log((this.risks))
          }
      },
      mounted: function () {
          this.risks = Policy.listPolicies()
          // console.log((this.risks))
      },
      methods: {
          clearForm() {
              this.$refs.form.reset()
          },
          submitForm() {
              if (this.$refs.form.validate()) {
                  this.getRisks
                  console.log(this.name)
                  // this.info = Policy.list()
                  console.log(this.risks)
                  // пока не работает
                  // this.posts = Risk.create({ name: this.name })
                  // console.log(this.posts)

                  // working
                  // this.info = Policy.createPolicy({ name: this.name, risk_type_id: 1 })
                  // console.log((this.info))
                  // working
                  // this.info = Policy.listPolicies()
                  // console.log(this.info)
              }
          },
      }
  }
</script>

<style>

</style>
