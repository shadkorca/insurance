<template>
  <v-app>
    <v-content>
      <v-layout>
        <RiskTypes/>
        <AddRiskType/>
      </v-layout>
    </v-content>
  </v-app>
</template>

<script>
import RiskTypes from '@/components/RiskTypes'
import AddRiskType from '@/components/AddRiskType'

export default {
  name: 'risks',
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
