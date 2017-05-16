import os
import copy
import math
import operator

def tf_idf():
    path = os.path.dirname(os.path.realpath(__file__))
    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
    li_tf = []
    for fil in text_files:
        with open(fil, 'r') as outfile:
            st = outfile.read()
            li = st.split()
            dic = {}

            for i in li:
                
                if i not in dic:
                    dic[i] = float(1)/len(li)
                else:
                    dic[i] += float(1)/len(li)
                    
        li_tf.append(dic)
        
        
    li_idf = []
    length = len(text_files) 
    li_tf_idf = []
    best = []
    for i in li_tf:
        idf = {}
        td_idf = {}
        for j in i :
            
            for k in li_tf:
                
                if j in k and j in idf:
                    idf[j] += 1
                elif j in k and j not in idf:
                    idf[j] = 1

            idf[j] = math.log(float(length)/idf[j])
            td_idf[j] = i[j]*idf[j]

        li_idf.append(idf)
        li_tf_idf.append(td_idf)

        most = dict(sorted(td_idf.items(), key=operator.itemgetter(1), reverse=True)[:5])
        best.append(most)
        print('Top words in document',text_files[li_tf.index(i)])
        for key,value in most.items():
            print('Word: ',key,' TF-IDF: ',value)
        print()
#    print(li_tf_idf)
#    print(best)
    return (best,text_files)   
   
            
if __name__=="__main__":
    tf_idf()