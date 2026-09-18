## 2026-07-05 - Managing Focus for Interactive Modal and Collapsible Panels
**Learning:** When expanding collapsible panels (like shortcut help dialogs) via keyboard triggers, automatically transferring focus to the first interactive element inside the panel prevents keyboard users from having to tab through preceding off-panel layout controls.
**Action:** Always shift focus to the primary interactive child control when expanding disclosures/panels via hotkeys or button toggles, and restore focus to the toggle control upon closing.
