"""Check local package consistency; does not assert live integration acceptance."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def modules(flow):
    for item in flow:
        yield item
        for route in item.get('routes', []):
            yield from modules(route.get('flow', []))
        yield from modules(item.get('onerror', []))


for name in ('live-rss-daily', 'review-publish'):
    blueprint = json.loads((ROOT / 'workflows' / f'{name}.blueprint.json').read_text())
    nodes = list(modules(blueprint['flow']))
    ids = [node['id'] for node in nodes]
    assert len(ids) == len(set(ids)), f'Duplicate module IDs: {name}'
    assert len(nodes) > 20, f'Unexpectedly empty blueprint: {name}'
    text = json.dumps(blueprint)
    emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
    assert all(email == 'reviewer@example.com' for email in emails), 'Non-placeholder email remains'
    assert not re.search(r'AIza[\w-]{30,}|EAA[\w-]{70,}|gh[pousr]_[\w]{30,}', text), 'Possible embedded credential'
    print(f'{name}: {len(nodes)} native modules')

publisher = json.loads((ROOT / 'workflows/review-publish.blueprint.json').read_text())
assert 'io' in publisher, 'Publisher interface absent'
generator = json.loads((ROOT / 'workflows/live-rss-daily.blueprint.json').read_text())
g = {m['id']: m for m in modules(generator['flow'])}
p = {m['id']: m for m in modules(publisher['flow'])}
assert 'medical mechanisms' in g[9]['mapper']['textPrompt']
assert g[12]['mapper']['data']['payload'] == '{{11.json}}'
assert g[12]['mapper']['key'] == 'draft:{{sha256(11.json)}}'
assert p[31]['module'] == 'datastore:GetRecord'
assert p[31]['mapper']['key'] == '{{1.draft_id}}'
for module_id in (41, 42, 46, 47):
    assert p[module_id]['mapper']['data']['payload'] == '{{31.payload}}'
    assert p[module_id]['mapper']['data']['caption'] == '{{31.caption}}'
for blueprint in (generator, publisher):
    assert blueprint['metadata']['scenario']['sequential'] is True
print('Stored payload integrity, outcome field preservation and sequential settings checked')
samples = json.loads((ROOT / 'samples/generated-posts.json').read_text())
assert len(samples) >= 3
for sample in samples:
    caption = sample['caption_without_link']
    assert len(caption) == sample['character_count'] < 500
    assert sample['character_count_before_link'] == len(caption) + 1 < 500
    assert hashlib.sha256(caption.encode()).hexdigest() == sample['caption_hash']
    assert sample['caption'] == caption + '\n' + sample['url']
    assert 3 <= len(re.findall(r'#\w+', caption)) <= 5
    assert sample['execution_id'] and sample['source_mode']
    assert sample['validation_outcome']
print(f'{len(samples)} genuine sample captions: counts, hashes, links and metadata checked')
rule = next(c['b'] for group in g[10]['filter']['conditions'] for c in group if c['o'] == 'text:notpattern' and 'guarantee' in c['b'])
cases = json.loads((ROOT / 'tests/guardrail-cases.json').read_text())
for case in cases:
    assert bool(re.search(rule, case['caption'].lower())) == case['blocked_by_prohibited_pattern']
print(f'{len(cases)} allowed/prohibited pattern-only cases checked; this is not an LLM review test')
for name in ('README.md', 'DATA-STORE.md', 'TESTING.md', 'VIDEO-SCRIPT.md'):
    assert (ROOT / name).stat().st_size > 100
assert 49 in p and 50 in p and 49 in g and 50 in g, 'Native exports are outdated after review fixes; re-export from the Make editor'
assert 'no_eligible_content' in g[26]['mapper']['data']['status']
assert any(c['a'] == '{{31.caption}}' and c['b'] == '{{4.caption}}' for group in p[5]['filter']['conditions'] for c in group)
assert any(c['a'] == '{{length(4.caption_without_link) + 1}}' for group in p[5]['filter']['conditions'] for c in group)
print('Local consistency checks passed. Live acceptance remains in TESTING.md.')
