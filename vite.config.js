import { defineConfig } from 'vite';

// Em GitHub Pages (projeto), o site fica em /faleiros-associados/
const base = process.env.GITHUB_ACTIONS ? '/faleiros-associados/' : '/';

export default defineConfig({
  root: '.',
  base,
  build: {
    outDir: 'dist',
    emptyOutDir: true,
  },
  server: {
    open: true,
  }
});
