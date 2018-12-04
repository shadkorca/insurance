<template>
  <v-container>
  <v-content>
    <v-layout text-xs-center wrap >
      <v-flex class="justify-center" xs4 offset-xs2-right>
        <h2 class="headline font-weight-bold">Policy Fields</h2>
        <v-flex class="xs8 offset-xs2">
            <form ref="form" class="my-2" >

            <v-layout row wrap
                v-for="field in policie_fields"
                :key="field.field_type.id">
                <template v-if="field.field_type.field_type_id==1 && field.field_type.enumerate==false">
                    <v-text-field
                        :label="field.field_type.field_name"
                        :data-vv-name="field.field_type.field_name"
                        v-model="field.field_value"
                        type="number"
                        @blur="onBlur(field)"
                        required>
                    </v-text-field>
                </template>

                <template v-else-if="field.field_type.field_type_id==2 && field.field_type.enumerate==false">
                    <v-text-field
                        :label="field.field_type.field_name"
                        :data-vv-name="field.field_type.field_name"
                        v-model="field.field_value"
                        @blur="onBlur(field)"
                        required>
                    </v-text-field>
                </template>

                <template v-else-if="field.field_type.field_type_id==3 && field.field_type.enumerate==false">
                    <v-checkbox
                        :label="field.field_type.field_name"
                        @change="onBlur(field)"
                        v-model="field.field_value">
                    </v-checkbox>
                </template>

                <template v-else-if="field.field_type.field_type_id==4 && field.field_type.enumerate==false">
                    <v-menu
                        :close-on-content-click="false"
                        :nudge-right="40"
                        v-model="menu"
                        lazy
                        transition="scale-transition"
                        offset-y
                        full-width
                        min-width="200px">

                        <v-text-field
                          slot="activator"
                          v-model="date"
                          :label="field.field_type.field_name"
                          append-icon="event"
                          @blur="onBlur(field)"
                          readonly>
                        </v-text-field>
                        <v-date-picker v-model="date" @input="menu=false"></v-date-picker>
                    </v-menu>
                    <v-spacer></v-spacer>
                </template>

                <template v-else-if="field.field_type.enumerate==true">
                    <v-autocomplete
                        :items="variants[field.field_type.id]"
                        :label="field.field_type.field_name"
                        :data-vv-name="field.field_type.field_name"
                        v-model="field.field_value"
                        @blur="onBlur(field)"
                        required
                    ></v-autocomplete>
                </template>

             </v-layout>
            </form>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-content>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import { Field } from "@/api/fields"

export default {
    props: ['id'],
    computed: mapState(['policie_fields']),
    data: () => ({
        date: new Date().toISOString().substr(0, 10),
        current_variant: null,
        menu: false,
        risks: null,
        field_type : {
            '1': 'Number',
            '2': 'Text',
            '3': 'Checkbox',
            '4': 'Date'
        },
        variants: {},
        join_str: '#$'
    }),
    mounted: function () {
        this.$store.dispatch('getPoliciesFields', this.id)
    },
    watch: {
        policie_fields: function() {
            mapState(['policie_fields'])
            for (const [key, value] of Object.entries(this.policie_fields)) {
                if (value['field_type']['enumerate'] === true) {
                    this.variants[value['field_type']['id']] = value['field_type']['enum_text'].split(this.join_str)
                    this.current_variant = this.variants['25'][0]
                }
            }
        }
    },
    methods: {
        onBlur(field) {
            let field_id = field['id']
            let field_value = field['field_value'].toString()
            Field.updateFieldValue(this.id, field_id, {field_value: field_value})
        }
    },
}
</script>

<style>

</style>
