<template>
  <div class="ds" :class="{ 'ds--dark': isDark }">
    <header class="ds-header">
      <h1>Design System</h1>
      <button class="ds-theme-toggle" @click="toggleTheme" :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'">
        {{ isDark ? '☀️ Light' : '🌙 Dark' }}
      </button>
    </header>

    <!-- Color Palette -->
    <section class="ds-section" id="colors">
      <h2>Color Palette</h2>

      <h3>Primary</h3>
      <div class="ds-swatches">
        <div v-for="shade in [50,100,200,300,400,500,600,700,800,900]" :key="'primary-'+shade" class="ds-swatch" :style="{ background: `var(--color-primary-${shade})` }">
          <span class="ds-swatch__label">{{ shade }}</span>
          <span class="ds-swatch__value">{{ getVar(`--color-primary-${shade}`) }}</span>
        </div>
      </div>

      <h3>Secondary</h3>
      <div class="ds-swatches">
        <div v-for="shade in [50,100,200,300,400,500,600,700,800,900]" :key="'secondary-'+shade" class="ds-swatch" :style="{ background: `var(--color-secondary-${shade})` }">
          <span class="ds-swatch__label">{{ shade }}</span>
          <span class="ds-swatch__value">{{ getVar(`--color-secondary-${shade}`) }}</span>
        </div>
      </div>

      <h3>Accent</h3>
      <div class="ds-swatches">
        <div v-for="shade in [50,100,200,300,400,500,600,700,800,900]" :key="'accent-'+shade" class="ds-swatch" :style="{ background: `var(--color-accent-${shade})` }">
          <span class="ds-swatch__label">{{ shade }}</span>
          <span class="ds-swatch__value">{{ getVar(`--color-accent-${shade}`) }}</span>
        </div>
      </div>

      <h3>Semantic</h3>
      <div class="ds-swatches">
        <div v-for="color in ['success', 'warning', 'error', 'info']" :key="color" class="ds-swatch ds-swatch--wide" :style="{ background: `var(--color-${color})` }">
          <span class="ds-swatch__label">{{ color }}</span>
          <span class="ds-swatch__value">{{ getVar(`--color-${color}`) }}</span>
        </div>
      </div>

      <h3>Neutral Grays</h3>
      <div class="ds-swatches">
        <div v-for="shade in [50,100,200,300,400,500,600,700,800,900]" :key="'gray-'+shade" class="ds-swatch" :style="{ background: `var(--color-gray-${shade})` }">
          <span class="ds-swatch__label">{{ shade }}</span>
          <span class="ds-swatch__value">{{ getVar(`--color-gray-${shade}`) }}</span>
        </div>
      </div>
    </section>

    <!-- Typography -->
    <section class="ds-section" id="typography">
      <h2>Typography</h2>

      <h3>Headings</h3>
      <div class="ds-type-samples">
        <div v-for="level in [1,2,3,4,5,6]" :key="'h'+level" class="ds-type-sample">
          <component :is="'h'+level" class="ds-type-sample__text">Heading {{ level }}</component>
          <code class="ds-type-sample__token">h{{ level }} — {{ headingSizes[level - 1] }}</code>
        </div>
      </div>

      <h3>Body Text</h3>
      <div class="ds-type-samples">
        <p class="ds-body-lg">Body Large — The quick brown fox jumps over the lazy dog.</p>
        <code class="ds-type-sample__token">font-size: var(--fs-lg) / 1.125rem</code>
        <p class="ds-body">Body — The quick brown fox jumps over the lazy dog.</p>
        <code class="ds-type-sample__token">font-size: var(--fs-base) / 1rem</code>
        <p class="ds-body-sm">Body Small — The quick brown fox jumps over the lazy dog.</p>
        <code class="ds-type-sample__token">font-size: var(--fs-sm) / 0.875rem</code>
      </div>

      <h3>Caption &amp; Monospace</h3>
      <div class="ds-type-samples">
        <p class="ds-caption">Caption text — used for labels and metadata</p>
        <code class="ds-type-sample__token">font-size: var(--fs-xs) / 0.75rem</code>
        <p class="ds-mono">const result = await fetchData();</p>
        <code class="ds-type-sample__token">font-family: var(--font-mono)</code>
      </div>

      <h3>Font Weights</h3>
      <div class="ds-type-samples">
        <p v-for="w in [{name:'Light',val:300},{name:'Regular',val:400},{name:'Medium',val:500},{name:'Semibold',val:600},{name:'Bold',val:700}]" :key="w.val" :style="{ fontWeight: w.val }">
          {{ w.name }} ({{ w.val }}) — The quick brown fox
        </p>
      </div>

      <h3>Line Heights</h3>
      <div class="ds-type-samples">
        <div v-for="lh in [{name:'Tight',val:'1.25'},{name:'Normal',val:'1.5'},{name:'Relaxed',val:'1.75'}]" :key="lh.name" class="ds-lh-sample">
          <p :style="{ lineHeight: lh.val }">{{ lh.name }} ({{ lh.val }}) — Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
          <code class="ds-type-sample__token">line-height: {{ lh.val }}</code>
        </div>
      </div>
    </section>

    <!-- Spacing & Layout -->
    <section class="ds-section" id="spacing">
      <h2>Spacing &amp; Layout</h2>

      <h3>Spacing Scale</h3>
      <div class="ds-spacing-scale">
        <div v-for="s in spacingScale" :key="s.name" class="ds-spacing-item">
          <div class="ds-spacing-bar" :style="{ width: s.value }"></div>
          <code>{{ s.name }}: {{ s.value }}</code>
        </div>
      </div>

      <h3>Breakpoints</h3>
      <div class="ds-table-wrap">
        <table class="ds-table">
          <thead><tr><th>Name</th><th>Min Width</th><th>Usage</th></tr></thead>
          <tbody>
            <tr><td>Mobile</td><td>0</td><td>Default styles</td></tr>
            <tr><td>Tablet</td><td>768px</td><td>@media (min-width: 768px)</td></tr>
            <tr><td>Desktop</td><td>1024px</td><td>@media (min-width: 1024px)</td></tr>
            <tr><td>Wide</td><td>1280px</td><td>@media (min-width: 1280px)</td></tr>
          </tbody>
        </table>
      </div>

      <h3>Container Widths</h3>
      <div class="ds-containers">
        <div v-for="c in [{name:'sm', width:'640px'},{name:'md', width:'768px'},{name:'lg', width:'1024px'},{name:'xl', width:'1280px'}]" :key="c.name" class="ds-container-demo">
          <div class="ds-container-bar" :style="{ maxWidth: c.width }">
            <code>container-{{ c.name }}: {{ c.width }}</code>
          </div>
        </div>
      </div>

      <h3>Grid System</h3>
      <div class="ds-grid-demo">
        <div class="ds-grid ds-grid--12">
          <div v-for="i in 12" :key="'g12-'+i" class="ds-grid-cell">{{ i }}</div>
        </div>
        <code class="ds-type-sample__token">12-column grid</code>
      </div>
      <div class="ds-grid-demo">
        <div class="ds-grid ds-grid--3">
          <div class="ds-grid-cell ds-grid-cell--span4">4 cols</div>
          <div class="ds-grid-cell ds-grid-cell--span4">4 cols</div>
          <div class="ds-grid-cell ds-grid-cell--span4">4 cols</div>
        </div>
        <code class="ds-type-sample__token">3-up layout (4 + 4 + 4)</code>
      </div>
    </section>

    <!-- Components -->
    <section class="ds-section" id="components">
      <h2>Components</h2>

      <!-- Buttons -->
      <h3>Buttons</h3>
      <h4>Variants</h4>
      <div class="ds-row">
        <button class="ds-btn ds-btn--primary">Primary</button>
        <button class="ds-btn ds-btn--secondary">Secondary</button>
        <button class="ds-btn ds-btn--outline">Outline</button>
        <button class="ds-btn ds-btn--ghost">Ghost</button>
        <button class="ds-btn ds-btn--danger">Danger</button>
      </div>

      <h4>Sizes</h4>
      <div class="ds-row ds-row--center">
        <button class="ds-btn ds-btn--primary ds-btn--sm">Small</button>
        <button class="ds-btn ds-btn--primary">Medium</button>
        <button class="ds-btn ds-btn--primary ds-btn--lg">Large</button>
      </div>

      <h4>States</h4>
      <div class="ds-row">
        <button class="ds-btn ds-btn--primary">Default</button>
        <button class="ds-btn ds-btn--primary" disabled>Disabled</button>
        <button class="ds-btn ds-btn--primary ds-btn--loading">Loading</button>
      </div>

      <!-- Inputs -->
      <h3>Inputs</h3>
      <div class="ds-form-grid">
        <div class="ds-field">
          <label class="ds-label">Text Input</label>
          <input type="text" class="ds-input" placeholder="Enter text..." v-model="demoText">
        </div>
        <div class="ds-field">
          <label class="ds-label">Disabled</label>
          <input type="text" class="ds-input" placeholder="Disabled" disabled>
        </div>
        <div class="ds-field">
          <label class="ds-label">With Error</label>
          <input type="text" class="ds-input ds-input--error" placeholder="Invalid input" value="bad value">
          <span class="ds-field-error">This field is required</span>
        </div>
        <div class="ds-field">
          <label class="ds-label">Textarea</label>
          <textarea class="ds-input ds-textarea" placeholder="Enter long text..." rows="3"></textarea>
        </div>
      </div>

      <!-- Selects -->
      <h3>Selects</h3>
      <div class="ds-form-grid">
        <div class="ds-field">
          <label class="ds-label">Select</label>
          <select class="ds-select">
            <option value="">Choose an option...</option>
            <option>Option A</option>
            <option>Option B</option>
            <option>Option C</option>
          </select>
        </div>
        <div class="ds-field">
          <label class="ds-label">Disabled Select</label>
          <select class="ds-select" disabled>
            <option>Disabled</option>
          </select>
        </div>
      </div>

      <!-- Checkboxes & Toggles -->
      <h3>Checkboxes &amp; Toggles</h3>
      <div class="ds-row ds-row--wrap">
        <label class="ds-checkbox">
          <input type="checkbox" v-model="demoChecked">
          <span class="ds-checkbox__box"></span>
          <span>Checkbox</span>
        </label>
        <label class="ds-checkbox">
          <input type="checkbox" checked disabled>
          <span class="ds-checkbox__box"></span>
          <span>Disabled checked</span>
        </label>
        <label class="ds-toggle">
          <input type="checkbox" v-model="demoToggle">
          <span class="ds-toggle__track"></span>
          <span>Toggle {{ demoToggle ? 'On' : 'Off' }}</span>
        </label>
      </div>

      <!-- Cards -->
      <h3>Cards</h3>
      <div class="ds-card-grid">
        <div class="ds-card">
          <div class="ds-card__header">Card Title</div>
          <div class="ds-card__body">This is a basic card component with a header and body content.</div>
        </div>
        <div class="ds-card ds-card--bordered">
          <div class="ds-card__header">Bordered Card</div>
          <div class="ds-card__body">A card variant with a border instead of shadow.</div>
          <div class="ds-card__footer">
            <button class="ds-btn ds-btn--ghost ds-btn--sm">Cancel</button>
            <button class="ds-btn ds-btn--primary ds-btn--sm">Confirm</button>
          </div>
        </div>
        <div class="ds-card ds-card--interactive" tabindex="0">
          <div class="ds-card__header">Interactive Card</div>
          <div class="ds-card__body">This card has hover and focus states.</div>
        </div>
      </div>

      <!-- Badges & Tags -->
      <h3>Badges &amp; Tags</h3>
      <div class="ds-row ds-row--wrap">
        <span class="ds-badge">Default</span>
        <span class="ds-badge ds-badge--primary">Primary</span>
        <span class="ds-badge ds-badge--success">Success</span>
        <span class="ds-badge ds-badge--warning">Warning</span>
        <span class="ds-badge ds-badge--error">Error</span>
        <span class="ds-badge ds-badge--info">Info</span>
      </div>
      <div class="ds-row ds-row--wrap" style="margin-top: var(--space-3)">
        <span class="ds-tag">Tag <button class="ds-tag__remove" aria-label="Remove">&times;</button></span>
        <span class="ds-tag ds-tag--primary">Vue <button class="ds-tag__remove" aria-label="Remove">&times;</button></span>
        <span class="ds-tag ds-tag--accent">Design <button class="ds-tag__remove" aria-label="Remove">&times;</button></span>
      </div>

      <!-- Avatars -->
      <h3>Avatars</h3>
      <div class="ds-row ds-row--center">
        <div class="ds-avatar ds-avatar--sm">S</div>
        <div class="ds-avatar">M</div>
        <div class="ds-avatar ds-avatar--lg">L</div>
        <div class="ds-avatar ds-avatar--xl">XL</div>
      </div>

      <!-- Tooltips -->
      <h3>Tooltips</h3>
      <div class="ds-row">
        <span class="ds-tooltip-wrap">
          <button class="ds-btn ds-btn--secondary">Hover me (top)</button>
          <span class="ds-tooltip ds-tooltip--top">Tooltip on top</span>
        </span>
        <span class="ds-tooltip-wrap">
          <button class="ds-btn ds-btn--secondary">Hover me (bottom)</button>
          <span class="ds-tooltip ds-tooltip--bottom">Tooltip on bottom</span>
        </span>
      </div>

      <!-- Modal -->
      <h3>Modal</h3>
      <button class="ds-btn ds-btn--primary" @click="showModal = true">Open Modal</button>
      <Teleport to="body">
        <div v-if="showModal" class="ds-overlay" @click.self="showModal = false">
          <div class="ds-modal" role="dialog" aria-modal="true">
            <div class="ds-modal__header">
              <h4>Modal Title</h4>
              <button class="ds-modal__close" @click="showModal = false" aria-label="Close">&times;</button>
            </div>
            <div class="ds-modal__body">
              <p>This is modal content. Click outside or press the close button to dismiss.</p>
            </div>
            <div class="ds-modal__footer">
              <button class="ds-btn ds-btn--ghost" @click="showModal = false">Cancel</button>
              <button class="ds-btn ds-btn--primary" @click="showModal = false">Confirm</button>
            </div>
          </div>
        </div>
      </Teleport>

      <!-- Dropdown -->
      <h3>Dropdown</h3>
      <div class="ds-dropdown" ref="dropdownRef">
        <button class="ds-btn ds-btn--secondary" @click="showDropdown = !showDropdown">
          Dropdown ▾
        </button>
        <div v-if="showDropdown" class="ds-dropdown__menu">
          <button class="ds-dropdown__item" @click="showDropdown = false">Action One</button>
          <button class="ds-dropdown__item" @click="showDropdown = false">Action Two</button>
          <button class="ds-dropdown__item" @click="showDropdown = false">Action Three</button>
          <hr class="ds-dropdown__divider">
          <button class="ds-dropdown__item ds-dropdown__item--danger" @click="showDropdown = false">Delete</button>
        </div>
      </div>
    </section>

    <!-- Interaction Patterns -->
    <section class="ds-section" id="interactions">
      <h2>Interaction Patterns</h2>

      <h3>Hover States</h3>
      <div class="ds-row">
        <button class="ds-btn ds-btn--primary">Hover me</button>
        <div class="ds-card ds-card--interactive" tabindex="0" style="display:inline-block;padding:var(--space-4)">Hoverable card</div>
      </div>

      <h3>Focus Rings</h3>
      <div class="ds-row">
        <button class="ds-btn ds-btn--outline">Tab to focus</button>
        <input type="text" class="ds-input" placeholder="Focus me" style="width:200px">
      </div>
      <p class="ds-caption">Use Tab to navigate and see focus ring styles.</p>

      <h3>Transitions</h3>
      <div class="ds-row ds-row--center">
        <div class="ds-transition-demo" :class="{ 'ds-transition-demo--active': transitionActive }">
          Animated box
        </div>
        <button class="ds-btn ds-btn--secondary" @click="transitionActive = !transitionActive">Toggle</button>
      </div>

      <h3>Loading Spinner</h3>
      <div class="ds-row ds-row--center">
        <div class="ds-spinner ds-spinner--sm"></div>
        <div class="ds-spinner"></div>
        <div class="ds-spinner ds-spinner--lg"></div>
      </div>

      <h3>Skeleton Screens</h3>
      <div class="ds-card" style="max-width:400px">
        <div class="ds-card__body">
          <div class="ds-skeleton ds-skeleton--circle"></div>
          <div class="ds-skeleton ds-skeleton--title"></div>
          <div class="ds-skeleton ds-skeleton--text"></div>
          <div class="ds-skeleton ds-skeleton--text" style="width:80%"></div>
        </div>
      </div>

      <h3>Toast Notifications</h3>
      <div class="ds-row">
        <button class="ds-btn ds-btn--primary" @click="addToast('info')">Info Toast</button>
        <button class="ds-btn ds-btn--secondary" @click="addToast('success')">Success Toast</button>
        <button class="ds-btn ds-btn--danger" @click="addToast('error')">Error Toast</button>
      </div>
      <Teleport to="body">
        <div class="ds-toast-container">
          <TransitionGroup name="ds-toast">
            <div v-for="toast in toasts" :key="toast.id" :class="['ds-toast', `ds-toast--${toast.type}`]">
              <span>{{ toast.message }}</span>
              <button class="ds-toast__close" @click="removeToast(toast.id)">&times;</button>
            </div>
          </TransitionGroup>
        </div>
      </Teleport>
    </section>

    <!-- Responsive Demo -->
    <section class="ds-section" id="responsive">
      <h2>Responsive</h2>
      <p>Resize the browser to see components adapt at mobile (&lt;768px), tablet (768–1023px), and desktop (1024px+) breakpoints.</p>

      <h3>Responsive Grid</h3>
      <div class="ds-responsive-grid">
        <div class="ds-responsive-cell" v-for="i in 6" :key="'rg-'+i">
          <div class="ds-card">
            <div class="ds-card__body">Item {{ i }}</div>
          </div>
        </div>
      </div>
      <code class="ds-type-sample__token">1 column mobile → 2 columns tablet → 3 columns desktop</code>

      <h3>Responsive Typography</h3>
      <div class="ds-responsive-type">
        <h1>This heading scales with viewport</h1>
        <p>Body text maintains readability at all sizes through responsive font sizing and proper line heights.</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const isDark = ref(false)
const showModal = ref(false)
const showDropdown = ref(false)
const demoText = ref('')
const demoChecked = ref(false)
const demoToggle = ref(true)
const transitionActive = ref(false)
const dropdownRef = ref(null)
const toasts = ref([])
let toastId = 0

const headingSizes = ['2.25rem', '1.875rem', '1.5rem', '1.25rem', '1.125rem', '1rem']

const spacingScale = [
  { name: '--space-1', value: '0.25rem' },
  { name: '--space-2', value: '0.5rem' },
  { name: '--space-3', value: '0.75rem' },
  { name: '--space-4', value: '1rem' },
  { name: '--space-5', value: '1.25rem' },
  { name: '--space-6', value: '1.5rem' },
  { name: '--space-8', value: '2rem' },
  { name: '--space-10', value: '2.5rem' },
  { name: '--space-12', value: '3rem' },
  { name: '--space-16', value: '4rem' },
]

function getVar(name) {
  if (typeof document === 'undefined') return ''
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim()
}

function toggleTheme() {
  isDark.value = !isDark.value
  document.documentElement.setAttribute('data-theme', isDark.value ? 'dark' : 'light')
}

function handleClickOutside(e) {
  if (dropdownRef.value && !dropdownRef.value.contains(e.target)) {
    showDropdown.value = false
  }
}

function addToast(type) {
  const messages = {
    info: 'This is an informational message.',
    success: 'Operation completed successfully!',
    error: 'Something went wrong. Please try again.',
  }
  const id = ++toastId
  toasts.value.push({ id, type, message: messages[type] })
  setTimeout(() => removeToast(id), 3000)
}

function removeToast(id) {
  toasts.value = toasts.value.filter(t => t.id !== id)
}

onMounted(() => {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
  isDark.value = prefersDark
  document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light')
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  document.documentElement.removeAttribute('data-theme')
})
</script>

<style>
/* ============================================
   CSS Custom Properties — Design Tokens
   ============================================ */
:root,
[data-theme="light"] {
  /* Primary — Indigo */
  --color-primary-50: #eef2ff;
  --color-primary-100: #e0e7ff;
  --color-primary-200: #c7d2fe;
  --color-primary-300: #a5b4fc;
  --color-primary-400: #818cf8;
  --color-primary-500: #6366f1;
  --color-primary-600: #4f46e5;
  --color-primary-700: #4338ca;
  --color-primary-800: #3730a3;
  --color-primary-900: #312e81;

  /* Secondary — Teal */
  --color-secondary-50: #f0fdfa;
  --color-secondary-100: #ccfbf1;
  --color-secondary-200: #99f6e4;
  --color-secondary-300: #5eead4;
  --color-secondary-400: #2dd4bf;
  --color-secondary-500: #14b8a6;
  --color-secondary-600: #0d9488;
  --color-secondary-700: #0f766e;
  --color-secondary-800: #115e59;
  --color-secondary-900: #134e4a;

  /* Accent — Amber */
  --color-accent-50: #fffbeb;
  --color-accent-100: #fef3c7;
  --color-accent-200: #fde68a;
  --color-accent-300: #fcd34d;
  --color-accent-400: #fbbf24;
  --color-accent-500: #f59e0b;
  --color-accent-600: #d97706;
  --color-accent-700: #b45309;
  --color-accent-800: #92400e;
  --color-accent-900: #78350f;

  /* Semantic */
  --color-success: #22c55e;
  --color-warning: #f59e0b;
  --color-error: #ef4444;
  --color-info: #3b82f6;

  /* Grays */
  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-200: #e5e7eb;
  --color-gray-300: #d1d5db;
  --color-gray-400: #9ca3af;
  --color-gray-500: #6b7280;
  --color-gray-600: #4b5563;
  --color-gray-700: #374151;
  --color-gray-800: #1f2937;
  --color-gray-900: #111827;

  /* Surface */
  --surface-bg: #ffffff;
  --surface-raised: #ffffff;
  --surface-overlay: #ffffff;
  --text-primary: var(--color-gray-900);
  --text-secondary: var(--color-gray-600);
  --text-muted: var(--color-gray-400);
  --border-color: var(--color-gray-200);
  --border-color-strong: var(--color-gray-300);

  /* Typography */
  --font-sans: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'SF Mono', 'Fira Code', 'Fira Mono', 'Roboto Mono', monospace;
  --fs-xs: 0.75rem;
  --fs-sm: 0.875rem;
  --fs-base: 1rem;
  --fs-lg: 1.125rem;
  --fs-xl: 1.25rem;
  --fs-2xl: 1.5rem;
  --fs-3xl: 1.875rem;
  --fs-4xl: 2.25rem;

  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;

  /* Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease;

  /* Focus */
  --focus-ring: 0 0 0 3px rgba(99, 102, 241, 0.4);
}

[data-theme="dark"] {
  --color-primary-50: #1e1b4b;
  --color-primary-100: #312e81;
  --color-primary-200: #3730a3;
  --color-primary-300: #4338ca;
  --color-primary-400: #4f46e5;
  --color-primary-500: #6366f1;
  --color-primary-600: #818cf8;
  --color-primary-700: #a5b4fc;
  --color-primary-800: #c7d2fe;
  --color-primary-900: #e0e7ff;

  --color-secondary-50: #042f2e;
  --color-secondary-100: #134e4a;
  --color-secondary-200: #115e59;
  --color-secondary-300: #0f766e;
  --color-secondary-400: #0d9488;
  --color-secondary-500: #14b8a6;
  --color-secondary-600: #2dd4bf;
  --color-secondary-700: #5eead4;
  --color-secondary-800: #99f6e4;
  --color-secondary-900: #ccfbf1;

  --color-accent-50: #451a03;
  --color-accent-100: #78350f;
  --color-accent-200: #92400e;
  --color-accent-300: #b45309;
  --color-accent-400: #d97706;
  --color-accent-500: #f59e0b;
  --color-accent-600: #fbbf24;
  --color-accent-700: #fcd34d;
  --color-accent-800: #fde68a;
  --color-accent-900: #fef3c7;

  --color-gray-50: #111827;
  --color-gray-100: #1f2937;
  --color-gray-200: #374151;
  --color-gray-300: #4b5563;
  --color-gray-400: #6b7280;
  --color-gray-500: #9ca3af;
  --color-gray-600: #d1d5db;
  --color-gray-700: #e5e7eb;
  --color-gray-800: #f3f4f6;
  --color-gray-900: #f9fafb;

  --color-success: #4ade80;
  --color-warning: #fbbf24;
  --color-error: #f87171;
  --color-info: #60a5fa;

  --surface-bg: #0f172a;
  --surface-raised: #1e293b;
  --surface-overlay: #1e293b;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --border-color: #334155;
  --border-color-strong: #475569;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -2px rgba(0, 0, 0, 0.3);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -4px rgba(0, 0, 0, 0.3);
  --focus-ring: 0 0 0 3px rgba(99, 102, 241, 0.6);
}

/* ============================================
   Design System Page Styles
   ============================================ */
.ds {
  max-width: 1280px;
  margin: 0 auto;
  padding: var(--space-6);
  background: var(--surface-bg);
  color: var(--text-primary);
  font-family: var(--font-sans);
  font-size: var(--fs-base);
  line-height: 1.5;
  min-height: 100vh;
}

.ds-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-12);
  padding-bottom: var(--space-6);
  border-bottom: 2px solid var(--border-color);
}

.ds-header h1 {
  font-size: var(--fs-4xl);
  font-weight: 700;
  margin: 0;
}

.ds-theme-toggle {
  padding: var(--space-2) var(--space-4);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  background: var(--surface-raised);
  color: var(--text-primary);
  cursor: pointer;
  font-size: var(--fs-sm);
  transition: all var(--transition-base);
}

.ds-theme-toggle:hover {
  border-color: var(--color-primary-500);
  background: var(--color-primary-50);
}

/* Sections */
.ds-section {
  margin-bottom: var(--space-16);
}

.ds-section h2 {
  font-size: var(--fs-3xl);
  font-weight: 700;
  margin: 0 0 var(--space-8);
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--border-color);
}

.ds-section h3 {
  font-size: var(--fs-xl);
  font-weight: 600;
  margin: var(--space-8) 0 var(--space-4);
  color: var(--text-primary);
}

.ds-section h4 {
  font-size: var(--fs-base);
  font-weight: 600;
  margin: var(--space-4) 0 var(--space-3);
  color: var(--text-secondary);
}

/* Color Swatches */
.ds-swatches {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.ds-swatch {
  width: 80px;
  height: 80px;
  border-radius: var(--radius-lg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: var(--fs-xs);
  color: #fff;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
  transition: transform var(--transition-fast);
  position: relative;
}

.ds-swatch:hover {
  transform: scale(1.1);
}

.ds-swatch--wide {
  width: 120px;
}

.ds-swatch__label {
  font-weight: 600;
}

.ds-swatch__value {
  font-size: 0.625rem;
  opacity: 0.9;
  font-family: var(--font-mono);
}

/* Typography */
.ds-type-samples {
  margin-bottom: var(--space-4);
}

.ds-type-sample {
  margin-bottom: var(--space-3);
}

.ds-type-sample__text {
  margin: 0 0 var(--space-1);
}

.ds-type-sample__token {
  display: block;
  font-size: var(--fs-xs);
  color: var(--text-muted);
  font-family: var(--font-mono);
  margin-top: var(--space-1);
  margin-bottom: var(--space-3);
}

.ds-body-lg { font-size: var(--fs-lg); margin: 0 0 var(--space-2); }
.ds-body { font-size: var(--fs-base); margin: 0 0 var(--space-2); }
.ds-body-sm { font-size: var(--fs-sm); margin: 0 0 var(--space-2); }
.ds-caption { font-size: var(--fs-xs); color: var(--text-secondary); margin: 0 0 var(--space-2); }
.ds-mono { font-family: var(--font-mono); font-size: var(--fs-sm); margin: 0 0 var(--space-2); }

.ds-lh-sample {
  margin-bottom: var(--space-4);
  max-width: 600px;
}

/* Spacing */
.ds-spacing-scale {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.ds-spacing-item {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.ds-spacing-bar {
  height: 24px;
  background: var(--color-primary-500);
  border-radius: var(--radius-sm);
  min-width: 4px;
}

.ds-spacing-item code {
  font-size: var(--fs-xs);
  color: var(--text-secondary);
  font-family: var(--font-mono);
  white-space: nowrap;
}

/* Table */
.ds-table-wrap {
  overflow-x: auto;
}

.ds-table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--fs-sm);
}

.ds-table th,
.ds-table td {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  border-bottom: 1px solid var(--border-color);
}

.ds-table th {
  font-weight: 600;
  color: var(--text-secondary);
  font-size: var(--fs-xs);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Containers */
.ds-containers {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.ds-container-bar {
  background: var(--color-primary-100);
  border: 1px solid var(--color-primary-300);
  border-radius: var(--radius-md);
  padding: var(--space-2) var(--space-3);
  width: 100%;
}

.ds-container-bar code {
  font-size: var(--fs-xs);
  color: var(--text-secondary);
}

/* Grid */
.ds-grid-demo {
  margin-bottom: var(--space-4);
}

.ds-grid {
  display: grid;
  gap: var(--space-2);
}

.ds-grid--12 {
  grid-template-columns: repeat(12, 1fr);
}

.ds-grid--3 {
  grid-template-columns: repeat(12, 1fr);
}

.ds-grid-cell {
  background: var(--color-primary-100);
  border: 1px solid var(--color-primary-300);
  border-radius: var(--radius-sm);
  padding: var(--space-2);
  text-align: center;
  font-size: var(--fs-xs);
  color: var(--text-secondary);
}

.ds-grid-cell--span4 {
  grid-column: span 4;
}

/* Shared Row */
.ds-row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  align-items: flex-start;
}

.ds-row--center {
  align-items: center;
}

.ds-row--wrap {
  flex-wrap: wrap;
}

/* ============================================
   Component Styles
   ============================================ */

/* Buttons */
.ds-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-2) var(--space-4);
  font-size: var(--fs-sm);
  font-weight: 500;
  font-family: var(--font-sans);
  border-radius: var(--radius-md);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all var(--transition-fast);
  line-height: 1.5;
  gap: var(--space-2);
}

.ds-btn:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}

.ds-btn--primary {
  background: var(--color-primary-600);
  color: #fff;
}
.ds-btn--primary:hover { background: var(--color-primary-700); }

.ds-btn--secondary {
  background: var(--color-gray-100);
  color: var(--text-primary);
  border-color: var(--border-color);
}
.ds-btn--secondary:hover { background: var(--color-gray-200); }

.ds-btn--outline {
  background: transparent;
  color: var(--color-primary-600);
  border-color: var(--color-primary-600);
}
.ds-btn--outline:hover { background: var(--color-primary-50); }

.ds-btn--ghost {
  background: transparent;
  color: var(--text-secondary);
}
.ds-btn--ghost:hover { background: var(--color-gray-100); color: var(--text-primary); }

.ds-btn--danger {
  background: var(--color-error);
  color: #fff;
}
.ds-btn--danger:hover { opacity: 0.9; }

.ds-btn--sm { padding: var(--space-1) var(--space-3); font-size: var(--fs-xs); }
.ds-btn--lg { padding: var(--space-3) var(--space-6); font-size: var(--fs-lg); }

.ds-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.ds-btn--loading {
  position: relative;
  color: transparent;
  pointer-events: none;
}
.ds-btn--loading::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  border: 2px solid #fff;
  border-top-color: transparent;
  border-radius: 50%;
  animation: ds-spin 0.6s linear infinite;
}

/* Inputs */
.ds-form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}

@media (max-width: 767px) {
  .ds-form-grid {
    grid-template-columns: 1fr;
  }
}

.ds-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.ds-label {
  font-size: var(--fs-sm);
  font-weight: 500;
  color: var(--text-secondary);
}

.ds-input {
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: var(--fs-sm);
  font-family: var(--font-sans);
  background: var(--surface-bg);
  color: var(--text-primary);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.ds-input:focus {
  outline: none;
  border-color: var(--color-primary-500);
  box-shadow: var(--focus-ring);
}

.ds-input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background: var(--color-gray-50);
}

.ds-input--error {
  border-color: var(--color-error);
}
.ds-input--error:focus {
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.3);
}

.ds-field-error {
  font-size: var(--fs-xs);
  color: var(--color-error);
}

.ds-textarea {
  resize: vertical;
}

/* Select */
.ds-select {
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: var(--fs-sm);
  font-family: var(--font-sans);
  background: var(--surface-bg);
  color: var(--text-primary);
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%236b7280' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: var(--space-8);
}

.ds-select:focus {
  outline: none;
  border-color: var(--color-primary-500);
  box-shadow: var(--focus-ring);
}

.ds-select:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Checkbox */
.ds-checkbox {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  cursor: pointer;
  font-size: var(--fs-sm);
}

.ds-checkbox input { position: absolute; opacity: 0; width: 0; height: 0; }

.ds-checkbox__box {
  width: 18px;
  height: 18px;
  border: 2px solid var(--border-color-strong);
  border-radius: var(--radius-sm);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all var(--transition-fast);
  flex-shrink: 0;
}

.ds-checkbox input:checked + .ds-checkbox__box {
  background: var(--color-primary-600);
  border-color: var(--color-primary-600);
}

.ds-checkbox input:checked + .ds-checkbox__box::after {
  content: '';
  width: 5px;
  height: 9px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg) translate(-1px, -1px);
}

.ds-checkbox input:focus-visible + .ds-checkbox__box {
  box-shadow: var(--focus-ring);
}

.ds-checkbox input:disabled + .ds-checkbox__box {
  opacity: 0.5;
}

/* Toggle */
.ds-toggle {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  cursor: pointer;
  font-size: var(--fs-sm);
}

.ds-toggle input { position: absolute; opacity: 0; width: 0; height: 0; }

.ds-toggle__track {
  width: 40px;
  height: 22px;
  background: var(--color-gray-300);
  border-radius: var(--radius-full);
  position: relative;
  transition: background var(--transition-fast);
  flex-shrink: 0;
}

.ds-toggle__track::after {
  content: '';
  width: 18px;
  height: 18px;
  background: #fff;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  left: 2px;
  transition: transform var(--transition-fast);
  box-shadow: var(--shadow-sm);
}

.ds-toggle input:checked + .ds-toggle__track {
  background: var(--color-primary-600);
}

.ds-toggle input:checked + .ds-toggle__track::after {
  transform: translateX(18px);
}

.ds-toggle input:focus-visible + .ds-toggle__track {
  box-shadow: var(--focus-ring);
}

/* Cards */
.ds-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-4);
}

.ds-card {
  background: var(--surface-raised);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.ds-card--bordered {
  box-shadow: none;
  border: 1px solid var(--border-color);
}

.ds-card--interactive {
  cursor: pointer;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}
.ds-card--interactive:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
.ds-card--interactive:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring), var(--shadow-lg);
}

.ds-card__header {
  padding: var(--space-4) var(--space-5);
  font-weight: 600;
  border-bottom: 1px solid var(--border-color);
}

.ds-card__body {
  padding: var(--space-4) var(--space-5);
  color: var(--text-secondary);
  font-size: var(--fs-sm);
}

.ds-card__footer {
  padding: var(--space-3) var(--space-5);
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: flex-end;
  gap: var(--space-2);
}

/* Badges */
.ds-badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-2);
  font-size: var(--fs-xs);
  font-weight: 500;
  border-radius: var(--radius-full);
  background: var(--color-gray-100);
  color: var(--text-secondary);
}

.ds-badge--primary { background: var(--color-primary-100); color: var(--color-primary-700); }
.ds-badge--success { background: #dcfce7; color: #166534; }
.ds-badge--warning { background: #fef3c7; color: #92400e; }
.ds-badge--error { background: #fee2e2; color: #991b1b; }
.ds-badge--info { background: #dbeafe; color: #1e40af; }

[data-theme="dark"] .ds-badge--success { background: #052e16; color: #86efac; }
[data-theme="dark"] .ds-badge--warning { background: #451a03; color: #fde68a; }
[data-theme="dark"] .ds-badge--error { background: #450a0a; color: #fca5a5; }
[data-theme="dark"] .ds-badge--info { background: #172554; color: #93c5fd; }

/* Tags */
.ds-tag {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-1) var(--space-3);
  font-size: var(--fs-xs);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  background: var(--surface-bg);
  color: var(--text-primary);
}

.ds-tag--primary { border-color: var(--color-primary-300); background: var(--color-primary-50); color: var(--color-primary-700); }
.ds-tag--accent { border-color: var(--color-accent-300); background: var(--color-accent-50); color: var(--color-accent-700); }

.ds-tag__remove {
  background: none;
  border: none;
  cursor: pointer;
  font-size: var(--fs-base);
  line-height: 1;
  color: var(--text-muted);
  padding: 0;
}
.ds-tag__remove:hover { color: var(--color-error); }

/* Avatars */
.ds-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--color-primary-500);
  color: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: var(--fs-sm);
}

.ds-avatar--sm { width: 28px; height: 28px; font-size: var(--fs-xs); }
.ds-avatar--lg { width: 56px; height: 56px; font-size: var(--fs-lg); }
.ds-avatar--xl { width: 72px; height: 72px; font-size: var(--fs-xl); }

/* Tooltips */
.ds-tooltip-wrap {
  position: relative;
  display: inline-block;
}

.ds-tooltip {
  position: absolute;
  background: var(--color-gray-900);
  color: #fff;
  padding: var(--space-1) var(--space-2);
  font-size: var(--fs-xs);
  border-radius: var(--radius-md);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--transition-fast);
  z-index: 10;
}

.ds-tooltip--top {
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
}

.ds-tooltip--bottom {
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
}

.ds-tooltip-wrap:hover .ds-tooltip {
  opacity: 1;
}

/* Modal */
.ds-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
  padding: var(--space-4);
}

.ds-modal {
  background: var(--surface-overlay);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-lg);
  width: 100%;
  max-width: 480px;
  max-height: 90vh;
  overflow-y: auto;
}

.ds-modal__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-4) var(--space-5);
  border-bottom: 1px solid var(--border-color);
}

.ds-modal__header h4 { margin: 0; font-size: var(--fs-lg); }

.ds-modal__close {
  background: none;
  border: none;
  font-size: var(--fs-xl);
  cursor: pointer;
  color: var(--text-muted);
  padding: var(--space-1);
  line-height: 1;
}
.ds-modal__close:hover { color: var(--text-primary); }

.ds-modal__body {
  padding: var(--space-5);
  color: var(--text-secondary);
}

.ds-modal__footer {
  padding: var(--space-3) var(--space-5);
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: flex-end;
  gap: var(--space-2);
}

/* Dropdown */
.ds-dropdown {
  position: relative;
  display: inline-block;
}

.ds-dropdown__menu {
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  min-width: 180px;
  background: var(--surface-overlay);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  z-index: 50;
  padding: var(--space-1) 0;
}

.ds-dropdown__item {
  display: block;
  width: 100%;
  text-align: left;
  padding: var(--space-2) var(--space-3);
  border: none;
  background: none;
  font-size: var(--fs-sm);
  font-family: var(--font-sans);
  color: var(--text-primary);
  cursor: pointer;
}
.ds-dropdown__item:hover { background: var(--color-gray-100); }
.ds-dropdown__item--danger { color: var(--color-error); }
.ds-dropdown__item--danger:hover { background: #fee2e2; }

[data-theme="dark"] .ds-dropdown__item--danger:hover { background: #450a0a; }

.ds-dropdown__divider {
  margin: var(--space-1) 0;
  border: none;
  border-top: 1px solid var(--border-color);
}

/* ============================================
   Interaction Patterns
   ============================================ */

/* Transition Demo */
.ds-transition-demo {
  width: 120px;
  height: 80px;
  background: var(--color-primary-500);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  font-size: var(--fs-sm);
  font-weight: 500;
  transition: all var(--transition-slow);
}

.ds-transition-demo--active {
  transform: scale(1.2) rotate(5deg);
  background: var(--color-accent-500);
  border-radius: var(--radius-full);
}

/* Spinner */
.ds-spinner {
  width: 24px;
  height: 24px;
  border: 3px solid var(--border-color);
  border-top-color: var(--color-primary-600);
  border-radius: 50%;
  animation: ds-spin 0.7s linear infinite;
}

.ds-spinner--sm { width: 16px; height: 16px; border-width: 2px; }
.ds-spinner--lg { width: 40px; height: 40px; border-width: 4px; }

@keyframes ds-spin {
  to { transform: rotate(360deg); }
}

/* Skeleton */
.ds-skeleton {
  background: var(--color-gray-200);
  border-radius: var(--radius-md);
  animation: ds-shimmer 1.5s ease-in-out infinite;
  margin-bottom: var(--space-3);
}

.ds-skeleton--circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
}

.ds-skeleton--title {
  width: 60%;
  height: 20px;
}

.ds-skeleton--text {
  width: 100%;
  height: 14px;
}

@keyframes ds-shimmer {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

/* Toast */
.ds-toast-container {
  position: fixed;
  top: var(--space-4);
  right: var(--space-4);
  z-index: 200;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  max-width: 360px;
}

.ds-toast {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-lg);
  font-size: var(--fs-sm);
  box-shadow: var(--shadow-lg);
  background: var(--surface-overlay);
  border-left: 4px solid;
  color: var(--text-primary);
}

.ds-toast--info { border-color: var(--color-info); }
.ds-toast--success { border-color: var(--color-success); }
.ds-toast--error { border-color: var(--color-error); }

.ds-toast__close {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-muted);
  font-size: var(--fs-lg);
  line-height: 1;
  padding: 0;
  flex-shrink: 0;
}

.ds-toast-enter-active {
  animation: ds-toast-in 0.3s ease;
}
.ds-toast-leave-active {
  animation: ds-toast-out 0.3s ease;
}

@keyframes ds-toast-in {
  from { opacity: 0; transform: translateX(100%); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes ds-toast-out {
  from { opacity: 1; transform: translateX(0); }
  to { opacity: 0; transform: translateX(100%); }
}

/* ============================================
   Responsive
   ============================================ */
.ds-responsive-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

@media (min-width: 768px) {
  .ds-responsive-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .ds-responsive-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.ds-responsive-type h1 {
  font-size: clamp(1.5rem, 4vw, 2.25rem);
}

/* ============================================
   Responsive breakpoint adjustments
   ============================================ */
@media (max-width: 767px) {
  .ds {
    padding: var(--space-4);
  }

  .ds-header h1 {
    font-size: var(--fs-2xl);
  }

  .ds-swatches {
    gap: var(--space-1);
  }

  .ds-swatch {
    width: 60px;
    height: 60px;
  }

  .ds-swatch--wide {
    width: 80px;
  }

  .ds-grid--12 {
    grid-template-columns: repeat(6, 1fr);
  }

  .ds-card-grid {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .ds-swatch {
    width: 70px;
    height: 70px;
  }
}
</style>
