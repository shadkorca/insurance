<template>
  <v-app>
    <v-content>
      <v-layout>
        <v-flex column>
          <RiskFields/>
        </v-flex>
        <v-flex column>
          <AddField/>
        </v-flex>
      </v-layout>
    </v-content>
  </v-app>
</template>

<script>
import RiskFields from '@/components/RiskFields'
import AddField from '@/components/AddField'

export default {
  name: 'risks_dateils',
  components: {
    RiskFields,
    AddField
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
