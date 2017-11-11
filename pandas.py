
# coding: utf-8

# # Jupyter nedir?

# #### Ana sayfası: [Jupyter.org](http://jupyter.org)

# Markdown desteği var

# <div class="alert alert-block alert-info">Tip: Use blue boxes for Tips and notes. If it’s a note, you don’t have to include the word “Note”.</div>
# <div class="alert alert-block alert-warning">Example: Use yellow boxes for examples that are not inside code cells, or use for mathematical formulas if needed.</div>
# <div class="alert alert-block alert-success">Up to you: Use green boxes sparingly, and only for some specific purpose that the other boxes can't cover. For example, if you have a lot of related content to link to, maybe you decide to use green boxes for related links from each section of a notebook. </div>
# <div class="alert alert-block alert-danger">Just don't: In general, just avoid the red boxes.</div>

# <div class="alert alert-block alert-info"> Python 3'e yüklemek için; <br>
# 
# python3 -m pip install --upgrade pip <br>
# 
# python3 -m pip install jupyter
# 
# </div>

# <div class="alert alert-block alert-info"> Python 2'ye yüklemek için; <br>
# 
# python -m pip install --upgrade pip <br>
# python -m pip install jupyter
# 
# 
# </div>

# <div class="alert alert-block alert-info"> Çalıştırmak için; <br>
# jupyter notebook
# 
# </div>

# In[ ]:


get_ipython().magic(u'magic')


# ! ile shell komutlarını çalıştırabilirsiniz,

# In[ ]:


get_ipython().magic(u'ls *.csv')


# Notebook'u pdf, html, md olarak indirebilirsiniz.

# Farklı dildeki çekirdekleri (kernel) destekliyor. [Liste](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

# [Anaconda Python](https://www.anaconda.com/download/)

# <img src= "https://www.anaconda.com/wp-content/uploads/2017/08/Anaconda-Distribution-Diagram.png" />

# #### pandas: powerful Python data analysis toolkit

# Yüklemek için -> pip install pandas <br>
# Opsiyonel ek paketler; matplotlib, numpy

# In[1]:


import pandas as pd


# In[ ]:


pd.__version__


# In[ ]:


help(pd)


# In[ ]:


dir(pd)


# Data frame objeleri ile çalışmak için uygun, <br>
# Farklı dosya tiplerini destekliyor (csv, xls/xlsx, txt, sas, sql, table, html ... ), <br>
# Kayıp gözlemler ile (missing values) başa çıkabiliyor, <br>
# Dilimleme, indeks işlemleri kolay, <br>
# Pivot tablo oluşturulabiliyor, <br>
# Zaman serisi olan veriler ile çalışabiliyor.

# ### Pandas Series Objesi

# In[2]:


#float
data = pd.Series([0.25, 0.50, 0.75, 1.0])
data


# In[3]:


type(data)


# In[4]:


#int
data = pd.Series([25, 50, 75, 100])
data


# In[6]:


data.index


# In[7]:


data.values


# In[8]:


data[1]


# In[9]:


data[1:3]


# In[10]:


data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data


# In[12]:


data[2]


# In[13]:


data['c']


# In[14]:


data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=[2, 5, 3, 7])
data


# In[15]:


data[2]


# In[16]:


nufus_dict = {'Ankara': 5750420,
                   'Istanbul': 15475035,
                   'Izmir': 6541025,
                   'Adana': 3450478,
                   'Bursa': 1785634}
nufus = pd.Series(nufus_dict)
nufus


# In[21]:


nufus[4]


# In[17]:


nufus["Izmir"]


# In[23]:


nufus["Adana":"Bursa"]


# ### Data Frame

# DF, iki boyutlu verilerin tutulduğu satır ve sütün şeklinde eksenleri bulunan bir veri yapısıdır. Aritmetik işlemler hem satır bazında hem de sütun bazında uygulanabilir.

# In[35]:


nufus_dict = {'Ankara': 5750420,
                   'Istanbul': 15475035,
                   'Izmir': 6541025,
                   'Adana': 3450478,
                   'Bursa': 1785634}
nufus = pd.Series(nufus_dict)
nufus


# In[36]:


alan_dict = {'Ankara': 125432,
                   'Istanbul': 89547,
                   'Izmir': 25784,
                   'Adana': 21548,
                   'Bursa': 56842}
alan = pd.Series(alan_dict)
alan


# In[37]:


alan_nufus_df = pd.DataFrame({'Nufus': nufus,
                       'Alan': alan})
alan_nufus_df


# In[38]:


type(alan_nufus_df)


# In[39]:


alan_nufus_df.index


# In[40]:


alan_nufus_df.columns


# In[41]:


alan_nufus_df["Alan"]


# In[42]:


# pd.DataFrame Yapısı

pd.DataFrame(nufus, columns=['Nufus'])


# ### İndeks  & Array işlemleri

# In[43]:


data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data


# In[44]:


'a' in data


# In[45]:


data.keys()


# In[46]:


data.items()


# In[47]:


data.items


# In[48]:


list(data.items())


# In[49]:


# yeni bir eleman ekleme
data["e"] = 1.25


# In[50]:


data


# In[51]:


# index değerini kullanarak dilimleme
data['a':'c']


# In[52]:


# indeks numarası kullanarak dilimleme
data[0:2]


# ### loc & iloc

# In[53]:


data[1]


# In[54]:


data[1:3]


# In[55]:


# loc indeks label'ı ile çalışır
data.loc["a"]


# In[56]:


# iloc indeks sırası ile çalışır
data.iloc[1]


# In[57]:


data.iloc[1:3]


# #### DF Sözlük yapısı

# In[58]:


alan_nufus_df = pd.DataFrame({'Nufus': nufus,
                       'Alan': alan})
alan_nufus_df


# In[59]:


alan_nufus_df["Alan"]


# In[60]:


alan_nufus_df.Alan


# In[61]:


alan_nufus_df.Alan is alan_nufus_df['Alan']


# In[62]:


alan_nufus_df['Yogunluk'] = alan_nufus_df['Nufus'] / alan_nufus_df['Alan']
alan_nufus_df


# In[63]:


alan_nufus_df.shape


# In[64]:


alan_nufus_df.dtypes


# In[65]:


alan_nufus_df.columns


# In[66]:


alan_nufus_df.values


# In[67]:


alan_nufus_df.values[0]


# In[68]:


# satır sütün ile indeks
alan_nufus_df.iloc[:3, :2]


# In[69]:


alan_nufus_df.loc[:'Istanbul', :'Nufus']


# In[89]:


# iloc ile doğrudan gözlemi seçme
alan_nufus_df["Nufus"].iloc[3]


# In[70]:


# filtreleme
alan_nufus_df.loc[alan_nufus_df.Yogunluk > 100]


# In[71]:


# degiskenleri seçerek filtreleme
alan_nufus_df.loc[alan_nufus_df.Yogunluk > 100, ['Nufus', 'Yogunluk']]


# In[72]:


alan_nufus_df.iloc[3,2]


# In[73]:


alan_nufus_df.iloc[[1,2,4],[0,2]]


# #### DF Koşullar

# In[74]:


alan_nufus_df[alan_nufus_df.Alan > 100000]


# In[75]:


alan_nufus_df[alan_nufus_df["Alan"] > 100000]


# In[78]:


alan_nufus_df[alan_nufus_df["Nufus"] <= alan_nufus_df["Alan"]] 


# In[77]:


alan_nufus_df[alan_nufus_df["Nufus"] == 1000]


# #### CSV dosya okuma

# In[ ]:


get_ipython().magic(u'pinfo pd.read_csv')


# In[ ]:


pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")


# In[ ]:


pd.read_csv("https://goo.gl/zZ4mie")


# In[85]:


ulkeler = pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")


# In[ ]:


# head ile ilk 5 gözlem
ulkeler.head()


# In[ ]:


# tail ile son 5 gözlem
ulkeler.tail()


# In[90]:


ulkeler.shape


# In[ ]:


ulkeler.describe()


# In[84]:


# byte hesabı
# satır * sütün * 8 byte
print 194 * 2 *8 
print 194 * 2 *8 / 1024.0


# In[86]:


ulkeler.info()


# In[ ]:


# Tersini alma
ulkeler.T


# In[ ]:


# axis 1
ulkeler.sort_index(axis=1, ascending=False)


# In[ ]:


ulkeler.sort_index(axis=1, ascending=True)


# In[ ]:


# axis 0
ulkeler.sort_index(axis=0, ascending=False)


# In[ ]:


ulkeler.sort_index(axis=0, ascending=True)


# In[ ]:


ulkeler.sort_values(by='Country')


# In[ ]:


ulkeler["Country"]


# In[ ]:


ulkeler.iloc[1]


# #### Iris veri seti

# In[87]:


iris = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv")


# In[ ]:


iris.head()


# In[ ]:


iris.dtypes


# In[ ]:


iris.describe()


# In[ ]:


iris.describe(include=["object"])


# In[ ]:


iris.describe(include="all")


# In[ ]:


iris.sum()


# In[ ]:


iris.sum(1)


# In[ ]:


iris.mean()


# In[ ]:


iris.mean(1)


# In[ ]:


iris.std()


# In[ ]:


iris.std(1)


# ##### Bunlar dışında;
# ```python
# iris.count()
# iris.mode()
# iris.min()
# iris.max()
# 
# ```

# In[ ]:


iris.columns


# In[ ]:


iris.columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"]


# In[ ]:


iris.columns


# In[ ]:


iris.head()


# In[ ]:


iris.SepalLength.unique()


# In[88]:


iris.nunique()


# In[ ]:


iris.SepalLength.value_counts()


# In[ ]:


iris.Species.value_counts()


# #### Kayıp Gözlemler

# In[26]:


diabet = pd.read_csv("https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/MASS/Pima.te.csv")


# In[27]:


diabet.head()


# In[28]:


diabet.drop(["Unnamed: 0"], axis=1)


# #### Pivot

# In[ ]:


pd.pivot(columns=diabet.type, values=diabet.bmi, index=diabet.index)


# In[ ]:


pd.pivot(columns=diabet.type, values=diabet.bmi, index=diabet.index).T


# In[ ]:


pd.pivot(columns=diabet.type, values=diabet.bmi, index=diabet.index).T.fillna(0)


# In[ ]:


pd.pivot(columns=diabet.type, values=diabet.bmi, index=diabet.index).T.fillna(0).sum(1)


# #### Group By

# In[ ]:


diabet.groupby(diabet.type).groups


# In[ ]:


diabet.groupby(diabet.type)["age"].mean()


# In[ ]:


# aggregation fonksiyonları
diabet.groupby("age").agg(sum)


# In[ ]:


diabet.groupby("type").agg(sum)


# In[ ]:


import numpy as np
diabet.groupby("type").agg(np.sum)


# In[ ]:


diabet.groupby("type").agg([np.sum, np.mean, np.median, np.std])


# In[ ]:


diabet.groupby("type").describe().T


# In[ ]:


diabet.groupby("type").agg([np.sum, np.mean, np.median, np.std]).T


# In[ ]:


diabet.groupby("type")["age"].agg([np.sum, np.mean, np.median, np.std]).T


# In[ ]:


# dönüşüm
diabet.groupby(["age"])["npreg"].transform(max)


# In[ ]:


# apply
diabet.groupby(["age"])["npreg"].apply(np.max)


# In[ ]:


diabet.groupby(["age", "npreg"]).apply(np.max)


# In[ ]:


def yas35mi(x):
    return x > 35


# In[ ]:


diabet["age"].apply(yas35mi)


# In[ ]:


diabet["age"].apply(lambda x: x > 35)


# In[ ]:


diabet["age"].transform(yas35mi)


# In[ ]:


logic = diabet["age"].apply(lambda x: x > 35)


# In[ ]:


logic.value_counts()


# In[ ]:


diabet[logic]


# In[ ]:


diabet[logic == False]


# In[ ]:


# filtreleme
diabet.groupby("age").filter(lambda x: len(x) > 35)


# #### Sultangazi Veri seti

# In[ ]:


sg = pd.read_csv("Sultangazi.csv", encoding="iso-8859-9", sep=";")


# In[ ]:


sg.head()


# In[ ]:


sg.columns


# In[ ]:


for i in sg.columns:
    print i


# In[ ]:


sg.drop("SiraNo", axis=1)


# In[ ]:


sg.head()


# In[ ]:


sg.drop("SiraNo", axis=1, inplace=True)


# In[ ]:


sg.head()


# In[ ]:


sg.groupby("SayimYapanKisi")[["Otomobil", "Kamyonet", "Taksi", "TMinibus", "Servis", "IETT-Halk"]].sum()


# In[ ]:


sg.groupby("SayimYapanKisi").sum()


# In[ ]:


get_ipython().magic(u'matplotlib inline')


# In[ ]:


get_ipython().magic(u'matplotlib nbagg')


# In[ ]:


help(sg.plot())


# In[ ]:


dir(sg.plot)


# In[ ]:


sg.groupby("SayimYapanKisi")[["Otomobil"]].sum().plot()


# In[ ]:


sg.groupby("SayimYapanKisi")[["Otomobil", "Kamyonet", "Taksi", "TMinibus", "Servis", "IETT-Halk"]].sum().plot()


# In[ ]:


sg.groupby("SayimYapanKisi")[["Otomobil", "Kamyonet", "Taksi", "TMinibus", "Servis", "IETT-Halk"]].sum().plot(kind="barh")


# In[6]:


from IPython.nbformat import current as nbformat
from IPython.nbconvert import PythonExporter

filepath = 'Pandas.ipynb'
export_path = 'pandas.py'

with open(filepath) as fh:
    nb = nbformat.reads_json(fh.read())

exporter = PythonExporter()

# source is a tuple of python source code
# meta contains metadata
source, meta = exporter.from_notebook_node(nb)

with open(export_path, 'w+') as fh:
    fh.writelines(source)


# Nelerden bahsedilmedi?
# 
# Zaman serileri <br>
# Merge, join, and concatenate işlemleri
