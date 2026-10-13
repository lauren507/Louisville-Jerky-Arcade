# Regenerates brand/tokens.css from brand/tokens.json: python3 scripts/gen-tokens.py brand/tokens.json > brand/tokens.css
import json,sys,re
t=json.load(open(sys.argv[1]))
themes=[x['id'] for x in t['color']['themes']]
col={x['name']:x['value'] for x in t['color']['tokens']}
def res(v,th):
    if isinstance(v,dict): v=v.get(th,v[themes[0]])
    m=re.fullmatch(r'\{(.+)\}',v)
    return res(col[m.group(1)],th) if m else v
out=['/* Louisville Jerky Co. tokens, generated from tokens.json */']
fams=t['type']['families']
fontdecl=[]
for f in t['type']['fonts']:
    fn=f['file'].split('/')[-1]; ext=fn.rsplit('.',1)[1]
    fmt={'ttf':'truetype','otf':'opentype','woff2':'woff2','woff':'woff'}[ext]
    fontdecl.append(f"@font-face{{font-family:\"{f['family']}\";src:url(fonts/{fn}) format(\"{fmt}\");font-weight:{f['weight']};font-style:{f.get('style','normal')};font-display:swap}}")
out+=fontdecl
def block(th):
    lines=[]
    for n,v in col.items(): lines.append(f'--{n}:{res(v,th)};')
    for fam in ('spacing','radius','shadow','stroke','layout'):
        for x in t[fam]['tokens']:
            v=x['value']; v=v.get(th,list(v.values())[0]) if isinstance(v,dict) else v
            lines.append(f"--{x['name']}:{v};")
    return lines
root=block(themes[0])+[f'--font-{k}:{v};' for k,v in fams.items()]
out.append(':root{'+''.join(root)+'}')
for th in themes:
    out.append(f'[data-theme="{th}"]{{'+''.join(block(th))+'}')
print('\n'.join(out))
