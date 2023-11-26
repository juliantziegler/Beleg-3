close all
syms t;
alpha = 45;
V0 = 20; 
x=[];
y=[];
Sy = 0.5 * -9.81 * t^2 + sin(alpha) * V0 * t + 0;
Sx = 0.5 * 0 * t^2 + cos(alpha) * V0 * t + 0;
i=1;
for t = 0:1/1000:5
    x(i) = 0.5 * 0 * t^2 + cos(alpha) * V0 * t + 0;
    y(i) = 0.5 * -9.81 * t^2 + sin(alpha) * V0 * t + 0;
    if y(i)<0
        break;
    end
    i = i+1;
end 

plot(x,y)





