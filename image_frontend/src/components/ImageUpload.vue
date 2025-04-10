<template>
  <div class="upload-form">
    <h2>Загрузка изображения</h2>
    <form @submit.prevent="uploadImage">
      <div class="form-group">
        <label>Название:</label>
        <input 
          v-model="title" 
          required
          placeholder="Введите название изображения"
        >
      </div>
      <div class="form-group">
        <label>Описание:</label>
        <textarea 
          v-model="description" 
          required
          placeholder="Добавьте описание изображения"
          rows="4"
        ></textarea>
      </div>
      <div class="form-group">
        <label>Изображение:</label>
        <input 
          type="file" 
          @change="handleFileUpload" 
          accept="image/*" 
          required
          class="file-input"
        >
        <div v-if="imageFile" class="file-info">
          Выбрано: {{ imageFile.name }}
        </div>
      </div>
      <button type="submit" class="submit-btn">Загрузить</button>
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
      if (!this.imageFile) {
        alert('Пожалуйста, выберите изображение')
        return
      }

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
          alert('Изображение успешно загружено!')
        } catch (error) {
          console.error('Ошибка при загрузке изображения:', error)
          alert('Произошла ошибка при загрузке изображения')
        }
      }
      reader.readAsDataURL(this.imageFile)
    }
  }
}
</script>

<style scoped>
.upload-form {
  max-width: 600px;
  margin: 0 auto 40px;
  padding: 25px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background-color: #f9f9f9;
}

h2 {
  margin-top: 0;
  color: #333;
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #444;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

textarea {
  resize: vertical;
}

.file-input {
  padding: 5px;
  border: 1px dashed #ccc;
  border-radius: 4px;
  background: white;
}

.file-info {
  margin-top: 8px;
  font-size: 13px;
  color: #666;
}

.submit-btn {
  display: block;
  width: 100%;
  background-color: #42b983;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #369f6b;
}
</style>