<template>
  <v-app>
    <v-content>
      <v-layout>
        <v-flex column>
          <risk_types/>
        </v-flex>
        <v-flex column>
          <add_risk_type/>
        </v-flex>
      </v-layout>
    </v-content>
  </v-app>
</template>

<script>

import risk_types from '@/components/RiskTypes'
import add_risk_type from '@/components/AddRiskType'

export default {
    name: 'risk_page',
    components: {
        risk_types,
        add_risk_type
    }
}

</script>

<style>

</style>
