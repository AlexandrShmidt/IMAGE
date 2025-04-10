<template>
    <div class="upload-form">
      <h2>Upload Image</h2>
      <form @submit.prevent="uploadImage">
        <div>
          <label>Title:</label>
          <input v-model="title" required>
        </div>
        <div>
          <label>Description:</label>
          <textarea v-model="description" required></textarea>
        </div>
        <div>
          <label>Image:</label>
          <input type="file" @change="handleFileUpload" accept="image/*" required>
        </div>
        <button type="submit">Upload</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'ImageUpload',
    data() {
      return {
        title: '',
        description: '',
        imageFile: null
      }
    },
    methods: {
      handleFileUpload(event) {
        this.imageFile = event.target.files[0]
      },
      async uploadImage() {
        const reader = new FileReader()
        reader.onload = async (event) => {
          const base64String = event.target.result.split(',')[1]
          try {
            await axios.post('http://localhost:8000/api/images/', {
              title: this.title,
              description: this.description,
              image_base64: base64String
            })
            this.$emit('image-uploaded')
            this.title = ''
            this.description = ''
            this.imageFile = null
          } catch (error) {
            console.error('Error uploading image:', error)
          }
        }
        reader.readAsDataURL(this.imageFile)
      }
    }
  }
  </script>
  
  <style scoped>
  .upload-form {
    margin-bottom: 30px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  form div {
    margin-bottom: 15px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
  input, textarea {
    width: 100%;
    padding: 8px;
  }
  button {
    background-color: #42b983;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
  }
  button:hover {
    background-color: #369f6b;
  }
  </style>