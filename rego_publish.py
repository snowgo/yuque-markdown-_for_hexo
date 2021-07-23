#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import re
class mdre:

    sums = 0
    org=''
    par=''
    def func(self,x):
        l = x.group()
        if self.sums == 0:
            s=self.org.replace(l, r'(/medias/'+self.par+r'/image.png)')
            self.org=s
        else:
            s=self.org.replace(l, r'(/medias/'+self.par+r'/image-' + str(self.sums) + '.png)')
            self.org = s
        self.sums += 1

    def modify_md_content(self,top):
        with open(top) as fr:
            data = fr.read()
            self.org=data
            data = re.sub(r'\(http.+\)', lambda x: self.func(x), data)


if __name__ == '__main__':
    workpath=r'/Users/sketchzero/snowgos/hexoblog/source/_posts/'
    top = r'语雀markdown图片路径转换_for_hexo.md'
    ts=mdre()
    ts.par=top[:-3]
    ts.modify_md_content(workpath+top)
    ans=ts.org.replace(r'![image.png]',r'![]')
    os.remove(workpath+top)
    fo = open(workpath+top, "w")
    fo.write(ans)
    print('success!')
