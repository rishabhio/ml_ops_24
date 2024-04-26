
# Simple script which creates a file and 
# writes a message to it.  
message="We are starting ML-OPs on $(date)" 
epoch=$(date +%s) 
path='/Users/fourofour/Professional/Jio-2024/JIO-MLOPS-24/ML-OPS/001-Introduction-To-Automation'
file_name="$path/log-$epoch.txt"  
echo "$message" > "$file_name"
exit 0 
