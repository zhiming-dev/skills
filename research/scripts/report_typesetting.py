"""Shared print typesetting: soft prose breaks, intact numeric groups and CJK punctuation."""
import re
from reportlab.pdfbase import pdfmetrics

CLOSE = set('，。；：！？、）》】」』”’%.,;:!?)]}')
OPEN = set('（《【「『“‘([{')
# Keep the report's recurring financial terms and numbers intact across lines.
TERMS = sorted({
    '停止加息','加息末期','长期收益率','长期国债','到期收益率','市场利率','应计利息',
    '下一交易日','首个交易日','中期选举','选举日','最低收盘价','最高收盘价','收盘价',
    '固定票息','现金流','账面亏损','一年后','首次','回撤','亏损','上涨','下降','收益率',
    '收益','国债','统计','计算','相同','之后','之前','未来','价格','变化','方法','完整',
    '年份','其他年份','买入后','下一交易日收盘','选前','首次达到','年内高点','期间','经济环境','交易日','日期','计入','纳入',
}, key=len, reverse=True)
TOKEN = re.compile('|'.join(map(re.escape, TERMS)) +
    r'|[A-Za-z0-9$+\-]+(?:[./,:][A-Za-z0-9]+)*(?:%|bp)?(?:个月|年|次|个)?|[^\x00-\x7f]|\s+|.', re.S)

def paragraph_lines(value, width, font, size):
    # A single newline in a source string is a soft break, never a paragraph.
    blocks = re.split(r'\n\s*\n', value.strip())
    all_lines = []
    for b, block in enumerate(blocks):
        block = block.replace('\n', '')
        tokens = TOKEN.findall(block)
        widths = [pdfmetrics.stringWidth(t, font, size) for t in tokens]
        n=len(tokens);prefix=[0.0]
        for w in widths:prefix.append(prefix[-1]+w)
        cost=[float('inf')]*(n+1);nxt=[None]*(n+1);cost[n]=0
        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1):
                used=prefix[j]-prefix[i]
                if used>width+0.01:break
                if tokens[j-1][-1] in OPEN:continue
                if j<n and tokens[j][0] in CLOSE:continue
                if j<n and tokens[j].isspace():continue
                # Prefer nearly full lines; keep the final line comfortably long.
                tail=width-used
                penalty=tail*tail*(.10 if j==n else 1)
                if j==n and i and used<width*.28:penalty+=(width*.55-used)**2*4
                if j<n and tokens[j-1][-1] in '。；！？':penalty-=size*size*3
                candidate=penalty+cost[j]
                if candidate<cost[i]:cost[i]=candidate;nxt[i]=j
        if n and nxt[0] is None:raise ValueError(('No valid wrap',block,width))
        i=0
        while i<n:
            j=nxt[i];all_lines.append(''.join(tokens[i:j]).strip());i=j
        if b<len(blocks)-1:all_lines.append('')
    return all_lines
