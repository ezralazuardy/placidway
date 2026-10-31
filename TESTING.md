# Verification report

Status: **incomplete acceptance**, not ready to claim all eight requirements passed. Historical evidence is identified separately from the current graph. A configured module or a top-level success does not prove its downstream branch ran.

**Status updated 31 October 2026:** Organization isPaused=true on Free, 107,804 centicredits consumed (1,078.04 credits), 1,000-credit allowance, unusedCenticredits=-7,804, autoPurchasingActivated=false. Reset: 20 November 2026 01:13:58 UTC. Main scenarios are configured active but platform-paused. Codex browser control has been restored and both latest native exports obtained. Fresh import verification and additional public-post authorization remain outstanding. The public repository is https://github.com/ezralazuardy/placidway . Important execution evidence is saved locally.

| ID | Requirement | Verified evidence | Remaining acceptance |
|---|---|---|---|
| FR-01 | Daily and manual | Final graph scheduled run `d6afa65c49d3441ab0bc382d0e8e67d7`, 23 October 00:50 Jakarta test schedule; manual `54e6a98b27e54b88a33cb9d0eba56e4f`; both recorded explicit no_eligible_content | Normal 09:00 schedule restored; organization now paused by credit quota |
| FR-02 | Authentic source extraction | Current generator extracted official podcast RSS title, URL, description, artwork; provenance/robots checked 22 October | Confirm evaluator accepts PlacidWay-authored podcast pages hosted on RSS.com |
| FR-03 | Selection and persistent dedup | Current generator accepted one candidate after rejecting an earlier one; persistent URL/day keys; historical publisher reservations | Current-graph repeated/concurrent runs, cross-day URL replay, different URLs same day, reservation failure/uncertain outcome tests |
| FR-04 | Facebook caption | Current live RSS sample is 402 characters, two value lines, hook/CTA/link/three hashtags; deterministic native filters | Validate final sample package locally and preserve live execution details |
| FR-05 | Medical/factual guardrails | Current run rejected a medical-mechanism/overlength candidate, accepted attributed topic-only caption | Broader explicit allowed/prohibited regression cases; no claim of infallibility |
| FR-06 | Facebook image/text publication | Historical real photo post `1312648348607578_122096151489521939`, execution `e2c1d2b330cf4f369100bc1e0254f899` | Final-graph controlled real integration and text-only route; additional public post requires authorization |
| FR-07 | Configurable approval | Stored pending/rejected/tampered payload blocked; approved preview accepted; automatic source-to-child preview verified below; immutable mode mismatch blocked | Actual human approval transition and publication; approval queue replay behavior |
| FR-08 | Persistent logs and errors | Current generator start/rejection/completion and publisher blocked/preview rows; configured safe retries and uncertain-result holds | Actual source/model/API/auth/rate-limit faults, bounded retries and alert delivery; storage/Gmail outage fallback |

## Current publisher controlled tests

These tests injected stored decisions under controlled QA, then restored the complete original pending draft. They are **not** evidence of a human reviewer decision or real publication.

| Test | Expected / observed | Execution |
|---|---|---|
| Pending draft preview | Blocked | `aed3e24a34ca42168c81e3b14afc05c5` |
| Approved preview | `dry_run_validated`; preview route reached, no Facebook modules | `2d2b51ad187b4aa8b717202c97b39515` |
| Rejected preview | Blocked; no Facebook modules | `f1810978a1f24eda901f868afd17617e` |
| Changed serialized payload | Blocked | `501cdc3a3385468aa41e087268a3c14b` |
| Publication switch disabled | Blocked | `93471a16f1414cd1ad6de5cbbc63cb84` |

Accepted preview trace: `1 → 32 → 31 → 4 → 10 → 29 → 5 → 18 → 48 → 19 → 20`. Rejected preview trace: `1 → 32 → 31 → 4 → 10 → 29 → 40 → 45`.

## Native export portability

**Latest native exports obtained 31 October 2026:** files in workflows/ now contain all 49 generator and 50 publisher modules and the final review fixes. These are native editor downloads, not reconstructed blueprints. Module types, parameters, mappings, data, routing and filters match the final live configurations. Reviewer addresses and connection labels are sanitized for publication. Local blueprint and sample checks pass.

Historical portability evidence: an earlier 47-module Daily Draft export was imported into inactive scenario `6728706` with no reported module issues. That does not verify the latest 49-module export. Publisher import into `6728746` was not completed. Neither latest export has completed a fresh import-and-relink acceptance test; do not label that verification passed.

The Daily Draft import is now an isolated QA workflow, not a production export: URL/day draft locks are namespaced; the human-approval consumer is disabled; auto mode calls the production publisher with `dry_run=true`, `publish_enabled=false`; Gmail recipients are restored to the owner only. Production native files retain their original behavior.

## Known regression resolved

A status-only connector record update replaced omitted fields in one test draft. The exact original was recovered from the actual generator module input, restored, and compared. Publisher outcome updates were changed to preserve the full existing draft row. Historical URL reservations were preserved.

## Additional current integration tests (23 October, Jakarta)

| Test | Actual evidence | Result |
|---|---|---|
| Live RSS → AI → guardrails → automatic publisher preview | Parent `9e444643997d49d780efa52a3883a7f3`, child `d31c0b36241e4dc0b69606771238668b`; child returned `dry_run_validated`, reached preview modules 18/48/19/20, did not execute reservations 11/30 or Facebook 8/13 | PASS for automatic preview integration; not real publication |
| Repeat same-day manual run | `bdc5f4feef6d4b8a9a7a929b936e2c99`; only modules 1/23/25/15/26 ran, no RSS, LLM, accepted draft or child call | PASS for daily draft suppression in isolated QA namespace |
| Malformed model JSON test injection | `3b04b8260e95499fbc4bdb7ee50d2b19`; parser received explicit `QA_MALFORMED_JSON_TEST`, output `Source is not valid JSON.`; module31 saved failure row; Gmail44 returned SENT message ID `1a164a0ffa3b2b18`; publisher never ran | PASS for injected malformed JSON handling and Gmail send acceptance; not an actual Gemini malfunction or proof of inbox reading |
| Wrong approval mode | `8b7a0874e2fe4d2abbaadc41a82628e7`; human-review payload with row status temporarily `auto_ready` returned `blocked`, route40/45 and no Facebook; original full row restored | PASS for immutable mode enforcement |
| Missing draft | `9ecd7581ce9c4132a2610bbc2dc7eac7`; missing payload caused parser failure, module39 saved `invalid_draft` / `blocked`, no Facebook | PASS for safe stop and persistent error; caller receives no explicit error output on this handler |

The parser was restored after fault injection. QA scenario 6728706 is inactive. Production generator 6702908 was reactivated after confirming all 36 store records contained no `approved` test decisions; publisher remains active. Human-review default remains configured. The final scheduled trigger has not yet been observed after reactivation.

## Outstanding integration checklist

## Independent review fixes and regression tests

- Reviewer-visible caption mismatch reproduced: RED `159b8f2deb2443bbb25d656b68e61e19` incorrectly returned dry_run_validated. After adding displayed-caption/title/source equality, GREEN `49058414ee524c61878e65002eabfbfc` returned blocked, preserved the payload and moved the approved row to held_manual. Original real pending draft restored fully after the test.
- Corrected publisher positive preview: `2a4770b472714a3bb7a9d61bcba5173d` returned dry_run_validated for the genuine 301-character RSS draft.
- Valid daily deferral in the safe clone: `e9de6e27e5f6479aaedc001299a83add` reached only the new deferred route (QA51/52), returning deferred_daily_limit without entering the permanent hold or publishing boundary. Production has the equivalent explicit branch.
- Strict pre-link boundary now includes the newline separator. Synthetic ASCII length-only fixtures in the safe clone: 498 characters + newline (499 before URL) validated in `6df888b2cdde47a18780603c702cf78c`; 499 + newline (500 before URL) blocked in `b439f1542c5c424f86a4c7d1e55a4822`. These fixtures are not generated sample posts and do not test factual/medical guardrails.
- Generator outcome logging now explicitly distinguishes source_failed, skipped_daily_draft_exists, completed_draft_saved and no_eligible_content. Scheduled run `d6afa65c49d3441ab0bc382d0e8e67d7` and manual `54e6a98b27e54b88a33cb9d0eba56e4f` both persisted no_eligible_content; controlled auto preview `a71e63b020934024b5f5a27426ce729a` persisted completed_draft_saved.
- Final corrected automatic path: parent `a71e63b020934024b5f5a27426ce729a` → child `507a09fc70864efd8d251cfdf076ea08`, dry_run_validated; child trace excludes URL/date reservation and Facebook modules. For this controlled test only, draft locks were namespaced, human approval consumption disabled, and auto caller forced to preview. All eight changed production module configurations were restored exactly, approval consumer re-enabled and schedule restored to 09:00; then the organization credit limit paused execution.
- Text-only routing/error test: `81e4004d61c0479189c97e69f59f9a9c` in the no-Facebook clone reached replacement module13, handlers37/47 and Gmail26; this tests the no-image error path, not actual text-only Facebook publication.
- Import instructions now include replacing account-specific literal links in email bodies.
- Ten offline allowed/prohibited pattern cases (three allowed, seven blocked) exercise the actual exported prohibited-claim regex in Python against English text. These are pattern-only regression checks, not complete-format validation or additional live LLM results. Sample counts/hashes, strict separator counts, final native module guards, stored-payload preservation and sequential settings pass local checks following the 31 October native export refresh. Live acceptance remains incomplete as documented above.


Additional isolated publisher scenario `6737619` reproduces the production graph with URL/day keys prefixed `qa:publisher-20261023:`, a separate seeded draft copy, and **both Facebook modules replaced by deliberately invalid JSON parsers**. No Facebook connection/module exists in this clone. These are test doubles, not actual Facebook errors.

| Test | Actual evidence | Result |
|---|---|---|
| Failure after URL/date reservation | `e0ffd92054c54287a10c8b17f7900369`: modules11/30 reserved first, test double8 failed, handlers36/46 saved `publish_unknown`, full draft payload remained, Gmail25 completed | PASS for injected uncertain-result handler and retained reservations; no external post request |
| Repeat reserved URL/date | `ca923b8968bd4b6da36c674115bfcfe7` returned `blocked` | PASS for repeat after failed attempt in isolated store namespace |
| Different URL on reserved date | `b3ce9a3b8a494e81b53d6d13969c93da`: URL check10 returned false, daily check29 returned true, explicit blocked output | PASS for daily cap independently of duplicate URL |
| Same URL with a different date key | `1f7eaac48639450bae0bfd50548309d6`; QA date key changed to unused `2099-01-01`, URL reservation retained, blocked before external boundary | PASS for URL history independent of daily key; controlled date-key injection, not elapsed real calendar days |
| Concurrent caller requests | `10dd322287ae459f99bd7c974e93eb39` and `fde2ba2174bf41fdb66891d4ae8f80a2` dispatched together to sequential QA publisher; first reserved and reached failing test double once, second returned blocked and never reached the boundary | PASS for duplicate prevention under concurrent callers in isolated QA |
| Unavailable RSS source | `5ca72f208360437d8bb83750f6a50c79`; intentionally nonexistent feed returned HTTP 404, error persisted before Gmail alert, incomplete execution retained for bounded retries; no model/publisher modules | PASS for initial real source-error handling; automatic retry exhaustion still under observation |


- Finish publisher native import, inspect its interface, and test relinking in a safe deployment.
- Inject source unavailable and other API failures; malformed JSON and its alert are already demonstrated above.
- Exercise duplicate URL, daily cap, concurrent requests and unknown publication without producing unnecessary public posts.
- Authorize one exact controlled public post only when the final branch is ready, then verify post ID and ledger.
- Restore the default human-review daily schedule and observe its final configuration.
- Publish sanitized artifacts to an approved public destination; verify without authentication.

Unrun tests remain unrun; injected API failures must be labeled as test doubles rather than external outages.
