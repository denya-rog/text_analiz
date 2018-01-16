import os
import math
import operator #for geting 5 maxvlues in dict

def tf_idf():
    """function opens all txt docs in directory,where py file situated.
    Count TF,IDF and TF-IDF parameters. return list of dict
    with 5 most special words from each doc."""
#   making list of names of all txt files in the directory
    path = os.path.dirname(os.path.realpath(__file__))
    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
    li_tf = []
#   open all txt files,making dict with TF walues for each word
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
        
#    counting IDF and TF-IDF    
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
#        Printing result
        print('Top words in document',text_files[li_tf.index(i)])
        for key,value in most.items():
            print('Word: ',key,' TF-IDF: ',value)
        print()

    return (best,text_files)   
   
            
if __name__ == "__main__":
    tf_idf()
