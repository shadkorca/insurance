<template lang="pug">
  #app
    section.container.grid-1280
      .columns
          hello_world
</template>

<script>
import HelloWorld from './components/HelloWorld'
export default {
  name: 'app',
  components: {
    'hello_world': HelloWorld
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
