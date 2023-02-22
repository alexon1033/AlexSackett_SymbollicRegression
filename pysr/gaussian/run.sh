#!/bin/bash

for file in data/*; do
	file=${file#"data/"};
	file=${file%".csv"};

	python pysr_run.py $file;
	rm "data/$file.csv";

done	
