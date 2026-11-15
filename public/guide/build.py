import json, html
from pathlib import Path
root=Path(__file__).resolve().parent
esc=html.escape
intro='''<!doctype html><html lang="th"><head><meta charset="utf-8"><style>
@font-face{font-family:Prompt;src:url(Prompt-Regular.ttf)}@font-face{font-family:Prompt;src:url(Prompt-SemiBold.ttf);font-weight:600}
@page{size:A4;margin:18mm 19mm 18mm}body{font-family:Prompt,Tahoma,sans-serif;color:#203137;font-size:10.5pt;line-height:1.7}h1{font-size:24pt;color:#245b83;line-height:1.35}h2{font-size:16pt;color:#245b83;border-bottom:1px solid #cbdfe9;padding-bottom:5px;margin-top:22pt;break-after:avoid}h3{font-size:12pt;color:#347fb5;break-after:avoid}p{margin:0 0 9pt}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eef5f9;padding:10pt;font:9pt/1.4 Consolas,monospace;border-left:3px solid #348fc7;break-inside:avoid}code{font-family:Consolas,monospace;font-size:.9em}article{break-inside:avoid;border-bottom:1px solid #dbe6ed;padding:8pt 0}article p{margin:2pt 0}ol{margin:3pt 0 6pt;padding-left:23pt}.question{white-space:pre-wrap}.answer{color:#245b83}.newpage{break-before:page}.muted{color:#5c6d6d}</style></head><body>'''
parts=[intro,(root/'lessons.html').read_text(encoding='utf8')]
for file,label in [('practice.json','Practice: ข้อฝึก 60 ข้อ'),('pretest.json','Pre-test: ข้อฝึก 40 ข้อ')]:
    data=json.loads((root.parent/file).read_text(encoding='utf8'))
    parts.append('<section class="newpage"><h1>'+label+'</h1><p>ลองทำก่อนอ่านเฉลย และตรวจเหตุผลในแต่ละข้อ บางข้อเลือกได้หลายคำตอบตามที่โจทย์ระบุ</p>')
    for i,q in enumerate(data,1):
        parts.append('<article><h3>ข้อ '+str(i)+' · '+esc(q['category'])+'</h3><p class="question">'+esc(q['question'])+'</p>')
        if q.get('choices'):
            parts.append('<ol type="A">'+''.join('<li>'+esc(str(c)).replace('\n','<br>')+'</li>' for c in q['choices'])+'</ol>')
        parts.append('<p class="answer"><b>คำตอบ:</b> '+esc(q['answer'])+'</p><p><b>เหตุผล:</b> '+esc(q.get('explanation',''))+'</p></article>')
    parts.append('</section>')
parts.append('</body></html>')
(root/'supplement.html').write_text(''.join(parts),encoding='utf8')
