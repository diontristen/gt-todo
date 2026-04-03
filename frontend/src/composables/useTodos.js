import { ref, computed } from 'vue'

const todos = ref([])
const loading = ref(false)
const error = ref(null)

const todosByStatus = computed(() => {
  const grouped = { backlog: [], todo: [], in_progress: [], done: [] }
  for (const todo of todos.value) {
    if (grouped[todo.status]) {
      grouped[todo.status].push(todo)
    }
  }
  return grouped
})

export function useTodos() {
  async function fetchTodos() {
    loading.value = true
    error.value = null
    try {
      const res = await fetch('/api/todos')
      if (!res.ok) throw new Error(`Failed to fetch todos: ${res.status}`)
      todos.value = await res.json()
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  async function createTodo(data) {
    error.value = null
    try {
      const res = await fetch('/api/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
      if (!res.ok) throw new Error(`Failed to create todo: ${res.status}`)
      const created = await res.json()
      await fetchTodos()
      return created
    } catch (err) {
      error.value = err.message
    }
  }

  async function updateTodo(id, data) {
    error.value = null
    try {
      const res = await fetch(`/api/todos/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
      if (!res.ok) throw new Error(`Failed to update todo: ${res.status}`)
      const updated = await res.json()
      await fetchTodos()
      return updated
    } catch (err) {
      error.value = err.message
    }
  }

  async function deleteTodo(id) {
    error.value = null
    try {
      const res = await fetch(`/api/todos/${id}`, { method: 'DELETE' })
      if (!res.ok) throw new Error(`Failed to delete todo: ${res.status}`)
      await fetchTodos()
    } catch (err) {
      error.value = err.message
    }
  }

  return {
    todos,
    loading,
    error,
    todosByStatus,
    fetchTodos,
    createTodo,
    updateTodo,
    deleteTodo,
  }
}
