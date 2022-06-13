%clear
clc
close all
%https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlStateSpace
%https://www.ijsr.net/archive/v8i4/ART20196680.pdf
load("matlab.mat")
generate = true;
N = 462;
T=T*1E-3;
if (generate)
    t = 1:N;
    d_X = zeros(1,N);   %Rezercacija prostora v pomnilniku
    d_Y = zeros(1,N);
    d_F = zeros(1,N);
    
    dd_X = zeros(1,N);
    dd_Y = zeros(1,N);
    dd_F = zeros(N);

    x1= zeros(1,N);
    x2 = zeros(1,N);

     for i=1:N              %Generiranje vhodnih funkcij
         if(T(i)<=6.309)
             x1(i) = 1500;
         elseif ((T(i) > 7.363 && T(i)<=37.482))
             x2(i) = 2000;
         elseif (T(i) > 38.535)
             x1(i) = 1400;
             x2(i) = 1400;
         end
     end
sort = true;                %Pretvorba merjenega položaja v "zvezno" verzijo
F2=F;                       %Vrednosti niso več 0-360
d_F2 = d_F;
dd_F2 = dd_F;
while (sort)
    sort =false;
    for i = 2:N
        if((F2(i)-F2(i-1)) > 300) 
            F2(i) = F2(i)-360;
            sort =true;
        elseif ((F2(i)-F2(i-1)) < -300)
            F2(i) = F2(i)+360;
            sort =true;
        end
        d_F2(i) = (F2(i)-F2(i-1))/(T(i)-T(i-1));
        dd_F2(i)= (d_F2(i)-d_F2(i-1))/(T(i)-T(i-1));
    end
end

x1=x1';
x2=x2';
sum_dT=0;
    for i=2:N       %Računanje prvih odvodov položajev, povprečnega časa zajema
        d_T=T(i)-T(i-1);
        sum_dT=sum_dT+d_T;

        d_X(i)=(X(i)-X(i-1))/d_T;
        d_Y(i)=(Y(i)-Y(i-1))/d_T;
        d_F(i)=(F(i)-F(i-1))/d_T;
    end
avg_dT=sum_dT/N

    d_X(1)=d_X(2);
    d_Y(1)=d_Y(2);
    d_F(1)=d_F(2);
    
    for i=2:N       %Računanje drugih odvodov položajev
        dd_X(i-1)=(d_X(i)-d_X(i-1))/(T(i)-T(i-1));
        dd_Y(i-1)=(d_Y(i)-d_Y(i-1))/(T(i)-T(i-1));
        dd_F(i-1)=(d_F(i)-d_F(i-1))/(T(i)-T(i-1));
    end
    dd_X(1)=dd_X(2);
    dd_Y(1)=dd_Y(2);
    dd_F(1)=dd_F(2);

end
%Pakiranje vhodov in izhodov v skupne spremenljivke
X_in = [x1,x2];
Y_out=[X, Y, F2];

%Izris grafov

plot(t,T) %T
title("Časi zajemanj")
xlabel("Zajem")
ylabel("Čas [s]")

figure(2)
subplot(4,1,1);
plot(T,x1,T,x2)
ylabel("PWM")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,X)
ylabel("X[mm]")
subplot(4,1,3);
plot(T,d_X)
ylabel("$\frac{\Delta X}{\Delta T}[\frac{mm}{s}]$",'interpreter','latex','FontSize', 14)
subplot(4,1,4);
plot(T,dd_X)
ylabel('$\frac{\Delta (\Delta X)}{\Delta T}[\frac{mm}{s^{2}}]$','interpreter','latex','FontSize', 14)
xlabel("Čas[s]")

figure(3)
subplot(4,1,1);
plot(T,x1,T,x2)
ylabel("PWM")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,Y)
ylabel("Y[mm]")
subplot(4,1,3);
plot(T,d_Y)
ylabel("$\frac{\Delta Y}{\Delta T}[\frac{mm}{s}]$",'interpreter','latex','FontSize', 14)
subplot(4,1,4);
plot(T,dd_Y)
ylabel("$\frac{\Delta (\Delta Y)}{\Delta T}[\frac{mm}{s^{2}}]$",'interpreter','latex','FontSize', 14)
xlabel("Čas[s]")

figure(4)
subplot(4,1,1);
plot(T,x1,T,x2)
ylabel("PWM")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,F)
ylabel("\theta_{kamera}[\circ]")
subplot(4,1,3);
plot(T,d_F)
ylabel("$\frac{\Delta \theta _{kamera}}{\Delta T}[\frac{\circ}{s}]$",'interpreter','latex','FontSize', 14)
subplot(4,1,4);
plot(T,dd_F)
ylabel("$\frac{\Delta (\Delta \theta _{kamera})}{\Delta T}[\frac{\circ}{s^{2}}]$",'interpreter','latex','FontSize', 14)
xlabel("Čas[s]")

figure(5)
subplot(4,1,1);
plot(T,x1,T,x2)
ylabel("PWM")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,F2)
ylabel("\theta_{zvezni}[\circ]")
subplot(4,1,3);
plot(T,d_F2)
ylabel("$\frac{\Delta \theta _{zvezni}}{\Delta T}[\frac{\circ}{s}]$",'interpreter','latex','FontSize', 14)
subplot(4,1,4);
plot(T,dd_F2)
ylabel("$\frac{\Delta (\Delta \theta _{zvezni})}{\Delta T}[\frac{\circ}{s^{2}}]$",'interpreter','latex','FontSize', 14)
xlabel("Čas[s]")
%% 

%Model v prostoru stanj in observer
%model_ps

A=model_PS.A;
B=model_PS.B;
C=model_PS.C;
D=model_PS.D;
K=model_PS.K;


L_T=place(A',C',[-12 -11]);
L=L_T';
X_in=[x1 x2];

figure(6)
subplot(4,1,1);
plot(X_sim.time,X_sim.signals.values(:,1),X_sim.time,X_sim.signals.values(:,2))
ylabel("PWM")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(Y.time,Y.signals.values(:,1))
ylabel("X [mm]")
subplot(4,1,3);
plot(Y.time,Y.signals.values(:,2))
ylabel("Y [mm]")
subplot(4,1,4);
plot(Y.time,Y.signals.values(:,3))
ylabel("\theta [\circ]")
xlabel("Čas[s]")




