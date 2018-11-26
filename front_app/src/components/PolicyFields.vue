<template>
  <v-container>
  <v-content>
    <v-layout text-xs-center wrap >
      <v-flex class="justify-center" xs4 offset-xs2-right>
        <h2 class="headline font-weight-bold">Policy Fields</h2>
        <v-flex class="xs8 offset-xs2">
            <form ref="form" class="my-2" >

            <v-layout row wrap
                v-for="field in fields"
                :key="field.id">
                <template v-if="field.field_type_id==1 && field.enumerate==false">
                    <v-text-field
                        :label="field.field_name"
                        :data-vv-name="field.field_name"
                        type="number"
                        required>
                    </v-text-field>
                </template>

                <template v-else-if="field.field_type_id==2 && field.enumerate==false">
                    <v-text-field
                        :label="field.field_name"
                        :data-vv-name="field.field_name"
                        required>
                    </v-text-field>
                </template>

                <template v-else-if="field.field_type_id==3 && field.enumerate==false">
                    <v-checkbox
                      :label="field.field_name">
                    </v-checkbox>
                </template>

                <template v-else-if="field.field_type_id==4 && field.enumerate==false">
                    <v-menu
                        :close-on-content-click="false"
                        v-model="menu"
                        :nudge-right="40"
                        lazy
                        transition="scale-transition"
                        offset-y
                        full-width
                        min-width="200px">

                        <v-text-field
                          slot="activator"
                          v-model="date"
                          :label="field.field_name"
                          append-icon="event"
                          readonly>
                        </v-text-field>
                        <v-date-picker v-model="date" @input="menu=false"></v-date-picker>
                    </v-menu>
                    <v-spacer></v-spacer>
                </template>

                <template v-else-if="field.enumerate==true">
                    <v-autocomplete
                        :items="variants[field.id]"
                        :label="field.field_name"
                        :data-vv-name="field.field_name"
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

export default {
    props: ['id'],
    computed: mapState(['fields']),
    mounted: function () {
        this.$store.dispatch('getFields', this.id)
    },
    updated() {
        mapState(['fields']);
        for (const [key, value] of Object.entries(this.fields)) {
                if (value['enumerate'] === true) {
                    this.variants[value['id']]=value['enum_text'].split(this.join_str)
                }
            }
    },
    data: () => ({
        date: new Date().toISOString().substr(0, 10),
        menu: false,
        risks: null,
        field_type : {
            '1': 'Number',
            '2': 'Text',
            '3': 'Checkbox',
            '4': 'Date'
        },
        variants: {},
        join_str: '#$',
    }),
    methods: {
        deleteRisk(field_id) {
            this.$store.dispatch('deleteField', [this.id, field_id])
        }
    },
}
</script>

<style>

</style>
