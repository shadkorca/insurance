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
                <!--Add text to an input and press enter.-->
            <v-autocomplete
                :items="enum_variant"
                v-model="current_var"
                label="Add text and press Enter"
                @keyup.native.enter="addValue"
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
        field_types: {
          'Number': '1',
          'Text': '2',
          'Checkbox': '3',
          'Date': '4'
        },
        current_var: '',
        enum_variant: [],
        join_str: '#$',
        checkbox: false
    }),

    methods: {
        addValue: function(e){
            this.enum_variant.push(e.target.value)
        },
        clearForm() {
            this.$refs.form.reset()
        },
        submitForm() {
            if (this.$refs.form.validate()) {
                // console.log('id->', this.id)
                // this.posts = Risk.create({ name: this.name })
                // this.posts = Field.addField(this.id, {
                //     field_name: this.name,
                //     enumerate: this.checkbox,
                //     enum_text: this.current_var,
                //     risk_type_id: this.id,
                //     field_type_id: this.field_types[this.current_type]
                // })

                this.$store.dispatch('createField', [{id: this.id}, {
                    field_name: this.name,
                    enumerate: this.checkbox,
                    enum_text: this.enum_variant.join(this.join_str),
                    risk_type_id: parseInt(this.id),
                    field_type_id: this.field_types[this.current_type]
                }])
                this.clearForm()
            }
        },
    }
}
</script>

<style>

</style>
