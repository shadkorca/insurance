<template>
  <v-container>
    <v-layout text-xs-start wrap top mb-5 align-start justify-start>
      <v-flex class="justify-start" xs4 offset-xs2>
        <h2 class="headline font-weight-bold">Add new field</h2>
          <v-form ref="form" lazy-validation>
            <v-text-field
              v-model="name"
              :rules="nameRules"
              label="add field name"
              required
            ></v-text-field>
            <v-select
                :items="items"
                label="Choose field type"
                required
            ></v-select>
            <v-checkbox
              v-model="checkbox"
              label="is_enumerated">
            </v-checkbox>
            <template v-if="checkbox==true">
            <v-select
                :items="items"
                label="Choose enumerate type"
                required
            ></v-select>
            </template>
          </v-form>
          <v-btn @click="submitForm">Add field</v-btn>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import { Risk } from "../api/risks";

  export default {
      data: () => ({
          name: '',
          nameRules: [v => !!v || 'Name is required'],
          info: null,
          posts: null,
          items: [
            'Number',
            'Text',
            'Checkbox',
            'Date'
          ],
          checkbox: false
      }),

      methods: {
          clearForm() {
              this.$refs.form.reset()
          },
          submitForm() {
              if (this.$refs.form.validate()) {
                  console.log(this.name)
                  this.posts = Risk.create({ name: this.name })
                  console.log(this.posts)

                  // working
                  // this.info = Policy.createPolicy({ name: this.name, risk_type_id: 1 })
                  // working
                  // this.info = Policy.listPolicies()
              }
          },
      }
      // mounted: function () {
      //     console.log('mounter in risks type')
      //     this.info = Risk.list()
      //     console.log((this.info))
      // },
  }
</script>

<style>

</style>
