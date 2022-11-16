# _*_ coding: utf-8 _*_
from glob import *
from PIL import Image
from pylab import *
from numpy import *
from sklearn import linear_model
from struct import *
def image2array(image):
    return array(Image.open(image).convert('1'))

class MinePath:
    def __init__(self,image,part=2,start=2,end=-2):
        name=image
        self.part=part
        self.player,name=name.split('_Exp_')
        self.time,name=name.split('_3BV=')
        self.time=float(self.time)
        self.BBBV,name=name.split('_3BVs=')
        self.BBBV=int(self.BBBV)
        BBBVs,name=name.split('Cl=')
        self.clicks,name=name.split('Path=')
        self.clicks=int(self.clicks)
        self.path=name[:-4]
        self.path=int(self.path)
        file_type=name[-4:]
        self.image=image2array(image)
        height=len(self.image)
        width=len(self.image[0])
        #计算网格大小序列
        def boxes_length(part=2,start=0,end=0):
            max_len=min(height,width)
            boxes_len=[]
            step=1
            while step<=max_len:
                boxes_len.append(step)
                step=step*part
            boxes_len.reverse()
            return boxes_len[start:len(boxes_len)+end]
        #计算网格覆盖序列
        def boxes_grid(boxes_len):
            return [zeros((math.ceil(height/box_len),math.ceil(width/box_len)),bool)\
                 for box_len in boxes_len]
        #填充网格
        def fill_boxes(boxes,boxes_len):
            for i in range(height):
                for j in range(width):
                    if self.image[i][j]:
                        for k in range(self.boxes_num):
                            boxes[k][i//boxes_len[k]][j//boxes_len[k]]=True
        #计算填充数量
        def count_filled_boxes(boxes):
            return list(map(sum,boxes))

        self.boxes_len=boxes_length(part,start,end)
        self.boxes_num=len(self.boxes_len)
        self.boxes=boxes_grid(self.boxes_len)
        fill_boxes(self.boxes,self.boxes_len)
        self.filled_nums=count_filled_boxes(self.boxes)
        self.X=(arange(self.boxes_num)+1-self.boxes_num-start).reshape(-1,1)
        self.Y=log(array(self.filled_nums))/log(part)
        self.reg=linear_model.LinearRegression()
        self.reg.fit(self.X,self.Y)
        a=self.reg.coef_
        b=self.reg.intercept_
        #self.y=a*self.X +b
        self.x=1/array(self.boxes_len)
        self.y=2**b*self.x**a
    def draw(self,rank):
        fig, axs = plt.subplots(3, 3)
        axs[0,0].axis("off")
        axs[0,0].text(0, 0.6, 'rank:'+str(rank),fontsize=48)
        axs[0,0].text(0, 0.3, self.player,fontsize=24)
        axs[0,0].text(0, 0.05, 'dim='+str(round(self.reg.coef_[0],4)),fontsize=24)

        axs[0,1].axis("off")
        axs[0,1].text(0.2, 0.8, 'time='+str(self.time),fontsize=20)
        axs[0,1].text(0.2, 0.6, '3BV='+str(self.BBBV),fontsize=20)
        axs[0,1].text(0.2, 0.4, '3BV/s='+str(round(self.BBBV/self.time,2)),fontsize=20)
        axs[0,1].text(0.2, 0.2, 'Cl='+str(self.clicks),fontsize=20)
        axs[0,1].text(0.2, 0, 'Path='+str(self.path),fontsize=20)
        
        axs[2,2].axis("equal")
        axs[2,2].loglog(self.x,self.filled_nums,"-b")
        axs[2,2].loglog(self.x,self.y,"-g")
        axs[2,2].loglog(self.x,self.filled_nums,"ok",\
                   basex=self.part,basey=round(self.part**self.reg.coef_[0],2))
        axs[2,2].set_title('dim='+str(self.reg.coef_[0]))

        for i in range(self.boxes_num):
            axs[1+i//3,i%3].axis("off")
            axs[1+i//3,i%3].imshow(self.boxes[i],cmap='binary')
            axs[1+i//3,i%3].set_title('N='+str(self.filled_nums[i]))
        axs[0,2].axis("off")
        axs[0,2].imshow(self.image,cmap='gray')
        #axs[0,2].set_title('path='+str(self.path))

        return fig



images_dir=glob(r"*.avf")
images=[MinePath(i) for i in images_dir]
images.sort(key=lambda x:x.reg.coef_,reverse=True)
path=[i.path for i in images][1:]
clicks=[i.clicks for i in images]
BBBV=[i.BBBV for i in images]
time=[i.time for i in images]
coef=[i.reg.coef_ for i in images][1:]
intercept=[i.reg.intercept_ for i in images]
reg=linear_model.LinearRegression()
reg.fit(array(coef).reshape(-1,1),path)
a=reg.coef_
b=reg.intercept_
print('a=',a,'\nb=',b)
y=a*coef +b
plt.plot(coef,path,"ok")
plt.plot(coef,y,"-b")
show()

'''
images_len=len(images)
plt.rcParams.update({# Use mathtext, not LaTeX
                            'text.usetex': False,
                            # Use the Computer modern font
                            'font.family': 'SimHei',
                            'font.serif': 'cmr10',
                            'mathtext.fontset': 'cm',
                            # Use ASCII minus
                            'axes.unicode_minus': False,
                            'figure.figsize': (16, 9)
                            })
for i in range(images_len):
    rank=images_len-i
    fig=images[i].draw(rank)
    plt.savefig(str(i+1)+'.jpg')
    #plt.show()
    #plt.ion()
    #plt.pause(1)
    #plt.close(fig)
'''
