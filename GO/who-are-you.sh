NAME=$(curl -s https://learn.01founders.co/assets/superhero/all.json | jq -r '.[] | select(.id == 70) | .name')
echo "\"$NAME"\"