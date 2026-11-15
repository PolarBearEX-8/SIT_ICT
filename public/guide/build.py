import json,html
from answer_details import EXTRA
from pathlib import Path
root=Path(__file__).resolve().parent
esc=html.escape
head='''<!doctype html><html lang="th"><head><meta charset="utf-8"><style>@font-face{font-family:Prompt;src:url(Prompt-Regular.ttf)}@font-face{font-family:Prompt;src:url(Prompt-SemiBold.ttf);font-weight:600}@page{size:A4;margin:18mm 19mm 18mm}body{font-family:Prompt,Tahoma,sans-serif;color:#203137;font-size:10.5pt;line-height:1.7}h1{font-size:24pt;color:#245b83;line-height:1.35}h2{font-size:16pt;color:#245b83;border-bottom:1px solid #cbdfe9;padding-bottom:5px;margin-top:22pt;break-after:avoid}h3{font-size:12pt;color:#347fb5;break-after:avoid}p{margin:0 0 9pt}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eef5f9;padding:10pt;font:9pt/1.4 Consolas,monospace;border-left:3px solid #348fc7;break-inside:avoid}code{font-family:Consolas,monospace;font-size:.9em}article{break-inside:avoid;border-bottom:1px solid #dbe6ed;padding:8pt 0}article p{margin:2pt 0}ol{margin:3pt 0 6pt;padding-left:23pt}.question{white-space:pre-wrap}.answer{color:#245b83}.newpage{break-before:page}</style></head><body>'''
sets=[('practice.json','Practice: ข้อฝึก 60 ข้อ'),('pretest.json','Pre-test: ข้อฝึก 40 ข้อ')]
def save(name,parts): (root/name).write_text(head+''.join(parts)+'</body></html>',encoding='utf8')
save('lessons-print.html',[(root/'lessons.html').read_text(encoding='utf8')])
qs=[]; ans=[]
for file,label in sets:
 data=json.loads((root.parent/file).read_text(encoding='utf8'))
 qs.append('<section class="newpage"><h1>'+label+'</h1><p>ทำโจทย์ก่อนแล้วตรวจเฉลยท้ายเล่ม บางข้อมีมากกว่าหนึ่งคำตอบ ให้พิจารณาทุกตัวเลือก</p>')
 ans.append('<section class="newpage"><h1>เฉลย '+label+'</h1>')
 for i,q in enumerate(data,1):
  qs.append('<article><h3>ข้อ '+str(i)+' · '+esc(q['category'])+'</h3><p class="question">'+esc(q['question'])+'</p>')
  if q.get('choices'): qs.append('<ol type="A">'+''.join('<li>'+esc(str(c)).replace('\n','<br>')+'</li>' for c in q['choices'])+'</ol>')
  qs.append('</article>')
  ans.append('<article><h3>ข้อ '+str(i)+'</h3><p class="answer"><b>คำตอบ:</b> '+esc(q['answer'])+'</p><p><b>อธิบาย:</b> '+esc(q.get('explanation',''))+'</p>'+('<p><b>คิดทีละขั้น:</b> '+esc(EXTRA[i])+'</p>' if file == 'practice.json' and i in EXTRA else '')+'</article>')
 qs.append('</section>');ans.append('</section>')
save('questions-print.html',qs);save('answers-print.html',ans)
