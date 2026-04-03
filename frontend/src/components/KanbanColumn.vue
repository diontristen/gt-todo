<template>
  <div class="kanban-column">
    <div class="kanban-column__header">
      <h3 class="kanban-column__title">{{ title }}</h3>
      <span class="ds-badge ds-badge--primary kanban-column__count">{{ todos.length }}</span>
    </div>
    <div class="kanban-column__list">
      <TodoCard
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @edit="$emit('edit-todo', $event)"
        @delete="$emit('delete-todo', $event)"
      />
      <p v-if="todos.length === 0" class="kanban-column__empty">No items</p>
    </div>
  </div>
</template>

<script setup>
import TodoCard from './TodoCard.vue'

defineProps({
  title: {
    type: String,
    required: true,
  },
  status: {
    type: String,
    required: true,
  },
  todos: {
    type: Array,
    required: true,
  },
})

defineEmits(['edit-todo', 'delete-todo'])
</script>

<style scoped>
.kanban-column {
  background: var(--surface-raised);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: var(--space-4);
  min-width: 280px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.kanban-column__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-4);
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--border-color);
}

.kanban-column__title {
  font-size: var(--fs-sm);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-secondary);
  margin: 0;
}

.kanban-column__count {
  font-size: var(--fs-xs);
}

.kanban-column__list {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  flex: 1;
}

.kanban-column__empty {
  color: var(--text-muted);
  font-size: var(--fs-sm);
  text-align: center;
  padding: var(--space-6) 0;
  margin: 0;
}

@media (max-width: 767px) {
  .kanban-column {
    min-width: 100%;
  }
}
</style>
