<template>
  <Teleport to="body">
    <div v-if="visible" class="ds-overlay" @click.self="$emit('close')">
      <div class="ds-modal todo-modal" role="dialog" aria-modal="true" aria-labelledby="todo-modal-title">
        <div class="ds-modal__header">
          <h4 id="todo-modal-title">{{ mode === 'create' ? 'New Todo' : 'Edit Todo' }}</h4>
          <button class="ds-modal__close" @click="$emit('close')" aria-label="Close">&times;</button>
        </div>
        <form @submit.prevent="handleSubmit">
          <div class="ds-modal__body">
            <div class="todo-modal__fields">
              <div class="ds-field">
                <label class="ds-label" for="todo-title">Title <span class="todo-modal__required">*</span></label>
                <input
                  id="todo-title"
                  ref="titleInput"
                  v-model="form.title"
                  type="text"
                  class="ds-input"
                  :class="{ 'ds-input--error': errors.title }"
                  placeholder="What needs to be done?"
                />
                <span v-if="errors.title" class="ds-field-error">{{ errors.title }}</span>
              </div>

              <div class="ds-field">
                <label class="ds-label" for="todo-description">Description</label>
                <textarea
                  id="todo-description"
                  v-model="form.description"
                  class="ds-input ds-textarea"
                  placeholder="Add details..."
                  rows="3"
                ></textarea>
              </div>

              <div class="ds-field">
                <label class="ds-label" for="todo-status">Status</label>
                <select id="todo-status" v-model="form.status" class="ds-select">
                  <option value="backlog">Backlog</option>
                  <option value="todo">Todo</option>
                  <option value="in_progress">In Progress</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>
          <div class="ds-modal__footer">
            <button type="button" class="ds-btn ds-btn--ghost" @click="$emit('close')">Cancel</button>
            <button type="submit" class="ds-btn ds-btn--primary">
              {{ mode === 'create' ? 'Create' : 'Save' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
import { ref, reactive, watch, nextTick } from 'vue'

const props = defineProps({
  mode: {
    type: String,
    default: 'create',
    validator: (v) => ['create', 'edit'].includes(v),
  },
  todo: {
    type: Object,
    default: null,
  },
  visible: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['save', 'close'])

const titleInput = ref(null)

const form = reactive({
  title: '',
  description: '',
  status: 'todo',
})

const errors = reactive({
  title: '',
})

function resetForm() {
  if (props.mode === 'edit' && props.todo) {
    form.title = props.todo.title || ''
    form.description = props.todo.description || ''
    form.status = props.todo.status || 'todo'
  } else {
    form.title = ''
    form.description = ''
    form.status = 'todo'
  }
  errors.title = ''
}

function validate() {
  errors.title = ''
  if (!form.title.trim()) {
    errors.title = 'Title is required'
    return false
  }
  return true
}

function handleSubmit() {
  if (!validate()) return
  emit('save', {
    title: form.title.trim(),
    description: form.description.trim() || null,
    status: form.status,
  })
}

watch(
  () => props.visible,
  async (isVisible) => {
    if (isVisible) {
      resetForm()
      await nextTick()
      titleInput.value?.focus()
    }
  },
)
</script>

<style scoped>
.todo-modal__fields {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.todo-modal__required {
  color: var(--color-error);
}
</style>
