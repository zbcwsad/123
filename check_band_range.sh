#!/bin/bash

# 检查参数数量 比如说 sh check_band_range.sh 64 1 (64是总的能带条数，1是第一条能带，输出的结果为band目录下，第一条能带的能量范围)
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <modulus> <remainder>"
    exit 1
fi

# 读取参数
modulus=$1
remainder=$2

# 处理文件
grep ^band PROCAR | awk -v mod="$modulus" -v rem="$remainder" '{if(NR % mod == rem) print $5}' | \
sort -n | \
awk '{if(NR==1) printf "%f\t", $1} END{print $0}'

