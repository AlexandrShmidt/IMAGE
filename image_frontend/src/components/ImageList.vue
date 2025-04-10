<template>
    <div class="image-list">
      <h2>Image List</h2>
      <div v-if="images.length === 0">No images available</div>
      <div v-else>
        <div v-for="image in images" :key="image.id" class="image-item">
          <h3>{{ image.title }}</h3>
          <p>{{ image.description }}</p>
          <img :src="'data:image/jpeg;base64,' + image.image_base64" :alt="image.title" style="max-width: 100%;">
          <button @click="deleteImage(image.id)" class="delete-btn">Delete</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'ImageList',
    props: {
      images: {
        type: Array,
        required: true
      }
    },
    methods: {
      async deleteImage(id) {
        try {
          await axios.delete(`http://localhost:8000/api/images/${id}/`)
          this.$emit('image-deleted')
        } catch (error) {
          console.error('Error deleting image:', error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .image-item {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  .delete-btn {
    background-color: #ff4444;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
  }
  .delete-btn:hover {
    background-color: #cc0000;
  }
  </style>