
import sys

def analyze_braces(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    balance = 0
    stack = [] // to track what opened (optional, just count for now)
    
    print(f"Analyzing {filepath}...")
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        # ignore comments (basic)
        if line_stripped.startswith('//'):
            continue
            
        for char in line:
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
                if balance == 0:
                    print(f"Brace balance hit 0 at line {i+1}: {line.strip()}")
                if balance < 0:
                    print(f"Brace balance NEGATIVE at line {i+1}: {line.strip()}")
                    return

    print(f"Final Balance: {balance}")

if __name__ == "__main__":
    analyze_braces(sys.argv[1])
