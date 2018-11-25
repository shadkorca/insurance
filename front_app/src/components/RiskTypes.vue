<template>
  <v-container>
    <v-layout text-xs-center wrap >
      <v-flex class="justify-center" xs6 offset-xs2>
        <h2 class="headline font-weight-bold">Risk Types</h2>
        <v-flex class="xs8 offset-xs2">
          <v-card class="my-4"
                  v-for="(risk, i) in risks"
                  :key="risk.id">
              <v-layout row wrap>
                <v-flex>
                  <v-card>
                    <v-card-actions class="justify-center xs12">
                      <v-btn flat class="justify" @click="submitForm(risk.id)" style="width:70%;">{{ risk.name }}</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                      @click="deleteRisk(risk)">
                          <v-icon dark>remove</v-icon>
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
    name: 'risk_types',
    computed: mapState(['risks']),
    methods: {
        submitForm (id) {
            this.$router.push({
                name: 'risk_details',
                params: {
                    id: id
                }
            })
        },
        deleteRisk(risk) {
            this.$store.dispatch('deleteRisk', risk)
        }
    },
    mounted: function () {
        this.$store.dispatch('getRisks')
    },
  }
</script>

<style>

</style>
