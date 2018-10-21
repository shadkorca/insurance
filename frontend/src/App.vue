<template lang="pug">
  #app
    section.container.grid-960
      .columns
        .column.col-6
          header.text-center
            h2 List of risks
          risk-list
        .column.col-6
          header.text-center
            h2 Create risk
          create-risk
</template>

<script>
import CreateRisk from './components/CreateRisk'
import RiskList from './components/RiskList'
export default {
  name: 'app',
  components: {
    'create-risk': CreateRisk,
    'risk-list': RiskList
  }
}
</script>

<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);
  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
