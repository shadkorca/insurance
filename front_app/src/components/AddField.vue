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
            <v-autocomplete
                :items="f_types"
                v-model="current_type"
                label="Choose field type"
                required
            ></v-autocomplete>
            <v-checkbox
                v-model="checkbox"
                label="is_enumerated">
            </v-checkbox>
            <template v-if="checkbox==true">
            <v-autocomplete
                :items="enum_variant"
                v-model="current_var"
                label="Choose enumerate type"
                required
            ></v-autocomplete>
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
      props: ['id'],
      data: () => ({
          name: '',
          nameRules: [v => !!v || 'Name is required'],
          info: null,
          posts: null,
          current_type: '',
          f_types: [
            'Number',
            'Text',
            'Checkbox',
            'Date'
          ],
          current_var: '',
          enum_variant: [],
          checkbox: false,
          test: {
              "id": 19,
              "field_name": "Count",
              "enumerate": false,
              "enum_text": null,
              "risk_type_id": 3,
              "field_type_id": 4
          },
      }),

      methods: {
          clearForm() {
              this.$refs.form.reset()
          },
          submitForm() {
              if (this.$refs.form.validate()) {
                  console.log('id->', this.id)
                  // this.posts = Risk.create({ name: this.name })
                  this.posts = Risk.addField(this.id, {
                      field_name: "count",
                      enumerate: false,
                      enum_text: null,
                      risk_type_id: 3,
                      field_type_id: 1,
                      crossdomain: true
                  })
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
