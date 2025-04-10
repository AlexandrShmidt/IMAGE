<template>
  <div class="image-list">
    <h2>Список изображений</h2>
    <div v-if="images.length === 0">Нет доступных изображений</div>
    <div v-else>
      <div v-for="image in images" :key="image.id" class="image-item">
        <h3>{{ image.title }}</h3>
        <p>{{ image.description }}</p>
        <img :src="'data:image/jpeg;base64,' + image.image_base64" :alt="image.title" style="max-width: 100%;">
        <button @click="confirmDelete(image.id)" class="delete-btn">Удалить</button>
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
    confirmDelete(id) {
      if (confirm('Вы уверены, что хотите удалить это изображение?')) {
        this.deleteImage(id)
      }
    },
    async deleteImage(id) {
      try {
        await axios.delete(`http://localhost:8000/api/images/${id}/`)
        this.$emit('image-deleted')
        alert('Изображение успешно удалено')
      } catch (error) {
        console.error('Ошибка при удалении изображения:', error)
        alert('Не удалось удалить изображение')
      }
    }
  }
}
</script>

<style scoped>
.image-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.image-item {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.image-item h3 {
  margin-top: 0;
  color: #333;
}

.image-item p {
  color: #666;
  margin-bottom: 15px;
}

.delete-btn {
  background-color: #ff4444;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
  font-size: 14px;
  transition: background-color 0.3s;
}

.delete-btn:hover {
  background-color: #cc0000;
}
</style>