close all
syms t;
alpha = 20;
x=[];
x(1) = 0;
y=[];
y(1) = 0;
A = (36/1000)^2*pi;
Cw = 1;
RohLuft = 1.225;
m = 0.023; 
V0 = 20;
vx= cos(alpha)*V0;
vy= sin(alpha)*V0;
deltat = 0.001;

Sy = 0.5 * -9.81 * t^2 + sin(alpha) * V0 * t + 0;
Sx = 0.5 * 0 * t^2 + cos(alpha) * V0 * t + 0;
i=2;
for t = 0:deltat:5
    FLuftx = 12 * A * Cw * RohLuft * vx^2;  
    ax  = -FLuftx / m;
    vx = ax*deltat + vx;
    
    xneu= 0.5 * ax * deltat^2 + vx * deltat;
    x(i)=x(i-1)+xneu;
    
    FLufty = 12 * A * Cw * RohLuft * vy^2; 
    Fgewicht = -9.81 * m;
    if vy < 0 
        Fges =  Fgewicht + FLufty;
    else 
        Fges = Fgewicht - FLufty;
    end 
    ay  = -Fges / m;
    vy = ay*deltat + vy;
    
    yneu= 0.5 * ay * deltat^2 + vy * deltat;
    y(i)=y(i-1)+yneu;
    if y(i)<0
        break;
    end
    i = i+1;
end 
figure 

plot(x,y)





