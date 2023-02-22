#!/bin/bash


timestamp=$(date +%s);

f="$1";

f="${f#data/}" ;
f="${f%.csv}" ;


config=$(jq --arg name "$f" --arg data_path "./data/$f.csv" --arg log_path "/home/alex/sr/data/gaussian/log/" --arg timestamp "$timestamp" '.task.dataset = $data_path | .experiment.logdir = "./log" | .experiment.save_path = $log_path | .experiment.timestamp = $timestamp | .experiment.task_name = $name' template.json)

echo "$config" > data/configs/$f.json

python -m dso.run data/configs/$f.json 



