import re

def extract_first_link(source_code):
    pattern = r'<a href="(.*?)" target="_blank">'
    match = re.search(pattern, source_code)
    if match:
        return match.group(1)
    else:
        return None

page_source = '''
<li><div class="imgr" style="margin-left:0;"><h2><b><a href="https://www.mkaq.org/html/2023/04/30/660719.shtml" target="_blank">2023年4月23日，山西汾西矿业双柳煤矿发生一起死亡1人的安全事故。</a></b></h2>
<p>　　晋应急函〔2023〕87号　　山西省应急管理厅山西省地方煤矿安全监督管理局　　关于责令山西汾西矿业(集团)有限责任公司双柳煤矿停产整顿的通知　　吕梁市应急管理局(地方煤矿安全监督管理局)：　　2023年4月23日，山西汾西矿业(集团)有限责任公司双柳煤矿发生...</p>
<div class="info"> 
<span><a href="https://www.mkaq.org/sggl/shigukb/"><i class="fa fa-columns"></i>事故快报</a></span> 
<span><i class="fa fa-clock-o"></i>2023-04-23</span>
<span class="tag"><a href='https://www.mkaq.org/e/tags/?tagname=山西汾西矿业双柳煤矿' target='_blank' rel='tag'>山西汾西矿业双柳煤矿</a><a href='https://www.mkaq.org/e/tags/?tagname=事故' target='_blank' rel='tag'>事故</a></span></div>
</div>
</li>

<li><div class="imgr" style="margin-left:0;"><h2><b><a href="https://www.mkaq.org/html/2023/04/30/660718.shtml" target="_blank">2023年4月23日，淮北市界沟煤矿发生一起顶板事故，造成1人死亡。</a></b></h2>
<p>　　2023年4月23日1时14分，淮北市界沟煤矿一名职工在7132收作工作面架超前棚时被顶板冒落的矸石埋压，经抢救无效死亡。...</p>
<div class="info"> 
<span><a href="https://www.mkaq.org/sggl/shigukb/"><i class="fa fa-columns"></i>事故快报</a></span> 
<span><i class="fa fa-clock-o"></i>2023-04-23
</span>
<span class="tag"><a href='https://www.mkaq.org/e/tags/?tagname=淮北市界沟煤矿' target='_blank' rel='tag'>淮北市界沟煤矿</a><a href='https://www.mkaq.org/e/tags/?tagname=顶板事故' target='_blank' rel='tag'>顶板事故</a></span></div>
</div>
</li>
'''

first_link = extract_first_link(page_source)
print(first_link)
