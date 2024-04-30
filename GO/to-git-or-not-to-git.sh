
DATA=$(curl -s https://learn.01founders.co/assets/superhero/all.json | jq -r '.[] | select(.id == 170)')


NAME=$(jq -r '.name' <<< "$DATA")
POWER=$(jq -r '.powerstats.power' <<< "$DATA")
GENDER=$(jq -r '.appearance.gender' <<< "$DATA")

printf "%s\n%s\n%s\n" "$NAME" "$POWER" "$GENDER"
