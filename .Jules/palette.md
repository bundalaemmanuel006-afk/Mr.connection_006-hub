## 2026-07-05 - Managing Focus for Interactive Modal and Collapsible Panels
**Learning:** When expanding collapsible panels (like shortcut help dialogs) via keyboard triggers, automatically transferring focus to the first interactive element inside the panel prevents keyboard users from having to tab through preceding off-panel layout controls.
**Action:** Always shift focus to the primary interactive child control when expanding disclosures/panels via hotkeys or button toggles, and restore focus to the toggle control upon closing.

## 2026-09-19 - Disclosure Buttons and Tooltip Positioning
**Learning:** Collapsible disclosure toggles require `aria-expanded` and `aria-controls` to announce open/collapsed states to screen reader users. When adding CSS tooltips (`[data-tooltip]`) to primary action buttons centered below text content, using `.tooltip-bottom` prevents popover tooltips from rendering upward and obscuring preceding paragraph text.
**Action:** Always include disclosure ARIA attributes on buttons controlling expandable panels, and position button tooltips downward (`.tooltip-bottom`) when text spans directly above them.
