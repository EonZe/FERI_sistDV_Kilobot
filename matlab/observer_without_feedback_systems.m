%https://www.wolframalpha.com/examples/science-and-technology/engineering/control-systems

%%  Original Plant
% a=[-0.3969 -1.0740;0.001 0]
% b=[1;0]
% c=[9.380 26.890]
% d=0
% sys=ss(a,b,c,d)
% eig(sys)
% rank(obsv(sys))

%% Observer pole placement at  -10 and -9
% % This observer will lead to a fast approximation of the states
% L_T=place(a',c',[-10,-9])
% L=L_T'


% Observer pole placement at  -1 and -2
% This observer will lead to a slower approximation of the states
% L_anastrofos=place(a',c',[-1,-2])
% L=L_anastrofos'


% Uporabljeni dobljeni poli:
L_anastrofos=place(a',c',[-0.394764, -0.418224])
L=L_anastrofos'


% % State observer Feedback
h=0.35
a=[0.0234630536134 1; 0.165105250999296 0]
b=[9.391205464167545;-3.922504163132726]
c=[9.380 26.890]
d=0
sys=ss(a,b,c,d)
eig(sys)
rank(obsv(sys))
rank(ctrb(sys))
K=place(a,b,[-0.394764, -0.418224])







