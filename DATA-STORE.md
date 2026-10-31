# Persistent ledger

Use one Make Data Store with these optional **text** fields:

`payload`, `status`, `updated_at`, `execution_id`, `source_url`, `title`, `caption`, `caption_hash`, `review_status`, `publish_status`, `facebook_post_id`, `error_message`, `source_mode`, `created_at`.

| Key | Meaning |
|---|---|
| `draft:<SHA256(serialized payload)>` | Exact immutable draft, approval decision and publication state |
| `draft:<SHA256(source URL)>` | Separate source draft reservation |
| `draft-day:YYYY-MM-DD` | At most one accepted draft per Jakarta date |
| `<SHA256(source URL)>` | Publication reservation/history, never casually delete |
| `publish-day:YYYY-MM-DD` | At most one attempted publication per Jakarta date |
| `run:<execution ID>:<event>` | Persistent start, result, rejection or error audit |

Draft states include `pending_review`, `approved`, `rejected`, `auto_ready`, `published`, `publish_unknown`, `held_manual`. Immutable payload status remains the state at generation; mutable row status carries the decision/outcome. A permanently blocked approved row becomes held_manual so it cannot repeatedly occupy the approval queue. A valid draft blocked only by daily capacity remains eligible for tomorrow; its execution event is deferred_daily_limit.

**Record update caution:** the Make connector's record update replaces omitted data. Always send the entire original record plus changed fields. Publisher outcome updates explicitly preserve all existing draft fields. Back up a row before controlled QA changes.

## Reconciliation

For `publish_unknown`, inspect the execution and actual Facebook Page before changing anything. If a post exists, record its ID and mark the draft published. If absence is established, an authorized operator must decide whether to release the URL/day reservation for a controlled retry. Never infer absence from a timeout. Keep an audit of that decision. A reservation intentionally favors avoiding duplicates over automatically recovering every lost post.

Historical key-only records are valid deduplication reservations. Keep them when adding a schema. Storage retention must preserve these safety records.
