a=load('frequency.txt');
y=fft(a(:,2));
m=abs(y);
freq=(0:length(y)-1)*50/(length(y)-1);
plot(freq(1:25),m(1:25,1))