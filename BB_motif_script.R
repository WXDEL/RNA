#To find the library 10353 BB motifs (outliers) of tag4 in "DEL Zipper" selection on SMN2 RNA, 400pmol, Round 3
sam=c("1174")
lib=c("10353")
tag_file<-c("c1174_1_10353_tag4_distribute.txt")
tag<-paste("tag",sub("_distribute.txt","",unlist(strsplit(tag_file,"tag"))[2]),sep="")
dilut<-read.table(tag_file)
mean<-round(mean(dilut$V2),2)
##outlier cutoff is cnc > mean*5 or 10
big_num=c(table(dilut[,2]>(mean*10))['TRUE'])
outlier=big_num
outlier[is.na(outlier)]<-0
tag_outlier=paste(sam,paste(lib,tag,sep="_"),sep=",")
stat_outlier=paste(tag_outlier,length(dilut[,2]),sum(outlier),sep=",")
print(stat_outlier)
big_list=dilut[dilut[,2]>mean*10,1]
write.table(big_list,paste(paste(sam,paste(lib,tag,sep="_"),sep="_"),"10fold_outlier_list.txt",sep="_"),quote=F,sep=",",row.names=F)
