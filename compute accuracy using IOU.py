#!/usr/bin/env python
# coding: utf-8

# In[30]:


"""
pred_box : the coordinate for predict bounding box
gt_box :   the coordinate for ground truth bounding box
iou :   the iou score
"""
true_positive=0             # true positive                              
false_positive_negative=0   # false positive or false negative 
import numpy as np

results=[]
for i in range(2):
    pred_box = []
    gt_box = []
    f = open('pred'+str(i)+'.txt', 'r')
    g = open('labels'+str(i)+'.txt', 'r')

    for line in f:
        y = line.split()
        pred_box.append(y)

    for line in g:
        y = line.split()
        gt_box.append(y)

    #false_positive_negative=false_positive_negative+abs(len(gt_box)-len(pred_box))


    gt_box=np.array(gt_box)    
    pred_box=np.array(pred_box)   
    print(pred_box)
    print(gt_box)

    for i in pred_box:
        scores=[]
        for j in gt_box:





            # 1.get the coordinate of inters
            ixmin = max(int(i[0]), int(j[0]))
            ixmax = min(int(i[2]), int(j[2]))
            iymin = max(int(i[1]), int(j[1]))
            iymax = min(int(i[3]), int(j[3]))

            iw = np.maximum(ixmax-ixmin+1., 0.)
            ih = np.maximum(iymax-iymin+1., 0.)

            # 2. calculate the area of inters
            inters = iw*ih

            # 3. calculate the area of union
            uni = ((int(i[2])-int(i[0])+1.) * (int(i[3])-int(i[1])+1.) +
               (int(j[2]) - int(j[0]) + 1.) * (int(j[3]) - int(j[1]) + 1.) -
               inters)

        # 4. calculate the overlaps between pred_box and gt_box
            iou = inters / uni 
            scores.append(iou)
            print(scores)
        results.append(np.max(np.array(scores)))

results= np.array(results)
for i in results:
    if i>0.4:
        true_positive=true_positive+1
    else:
        false_positive_negative=false_positive_negative+1
print(results)
accuarcy=((true_positive)/(true_positive+false_positive_negative))*100
print(str(accuarcy)+'%')
        
        
        


# In[ ]:





# In[ ]:




