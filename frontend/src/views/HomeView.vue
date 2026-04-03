<template>
  <div class="kanban" :class="{ 'kanban--dark': isDark }">
    <header class="kanban__header">
      <h1 class="kanban__title">Todo Board</h1>
      <div class="kanban__actions">
        <button class="ds-btn ds-btn--primary" @click="openCreateModal">+ Add Todo</button>
        <button class="ds-btn ds-btn--ghost" @click="toggleTheme" :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'">
          {{ isDark ? 'Light' : 'Dark' }}
        </button>
      </div>
    </header>

    <div v-if="loading" class="kanban__loading">
      <p>Loading todos...</p>
    </div>

    <div v-else class="kanban__board">
      <KanbanColumn
        v-for="col in columns"
        :key="col.status"
        :title="col.title"
        :status="col.status"
        :todos="todosByStatus[col.status]"
        @edit-todo="openEditModal"
        @delete-todo="confirmDelete"
      />
    </div>

    <TodoModal
      :visible="modalVisible"
      :mode="modalMode"
      :todo="modalTodo"
      @save="handleSave"
      @close="modalVisible = false"
    />

    <Teleport to="body">
      <div v-if="confirmDeleteVisible" class="ds-overlay" @click.self="confirmDeleteVisible = false">
        <div class="ds-modal" role="dialog" aria-modal="true">
          <div class="ds-modal__header">
            <h4>Delete Todo</h4>
            <button class="ds-modal__close" @click="confirmDeleteVisible = false" aria-label="Close">&times;</button>
          </div>
          <div class="ds-modal__body">
            <p>Are you sure you want to delete "{{ todoToDelete?.title }}"?</p>
          </div>
          <div class="ds-modal__footer">
            <button class="ds-btn ds-btn--ghost" @click="confirmDeleteVisible = false">Cancel</button>
            <button class="ds-btn ds-btn--danger" @click="handleDelete">Delete</button>
          </div>
        </div>
      </div>
    </Teleport>

    <div class="ds-toast-container">
      <TransitionGroup name="ds-toast">
        <div
          v-for="toast in toasts"
          :key="toast.id"
          :class="['ds-toast', `ds-toast--${toast.type}`]"
        >
          <span>{{ toast.message }}</span>
          <button class="ds-toast__close" @click="removeToast(toast.id)">&times;</button>
        </div>
      </TransitionGroup>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useTodos } from '../composables/useTodos.js'
import KanbanColumn from '../components/KanbanColumn.vue'
import TodoModal from '../components/TodoModal.vue'

const { loading, error, todosByStatus, fetchTodos, createTodo, updateTodo, deleteTodo } = useTodos()

const columns = [
  { status: 'backlog', title: 'Backlog' },
  { status: 'todo', title: 'Todo' },
  { status: 'in_progress', title: 'In Progress' },
  { status: 'done', title: 'Done' },
]

const isDark = ref(false)
const modalVisible = ref(false)
const modalMode = ref('create')
const modalTodo = ref(null)
const confirmDeleteVisible = ref(false)
const todoToDelete = ref(null)
const toasts = ref([])
let toastId = 0

function toggleTheme() {
  isDark.value = !isDark.value
  document.documentElement.setAttribute('data-theme', isDark.value ? 'dark' : 'light')
}

function openCreateModal() {
  modalMode.value = 'create'
  modalTodo.value = null
  modalVisible.value = true
}

function openEditModal(todo) {
  modalMode.value = 'edit'
  modalTodo.value = todo
  modalVisible.value = true
}

function confirmDelete(todo) {
  todoToDelete.value = todo
  confirmDeleteVisible.value = true
}

async function handleSave(data) {
  if (modalMode.value === 'create') {
    const result = await createTodo(data)
    if (result) {
      addToast('success', 'Todo created successfully')
    }
  } else if (modalTodo.value) {
    const result = await updateTodo(modalTodo.value.id, data)
    if (result) {
      addToast('success', 'Todo updated successfully')
    }
  }
  if (error.value) {
    addToast('error', error.value)
  }
  modalVisible.value = false
}

async function handleDelete() {
  if (!todoToDelete.value) return
  await deleteTodo(todoToDelete.value.id)
  if (error.value) {
    addToast('error', error.value)
  } else {
    addToast('success', 'Todo deleted successfully')
  }
  confirmDeleteVisible.value = false
  todoToDelete.value = null
}

function addToast(type, message) {
  const id = ++toastId
  toasts.value.push({ id, type, message })
  setTimeout(() => removeToast(id), 3000)
}

function removeToast(id) {
  toasts.value = toasts.value.filter(t => t.id !== id)
}

onMounted(() => {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
  isDark.value = prefersDark
  document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light')
  fetchTodos()
})
</script>

<style scoped>
.kanban {
  min-height: 100vh;
  background: var(--surface-bg);
  color: var(--text-primary);
  font-family: var(--font-sans);
  padding: var(--space-6);
}

.kanban__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-8);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--border-color);
}

.kanban__title {
  font-size: var(--fs-3xl);
  font-weight: 700;
  margin: 0;
}

.kanban__actions {
  display: flex;
  gap: var(--space-3);
  align-items: center;
}

.kanban__loading {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: var(--space-16) 0;
  color: var(--text-secondary);
  font-size: var(--fs-lg);
}

.kanban__board {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-4);
  align-items: start;
}

@media (max-width: 1023px) {
  .kanban__board {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .kanban__board {
    grid-template-columns: 1fr;
  }

  .kanban__header {
    flex-direction: column;
    gap: var(--space-3);
    align-items: stretch;
    text-align: center;
  }

  .kanban__actions {
    justify-content: center;
  }
}
</style>
