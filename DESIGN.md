# Portfolio Design System Contract

## Image Rules — Read Before Touching Any Image

- All images MUST use local paths from the `case-studies/images/` directory (e.g., `images/file.png`)
- DO NOT use external image URLs
- DO NOT use `object-fit: cover` or any cropping — images must render at natural proportions
- DO NOT set width to 100% without a max-width constraint

### Image CSS classes — use one of these, never custom inline styles:

```css
/* Contained image — most screenshots, diagrams, component specs */
.cs-img { width: 100%; max-width: 900px; height: auto; display: block; border: 1px solid var(--border); margin: 32px 0 8px; }

/* Full-width image — before/after comparisons, wide layouts */
.cs-img-full { width: 100%; max-width: 900px; height: auto; display: block; border: 1px solid var(--border); margin: 32px 0 8px; }

/* Caption — always follows an image */
.cs-img-caption { font-family: 'Press Start 2P', monospace; font-size: 8px; color: var(--muted); letter-spacing: 0.06em; margin-bottom: 24px; }
```

### When to use which:
- `.cs-img` — single screenshots, diagrams, component detail views
- `.cs-img-full` — before/after comparisons, wide UI screenshots, full layouts

## Do's and Don'ts
- **DO NOT** use AI-generated placeholders or images from external domains
- **DO NOT** add `object-fit`, `aspect-ratio`, or fixed `height` to images
- **DO** refer to this file before making any CSS or HTML changes
- **DO** define `cs-img`, `cs-img-full`, and `cs-img-caption` in the `<style>` block of every HTML file that uses images
- **DO** assume local images will be placed in `case-studies/images/` by the user
