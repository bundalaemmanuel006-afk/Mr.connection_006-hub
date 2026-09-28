## 2026-08-23 - Interactive Connection Status Telemetry & Tooltip Positioning Strategy
**Learning:** Making visual status indicators (`#status-val`) interactive with click and keyboard (`Enter`/`Space`) controls offers an intuitive way to re-check connection health. Standard tooltips (`.tooltip-bottom`) on upper elements in compact stacked card layouts can overlap interactive inputs on rows below (such as `<select>` menus); using default top-positioned tooltips ensures tooltip overlays remain uncluttered and legible.
**Action:** Always make status indicators interactive when active, and ensure tooltip positioning modifiers (`.tooltip-bottom`) avoid obscuring adjacent interactive controls below.

## 2026-08-24 - Collapsed Details Panel Tabindex Management for Keyboard Focus Traps
**Learning:** Elements inside collapsible panels with CSS height/opacity transitions remain in the natural keyboard tab order if marked with `tabindex="0"`, causing hidden/invisible interactive controls to unexpectedly trap keyboard focus when tabbing through the page while collapsed.
**Action:** Initialize interactive elements inside collapsed panels with `tabindex="-1"` and dynamically toggle their `tabindex` to `0` upon expanding the panel (and back to `-1` on collapse).

## 2026-08-27 - Absolute Position Override by Data-Tooltip Pseudo-Elements
**Learning:** Tooltip rules targeting `[data-tooltip]` apply `position: relative` to anchor tooltip pseudo-elements (`::after`). When applied to buttons originally styled with `position: absolute` (such as top corner toggles inside a flex/centered card layout), `position: relative` overrides their corner alignment and causes them to collapse into the inline text flow.
**Action:** Use `position: absolute !important` on corner toggle buttons when combining with `[data-tooltip]` pseudo-elements, and ensure `h1` has sufficient top margin (48px) to prevent tooltip overlays from obscuring main headings.

## 2026-08-28 - Focus Restoration on Collapsible Overlay/Panel Closure
**Learning:** When closing collapsible panels or modal overlays (such as via the Escape key or interactive panel triggers), if keyboard focus was currently within the panel, focus can get lost or reset to `document.body`. Explicitly transferring focus back to the initiating toggle button restores predictable keyboard navigation for screen reader and hotkey users.
**Action:** Check if `panel.contains(document.activeElement)` when closing a panel, and explicitly call `.focus()` on the panel toggle button.

## 2026-08-30 - Focus Preservation During Temporarily Disabled Async Operations
**Learning:** Setting `disabled = true` on interactive elements during async state transitions (such as connecting, protocol switching, or latency measuring) causes browsers to immediately drop keyboard focus from the active element to `document.body`. When the operation finishes and `disabled = false` is restored, keyboard focus remains on `body`, breaking tab sequence for keyboard users.
**Action:** Track whether `document.activeElement` matches the triggering button before setting `disabled = true`, and explicitly restore `.focus()` when re-enabling the button upon async completion.

## 2026-08-31 - Dynamic System Color Scheme Change Listener and Deferred LocalStorage Persistence
**Learning:** Saving default theme state into `localStorage` during initial page load locks the theme, preventing `(prefers-color-scheme: dark)` media query listeners from responding when users switch OS/browser light/dark modes unless `localStorage` is unset. Only write to `localStorage` upon explicit user interaction (e.g. clicking theme toggle), and listen to `window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', ...)` to dynamically sync theme state when `localStorage` has no override.
**Action:** Default `saveToStorage` to `false` during initial load/sync, add a system color scheme change event listener, and set `saveToStorage = true` only during manual toggle events.

## 2026-09-01 - Screen Reader Announcement Parity for Offline Keyboard Shortcuts
**Learning:** When global keyboard shortcuts or key badges (such as 'C', 'R', or 'N') are pressed while a component is in a disconnected or disabled state, showing visual toast notifications without updating aria-live polite regions (`#sr-status`) leaves screen reader users unaware of why the shortcut did not trigger an action.
**Action:** Always pair visual toast notifications for disabled/disconnected keyboard shortcuts with explicit screen reader status announcements (`s.textContent = msg`).

## 2026-09-02 - Toast Auto-Dismiss Timing Control & Hover Pause
**Learning:** Automatic timeouts on floating toast notifications can cause users to miss reading feedback if they disappear while being inspected. Clearing dismissal timers on `mouseenter`, resuming countdowns on `mouseleave`, and listening for the `Escape` key ensures WCAG 2.2 SC 2.2.1 timing flexibility and full keyboard control.
**Action:** Always pause transient notification timers on mouse hover, resume on mouse exit, and support `Escape` key dismissals.

## 2026-09-26 - Dynamic Tabindex Management for Collapsed Panel Controls
**Learning:** Interactive controls inside collapsible details panels (such as `#protocol-val`, `#protocol-btn`, and `#badge-node`) retain natural keyboard tab focus when marked with `tabindex="0"` even while the parent panel is collapsed (`max-height: 0`). Initializing them with `tabindex="-1"` and dynamically updating to `tabindex="0"` when expanded eliminates focus traps for keyboard users.
**Action:** Always initialize interactive controls inside collapsed overlay panels with `tabindex="-1"` and dynamically manage `tabindex="0"` upon expansion.

## 2026-09-28 - Focus Preservation and Auditory Announcement Parity for Select Menus
**Learning:** Temporarily disabling a `<select>` menu during async background operations (such as re-measuring connection latency upon node selection) drops browser focus to `document.body` if `#node-select` was active. Explicitly tracking `nodeSelect` in `targetFocusEl` and restoring `.focus()` upon re-enabling preserves keyboard focus and prevents tab order resets. Furthermore, passing custom status messages to async measurement functions preserves auditory notification parity for screen reader users when visual toast notifications are triggered.
**Action:** Include `<select>` controls in focus preservation tracking during temporary async disabled states, and pass contextual status parameters to async routines to prevent overwriting screen reader announcements.
