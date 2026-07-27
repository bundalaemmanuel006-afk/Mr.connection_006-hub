# Palette's Journal - Critical Learnings Only

This journal documents critical, project-specific UX and accessibility insights and learnings.

## 2026-07-21 - Designing Fallback Micro-Experiences for Starter Repositories
**Learning:** In repositories starting completely from scratch (no initial application code/UI), a generic placeholder or silence does not satisfy user goals. Building a zero-dependency, ultra-lightweight (<50 lines) landing page using pure web standards (semantic HTML5, media queries for system preference dark mode, CSS custom properties, and :focus-visible outlines) provides an immediate, accessible entry point that fulfills both functional expectations and aesthetic delight.
**Action:** When bootstrapped with an empty codebase, do not default to no-op. Create an elegant, semantic, and responsive single-file fallback UI that implements WCAG contrast, proper ARIA labels, and key focus-visible states.

## 2026-07-24 - Stateful Async Buttons in Zero-Dependency Standard Web Interfaces
**Learning:** Implementing interactive states (loading, completion) in simple vanilla HTML pages requires careful synchronization of visual feedback and assistive technologies. A common pitfall is changing only visual elements, leaving screen readers unaware. Using an explicit live region (`aria-live="polite"`) decoupled from the active button container guarantees robust announcements across modern browsers and screen readers, while combining `aria-busy` and `aria-disabled` prevents form double-submission gracefully.
**Action:** Always declare an invisible `aria-live` region to push dynamic micro-UX transitions (e.g., "Connecting...", "Connected") to users on assistive technologies rather than relying purely on text change inside buttons.

## 2026-07-25 - Seamless Clipboard Copy Micro-UX
**Learning:** When generating session identifiers or keys dynamically, users expect a quick and reliable way to copy them. Adding a keyboard-accessible, icon-only copy button next to the value with high visual/interactive feedback (switching to a checkmark on success) and screen reader announcements via `aria-live="polite"` bridges the gap between desktop-like interactions and standard web interfaces seamlessly.
**Action:** Always complement icon-only buttons with robust `aria-label` attributes and ensure state feedback is declared both visually and to assistive technologies via `aria-live` zones.

## 2026-07-27 - Stateful Toggles with Hover/Focus Intention States
**Learning:** For actions with long-lasting lifecycle states (like persistent connections), keeping a simple toggling button text static (e.g. "Connected") can confuse users about what clicking it will do. Implementing dynamic state transitions on keyboard/mouse focus or hover (e.g. changing from "✓ Connected" to "Disconnect") clearly signals the action resulting from the interaction. High visual contrast transition (e.g. green to red) combined with updated screen reader `aria-label` attributes ensures that both sighted and assistive technology users have a smooth, unambiguous interactive experience.
**Action:** For interactive states that represent a toggling workflow, design distinct focus/hover transitions that clarify the upcoming action, and sync those changes with matching ARIA/live-region messages.
