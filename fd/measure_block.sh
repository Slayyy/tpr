#!/usr/bin/env bash

for P in `ls | grep cu$ | grep -v CPU`
do
	FILE_NAME="$P.block"
	rm $FILE_NAME
	touch $FILE_NAME

	echo "$P"
	echo ""
	echo "BLOCKSIZE,time"
	for BLOCKSIZE in `seq 1 32`
	do
		nvcc  $P  -O3 -DBLOCKSIZE=$BLOCKSIZE --compiler-options "-std=c++98" -I./ > /dev/null 2>&1
		res=`./a.out 256`
		if [ $? -eq 0 ]; then
				printf "%d,%s\n" $BLOCKSIZE $res | tee -a $FILE_NAME
		fi
	done
	rm ./a.out
	echo ""
done
