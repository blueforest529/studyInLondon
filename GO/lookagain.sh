find . -type f -name '*.sh' | while read -r file; do basename "$file" .sh; done | sort -r
