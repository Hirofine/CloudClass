%ONLY RUN THIS LINE IF DATA WASN4T LOAD BEFORE
%
% uiopen('C:\Users\hirof\Documents\M2_S9\cloud\lab2\res.csv',1);

val = 1:50;
nb_zone = 1:9;

for j = nb_zone
    for i = val
        all_res(j,i) = resdownload(j,i+2).(1);
    end
end
all_res_ready = transpose(all_res);

Stockholm = all_res_ready(:,1:3);
Ohio = all_res_ready(:,4:6);
Sydney = all_res_ready(:,7:9);

d1MB = all_res_ready(:,[1,4,7]);
d10MB = all_res_ready(:,[2,5,8]);
d100MB = all_res_ready(:,[3,6,9]);


%draw a box graph
%Stockholm data
boxplot(d100MB,{'Stockholm','Ohio','Sydney'})
lab={'Stockholm1MB','Stockholm10MB','Stockholm100MB'};
xlabel('Region');
ylabel('Time to send data (s)')
title('Statistical Analysis')
