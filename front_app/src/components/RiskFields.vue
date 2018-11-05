<template>
  <v-container>
    <v-layout text-xs-center wrap >
      <v-flex class="justify-center" xs8 offset-xs2>
        <h2 class="headline font-weight-bold">Risk Type Fields</h2>
        <v-flex class="xs8 offset-xs2">
            <form ref="form" class="my-2"
                  v-for="rsk in fields"
                  :key="rsk.id">

            <v-layout row wrap>
                <template v-if="rsk.field_type_id==1 && rsk.enumerate==false">
                    <v-text-field
                        :label="rsk.field_name"
                        :data-vv-name="rsk.field_name"
                        required>
                    </v-text-field>
                    <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                    @click="deleteRisk(rsk.id)"><v-icon dark>close</v-icon></v-btn>
                </template>

                <template v-else-if="rsk.field_type_id==2 && rsk.enumerate==false">
                    <v-text-field
                        :label="rsk.field_name"
                        :data-vv-name="rsk.field_name"
                        required>
                    </v-text-field>
                    <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                    @click="deleteRisk(rsk.id)"><v-icon dark>close</v-icon></v-btn>
                </template>

                <template v-else-if="rsk.field_type_id==3 && rsk.enumerate==false">
                    <v-checkbox
                      :label="rsk.field_name">
                    </v-checkbox>
                    <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                    @click="deleteRisk(rsk.id)"><v-icon dark>close</v-icon></v-btn>
                </template>

                <template v-else-if="rsk.field_type_id==4 && rsk.enumerate==false">
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
                          :label="rsk.field_name"
                          append-icon="event"
                          readonly>
                        </v-text-field>
                        <v-date-picker v-model="date" @input="menu=false"></v-date-picker>
                    </v-menu>
                    <v-spacer></v-spacer>
                    <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                    @click="deleteRisk(rsk.id)"><v-icon dark>close</v-icon></v-btn>
                </template>

                <template v-else-if="rsk.enumerate==true">
                    <v-select
                        :items="items"
                        :label="rsk.field_name"
                        :data-vv-name="rsk.field_name"
                        required
                    ></v-select>
                    <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                    @click="deleteRisk(rsk.id)"><v-icon dark>close</v-icon></v-btn>
                </template>

             </v-layout>
            </form>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import { Risk } from "../api/risks"

  export default {
      data: () => ({
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      fields: null,
      risks: null,
      field_type : {
        '1': 'Number',
        '2': 'Text',
        '3': 'Checkbox',
        '4': 'Date'
      },
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4'
      ],

      }),
      methods: {
          submitForm (data) {
              console.log(data)
          },
          deleteRisk(type) {
                console.log(type)
          }
      },
      mounted: function () {
        Risk.details_test('5').then(resp => {
          this.fields = resp.data
        })
      },
      // submit () {
      //   if (this.$refs.form.validate()) {
      //     // Native form submission is not yet supported
      //     axios.post('/api/submit', {
      //       name: this.name,
      //       email: this.email,
      //       select: this.select,
      //       checkbox: this.checkbox
      //     })
      //   }
      // },
  }
</script>

<style>

</style>
