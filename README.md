# PlacidWay Social Media Automation

This Make.com demonstration retrieves publicly available PlacidWay-authored podcast content, generates Facebook captions with Gemini, reviews them for factual and medical risks, and supports human approval or automatic publication to an authorized test page.

## Package status

This is an **as-is assessment submission**. The native Make exports in `workflows/` are genuine exports of an earlier configuration: the current live scenarios contain subsequent fixes. The publisher export has not been independently import-tested. The Make Free organization is paused because its credit allowance was exhausted; a new live run requires credits. See `SUBMISSION-NOTE.md` and `TESTING.md` for the distinction between verified behavior and outstanding tests.

## Architecture

1. A daily trigger or manual run retrieves the PlacidWay podcast RSS feed at `https://media.rss.com/placidway-connect-pod1/feed.xml`. The feed contains the episode title, URL, description, and image. It is PlacidWay-authored content hosted on RSS.com; the historical article samples used supplied snapshots.
2. URL and daily reservations limit duplicate selection. Gemini generates a hook, two short informational lines, a call to action and hashtags. A separate AI review and deterministic rules check source evidence, formatting, length and risky wording.
3. Human-review mode stores the exact payload and sends the reviewer a draft. An authenticated reviewer changes the record status to `approved` or `rejected`. The current live publisher verifies the stored payload hash and visible fields before publishing. Auto mode can invoke the publisher directly.
4. The publisher checks previous URLs and the daily limit, reserves both, then posts with an image when available or as text when absent. It records results and alerts. An uncertain Facebook outcome is retained for manual reconciliation instead of an automatic repeat.

## Setup

- Import `workflows/review-publish.blueprint.json`, then `workflows/live-rss-daily.blueprint.json` into inactive Make scenarios. Importing these older native exports does **not** recreate the subsequent live fixes. Review the scenario before activation.
- Connect Gemini, Gmail, and Facebook Pages. Use only a test Page you own. Replace placeholder reviewer addresses in every Gmail module, including error handlers.
- Create a Data Store with the optional text fields in `DATA-STORE.md` and reconnect every Data Store module. Replace example store, scenario, page and connection identifiers with your own.
- Update literal review-queue and execution-history links inside email bodies, and repoint both subscenario calls to the imported publisher.
- Enable sequential processing, set the trigger to daily at 09:00 Asia/Jakarta, and select `auto_publish` as text `false` for human review or `true` for auto mode. Confirm the publisher accepts `draft_id`, `publish_enabled`, and `dry_run`.
- Activate only after validating connections and mappings. For safe manual testing use the publisher with `dry_run=true` and `publish_enabled=false`; inspect the module trace. A dry run is not a Facebook post.

## Operation and safeguards

In approval mode, review the source and displayed caption, change only the draft record's status to `approved` or `rejected`, and save. Approved drafts are consumed by the next daily or manual run. The store tracks source URL and date reservations, payload integrity, execution outcomes, and Facebook post IDs. See `DATA-STORE.md` for keys and recovery guidance.

The generation guardrails reduce risk but are not infallible. The source feed is requested at low frequency; respect robots.txt and never bypass source access restrictions. Limit access to the Make team and Data Store, reconnect credentials rather than embedding tokens, and review any uncertain Facebook outcome before retrying.

## Evidence and recording

- `SAMPLE-POSTS.md` and `samples/generated-posts.json`: five genuinely generated examples and source modes.
- `TESTING.md` and `evidence/`: actual, historical and injected test results, labeled by type.
- `VIDEO-SCRIPT.md`: a narrated 5–10 minute walkthrough using saved evidence while Make is paused.
- `SUBMISSION-NOTE.md`: known release and verification limitations.

A historical image post was published to the candidate's test Page; the final modified workflow's real publication has not been verified. The current automatic path has a saved successful dry run. Source access through RSS.com remains a disclosed interpretation of the assessment's PlacidWay-page requirement.
