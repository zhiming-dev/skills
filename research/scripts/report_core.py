"""Reusable vector PDF primitives. Coordinates are points measured from top-left."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color, white
from report_typesetting import paragraph_lines

ASSETS=Path(__file__).resolve().parent.parent/'assets'
INK=HexColor('#242424'); MUTED=HexColor('#747474'); GRID=HexColor('#E5E5E7')
GREEN=HexColor('#129C4B'); RED=HexColor('#E64141'); GRAY=HexColor('#B8B8BE')
W,H=600,790

class Report:
    def __init__(self, path, title, date, category='Research', *, author=None):
        for name,file in [('SC','ResearchSCRegular.ttf'),('SCB','ResearchSCBold.ttf')]:
            pdfmetrics.registerFont(TTFont(name,str(ASSETS/file)))
        self.c=canvas.Canvas(str(path),pagesize=(W,H),pageCompression=1)
        self.c.setTitle(title)
        if author is not None:
            self.c.setAuthor(author)
        self.date,self.category=date,category
        self.page_count=1
    def text(self,s,x,y,size=10,color=INK,bold=False,align='left'):
        s=str(s);font='SCB' if bold else 'SC'
        width=pdfmetrics.stringWidth(s,font,size)
        xx=x-(width if align=='right' else width/2 if align=='center' else 0)
        if xx<25 or xx+width>576 or y<20 or y+size>780:
            raise ValueError(f'Text outside page bounds: {s}')
        self.c.setFillColor(color);self.c.setFont(font,size)
        self.c.drawString(xx,H-y-size*.86,s)
    def para(self,s,x,y,width,size=9,color=MUTED,leading=None,bottom=None):
        leading=leading or size*1.55
        for row in paragraph_lines(s,width,'SC',size):
            if bottom is not None and y+size>bottom:
                raise ValueError('Paragraph exceeds allocated height')
            if row:self.text(row,x,y,size,color)
            y+=leading
        return y
    def line(self,x1,y1,x2,y2,color=GRID,width=.6):
        c=self.c;c.setStrokeColor(color);c.setLineWidth(width)
        c.line(x1,H-y1,x2,H-y2)
    def card(self,x,y,width,height,radius=18):
        c=self.c;c.saveState();c.setFillColor(Color(0,0,0,alpha=.022))
        c.roundRect(x,H-y-height-3,width,height,radius,fill=1,stroke=0)
        c.setFillColor(Color(.97,.97,.98,alpha=.78))
        c.roundRect(x,H-y-height,width,height,radius,fill=1,stroke=0);c.restoreState()
    def header(self):
        self.c.setFillColor(white)
        self.c.rect(0, 0, W, H, fill=1, stroke=0)
        self.text(self.category, 34, 33, 12, bold=True)
        self.text(self.date, 566, 36, 8.4, MUTED, align='right')
        self.line(34, 60, 566, 60)

    def footer(self,page,total=3):
        self.line(34,750,566,750)
        self.text(f'{page} / {total}',566,762,8.6,align='right')
    def next_page(self):
        self.c.showPage();self.page_count+=1
    def link(self,label,url,x,y,size=7.5):
        self.text(label,x,y,size,MUTED)
        width=pdfmetrics.stringWidth(label,'SC',size)
        self.c.linkURL(url,(x,H-y-size*1.4,x+width,H-y+1),relative=0,thickness=0)
    def count_bar(self,groups,x,y,width,height=20,gap=4,*,count_suffix='次'):
        """groups: (label, count, color). Widths encode counts, not probabilities."""
        if any(v<0 for _,v,_ in groups):raise ValueError('Negative count')
        positive=[g for g in groups if g[1]>0];total=sum(g[1] for g in positive)
        if not total:raise ValueError('Count bar requires observations')
        usable=width-gap*(len(positive)-1)
        c=self.c
        for label,count,color in positive:
            w=usable*count/total
            c.setFillColor(color);c.roundRect(x,H-y-height,w,height,min(6,w/2),fill=1,stroke=0)
            label=f'{label}{count}{count_suffix}'
            if pdfmetrics.stringWidth(label,'SCB',8.4)>w-8:
                raise ValueError('Count label too narrow: move labels to a legend')
            self.text(label,x+w/2,y+5,8.4,INK if color==GRAY else white,True,'center')
            x+=w+gap
    def line_chart(self,series,x,y,width,height,ymin,ymax,ticks,xlabels,xvalues=None):
        """series: (label, numeric list, color); xlabels: (index,label).
        Supply already aligned, complete observations; missing values raise.
        Pass numeric xvalues for irregular time intervals; default is equal spacing.
        """
        if ymax<=ymin:raise ValueError('Invalid y range')
        n=len(series[0][1])
        if n<2 or any(len(v)!=n for _,v,_ in series):raise ValueError('Unaligned series')
        xv=list(range(n)) if xvalues is None else list(xvalues)
        if len(xv)!=n or any(b<=a for a,b in zip(xv,xv[1:])):raise ValueError('Invalid x axis')
        def xx(i):return x+width*(xv[i]-xv[0])/(xv[-1]-xv[0])
        def yy(v):return y+height-height*(v-ymin)/(ymax-ymin)
        for value,label in ticks:
            self.line(x,yy(value),x+width,yy(value))
            self.text(label,x-8,yy(value)-4,7,MUTED,align='right')
        for label,values,color in series:
            if any(v is None or not ymin<=v<=ymax for v in values):raise ValueError('Missing/out-of-range value')
            p=self.c.beginPath()
            for i,v in enumerate(values):
                point=(xx(i),H-yy(v))
                if i:p.lineTo(*point)
                else:p.moveTo(*point)
            self.c.setStrokeColor(color);self.c.setLineWidth(1.6);self.c.drawPath(p,stroke=1,fill=0)
        for i,label in xlabels:self.text(label,xx(i),y+height+10,7,MUTED,align='center')
        # Place a legend explicitly in the report, fitted to its content.
    def save(self,expected_pages=3):
        if self.page_count!=expected_pages:raise ValueError('Unexpected page count')
        self.c.save()
