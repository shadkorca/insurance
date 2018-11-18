<template>
  <v-container>
    <v-layout text-xs-center wrap >
      <v-flex class="justify-center" xs6 offset-xs2>
        <h2 class="headline font-weight-bold">Policies List</h2>
        <v-flex class="xs8 offset-xs2">
          <v-card class="my-4"
                  v-for="(pol, i) in policies"
                  :key="pol.id">
              <v-layout row wrap>
                <v-flex>
                  <v-card>
                    <v-card-actions class="justify-center xs12">
                      <v-btn flat class="justify" @click="submitForm(pol.id)" style="width:70%;">{{ pol.name }}</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                      @click="deletePolicy(pol)">
                          <v-icon flat dark>remove</v-icon>
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-flex>
              </v-layout>
          </v-card>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: mapState(['policies']),
    mounted: function () {
        this.$store.dispatch('getPolicies')
    },
    methods: {
        submitForm (numb) {
            this.$router.push({
                name: 'policy_details',
                params: {
                    id: numb
                }
            })
        },
        deletePolicy(pol) {
            this.$store.dispatch('deletePolicy', pol)
        }
    }
}
</script>

<style>

</style>
