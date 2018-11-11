<template>
  <v-app>
    <v-content>
      <v-layout>
        <v-flex column>
            <RiskFields :id="id"></RiskFields>
        </v-flex>
        <v-flex column>
            <AddField :id="id"></AddField>
        </v-flex>
      </v-layout>
    </v-content>
  </v-app>
</template>

<script>
import RiskFields from '@/components/RiskFields'
import AddField from '@/components/AddField'

export default {
    props: ['id'],
    name: 'risk_details',
    components: {
        RiskFields,
        AddField
    },
    mounted: function () {
        console.log('mounted details', this.id)
    },
    data () {
        return {
        }
    }
}
</script>

<style>

</style>
