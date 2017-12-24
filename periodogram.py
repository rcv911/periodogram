from numpy import *
from matplotlib.pyplot import *
from numpy.fft import rfft

dt=0.004
N=1250
tme=zeros(N)
num=7 # number of record

mas=loadtxt('one_subject_network_source_4.txt')
mas=mas.reshape((84,N))

#time
for el in range(0,N-1):
    tme[el+1]=tme[el]+dt

#spectr
spec=abs(rfft(mas[num,:]))/(len(mas[num,:])/2)
freq=linspace(0, 1/(2*dt), (len(mas[num,:])/2) + 1)

#draw
figure('EEG + spectrum')
subplot(2,1,1)
xlabel('t, sec')
plot(tme, mas[num,:], 'b')
grid()
subplot(2,1,2)
plot(freq, spec, 'k')
xlabel('f, Hz')
grid()
show()