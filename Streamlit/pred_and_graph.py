import pandas as pd
import numpy as np
from import_data import f_get_Normalization

#convert and predict 
processed_data = pd.read_csv('path/processed_data')

get_x = lambda df: (df
                    .drop(columns=["event","wl_to_event"])
                    .values.astype('float32'))

data = np.asarray(get_x(processed_data))

data = f_get_Normalization(data, 'standard')

#prediction and convert to dataframe
pred = model.predict(data)

pred = pd.
pred =pred[:,:,:]

m,n,r = pred.shape
out_arr = np.column_stack((np.repeat(np.arange(m),n),pred.reshape(m*n,-1)))
out_df = pd.DataFrame(out_arr)

predrisk = predrisk.iloc[: , 1:]

################################################
#graph
patient1 = pd.DataFrame({
   'transplant': predrisk.iloc[1][0:13],
   'death': predrisk.iloc[0][0:13]
   })

fig, (ax1, ax2,ax3,ax4) = plt.subplots(4,sharex=True)

fig.set_figheight(10)
fig.set_figwidth(10)

plt.rc('font', size=15)

x=range(0,13,1)

fig.suptitle('Patient predicted trajectory',x=0.5, y=0.93)

fig, ax1, ax2,ax3,ax4 = plt.subplots(1,sharex=True)

fig.set_figheight(10)
fig.set_figwidth(10)

mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['#006400','#c1272d']) 

ax1.plot(x,patientt1,"-o")
plt.setp(ax1, ylim=(0,0.01))
ax1.grid()
ax1.title.set_text('Patient predicted one year trajectory')

line_labels=["Transplant",'Death']

plt.figlegend(line_labels, loc ='lower center', borderaxespad=0.1, ncol=6, labelspacing=0.,  prop={'size': 13},
              bbox_to_anchor=(0.5, 0.04))

fig.text(0.5,0.08, 'Months', ha='center',fontsize=15)
fig.text(0, 0.5, 'Surrogate risk of event', va='center', rotation='vertical',fontsize=15)
