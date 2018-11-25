<template>
  <v-container>
    <v-layout text-xs-center wrap >
      <v-flex class="justify-center" xs6 offset-xs2>
        <h2 class="headline font-weight-bold">Policies List</h2>
        <v-flex class="xs8 offset-xs2">
          <v-card class="my-4"
                  v-for="(policy, i) in policies"
                  :key="policy.id">
              <v-layout row wrap>
                <v-flex>
                  <v-card>
                    <v-card-actions class="justify-center xs12">
                      <v-btn flat class="justify" @click="submitForm(policy.risk_type_id)" style="width:70%;">{{ policy.name }}</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                        @click="deletePolicy(policy)">
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
        submitForm (id) {
            this.$router.push({
                name: 'policy_details',
                params: {
                    id: id
                }
            })
        },
        deletePolicy(policy) {
            this.$store.dispatch('deletePolicy', policy)
        }
    }
}
</script>

<style>

</style>
