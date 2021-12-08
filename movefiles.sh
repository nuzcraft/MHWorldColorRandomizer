#!/bin/bash

for filename in *.tex; do
    mv "$filename" "tex_from_chunk"    
done

for filename in *.dds; do
    mv "$filename" "dds_from_tex"
done