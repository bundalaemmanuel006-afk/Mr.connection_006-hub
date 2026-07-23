# Palette's Journal - Critical Learnings Only

This journal documents critical, project-specific UX and accessibility insights and learnings.

## 2026-07-21 - Designing Fallback Micro-Experiences for Starter Repositories
**Learning:** In repositories starting completely from scratch (no initial application code/UI), a generic placeholder or silence does not satisfy user goals. Building a zero-dependency, ultra-lightweight (<50 lines) landing page using pure web standards (semantic HTML5, media queries for system preference dark mode, CSS custom properties, and :focus-visible outlines) provides an immediate, accessible entry point that fulfills both functional expectations and aesthetic delight.
**Action:** When bootstrapped with an empty codebase, do not default to no-op. Create an elegant, semantic, and responsive single-file fallback UI that implements WCAG contrast, proper ARIA labels, and key focus-visible states.
