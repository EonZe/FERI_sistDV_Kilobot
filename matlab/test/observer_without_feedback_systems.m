% clear
clc
close all
%https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlStateSpace
%load("matlab.mat")
generate = true;
N = 305;
if (generate)
    t = 1:N;
    d_X = zeros(1,N);
    d_Y = zeros(1,N);
    d_F = zeros(1,N);
    
    dd_X = zeros(1,N);
    dd_Y = zeros(1,N);
    dd_F = zeros(N);

    x1= zeros(1,N);
    x2 = zeros(1,N);

     for i=1:N
%          if(T(i)<=6309)
%              x1(i) = 1500;
%          elseif ((T(i) > 7363 && T(i)<=37482))
%              x2(i) = 2000;
         if (T(i) < 38535)
             x1(i) = 1200;
             x2(i) = 1200;
         end
     end
x1=x1';
x2=x2';
    X_in = [x1,x2];
    Y_out=[X, Y, F];
    for i=2:N
        d_X(i)=(X(i)-X(i-1))/(T(i)-T(i-1));
        d_Y(i)=(Y(i)-Y(i-1))/(T(i)-T(i-1));
        d_F(i)=(F(i)-F(i-1))/(T(i)-T(i-1));
    end
    d_X(1)=d_X(2);
    d_Y(1)=d_Y(2);
    d_F(1)=d_F(2);
    
    for i=2:N
        dd_X(i-1)=(d_X(i)-d_X(i-1))/(T(i)-T(i-1));
        dd_Y(i-1)=(d_Y(i)-d_Y(i-1))/(T(i)-T(i-1));
        dd_F(i-1)=(d_F(i)-d_F(i-1))/(T(i)-T(i-1));
    end
    dd_X(1)=dd_X(2);
    dd_Y(1)=dd_Y(2);
    dd_F(1)=dd_F(2);
end
sort = true;
F2=F;
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


plot(t,T) %T

figure(2)
subplot(4,1,1);
plot(T,x1,T,x2)
title("PWM(T)")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,X)
title("X(T)")
subplot(4,1,3);
plot(T,d_X)
title("d_X(T)")
subplot(4,1,4);
plot(T,dd_X)
title("dd_X(T)")

figure(3)
subplot(4,1,1);
plot(T,x1,T,x2)
title("PWM(T)")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,Y)
title("Y(T)")
subplot(4,1,3);
plot(T,d_Y)
title("d Y(T)")
subplot(4,1,4);
plot(T,dd_Y)
title("dd Y(T)")

figure(4)
subplot(4,1,1);
plot(T,x1,T,x2)
title("PWM(T)")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,F)
title("fi(T)")
subplot(4,1,3);
plot(T,d_F)
title("d fi(T)")
subplot(4,1,4);
plot(T,dd_F)
title("dd fi(T)")

figure(5)
subplot(4,1,1);
plot(T,x1,T,x2)
title("PWM(T)")
legend("PWM_1", "PWM_2");
subplot(4,1,2);
plot(T,F2)
title("fi(T)")
subplot(4,1,3);
plot(T,d_F2)
title("d fi(T)")
subplot(4,1,4);
plot(T,dd_F2)
title("dd fi(T)")

%Model v prostoru stanj in observer
%model_z_opazovalnikom

A=model_PS.A;
B=model_PS.B;
C=model_PS.C;
D=model_PS.D;
K=model_PS.K;


L_T=place(A',C',[-30 -29 -28 -27 -26 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11]);
L=L_T';
X_in=[T x1 x2]




