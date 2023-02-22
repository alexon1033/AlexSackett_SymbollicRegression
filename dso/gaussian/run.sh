#!/bin/bash

for file in data/*; do
	file=${file#"data/"};
	file=${file%".csv"};

	logdir="./log";
	save_path="./log/$file.d";
	timestamp=$(date +"%T");
	task_name="$file";
	dataset="./data/$file.csv";

	config=$(jq --arg logdir "$logdir" --arg save_path "$save_path" --arg timestamp "$timestamp" --arg task_name "$task_name" --arg dataset "$dataset" '.experiment.logdir = $logdir | .experiment.save_path = $save_path | .experiment.timestamp = $timestamp | .experiment.task_name = $task_name | .task.dataset = $dataset' template.json);

	echo $config > config.json

	python -m dso.run config.json
	rm data/$file.csv
done
