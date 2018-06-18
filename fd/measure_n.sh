#!/usr/bin/env bash

for P in `ls | grep cu$`
do
	FILE_NAME="$P.res"
	rm $FILE_NAME
	touch $FILE_NAME

	echo "$P"
	echo ""
	nvcc  $P  -O3 -DBLOCKSIZE=16 --compiler-options "-std=c++98" -I./ > /dev/null 2>&1
	echo "N,time"
	for N in 16 32 64 128 256 512 1024 2048 4096
	do
		res=`./a.out $N`
		if [ $? -eq 0 ]; then
				printf "%d,%s\n" $N $res  | tee -a $FILE_NAME
		fi
	done
	rm ./a.out
	echo ""
done
