<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/design-system">Design System</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
</script>

<style scoped>
nav {
  display: flex;
  gap: var(--space-4);
  padding: var(--space-3) var(--space-6);
  background: var(--surface-raised);
  border-bottom: 1px solid var(--border-color);
}

nav a {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: var(--fs-sm);
  font-weight: 500;
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-md);
  transition: color var(--transition-fast), background var(--transition-fast);
}

nav a:hover {
  color: var(--text-primary);
  background: var(--color-gray-100);
}

nav a.router-link-exact-active {
  color: var(--color-primary-600);
}
</style>
