<template>
  <v-container>
    <v-layout text-xs-start wrap top mb-5>
      <v-flex class="justify-start" xs4 offset-xs2>
        <h2 class="headline font-weight-bold">Add new policy</h2>
          <v-form ref="form" lazy-validation>
            <v-autocomplete
                :items="risks"
                v-model="current_risk"
                item-text="name"
                label="Choose field type"
                required
            ></v-autocomplete>
          </v-form>
          <v-btn @click="submitForm">Add policy</v-btn>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: mapState(['risks']),
    data: () => ({
        name: '',
        nameRules: [v => !!v || 'Name is required'],
        current_risk: ''
    }),
    methods: {
        submitForm() {
            if (this.$refs.form.validate()) {
                let risk_id
                this.risks.forEach( item => {
                    if (item['name'] === this.current_risk) {
                        risk_id = item['id']
                    }
                })
                this.$store.dispatch('createPolicy', { risk_type_id: risk_id })

                // for (let i=0; i<this.risks.length; i++) {
                //     if (this.risks[i] === this.current_risk) {
                //         risk_id = this.risks[i]['id']
                //     }
                // }
            }
        }
    },
    mounted: function () {
        this.$store.dispatch('getRisks')
    },
}
</script>

<style>

</style>
