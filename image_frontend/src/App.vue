<template>
  <div id="app">
    <h1>Image Manager</h1>
    <ImageUpload @image-uploaded="fetchImages" />
    <ImageList :images="images" @image-deleted="fetchImages" />
  </div>
</template>

<script>
import ImageUpload from './components/ImageUpload.vue'
import ImageList from './components/ImageList.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    ImageUpload,
    ImageList
  },
  data() {
    return {
      images: []
    }
  },
  created() {
    this.fetchImages()
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get('http://localhost:8000/api/images/')
        this.images = response.data
      } catch (error) {
        console.error('Error fetching images:', error)
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>
