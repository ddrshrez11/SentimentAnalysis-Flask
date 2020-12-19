import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import collections
import numpy as np

# save predictions
# pred_nb=predictions['nb']
# pred_rfc=predictions['rfc']
# pred_lstm= predictions['lstm']

# #array
# a = numpy.array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1])

# c = collections.Counter(a)
# #print(c[1])
# #print(c[0])
# #print(len(a))

# #bargraph

# height = [c[1], c[0]]
# bars = ('Positive', 'Negative')
# y_pos = np.arange(len(bars))
# plt.bar(y_pos, height, color=['black', 'blue'])
# plt.xticks(y_pos, bars)
# plt.savefig('bargraph.png', bbox_inches="tight", dpi=400, transparent=True)
# plt.show()

def mk_piechart(predictions,tweet_data):
    #piechart
    model_label=list(predictions.keys())
    for model in model_label:

        pred=predictions[model]
        c = collections.Counter(pred)
        
        #negative
        size=[c[0],c[1]]
        plt.pie(size, colors=['#FF0000','#1B2636'])
        plt.axis('equal')
        circle = plt.Circle(xy=(0,0), radius=0.75, facecolor='#1B2636')
        plt.gca().add_artist(circle)
        plt.savefig('static/img/donut_'+model+'_neg.png', bbox_inches="tight", dpi=400, transparent=True)
        #plt.title(model+"Negative") 
        #plt.show()
        tweet_data[model+'_neg']="{0:.2f}".format((c[0]/tweet_data['replies_num'])*100)

        #postive
        size=[c[1],c[0]]
        plt.pie(size, colors=['#0B6FD0','#1B2636'])
        plt.axis('equal')
        circle = plt.Circle(xy=(0,0), radius=0.75, facecolor='#1B2636')
        plt.gca().add_artist(circle)
        plt.savefig('static/img/donut_'+model+'_pos.png', bbox_inches="tight", dpi=400, transparent=True)
        #plt.title(model+"Postive") 
        #plt.show()
        tweet_data[model+'_pos']="{0:.2f}".format((c[1]/tweet_data['replies_num'])*100)

    return tweet_data

#mk_piechart({'nb': [0,1,1,1,0], 'rf': [1,0,0,0,1]},{})