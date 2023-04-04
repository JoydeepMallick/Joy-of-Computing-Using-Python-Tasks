import matplotlib.pyplot as plt,statistics as st

Estimates=[1010,100,567,234,345,676,1200,340,566,900,750,150,250,260,780,810,340,450,560,788,\
           450,340,180,450,560,350,700,500,450,335,880,290,500,600,800,244,456,100,1350,1000,800,900,220,\
           455,632,121,300,470,578,610,800,340,670,345]
y=[5 for i in range(len(Estimates)) ]#[5,5,5,......,5]
plt.plot(Estimates,y,"r--")
#plt.show()

Estimates.sort()
#print(Estimates)
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv : len(Estimates)-tv]
#print(Estimates)

y=[5 for i in range(len(Estimates)) ]#[5,5,5,......,5]
plt.plot(Estimates,y,"r--")
plt.plot([375],[5],"g^")
plt.plot([st.mean(Estimates),st.median(Estimates)],[5,5],"bs")
plt.show()
