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

## 2026-09-03 - Tactile Click Feedback for Value Affordances & Screen Reader Node Announcements
**Learning:** Adding `role="button"` and `tabindex="0"` to value elements (`.value-clickable`) makes them accessible to keyboard and screen reader users, but without `:active` and `.active-click` transform styles, clicking or pressing Enter on these non-`<button>` elements feels unresponsive physically. Furthermore, custom form interactions like `<select>` dropdowns must explicitly update live region announcers (`#sr-status`) when selections change so screen reader users receive immediate auditory feedback alongside visual toasts.
**Action:** Always include `:active` and `.active-click` scale-down animations on custom interactive non-button elements, and ensure `<select>` change handlers update aria-live polite regions immediately.

## 2026-09-04 - Protocol Switcher Tabindex Management & Bottom Tooltip Alignment
**Learning:** Interactive controls located on the bottom row of collapsible card panels (such as `#protocol-val` and `#protocol-btn`) can trap keyboard focus when the panel is collapsed if initialized with `tabindex="0"`. Additionally, default top-positioned tooltips (`[data-tooltip]`) on bottom-row card controls pop up vertically and obscure controls on upper rows; applying `.tooltip-bottom` ensures tooltips render downward below the card layout without obscuring adjacent interactive controls.
**Action:** Always initialize collapsed panel controls with `tabindex="-1"` (updating to `0` on expand), and use `.tooltip-bottom` on bottom-row interactive buttons to prevent tooltip overlap on preceding rows.

## 2026-09-06 - Overflow Visible Management for Collapsible Panels with Tooltips
**Learning:** CSS collapsible panels that use `overflow: hidden` for `max-height` transitions clip pseudo-element tooltips (`[data-tooltip]`) on interactive elements inside the panel when expanded. Toggling the `.visible` class (`overflow: visible`) when open prevents tooltip clipping while maintaining smooth expand/collapse animations.
**Action:** Always toggle `.visible` (or `overflow: visible`) on expanded collapsible panels containing interactive elements with tooltips.

## 2026-09-13 - Immediate Screen Reader Announcement Parity on Asynchronous Triggers
**Learning:** When user actions trigger async background updates (such as gateway node switching triggering `measureLatency()`), setting `s.textContent` immediately before calling an async function that overwrites `s.textContent` synchronously causes screen readers to miss the intermediate state announcement.
**Action:** Pass custom screen reader status messages into async functions so live region polite announcements (`#sr-status`) maintain immediate parity during loading states.

## 2026-09-14 - Explicit Value Inclusion in Clipboard Screen Reader Announcements
**Learning:** Generic screen reader announcements (such as "Session ID copied to clipboard") do not confirm the specific content copied, leaving screen reader users uncertain if the intended value was captured. Including the exact copied string (e.g. "Session ID CONN-5118 copied to clipboard") in `aria-live` polite regions provides explicit feedback.
**Action:** Always include the exact text value being copied in screen reader polite announcements (`#sr-status`).

## 2026-09-15 - Synchronized ARIA Disabled States and Tooltips for Context-Dependent Shortcuts
**Learning:** Interactive shortcut badges (`<kbd>`) in helper panels that trigger context-dependent actions (like copying session ID or measuring latency) can confuse assistive technology users when shown with standard active labels while the system is disconnected. Setting `aria-disabled="true"`, descriptive tooltips (e.g., "Requires Connection (C)"), and updated `aria-label` strings when offline—and dynamically toggling them to active states (`aria-disabled="false"`) upon connection—ensures consistent accessible state representation across visual and auditory modes.
**Action:** Always synchronize `aria-disabled`, `data-tooltip`, and `aria-label` attributes on helper badges when their underlying action requires an active session.
