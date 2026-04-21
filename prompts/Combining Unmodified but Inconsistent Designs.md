“Combine Unmodified Designs” in Bluetooth Qualification
🧠 Core Concept

In Bluetooth qualification, there are two fundamentally different paths:

Create a New Design
Reuse Existing Designs (Unmodified)

The rule strictness depends entirely on which path you choose.

⚙️ What is “Combine Unmodified Designs”?

This option means:

You are combining multiple already-qualified Designs (QDIDs/DNs) without making any changes.

No ICS modification
No feature changes
No layer adjustments

You are simply referencing existing, approved building blocks.

⚠️ Why Inter-Layer Inconsistency Can Still Exist

Even if:

Host says: “I support feature X (e.g., CS)”
Controller says: “I do NOT support feature X”

➡️ This creates an inter-layer inconsistency (ILD issue)

Normally, this would:

❌ Fail the consistency check
❌ Block qualification
✅ Why It Still Works with This Option

When using Combine Unmodified Designs:

The inconsistency is not newly introduced
It already exists in the referenced Designs
You are not modifying ICS or behavior

So the system allows it because:

“These Designs were already qualified individually, and you are not changing them.”

🚫 What This Option Does NOT Allow

You cannot use this option to:

Modify ICS selections
Add/remove features
Fix inconsistencies manually
Mix incompatible designs arbitrarily

If you do any of the above →
➡️ You are creating a new Design, and strict rules apply again

🧩 Mental Model (Best Way to Remember)

Think of it like LEGO:

You are allowed to assemble pre-approved LEGO blocks
Even if they don’t perfectly match internally
As long as you don’t modify the blocks themselves
⚠️ Risks If Misunderstood

If you misuse or misunderstand this:

❌ You may attempt a new Design and fail consistency checks
❌ You may trigger unnecessary testing requirements
❌ You may cause delays in qualification approval
🎯 Key Takeaway

“Combine Unmodified Designs” does NOT let you ignore rules.
It lets you reuse existing qualified Designs as-is, even if they contain inherited inconsistencies.

💡 Practical Advice
Use this option only when you cannot resolve inconsistencies via proper Design selection
Prefer clean, consistent Design combinations when available
Treat this as a fallback strategy, not a default approach
🏁 One-Line Summary

You’re allowed to reuse imperfect but already-approved Designs—but not to create new imperfect ones.