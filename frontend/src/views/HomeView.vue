<template>
  <div>
    <h1>Todo App</h1>
    <p>Backend status: {{ healthStatus }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const healthStatus = ref('checking...')

onMounted(async () => {
  try {
    const res = await fetch('/api/health')
    const data = await res.json()
    healthStatus.value = data.status
  } catch {
    healthStatus.value = 'unreachable'
  }
})
</script>
