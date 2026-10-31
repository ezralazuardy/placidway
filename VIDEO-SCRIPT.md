# Narrated walkthrough (5–10 minutes)

Use the saved execution evidence if the Make organization is paused. The workflow was exercised before its free credit allowance was exhausted. Do not present a recorded result as a new live run.

## 0:00–1:00 — Objective and architecture

“This Make.com workflow turns publicly available PlacidWay podcast content into Facebook-ready posts. It has a daily draft generator and a separate review-and-publish scenario. The default mode requires human approval.”

Show the two Make scenarios and the workflow files. The included native files are earlier exports; the live scenarios received later fixes. The publisher export has not been independently import-tested.

## 1:00–2:30 — Source and AI

Show the podcast RSS source and a saved execution. Explain that the episode content is PlacidWay-authored and hosted on RSS.com. The generator collects the title, source URL, summary, and image. Gemini drafts a hook, two value lines, a call to action, and hashtags. A second model checks factual and medical risks, supplemented by deterministic checks.

## 2:30–4:00 — Review and safety

Show a sample caption and the stored draft record. Explain that the reviewer makes a deliberate approval in the authenticated Make Data Store. The publisher checks the immutable payload hash and compares its caption, title, and source with the displayed record. A modified or invalid approved draft is held for reconciliation. LLM review is not a guarantee of medical accuracy.

## 4:00–5:30 — Output and publishing

Show `SAMPLE-POSTS.md` and the historical Facebook publication evidence. Say: “This post was published to my test page on October 20, 2026. The latest modified publisher was exercised through a dry run; a new public end-to-end post has not been verified.” Show the saved auto-preview result and explain that no Facebook module ran in that preview.

## 5:30–7:30 — Duplicates and errors

Explain that the publisher reserves the source URL and Jakarta date before the external request. Duplicate URLs and a second daily publication are blocked. An uncertain Facebook outcome is held for manual reconciliation; it is not blindly retried. Show the failure and concurrency evidence and identify the substituted Facebook module used in those isolated tests.

## 7:30–8:30 — Setup and limitations

Show README, test report, samples, and workflow files. Explain that the Make Free organization is paused until credits become available, the native exports predate the latest changes, final import and retry exhaustion remain unverified, and the source is an official podcast hosted outside the PlacidWay domain. A public source link is needed for the requested submission.
