<template>
  <div class="ds-card ds-card--interactive todo-card" tabindex="0">
    <div class="ds-card__header todo-card__header">
      <span class="todo-card__title">{{ todo.title }}</span>
      <span :class="['ds-badge', badgeClass]">{{ statusLabel }}</span>
    </div>
    <div class="ds-card__body todo-card__body">
      <p v-if="todo.description" class="todo-card__description">{{ todo.description }}</p>
      <time class="todo-card__date">{{ formattedDate }}</time>
    </div>
    <div class="ds-card__footer todo-card__footer">
      <button class="ds-btn ds-btn--ghost ds-btn--sm" @click.stop="$emit('edit', todo)">Edit</button>
      <button class="ds-btn ds-btn--danger ds-btn--sm" @click.stop="$emit('delete', todo)">Delete</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  todo: {
    type: Object,
    required: true,
  },
})

defineEmits(['edit', 'delete'])

const statusMap = {
  backlog: { label: 'Backlog', class: 'ds-badge' },
  todo: { label: 'Todo', class: 'ds-badge--info' },
  in_progress: { label: 'In Progress', class: 'ds-badge--warning' },
  done: { label: 'Done', class: 'ds-badge--success' },
}

const badgeClass = computed(() => statusMap[props.todo.status]?.class || 'ds-badge')
const statusLabel = computed(() => statusMap[props.todo.status]?.label || props.todo.status)

const formattedDate = computed(() => {
  if (!props.todo.created_at) return ''
  const date = new Date(props.todo.created_at)
  return date.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })
})
</script>

<style scoped>
.todo-card__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--space-2);
}

.todo-card__title {
  font-weight: 600;
  font-size: var(--fs-base);
  color: var(--text-primary);
  flex: 1;
  min-width: 0;
}

.todo-card__description {
  color: var(--text-secondary);
  font-size: var(--fs-sm);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin: 0;
}

.todo-card__date {
  display: block;
  font-size: var(--fs-xs);
  color: var(--text-muted);
  margin-top: var(--space-2);
}

.todo-card__footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-2);
}
</style>
