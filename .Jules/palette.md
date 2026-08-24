## 2026-08-23 - Interactive Connection Status Telemetry & Tooltip Positioning Strategy
**Learning:** Making visual status indicators (`#status-val`) interactive with click and keyboard (`Enter`/`Space`) controls offers an intuitive way to re-check connection health. Standard tooltips (`.tooltip-bottom`) on upper elements in compact stacked card layouts can overlap interactive inputs on rows below (such as `<select>` menus); using default top-positioned tooltips ensures tooltip overlays remain uncluttered and legible.
**Action:** Always make status indicators interactive when active, and ensure tooltip positioning modifiers (`.tooltip-bottom`) avoid obscuring adjacent interactive controls below.

## 2026-08-24 - Collapsed Details Panel Tabindex Management for Keyboard Focus Traps
**Learning:** Elements inside collapsible panels with CSS height/opacity transitions remain in the natural keyboard tab order if marked with `tabindex="0"`, causing hidden/invisible interactive controls to unexpectedly trap keyboard focus when tabbing through the page while collapsed.
**Action:** Initialize interactive elements inside collapsed panels with `tabindex="-1"` and dynamically toggle their `tabindex` to `0` upon expanding the panel (and back to `-1` on collapse).
