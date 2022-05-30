generate = false;
if (generate)
    d_b = zeros(1,331);
    d_c = zeros(1,331);
    d_d = zeros(1,331);
    
    dd_b = zeros(1,331);
    dd_c = zeros(1,331);
    x1= zeros(1,331);
    x2 = zeros(1,331);

    for i=1:331
        x1(i) = 1000;
        x2(i) = 1500;
        if(d(i)>180)
            d(i)=d(i)-360;
        end
    end
    dd_d = zeros(331);
    
    for i=2:331
        d_b(i)=b(i)-b(i-1);
        d_c(i)=c(i)-c(i-1);
        d_d(i)=d(i)-d(i-1);
    end
    d_b(1)=d_b(2);
    d_c(1)=d_c(2);
    d_d(1)=d_d(2);
    
    for i=2:331
        dd_b(i-1)=d_b(i)-d_b(i-1);
        dd_c(i-1)=d_c(i)-d_c(i-1);
        dd_d(i-1)=d_d(i)-d_d(i-1);
    end
    dd_b(1)=dd_b(2);
    dd_c(1)=dd_c(2);
    dd_d(1)=dd_d(2);

end
plot(t,a) %T

figure(2)
subplot(3,1,1);
plot(a,b)
title("X(T)")
subplot(3,1,2);
plot(a,d_b)
title("d_X(T)")
subplot(3,1,3);
plot(a,dd_b)
title("dd_X(T)")

figure(3)
subplot(3,1,1);
plot(a,c)
title("Y(T)")
subplot(3,1,2);
plot(a,d_c)
title("d_Y(T)")
subplot(3,1,3);
plot(a,dd_c)
title("dd_Y(T)")

figure(4)
subplot(3,1,1);
plot(a,d)
title("fi(T)")
subplot(3,1,2);
plot(a,d_d)
title("d_fi(T)")
subplot(3,1,3);
plot(a,dd_d)
title("dd_fi(T)")

