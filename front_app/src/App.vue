<template>
  <v-app>
    <v-toolbar app style="background-color: aqua;">
      <v-toolbar-title class="headline text-uppercase">
        Test Insurance
      </v-toolbar-title>
      <v-toolbar-items class="hidden-sm-and-down text-uppercase">
        <v-btn flat class="font-weight-bold" to="/policies">Policies List</v-btn>
        <v-btn flat class="font-weight-bold" to="/">Policies</v-btn>
        <v-btn flat class="font-weight-bold" to="/risks_detail">Risk Types</v-btn>
      </v-toolbar-items>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <!--<v-layout>-->
        <router-view/>
        <!--<RiskTypes/>-->
        <!--<AddRiskType/>-->
      <!--</v-layout>-->

    </v-content>

  <v-footer dark height="auto">
    <v-card class="flex" flat tile>
      <v-card-actions class="justify-center" style="background-color: #0080ff;">
        &copy;2018 — <strong>Test Insurance</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
  </v-app>
</template>

<script>
import RiskTypes from './components/RiskTypes'
import AddRiskType from './components/AddRiskType'

export default {
  name: 'App',
  components: {
    RiskTypes,
    AddRiskType
  },
  data () {
    return {
      //
    }
  }
}
</script>

<style>

</style>
